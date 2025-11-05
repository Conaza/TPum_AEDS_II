import random

def gerar_alunos(qtd=10):
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena"]
    cursos = ["Computação", "Engenharia", "Matemática", "Administração"]
    alunos = []

    for _ in range(qtd):
        aluno = {
            "matricula": str(random.randint(100000000, 999999999)),
            "nome": random.choice(nomes),
            "curso": random.choice(cursos),
            "ano": str(random.randint(2018, 2025)),
            "ca": f"{random.uniform(5, 10):.2f}"
        }
        alunos.append(aluno)
    return alunos
