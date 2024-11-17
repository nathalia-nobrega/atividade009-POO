from models.university import University
from models.department import Department
from models.professor import Professor
from models.discipline import Discipline

def main():
    # Criando uma universidade
    uea_est = University(1, "Universidade do Estado do Amazonas - Unidade EST")

    # Criando departamentos
    dept_comp = Department(102, "Engenharia de Computação", uea_est)
    dept_sis = Department(103, "Sistemas de Informação", uea_est)

    # Criando professores
    prof_joao = Professor(201, "João Ponciano", dept_sis, uea_est)
    prof_osvaldo = Professor(202, "Osvaldo Viana", dept_comp, uea_est)
    prof_elloa = Professor(203, "Elloá Guedes", dept_comp, uea_est)
    prof_palheta = Professor(204, "Márcio Palheta", dept_sis, uea_est)

    # Criando disciplinas
    discipline_calc = Discipline(301, "Cálculo 1", dept_sis, uea_est)
    discipline_algo = Discipline(302, "Algoritmos e Estruturas de Dados", dept_sis, uea_est)
    discipline_md = Discipline(303, "Matemática Discreta", dept_comp, uea_est)
    discipline_oac = Discipline(304, "Organização e Arquitetura de Computadores", dept_comp, uea_est)


    # Associando professores às disciplinas
    discipline_calc.professors.append(prof_joao)
    prof_joao.disciplines.append(discipline_calc)

    discipline_md.professors.append(prof_elloa)
    discipline_algo.professors.append(prof_elloa)
    prof_elloa.disciplines.append(discipline_md)
    prof_elloa.disciplines.append(discipline_algo)


    discipline_oac.professors.append(prof_osvaldo)
    prof_osvaldo.disciplines.append(discipline_oac)

    discipline_algo.professors.append(prof_palheta)
    discipline_md.professors.append(prof_palheta)
    prof_palheta.disciplines.append(discipline_md)
    prof_palheta.disciplines.append(discipline_algo)




    # Exibindo informações
    print("===== Informações da Universidade =====")
    print(f"\nUniversidade: {uea_est.name}")
    print("\n===== Departamentos da Universidade =====")
    for dept in uea_est.list_departments():
        dept.display_department_info()

    print("\n===== Professores da Universidade =====")
    for professor in uea_est.list_professors():
        professor.display_professor_info()

    print("\n===== Disciplinas da Universidade =====")
    for discipline in uea_est.list_disciplines():
            discipline.display_discipline_info()

    # Testando DELEÇÃO

    print("\n\t===== Demonstração de deleção =====")

    # DELETE: PROFESSOR
    print("\n\tOPERAÇÃO 001: Deletar PROFESSOR João...")
    prof_joao.delete()

    print("\n\t===== [DEPOIS DA DELEÇÃO DE PROFESSOR] Disciplinas da Universidade =====")
    for discipline in uea_est.list_disciplines():
        discipline.display_discipline_info()

    print("\n\tOPERAÇÃO 002: Deletar DISCIPLINA Matemática Discreta...")
    discipline_md.delete()

    print("\n\t===== [LISTA DE DISCIPLINAS DEPOIS DA DELEÇÃO DA DISCIPLINA] =====")
    for discipline in uea_est.list_disciplines():
        discipline.display_discipline_info()

    # DELETE: DEPARTMENT
    print("\n\tOPERAÇÃO 003: Deletar o DEPARTAMENTO de Engenharia da Computação...")
    dept_comp.delete()

    print("\n\t===== [LISTA DE DISCIPLINAS DEPOIS DA DELEÇÃO DO DEPARTAMENTO] =====")
    for discipline in uea_est.list_disciplines():
        discipline.display_discipline_info()

    # DELETE: uea_est
    print("\n\tOPERAÇÃO 004: Deletar a UNIVERSIDADE UEA-EST...")
    uea_est.delete()

    print("\n\t===== [LISTA DE DEPARTAMENTOS DEPOIS DA DELEÇÃO DA UNIVERSIDADE] =====")
    for dept in uea_est.list_departments():
        dept.display_department_info()

    print("\n\t===== [LISTA DE PROFESSORES DEPOIS DA DELEÇÃO DA UNIVERSIDADE] =====")
    for professor in uea_est.list_professors():
        professor.display_professor_info()

    print("\n\t===== [LISTA DE DISCIPLINAS DEPOIS DA DELEÇÃO DA UNIVERSIDADE] =====")
    for discipline in uea_est.list_disciplines():
        discipline.display_discipline_info()

if __name__ == "main":
    main()