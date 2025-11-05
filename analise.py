import os

def analisar_arquivo(nome_arquivo, tipo="fixo"):
    try:
        tamanho_total = os.path.getsize(nome_arquivo)
        if tipo == "fixo":
            qtd_registros = tamanho_total // 60
        else:
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                qtd_registros = len(f.readlines())
        tamanho_medio = tamanho_total / max(qtd_registros, 1)

        print(f"\n--- Análise do arquivo {nome_arquivo} ---")
        print(f"Tamanho total: {tamanho_total} bytes")
        print(f"Registros: {qtd_registros}")
        print(f"Tamanho médio por registro: {tamanho_medio:.2f} bytes")
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")