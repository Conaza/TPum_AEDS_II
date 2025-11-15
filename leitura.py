def ler_fixo(nome_arquivo="alunos_fixo.dat"):
    alunos = []
    TAM_REG = 170
    try:
        with open(nome_arquivo, "rb") as arq:
            while True:
                dados = arq.read(TAM_REG)
                if not dados:
                    break
                s = dados.decode("utf-8")
                # remover padding '#' e espaços finais
                matricula = s[0:9].replace("#", "").strip()
                nome = s[9:59].replace("#", "").strip()
                cpf = s[59:70].replace("#", "").strip()
                curso = s[70:100].replace("#", "").strip()
                mae = s[100:130].replace("#", "").strip()
                pai = s[130:160].replace("#", "").strip()
                ano = s[160:164].replace("#", "").strip()
                ca = s[164:170].replace("#", "").strip()
                alunos.append((matricula, nome, cpf, curso, mae, pai, ano, ca))
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    return alunos


def ler_variavel(nome_arquivo="alunos_variavel.dat"):
    alunos = []
    try:
        with open(nome_arquivo, "rb") as arq:
            for linha in arq:
                partes = linha.decode("utf-8").rstrip("\n").split("|")
                if len(partes) == 8:
                    alunos.append(tuple(partes))
                else:
                    # linha malformada: ignorar ou tratar; aqui ignoramos
                    continue
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    return alunos
