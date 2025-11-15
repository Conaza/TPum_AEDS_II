import random

def gerar_alunos(qtd=10):
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia"]
    sobrenomes = ["Silva", "Souza", "Oliveira", "Santos", "Lima", "Costa", "Ribeiro"]
    cursos = ["Computação", "Engenharia", "Matemática", "Administração"]
    nomes_pais = ["José", "Mariana", "Paulo", "Adriana", "Ricardo", "Patrícia", "Roberto", "Clara"]

    alunos = []
    for _ in range(qtd):
        nome = f"{random.choice(nomes)} {random.choice(sobrenomes)} {random.choice(sobrenomes)}"
        mae = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        pai = f"{random.choice(nomes_pais)} {random.choice(sobrenomes)}"
        aluno = {
            "matricula": str(random.randint(100000000, 999999999)),
            "nome": nome,
            "cpf": "".join(str(random.randint(0,9)) for _ in range(11)),
            "curso": random.choice(cursos),
            "mae": mae,
            "pai": pai,
            "ano": str(random.randint(2018, 2025)),
            "ca": f"{random.uniform(5, 10):.2f}"
        }
        alunos.append(aluno)
    return alunos
