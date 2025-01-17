try:
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Permissão negada.")
except Exception as e:
    print(f"Erro inesperado: {e}")
