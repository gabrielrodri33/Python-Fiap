import requests

cep = "02346-000"
cep = cep.replace("-", "").replace(".", "").strip()
print(f"CEP: {cep}")

if len(cep) == 8:
    url = f'https://viacep.com.br/ws/{cep}/json'
    
    requisicao = requests.get(url)
    print(requisicao)

    dic = requisicao.json()
    print(dic)