from typing import List

class Professor:
    def __init__(self, code: int, name: str, department: 'Department', university: 'University'):
        self.code = code
        self.name = name
        self.disciplines: List['Discipline'] = []
        self.department = department
        self.university = university
        department.professors.append(self)
        university.professors.append(self)

    def get_department(self) -> 'Department':
        return self.department

    def list_disciplines_by_professor(self) -> List['Discipline']:
        return self.disciplines

    def get_university(self) -> 'University':
        return self.university

    def delete(self):
        if self in self.department.professors:
            self.department.professors.remove(self)
        if self in self.university.professors:
            self.university.professors.remove(self)
        for discipline in self.disciplines:
            if self in discipline.professors:
                discipline.professors.remove(self)
                print(f"\tO professor {self.name} foi removido da disciplina {discipline.name}.")


    def display_professor_info(self):
        print(f"\n\tProfessor: {self.name}")
        if self.get_department() is not None:
            print(f"\t\tDepartamento: {self.get_department().name}")
        else:
            print(f"\t\tDepartamento: N/A")
        print("\t\tDisciplinas:")
        for discipline in self.disciplines:
            if self in discipline.professors:
                print(f"\t\t    - {discipline.name}")