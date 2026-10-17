# Dicionário

pessoas = {
    "pessoa1":{
        "nome":"Steve",
        "idade": 28,
        "email": "ste@fiap.com.br"
    },
    "pessoa2":{
        "nome":"Alex",
        "idade": 32,
        "email": "alex@fiap.com.br"
    },
    "pessoa3":{
        "nome":"Bob",
        "idade": 30,
        "email": "bob98@fiap.com.br"
    }
}

# Bilioteca JSON
import json

pessoas_json = json.dumps(pessoas, indent=4)

# Mostrando o dicionário
print("Exibição do dicionário: ")
print(pessoas)

# Mostrando o arquivo JSON
print("\nExibição do JSON: ")
print(pessoas_json)

# Abrindo o arquivo para gravação
with open('pessoas.json', 'w+') as file:
    file.write(pessoas_json) # Gravando o objeto nor arquivo .json

with open('pessoas.json', 'r') as file:
    # Lendo o arquivo .json
    file.seek(0)
    pessoas_json = file.read()
    pessoas = json.loads(pessoas_json)

# Formatando
print("Exibição formatada dos dados: ")
for k, v in pessoas.items():
    print(f"Registro....: {k}")
    for k1, v1 in v.items():
        print("\t" + k1 + ": " + str(v1))