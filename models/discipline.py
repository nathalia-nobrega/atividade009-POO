from typing import List


class Discipline:
    def __init__(self, code: int, name: str, department: 'Department', university: 'University'):
        self.code = code
        self.name = name
        self.professors: List['Professor'] = []
        self.department = department
        self.university = university
        department.disciplines.append(self)
        university.disciplines.append(self)

    def get_department(self) -> 'Department':
        return self.department

    def list_professors(self) -> List['Professor']:
        return self.professors

    def delete(self):
        self.department.disciplines.remove(self)
        self.university.disciplines.remove(self)
        for professor in self.professors:
            if self in professor.disciplines:
                professor.disciplines.remove(self)
        print(f"\tDisciplina {self.name} foi removida do departamento {self.department.name} e da universidade {self.university.name}.")

    def display_discipline_info(self):
        print(f"\n\tDisciplina: {self.name}")
        if self.get_department() is not None:
            print(f"\t\tDepartamento: {self.get_department().name}")
        else:
            print(f"\t\tDepartamento: N/A")
        print("\t\tProfessores:")
        for professor in self.list_professors():
            print(f"\t\t    - {professor.name}")