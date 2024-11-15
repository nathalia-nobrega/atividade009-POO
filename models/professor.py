from typing import List

from models.department import Department
from models.university import University


class Professor:
    def __init__(self, code: int, name: str, department: Department, university: University):
        self.code = code
        self.name = name
        self.disciplines: List['Discipline'] = []
        self.department = department
        self.university = university
        department.professors.append(self)
        university.professors.append(self)

    def get_department(self) -> Department:
        return self.department

    def list_disciplines_by_professor(self) -> List['Discipline']:
        return self.disciplines

    def get_university(self) -> University:
        return self.university

    def display_professor_info(self):
        print(f"\nProfessor: {self.name}")
        print(f"  Departamento: {self.get_department().name}")
        print("  Disciplinas:")
        for discipline in self.list_disciplines_by_professor():
            print(f"    - {discipline.name}")