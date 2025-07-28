# Conceitos Básicos de Python - Guia prático para o trabalho

# 1. Sintaxe básica
print("Olá, mundo!")  # ou print('Olá, mundo!')

# 2. Variáveis e tipos primitivos
nome = "João"
idade = 25
altura = 1.75
ativo = True

# 3. Condicionais
if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")

# 4. Laços de repetição
for i in range(5):
    print(i)

contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# 5. Funções
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("João"))

# 6. Listas
nomes = ["João", "Maria", "Carlos"]
nomes.append("Ana")
print(nomes[0])
print(len(nomes))

# 7. Dicionários
usuario = {"nome": "João", "idade": 25}
print(usuario["nome"])
usuario["email"] = "joao@email.com"

# 8. Percorrendo estruturas
for nome in nomes:
    print(nome)

for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# 9. Tratamento de erros
try:
    numero = int("abc")
except ValueError:
    print("Erro: valor inválido")

# 10. Manipulação de arquivos
with open("arquivo.txt", "w") as f:
    f.write("Olá, mundo!")

with open("arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

# 11. Módulos
import math
print(math.sqrt(16))

# 12. Classes e objetos
class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Oi, sou {self.nome} e tenho {self.idade} anos.")

p = Pessoa("João", 25)
p.falar()

# 13. Funções lambda e list comprehension
quadrado = lambda x: x * x
print(quadrado(5))

numeros = [1, 2, 3, 4]
dobro = [n * 2 for n in numeros]
print(dobro)

# 14. Requisição HTTP com requests
import requests

response = requests.get("https://viacep.com.br/ws/01001000/json/")
dados = response.json()
print(f"CEP: {dados['cep']}, Cidade: {dados['localidade']} - {dados['uf']}")

# 15. Números e operadores
x = 10
y = 3
print(x + y)
print(x ** y)
print(x // y)
print(x > 5 and x < 20)

# 16. Caminhos e arquivos
import os
print(os.getcwd())
print(os.path.exists("arquivo.txt"))

# 17. Aspas e ponto e vírgula
print('Pode usar aspas simples')
print("Ou aspas duplas")
# print("João's casa")  # evita conflito com aspas
# Pode usar ; para múltiplos comandos na mesma linha, mas é desnecessário
x = 1; y = 2; print(x + y)

# 18. Sem ++ em Python
contador = 0
contador += 1  # correto

# 19. API com Flask (básico)
from flask import Flask, jsonify, request

app = Flask(_name_)

usuarios = [{"id": 1, "nome": "João"}, {"id": 2, "nome": "Maria"}]

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios/<int:id>", methods=["GET"])
def get_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    return jsonify(usuario) if usuario else ('Usuário não encontrado', 404)

# if _name_ == "_main_":
#     app.run(debug=True)