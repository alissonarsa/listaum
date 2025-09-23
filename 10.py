import time
import os

class CarregadorPreguicoso:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self._dados = None
        print(f"Objeto CarregadorPreguicoso criado para o arquivo '{nome_arquivo}', mas os dados ainda NÃO foram lidos.")

    @property
    def dados(self):
        if self._dados is None:
            print(f"\n--- Primeira vez que 'dados' foi acessado. ---")
            print(f"Carregando os dados do arquivo '{self.nome_arquivo}' agora...")
            
            time.sleep(2) 
            
            with open(self.nome_arquivo, 'r', encoding='utf-8') as f:
                self._dados = f.readlines()
            
            print("--- Dados carregados e armazenados em memória. ---")
        
        return self._dados


NOME_DO_ARQUIVO = "dados_pesados.txt"
with open(NOME_DO_ARQUIVO, "w", encoding='utf-8') as f:
    for i in range(10):
        f.write(f"Esta é a linha de dados número {i+1}\n")


print("Criando o objeto...")
meu_carregador = CarregadorPreguicoso(NOME_DO_ARQUIVO)
print("\nObjeto criado. Note como nenhuma leitura de arquivo aconteceu ainda.")
print("-" * 40)

print("\nAgora, vamos acessar os dados pela PRIMEIRA vez...")
primeiro_acesso = meu_carregador.dados
print("\nConteúdo do primeiro acesso:")
print("".join(primeiro_acesso))
print("-" * 40)

print("\nVamos acessar os dados pela SEGUNDA vez...")
segundo_acesso = meu_carregador.dados
print("Acesso foi instantâneo, sem mensagem de 'Carregando...'.")
print("\nConteúdo do segundo acesso:")
print("".join(segundo_acesso))

os.remove(NOME_DO_ARQUIVO)