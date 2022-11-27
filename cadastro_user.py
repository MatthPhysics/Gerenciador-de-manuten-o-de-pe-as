
#Autenticador#

import json

autenc = {}

def cria_user(l, s, dic):
	dic[l] = s
	return dic


def main():
	user = str(input("Se identifique: \n 1 - Solicitante \n 2 - Manutentor \n"))

	while user != '1' and user != '2':
			user = str(input("Escolha uma opcao válida: \n"))	


	if (user == '1'):
		while True:
			login = str(input("digite um login: \n"))
			senha = str(input("digite uma senha: \n"))
			jaison = open("usuarios_1.json", "r")
			users = json.load(jaison)		
			users[login] = senha
			registro = open("usuarios_1.json", "w")
			json.dump(users,registro)
			registro.close()		
		
			opc = str(input("deseja cadastrar outro solicitante? 1 - Sim 2 - Não \n"))
			if (opc == '2'):
				print("Serviço encerrado!!!")
				break

	if (user == '2'):
		while True:
			login = str(input("digite um login: \n"))
			senha = str(input("digite uma senha: \n"))
			jaison = open("usuarios_2.json", "r")
			users = json.load(jaison)		
			users[login] = senha
			registro = open("usuarios_2.json", "w")
			json.dump(users,registro)
			registro.close()								
	
			opc = str(input("deseja cadastrar outro Manutentor? 1 - Sim 2 - Não \n"))
			if (opc == '2'):
				print("Serviço encerrado!!!")
				break
while True:
	main()
	saida = str(input("Deseja retornar ao menu inicial? 1-Sim  2-Não \n"))
	if(saida == '2'):
		print("Serviço encerrado!!")		
		break
	if(saida != '1' and saida != '2'):
		print("Escolha uma opção válida! \n")
	
