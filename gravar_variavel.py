def salvar_variavel(lista, nome_arquivo="alunos_variavel.dat"):

    with open(nome_arquivo, "wb") as arq:
        for aluno in lista:
            linha = f"{aluno['matricula']}|{aluno['nome']}|{aluno['curso']}|{aluno['ano']}|{aluno['ca']}\n"
            arq.write(linha.encode())
    print(f"Arquivo '{nome_arquivo}' gravado com sucesso!")
