from abc import ABC, abstractmethod
from enum import Enum, unique


class Filter(ABC):
    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP001)."""
        pass

    @abstractmethod
    def matches(self, line: str) -> bool:
        """Returns True if a given line matches the filter, otherwise, returns False."""
        pass


class EndsWithDot(Filter):
    def name(self) -> str:
        return 'FP001'

    def matches(self, line: str) -> bool:
        """
        Check if the string matches rule FP001.
        FR001 - string ends with a dot.
        :param line: string from open file.
        :return:True if line ends with a dot, otherwise False.
        """
        return line.strip().endswith('.')


class LessOneHundredChars(Filter):
    def name(self) -> str:
        return 'FP002'

    def matches(self, line: str) -> bool:
        """
        Check if the string matches rule FP002.
        FP002 - string is less than 100 characters.
        :param line: string from open file.
        :return:True if line is less than 100 characters, otherwise False.
        """
        return len(line) < 100


class AtLeastFiveALetters(Filter):
    def name(self) -> str:
        return 'FP003'

    def matches(self, line: str) -> bool:
        """
        Check if the string matches rule FP003.
        FP003 - string has at least 5 a letters.
        :param line: string from open file.
        :return:True if line has at least 5 a letters, otherwise False.
        """
        return line.count('a') >= 5


class MoreThreeZLetters(Filter):
    def name(self) -> str:
        return 'FN201'

    def matches(self, line: str) -> bool:
        """
        Check if the string matches rule FN201.
        FN201 - string has more than 3 z letters.
        :param line: string from open file.
        :return:True if line has more than 3 z letters, otherwise False.
        """
        return line.count('z') > 3


class EmptyLine(Filter):
    def name(self) -> str:
        return 'FN202'

    def matches(self, line: str) -> bool:
        """
        Check if the string matches rule FN202.
        FN202 - string is an empty line.
        Zero string without spaces is empty.
        Zero string with just spaces is not empty.
        :param line: string from open file.
        :return:True if line is an empty line, otherwise False.
        """
        return len(line.strip()) == 0


class ConsistsNonLetterChars(Filter):
    def name(self) -> str:
        return 'FN203'

    def matches(self, line: str) -> bool:
        """
        Check if the string matches rule FN203.
        FN203 - string consists only from non-letter characters.
        Empty line returns False.
        :param line: string from open file.
        :return:True if line consists only from non-letter characters, otherwise False.
        """
        non_letter_characters_counter = 0
        line_length = len(line.strip())
        for symbol in line.strip():
            if symbol.isalpha():
                continue
            else:
                non_letter_characters_counter += 1
        if len(line.strip()) == 0:
            return False
        elif line_length == non_letter_characters_counter:
            return True
        else:
            return False


@unique
class RuleDisplay(Enum):
    """
    Class consits only from instances of rules, that must be printed.
    """
    RULE_FP001 = EndsWithDot()
    RULE_FP002 = LessOneHundredChars()
    RULE_FP003 = AtLeastFiveALetters()


@unique
class RuleNotDisplay(Enum):
    """
    Class consits only from instances of rules, that must not be printed.
    """
    RULE_FN201 = MoreThreeZLetters()
    RULE_FN202 = EmptyLine()
    RULE_FN203 = ConsistsNonLetterChars()


class Option(ABC):
    """
    Сlass creates an instance of the desired class.
    """
    @abstractmethod
    def filter_file(self, file: str):
        """
        Method must be implemented by class AnnotationOption or class FilterOption.
        :param file: path to the file which want to analyze.
        """
        pass

    @staticmethod
    def get_option(option: str):
        """
        Method decides which instance it will create FilterOption() or AnnotationOption().
        :param option: string, for instance 'filter'.
        :return: instance of the desired class.
        """
        if option == 'filter':
            return FilterOption()
        elif option == 'annotate':
            return AnnotationOption()


class AnnotationOption(Option):
    def filter_file(self, file):
        """
        Method has to display the information about which rules are
        applicable for each line using <line number>: [rule] ... format.
        :param file: path to the file which want to analyze.
        :return: None
        """
        with open(file, 'r', encoding='utf8') as file_stream:
            for num, line in enumerate(file_stream, 1):
                rules_for_line = list()
                for rule in RuleDisplay:
                    if rule.value.matches(line.strip()):
                        rules_for_line.append(rule.value.name())
                for rule in RuleNotDisplay:
                    if rule.value.matches(line.strip()):
                        rules_for_line.append(rule.value.name())
                print('{}: {}'.format(num, ' '.join(rules_for_line)))


class FilterOption(Option):
    def filter_file(self, file):
        """
        Method should display lines based on rules, that are contained at the Class Rule.
        :param file: path to the file which want to analyze.
        :return: None
        """
        with open(file, 'r', encoding="utf8") as file_stream:
            for line in file_stream:

                priority_display = 0
                for rule in RuleDisplay:
                    if rule.value.matches(line):
                        priority_display += 1

                priority_not_display = 0
                for rule in RuleNotDisplay:
                    if rule.value.matches(line):
                        priority_not_display += 1

                if priority_display >= priority_not_display:
                    print(line.strip())
