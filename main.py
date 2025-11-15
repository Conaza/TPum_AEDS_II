from gerar_dados import gerar_alunos
from gravar_fixo import salvar_fixo
from gravar_variavel import salvar_variavel
from leitura import ler_fixo, ler_variavel
from analise import analisar_arquivo

def main():
    print("\n=== SISTEMA DE ARMAZENAMENTO DE ALUNOS ===")

    bloco = int(input("\nInforme o tamanho máximo do bloco (em bytes): "))

    print("\nEscolha o tipo de registro:")
    print("1 - Tamanho Fixo")
    print("2 - Tamanho Variável")
    tipo = input("Opção: ")

    alunos = gerar_alunos(15)

    if tipo == "1":
        print("\n=== REGISTROS DE TAMANHO FIXO ===")

        # Cada registro no fixo tem 170 bytes
        TAM_REG = 170

        print(f"\nCada registro possui {TAM_REG} bytes.")
        print(f"Bloco informado: {bloco} bytes.")

        if TAM_REG > bloco:
            print("\nO registro é MAIOR do que o bloco.")
            print("Isso simula necessidade de múltiplos blocos por registro ou overflow.")
        
        salvar_fixo(alunos)

    elif tipo == "2":
        print("\n=== REGISTROS DE TAMANHO VARIÁVEL ===")

        esp = input("Haverá espalhamento (fragmentação)? (s/n): ").lower()

        salvar_variavel(alunos)

        if esp == "s":
            print("\nModo com ESPALHAMENTO ativado.")
            print("Registros podem ultrapassar o tamanho do bloco.")
        else:
            print("\nModo SEM espalhamento.")
            print("Registros que ultrapassam o bloco devem ser divididos ou rejeitados.")
            print("Você pode implementar regras específicas depois.")

    else:
        print("Opção inválida!")
        return

    print("\n--- Primeiros registros lidos ---")
    if tipo == "1":
        registros = ler_fixo()
    else:
        registros = ler_variavel()

    for i, r in enumerate(registros[:5], 1):
        print(f"{i}. {r}")

    if tipo == "1":
        analisar_arquivo("alunos_fixo.dat", tipo="fixo")
    else:
        analisar_arquivo("alunos_variavel.dat", tipo="variavel")


if __name__ == "__main__":
    main()
