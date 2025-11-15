def salvar_variavel(lista, nome_arquivo="alunos_variavel.dat"):

    with open(nome_arquivo, "wb") as arq:
        for aluno in lista:
            linha = (
                f"{aluno['matricula']}|{aluno['nome']}|{aluno['cpf']}|"
                f"{aluno['curso']}|{aluno['mae']}|{aluno['pai']}|{aluno['ano']}|{aluno['ca']}\n"
            )
            arq.write(linha.encode("utf-8"))
    print(f"Arquivo '{nome_arquivo}' gravado com sucesso ({len(lista)} registros).")
