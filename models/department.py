from typing import List

from models.university import University


class Department:
    def __init__(self, code: int, name: str, university: University):
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

    def get_university(self) -> University:
        return self.university

    def display_department_info(self):
        print(f"\nDepartamento: {self.name}")
        print("  Professores:")
        for professor in self.list_professors():
            print(f"    - {professor.name}")
        print("  Disciplinas:")
        for discipline in self.list_disciplines():
            print(f"    - {discipline.name}")