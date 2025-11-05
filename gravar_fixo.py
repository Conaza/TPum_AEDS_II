def salvar_fixo(lista, nome_arquivo="alunos_fixo.dat"):
    
    with open(nome_arquivo, "wb") as arq:
        for aluno in lista:
            linha = f"{aluno['matricula']:<9}{aluno['nome']:<20}{aluno['curso']:<20}{aluno['ano']:<4}{aluno['ca']:<5}"
            linha = linha.ljust(60, "#")  # garante 60 bytes por registro
            arq.write(linha.encode())
    print(f"Arquivo '{nome_arquivo}' gravado com sucesso!")
