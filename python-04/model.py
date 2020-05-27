from math import sqrt


class Project:
    def __init__(self, name):
        self.name = name
        self.list_estimates = list()
        self.list_standard_deviation = list()

    def add_estimate(self, estimate_of_task):
        self.list_estimates.append(estimate_of_task)

    def add_standard_deviation(self, standard_deviation_of_task):
        self.list_standard_deviation.append(standard_deviation_of_task)

    def calculate_an_estimate_of_project(self):
        return round(sum(self.list_estimates),2)

    def calculate_standard_deviation_of_project(self):
        return round(sqrt(sum([pow(standard_deviation, 2) for standard_deviation in self.list_standard_deviation])), 2)

    @staticmethod
    def calculate_confidence_interval(estimate_of_project, standard_deviation_of_project):
        return estimate_of_project - 2 * standard_deviation_of_project, estimate_of_project + 2 * standard_deviation_of_project


class Task:
    def __init__(self, best_case_estimate, most_likely_estimate, worst_case_estimate):
        self.best_case_estimate = best_case_estimate
        self.most_likely_estimate = most_likely_estimate
        self.worst_case_estimate = worst_case_estimate

    def calculate_an_estimate_of_task(self):
        return round((self.best_case_estimate + 4 * self.most_likely_estimate + self.worst_case_estimate) / 6, 2)

    def calculate_standard_deviation_of_task(self):
        return round((self.worst_case_estimate - self.best_case_estimate) / 6, 2)




