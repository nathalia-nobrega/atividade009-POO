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
