from functions import *

print("###########################")
print("Qual a data de vencimento? ")
print("###########################")

due_date = input("Qual a data de vencimento?: ")

if len(due_date) == 10:
    print(verify_due(due_date))
else:
    print("Entrada inválida!!!")


