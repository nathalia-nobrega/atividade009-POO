from typing import List

from models.department import Department
from models.university import University


class Discipline:
    def __init__(self, code: int, name: str, department: Department, university: University):
        self.code = code
        self.name = name
        self.professors: List['Professor'] = []
        self.department = department
        self.university = university
        department.disciplines.append(self)
        university.disciplines.append(self)

    def get_department(self) -> Department:
        return self.department

    def list_professors(self) -> List['Professor']:
        return self.professors

    def get_university(self) -> University:
        return self.university

    def display_discipline_info(self):
        print(f"\nDisciplina: {self.name}")
        print(f"  Departamento: {self.get_department().name}")
        print("  Professores:")
        for professor in self.list_professors():
            print(f"    - {professor.name}")