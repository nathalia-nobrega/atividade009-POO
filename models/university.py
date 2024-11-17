from typing import List


class University:
    def __init__(self, code: int, name: str):
        self.code = code
        self.name = name
        self.departments: List['Department'] = []
        self.professors: List['Professor'] = []
        self.disciplines: List['Discipline'] = []

    def list_departments(self) -> List['Department']:
        return self.departments

    def list_professors(self) -> List['Professor']:
        return self.professors

    def list_disciplines(self) -> List['Discipline']:
        return self.disciplines

    def delete(self):
        # Remove todas as relações com a universidade
        for professor in list(self.list_professors()):
            professor.delete()
        self.professors.clear()

        for department in self.departments:
            department.delete()
        self.departments.clear()

        # for discipline in self.list_disciplines():
        #     discipline.delete()
        self.disciplines.clear()

        print(f"\tUniversidade {self.name} foi deletada junto com suas entidades relacionadas.")