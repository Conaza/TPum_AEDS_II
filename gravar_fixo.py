def salvar_fixo(lista, nome_arquivo="alunos_fixo.dat"):
    
    with open(nome_arquivo, "wb") as arq:
        for aluno in lista:
            parts = []
            parts.append(aluno['matricula'][:9].ljust(9, "#"))
            parts.append(aluno['nome'][:50].ljust(50, "#"))
            parts.append(aluno['cpf'][:11].ljust(11, "#"))
            parts.append(aluno['curso'][:30].ljust(30, "#"))
            parts.append(aluno['mae'][:30].ljust(30, "#"))
            parts.append(aluno['pai'][:30].ljust(30, "#"))
            parts.append(aluno['ano'][:4].ljust(4, "#"))
            parts.append(aluno['ca'][:6].ljust(6, "#"))
            linha = "".join(parts)
            arq.write(linha.encode("utf-8"))
    print(f"Arquivo '{nome_arquivo}' gravado com sucesso ({len(lista)} registros, 170 bytes cada).")
