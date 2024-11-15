import random
from models.university import University
from models.department import Department
from models.professor import Professor
from models.discipline import Discipline

# Dados de professores
professor_names_est = [
    "Carlos Silva", "Ana Pereira", "Marcos Santos", "Juliana Lima", "Fernando Oliveira",
    "Patrícia Almeida", "Ricardo Souza", "Camila Mendes", "José Barbosa", "Maria Costa"
]

professor_names_esa = [
    "Paulo Andrade", "Fernanda Ribeiro", "Leonardo Azevedo", "Sofia Campos", "Rafael Moura",
    "Isabela Castro", "Fábio Cardoso", "Luana Almeida", "André Fernandes", "Marta Ferreira"
]

# Disciplinas por departamento
disciplines_esa = {
    "Medicina": ["Atenção Integral À Saúde", "Genética Humana", "Bioética e ÉTICA Médica", "Telemedicina"],
    "Odontologia": ["Atenção Integral À Saúde", "Genética Humana", "Português Instrumental", "Endodontia II"],
    "Enfermagem": ["Atenção Integral À Saúde", "Genética Humana", "Português Instrumental", "Ética, Biodireito E Legislação De Enfermagem"],
    "Educação Física": ["Anatomia Funcional", "Axiologia Educacional", "Biomecânica", "Educação Física Adaptada"]
}

disciplines_est = {
    "Meteorologia": ["Calculo I", "Álgebra Linear I", "Probabilidade e Estatística", "Meteorologia Tropical"],
    "Engenharia Civil": ["Calculo I", "Álgebra Linear I", "Probabilidade e Estatística", "Introdução À Engenharia Civil"],
    "Sistemas de Informação": ["Calculo I", "Álgebra Linear I", "Probabilidade e Estatística", "Laboratório de Programação"],
    "Engenharia de Computação": ["Calculo I", "Álgebra Linear I", "Probabilidade e Estatística", "Matemática Discreta"],
    "Engenharia Eletrônica": ["Análise de Sinais", "Fenômenos de Transporte I", "Introdução a Eletroquímica", "Circuitos Lógicos"]
}

def add_professors_and_disciplines(department: Department, university: University, professor_names: list,
                                   discipline_pool: list):
    professors = []
    for i, professor_name in enumerate(professor_names):
        professor = Professor(
            code=department.code * 10 + i,
            name=professor_name,
            department=department,
            university=university
        )
        professors.append(professor)
        department.professors.append(professor)  # Adiciona o professor ao departamento

    # Associa disciplinas aos professores
    for j, discipline_name in enumerate(discipline_pool):
        discipline = Discipline(
            code=department.code * 100 + j,
            name=discipline_name,
            department=department,
            university=university
        )
        department.disciplines.append(discipline)  # Adiciona a disciplina ao departamento

        # Atribui a disciplina a um professor aleatório
        assigned_professor = random.choice(professors)
        discipline.professors.append(assigned_professor)
        assigned_professor.disciplines.append(discipline)

    # Garante que todos os professores tenham pelo menos uma disciplina
    for professor in professors:
        if not professor.disciplines:
            random_discipline = random.choice(department.disciplines)
            professor.disciplines.append(random_discipline)
            random_discipline.professors.append(professor)

def main():
    uea_est = University(code=1, name="Universidade do Estado do Amazonas - Unidade EST")
    uea_esa = University(code=2, name="Universidade do Estado do Amazonas - Unidade ESA")

    departments_est = [
        Department(code=101, name="Engenharia Civil", university=uea_est),
        Department(code=102, name="Engenharia de Computação", university=uea_est),
        Department(code=103, name="Engenharia Eletrônica", university=uea_est),
        Department(code=104, name="Sistemas de Informação", university=uea_est),
        Department(code=105, name="Meteorologia", university=uea_est),
    ]

    departments_esa = [
        Department(code=201, name="Educação Física", university=uea_esa),
        Department(code=202, name="Medicina", university=uea_esa),
        Department(code=203, name="Enfermagem", university=uea_esa),
        Department(code=204, name="Odontologia", university=uea_esa),
    ]

    for department in departments_est:
        discipline_pool = disciplines_est[department.name]
        add_professors_and_disciplines(department, department.university, professor_names_est, discipline_pool)

    for department in departments_esa:
        discipline_pool = disciplines_esa[department.name]
        add_professors_and_disciplines(department, department.university, professor_names_esa, discipline_pool)

    universities = {1: uea_est, 2: uea_esa}

    # Menu Interativo
    while True:
        print("\n[DIGITE O CÓDIGO DA UNIVERSIDADE PARA CONSULTAR]")
        print("(1) EST - Universidade do Estado do Amazonas - Unidade EST")
        print("(2) ESA - Universidade do Estado do Amazonas - Unidade ESA")
        print("(0) Sair")
        uni_code = int(input("Escolha uma universidade (1, 2 ou 0 para sair): "))

        if uni_code == 0:
            print("Encerrando o programa.")
            break

        university = universities.get(uni_code)
        if not university:
            print("Código inválido! Tente novamente.")
            continue

        while True:
            print("\n[O QUE VOCÊ DESEJA CONSULTAR?]")
            print("(1) DEPARTAMENTOS")
            print("(2) PROFESSORES")
            print("(3) DISCIPLINAS")
            print("(0) Voltar")
            choice = int(input("Escolha uma opção (1, 2, 3 ou 0 para voltar): "))

            if choice == 0:
                break

            if choice == 1:
                print("\nDepartamentos:")
                for dept in university.list_departments():
                    print(f"  - ({dept.code}) {dept.name}")
                dept_code = int(input("\nDigite o código do departamento para mais detalhes (ou 0 para voltar): "))
                if dept_code == 0:
                    continue
                department = next((d for d in university.list_departments() if d.code == dept_code), None)
                if department:
                    department.display_department_info()
                else:
                    print("Departamento não encontrado.")

            elif choice == 2:
                print("\nProfessores:")
                for prof in university.list_professors():
                    print(f"  - ({prof.code}) {prof.name}")
                prof_code = int(input("\nDigite o código do professor para mais detalhes (ou 0 para voltar): "))
                if prof_code == 0:
                    continue
                professor = next((p for p in university.list_professors() if p.code == prof_code), None)
                if professor:
                    professor.display_professor_info()
                else:
                    print("Professor não encontrado.")

            elif choice == 3:
                print("\nDisciplinas:")
                for disc in university.list_disciplines():
                    print(f"  - ({disc.code}) {disc.name}")
                disc_code = int(input("\nDigite o código da disciplina para mais detalhes (ou 0 para voltar): "))
                if disc_code == 0:
                    continue
                discipline = next((d for d in university.list_disciplines() if d.code == disc_code), None)
                if discipline:
                    discipline.display_discipline_info()
                else:
                    print("Disciplina não encontrada.")

            else:
                print("Opção inválida.")


if __name__ == "__main__":
    main()