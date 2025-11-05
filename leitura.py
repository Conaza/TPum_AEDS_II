def ler_fixo(nome_arquivo="alunos_fixo.dat"):
    
    alunos = []
    try:
        with open(nome_arquivo, "rb") as arq:
            while True:
                dados = arq.read(60)
                if not dados:
                    break
                linha = dados.decode().replace("#", "").strip()
                matricula = linha[0:9].strip()
                nome = linha[9:29].strip()
                curso = linha[29:49].strip()
                ano = linha[49:53].strip()
                ca = linha[53:].strip()
                alunos.append((matricula, nome, curso, ano, ca))
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    return alunos


def ler_variavel(nome_arquivo="alunos_variavel.dat"):
    alunos = []
    try:
        with open(nome_arquivo, "rb") as arq:
            for linha in arq:
                partes = linha.decode().strip().split("|")
                if len(partes) == 5:
                    alunos.append(tuple(partes))
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    return alunos
