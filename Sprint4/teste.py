import webbrowser
from api import viacep

def consultaCep():
    cep = input("Informe seu CEP!\nCaso não saiba apenas tecle ENTER!\nCEP: ").replace(" ", "").replace(".", "").replace("-", "")

    while len(cep) != 8 or not cep.isdigit():
        print("Inválido!")
        cep = input("Informe seu CEP!\nCaso não saiba apenas tecle ENTER!\nCEP: ").replace(" ", "").replace(".", "").replace("-", "")
    
    if cep == "":
        link = "https://buscacepinter.correios.com.br/app/endereco/index.php"
        webbrowser.open(link)
        cep = input("CEP: ")
    
    cep, dic = viacep.cep(cep)
    print(cep)
    print(dic)
    return cep, dic

consultaCep()
