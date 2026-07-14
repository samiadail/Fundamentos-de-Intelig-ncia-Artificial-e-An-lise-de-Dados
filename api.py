import requests

cep = input("Digite se CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)

endereco = dados.json()

print(endereco["logradouro"])



