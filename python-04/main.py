from python04.model import Task, Project


def new_project():
    """Create an instance of the class Project."""
    name_of_project = input('Enter a name for your project: ')
    return Project(name_of_project)


def new_task():
    """Create an instance of the class Task."""
    best_case_estimate = int(input('Enter the best-case estimate: '))
    most_likely_estimate = int(input('Enter the most likely estimate: '))
    worst_case_estimate = int(input('Enter the worst-case estimate: '))
    return Task(best_case_estimate, most_likely_estimate, worst_case_estimate)


def main_console_menu():
    """Entry point for console version."""
    choice_about_new_project = 'y'
    choice_about_new_task = 'y'
    while choice_about_new_project.lower() == 'y':
        project = new_project()
        while choice_about_new_task == 'y':
            task = new_task()
            estimate_of_task = task.calculate_an_estimate_of_task()
            standard_deviation_of_task = task.calculate_standard_deviation_of_task()
            project.add_estimate(estimate_of_task)
            project.add_standard_deviation(standard_deviation_of_task)
            print('E(task): ', estimate_of_task)
            print('SD(task): ', standard_deviation_of_task)
            choice_about_new_task = input('Do you want to add another task to the project? [Y/N] ')
        estimate_of_project = project.calculate_an_estimate_of_project()
        standard_deviation_of_project = project.calculate_standard_deviation_of_project()
        confidence_interval_min, confidence_interval_max = Project.calculate_confidence_interval(estimate_of_project, standard_deviation_of_project)
        print('E(project): ', estimate_of_project)
        print('SE(project): ', standard_deviation_of_project)
        print('Project\'s 95% confidence interval: {} ... {} points '.format(confidence_interval_min, confidence_interval_max))
        choice_about_new_project = input('Do you want to create another project? [Y/N] ')
        choice_about_new_task = 'y'


if __name__ == '__main__':
    main_console_menu()





