from gerar_dados import gerar_alunos
from gravar_fixo import salvar_fixo
from gravar_variavel import salvar_variavel
from leitura import ler_fixo, ler_variavel
from analise import analisar_arquivo

def main():
    alunos = gerar_alunos(15)

    salvar_fixo(alunos)
    salvar_variavel(alunos)

    lista_fixo = ler_fixo()
    lista_var = ler_variavel()

    print("\n--- Primeiros registros (fixo) ---")
    for i, a in enumerate(lista_fixo[:3]):
        print(f"{i+1}. {a}")

    print("\n--- Primeiros registros (variável) ---")
    for i, a in enumerate(lista_var[:3]):
        print(f"{i+1}. {a}")

    analisar_arquivo("alunos_fixo.dat", tipo="fixo")
    analisar_arquivo("alunos_variavel.dat", tipo="variavel")

if __name__ == "__main__":
    main()
