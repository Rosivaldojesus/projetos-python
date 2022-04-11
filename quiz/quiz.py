print("olá, seja bem vindo ao quiz!!!")
answer_user = input("Vamos começar s/n.")
    
if answer_user != 's':
    quit()

score = 0

print("Començado...........") 
print("Quem desenvolveu o jogo GTA?\n (A) Rockstar \n (B) Ubisot \n (C) Activision \n (D) EA \n")

answer_user = input("Resposta: ")

try:
    if answer_user == "A":
        print("Correto!")
        score = score + 1
    else:
        print("Incorreto!")
except:
    print("Algo deu errado na sua resposta!")

print(f'Resultado final: {score}')
