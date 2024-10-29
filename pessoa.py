nome_digitado = input("Digite seu nome: ")
idade_digitada = int(input("Digite sua idade: "))
cpf_digitado = (input("Digite seu CPF: "))
num_digitado = (input("Digite seu telefone: "))

if idade_digitada > 0 and len(cpf_digitado) == 11:
    aluno = {
    "Nome": nome_digitado,
    "Idade": idade_digitada,
    "CPF": cpf_digitado,
    "Telefone": num_digitado
    }
    if idade_digitada >= 18:
        print(f"O aluno {aluno["Nome"]} é maior de idade.")
    else:
        print(f"O aluno {aluno["Nome"]} é menor de idade.")
else: 
    print("Digite dados válidos!")