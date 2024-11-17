from typing import List

from models.discipline import Discipline
from models.professor import Professor
from models.university import University


class Department:
    def __init__(self, code: int, name: str, university: 'University'):
        self.code = code
        self.name = name
        self.professors: List['Professor'] = []
        self.disciplines: List['Discipline'] = []
        self.university = university
        university.departments.append(self)

    def list_professors(self) -> List['Professor']:
        return self.professors

    def list_disciplines(self) -> List['Discipline']:
        return self.disciplines

    def delete(self):
        # Remove disciplinas, mas não as exclui da lista global
        for discipline in self.disciplines:
            discipline.department = None
        self.disciplines.clear()
        self.university.departments.remove(self)
        print(f"\tDepartamento {self.name} foi removido da universidade {self.university.name}.")

    def display_department_info(self):
        print(f"\n\tDepartamento: {self.name}")
        print("\t\tProfessores:")
        for professor in self.list_professors():
            print(f"\t\t    - {professor.name}")
        print("\t\tDisciplinas:")
        for discipline in self.list_disciplines():
            print(f"\t\t    - {discipline.name}")