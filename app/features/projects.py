class Projects:
    def __init__(self, projects=[]):
        self.projects = projects

    @property
    def names(self):
        return [project.name for project in self.projects]

    def add(self, project):
        self.projects.append(project)

    def delete(self, project_index):
        self.projects.pop(project_index)
