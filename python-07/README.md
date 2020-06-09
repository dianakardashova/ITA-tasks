Task description
Write a program which filters a given file or annotates its lines with relevant rules. It should
run like

python -m silters (filter | annotate) <a file path>
If filter option is requested, the program should display lines based on rules below. If
annotate option is requested, the program has to display the information about which rules are
applicable for each line using <line number>: [rule] ... format. For instance, like this

1: FP001
2:
3: FP001 FP002 FN203
4: FN203
There are the following rules for the content:

display a line if it
ends with a dot (FP001)
is less than 100 characters (FP002)
has at least 5 a letters (FP003)
don't display a line if it
has more than 3 z letters (FN201)
is an empty line (FN202)
consists only from non-letter characters (FN203)
The "display" rules have a priority over the "non-display" rules. For instance, if there is a line
like zaz zara Ararat ZULU Ozz and more amazing words, it should be printed.

Also, each rule has to be implemented by extending the following abstraction

from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP005)."""
        pass
    
    @abstractmethod
    def matches(self, line: str) -> bool:
        """Returns True if a given line matches the filter, otherwise, returns False."""
        pass
Also, try to create an abstraction to express different options (we have filter and annotate)
now. And don't forget to apply other OOD design approaches if any. Ideally, the implementation
should have no functions, only classes.