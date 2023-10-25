import requests

cep = "87.910-000"
cep = cep.replace("-", "").replace(".", "").strip()
print(f"CEP: {cep}")

if len(cep) == 8:
    url = f'https://viacep.com.br/ws/{cep}/json'
    