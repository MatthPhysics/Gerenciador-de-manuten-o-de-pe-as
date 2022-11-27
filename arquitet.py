import json 
import os

print("#################################################################")
print("#                                                               #")
print("#                                                               #")
print("#                    MANUTENÇÃO DE PEÇAS                        #")
print("#                                                               #")
print("#                                                               #")
print("#################################################################\n")     


dic = {
		'nome_solicitante': [],
		'nome_peca': [],
		'nº_serie': [],
		'defeito': [],
		'parecer' : [],
		'data': []	 	
	}

valores_peca = { 'Placa mãe': ['890.87'],
				 'Processador': ['569.90'],	
				 'Placa de vídeo': ['345.80'],
				 'Monitor': ['500.00'],
				 'Disco Rígido': ['150.00'],
				 'Fonte de alimentação': ['800.50'],
				 'Memória (RAM)': ['500.00'],
				 'SSD': ['300.00'] 
		
			}


registro_v = open("valores.json", "w")
json.dump(valores_peca,registro_v)
registro_v.close()


usuarios_1 = open("usuarios_1.json", "r")
autenc_1 = json.load(usuarios_1)


usuarios_2 = open("usuarios_2.json", "r")
autenc_2 = json.load(usuarios_2)

"""
print("Bem vindo ao gerenciado de peças!!")
user = str(input("Se identifique como solicitante ou manutentor: 1 - Solicitante 2 - Manutentor"))
"""


#def gera_protocol(n_serie):
	

def historico(nome_peca, solv, cust):
	dic_hist = {'nome_peca': [nome_peca],
		    'Solução': [solv],
                    'Custo': [cust] 						
	
		}
	
	registro = open(nome_peca + ".json", "w")
	json.dump(dic_hist,registro)
	registro.close()
	
	return dic_hist	

def add_custo_rep(dicc, nome_pecaa, custoo):
	dicc[nome_pecaa] = custoo
	registro = open("valores.json", "w")
	json.dump(dicc,registro)
	registro.close()		

	print(dicc)
			

class gerenciador_s:
	def __init__(self, dicionario):
		self.geren = dicionario

	def add_registro(self, sol, nome_p, n_serie, defeito, par, data):
		#dataa = datetime.date.today()
		
		self.geren.update({'nome_solicitante': sol}) 
		self.geren.update({'nome_peca' : nome_p})
		self.geren.update({'nº_serie':  n_serie}) 
		self.geren.update({'defeito': defeito}) 
		self.geren.update({'parecer': par}) 
		self.geren.update({'data': data})		
		print(self.geren) 		
		registro = open(n_serie + ".json", "w")
		json.dump(self.geren,registro)
		registro.close()
	
	def consulta(self, n_serie, info):
				
		jaison = open(n_serie + ".json", "r")
		self.geren = json.load(jaison)
		#self.geren = new_dict		
		print(self.geren[info])		
		#print(new_dict)		
		
	
	
	def add_parecer(self, n_serie, novo_parecer):
				
		jaison = open(n_serie + ".json", "r")
		self.geren = json.load(jaison)		
		self.geren.update({'parecer': novo_parecer})
		registro = open(n_serie + ".json", "w")
		json.dump(self.geren,registro)
		registro.close()		
		print(self.geren)
		
	def altera_info(self, n_serie, info, up):
				
		jaison = open(n_serie + ".json", "r")
		self.geren = json.load(jaison)		
		self.geren.update({info : up})
		registro = open(n_serie + ".json", "w")
		json.dump(self.geren,registro)
		registro.close()		
		
		print(self.geren)
		

	def drop(self, n_serie):
		
		if os.path.exists(n_serie + ".json"):
			os.remove(n_serie + ".json")
		else:
			print("Registro inexistente!!!")

class gerenciador_m(gerenciador_s):
	def __init__(self, dic):
		self.conc = dic
		
	
	def arruma(self, n_serie, solv, cust):
		jaison = open(n_serie + ".json", "r")
		self.geren = json.load(jaison)			
		self.geren['Solução'] = solv
		self.geren['Custo'] = cust
		historico(self.geren['nome_peca'], solv, cust)		
		registro = open(n_serie + ".json", "w")
		json.dump(self.geren,registro)
		registro.close()
	 
	def consulta_hist(self, nome_peca):
				
		jaison = open(nome_peca + ".json", "r")
		self.geren = json.load(jaison)		
		#self.geren = new_dict		
		print(self.geren)		
		#print(new_dict)
			
	def custo_rep(self, nome):
		print("Caro ", nome, ", estes são os valores para reposição de peças")		
		jaison = open("valores.json", "r")
		valores = json.load(jaison)
			#self.geren = new_dict		
		print(valores)		
		resp = str(input("Deseja add mais algum item? 1 - Sim  2 - Não \n"))
		if resp == '1':
			while True:
				name = str(input("Digite o nome da peça: \n"))
				preco = str(input("Digite o preco da peça: \n"))
				add_custo_rep(valores, name, preco)
								
				resp = str(input("Deseja add outro item? 1 - Sim  2 - Não \n"))	
				if(resp == '2'):
					print("Serviço encerrado !!!")
					break
				if(saida != '1' and saida != '2'):
					print("Escolha uma opção válida! \n")
		
		
	def drop_s(self, n_serie):
		
		if os.path.exists(n_serie + ".json"):
			os.remove(n_serie + ".json")
		else:
			print("Registro inexistente!!!")

	def drop_h(self, nome_peca):
		
		if os.path.exists(nome_peca + ".json"):
			os.remove(nome_peca + ".json")
		else:
			print("Registro inexistente!!!")

obj = gerenciador_s(dic)

obj2 = gerenciador_m(gerenciador_s)

def main_1():
	
	print("Seguem as opções de serviço\n")
	print("1 - Adicionar registro \n")
	print("2 - Consultar registro \n")
	print("3 - Add parecer \n")
	print("4 - altera informações \n")	
	print("5 - exclui registro \n")	
	
	opc = str(input("Selecione a opção desejada:"))
	while opc != '1' and opc != '2' and opc != '3' and opc != '4' and opc != '5':
		opc = str(input("Escolha uma opcao válida: \n"))	
	if(opc == '1'):		
		while True:
			nome_c = str(input("digite seu nome: \n"))		 			
			nome_p = str(input("Identifique a peça: \n"))
			num_serie = str(input("digite o numero de serie da peça: \n"))
			probl = str(input("Qual problema identificou: \n"))
			data = str(input("digite a data de cadastro: \n"))
			obj.add_registro(nome_c, nome_p, num_serie, probl, 'em andamento', data)	
			perg_1 = str(input("Deseja adicionar mais algum registro? 1 - Sim  2 - Não \n"))
			if(perg_1 == '2'):
				print("Serviço encerrado!")
				break
			if(perg_1 != '1' and perg_1 != '2'):
				print("Escolha uma opção válida! \n")
	
	elif(opc == '2'):
		num = str(input("digite qual o numero de serie da peça: \n"))
		if os.path.exists(num + ".json"):		
			while True:			
				inf = str(input("Sobre qual informação quer consultar:\n 1 - Nome solicitante \n 2 - Nome da peça \n 3 - Problema da peça \n 4 - data  		  				\n"))		
				while inf != '1' and inf != '2' and inf != '3' and inf != '4':
					opc = str(input("Escolha uma opcao válida: \n"))			
				if(inf == '1'):
					obj.consulta(num, 'nome_solicitante')
				elif(inf == '2'):
					obj.consulta(num, 'nome_peca')
				elif(inf == '3'):
					obj.consulta(num, 'defeito')
				elif(inf == '4'):
					obj.consulta(num, 'data')	
				perg_2 = str(input("Deseja consultar mais algum registro? 1 - Sim  2 - Não \n"))
				if(perg_2 == '2'):
					print("Serviço encerrado!")
					break
				if(perg_2 != '1' and perg_2 != '2'):
					print("Escolha uma opção válida! \n")
			
		else:
			print("Registro inexistente!!!")
	
	elif(opc == '3'):
		while True:		
			num = str(input("digite qual o numero de serie da peça: \n"))				
			if os.path.exists(num + ".json"):		
				novo_par = str(input("Qual é o novo parecer? \n"))
				obj.add_parecer(num, novo_par)
				perg_3 = str(input("Deseja mudar o parecer de outro registro? 1 - Sim  2 - Não \n"))
				if(perg_3 == '2'):
					print("Serviço encerrado!")
					break
				if(perg_3 != '1' and perg_3 != '2'):
					print("Escolha uma opção válida! \n")			

			else:
				print("Este registro é inexistente")	
				break
				
	elif(opc == '5'):
		while True:		
			num = str(input("digite qual o numero de serie da peça: \n"))
			if os.path.exists(num + ".json"):			
				obj.drop(num)					
				perg_4 = str(input("Deseja excluir outro registro? 1 - Sim  2 - Não \n"))
				if(perg_4 == '2'):
					print("Serviço encerrado!")
					break
				if(perg_4 != '1' and perg_4 != '2'):
					print("Escolha uma opção válida! \n")
			else:
				print("Este registro é inexistente")	
				break
			
	elif(opc == '4'):
		num = str(input("digite qual o numero de serie da peça: \n"))
		if os.path.exists(num + ".json"):		
			while True:			
				inf_2 = str(input("Qual info quer alterar:\n 1 - Nome solicitante \n 2 - Nome da peça \n 3 - Problema da peça \n 4 - parecer \n 5 -     data"))
				while inf_2 != '1' and inf_2 != '2' and inf_2 != '3' and inf_2 != '4' and inf_2 != '5':
					opc = str(input("Escolha uma opcao válida: \n"))			
				if(inf_2 == '1'):
					n_inf = str(input("digite a alteração: \n"))			
					obj.altera_info(num, 'nome_solicitante', n_inf)
				elif(inf_2 == '2'):
					n_inf = str(input("digite a alteração: \n"))			
					obj.altera_info(num, 'nome_peca', n_inf)
				elif(inf_2 == '3'):
					n_inf = str(input("digite a alteração: \n"))			
					obj.altera_info(num, 'defeito', n_inf)
				elif(inf_2 == '4'):
					n_inf = str(input("digite a alteração: \n"))			
					obj.altera_info(num, 'parecer', n_inf)
				elif(inf_2 == '5'):
					n_inf = str(input("digite a alteração: \n"))			
					obj.altera_info(num, 'data', n_inf)
						
				perg_5 = str(input("Deseja outra informação deste registro? 1 - Sim  2 - Não \n"))
				if(perg_5 == '2'):
					print("Serviço encerrado!")
					break
				if(perg_5 != '1' and perg_5 != '2'):
					print("Escolha uma opção válida! \n")
		else:
			print("Este registro é inexistente!!!")



def main_2():
	
	print("Seguem as opções de serviço\n")
	print("1 - arrumar peça \n")
	print("2 - Consultar histórico de manutenção\n")
	print("3 - Consultar valores de reposição \n")
	print("4 - exclui registro de manutenção \n")	
	print("5 - exclui registro de solicitação \n")	
	
	opc = str(input("Selecione a opção desejada:"))
	while opc != '1' and opc != '2' and opc != '3' and opc != '4' and opc != '5':
		opc = str(input("Escolha uma opcao válida: \n"))	
	if(opc == '1'):		
		while True:		
			num_serie = str(input("digite o numero de serie da peça: \n"))		
			if os.path.exists(num_serie + ".json"):		
				solution = str(input("Qual foi a solução do problema amigão?? \n"))		
				custo = str(input("Qual foi o custo para a solução?? \n"))		
				obj2.arruma(num_serie, solution, custo)	
				perg_1 = str(input("Deseja adicionar arrumar outra peça? 1 - Sim  2 - Não \n"))
				if(perg_1 == '2'):
					print("Serviço encerrado!")
					break
				if(perg_1 != '1' and perg_1 != '2'):
					print("Escolha uma opção válida! \n")
		
			else:
				print("Registro inexistente!!!")
				break
	elif(opc == '2'):
		while True:		
			name = str(input("digite qual o nome da peça que quer saber o histórico: \n"))
			if os.path.exists(name + ".json"):		
				obj2.consulta_hist(name)	
				perg_2 = str(input("Deseja consultar outro histórico? 1 - Sim  2 - Não \n"))
				if(perg_2 == '2'):
					print("Serviço encerrado!")
					break
				if(perg_2 != '1' and perg_2 != '2'):
					print("Escolha uma opção válida! \n")
				
			else:
				print("Registro inexistente!!!")
				break
	elif(opc == '3'):
		nname = str(input("Nome do usuário: \n"))		
		obj2.custo_rep(nname)	
	elif(opc == '4'):
		while True:		
			if os.path.exists(name + ".json"):			
				nome_pec = str(input("digite qual o nome da peça que deseja excluir o registro: \n"))
				obj2.drop_h(nome_pec)					
				perg_3 = str(input("Deseja consultar outro histórico? 1 - Sim  2 - Não \n"))
				if(perg_3 == '2'):
					print("Serviço encerrado!")
					break
				if(perg_3 != '1' and perg_3 != '2'):
					print("Escolha uma opção válida! \n")
				
			else:
				print("Registro inexistente!!!")
				break
	elif(opc == '5'):
		while True:		
			num = str(input("digite qual o numero de serie da peça: \n"))
			if os.path.exists(num + ".json"):
				obj.drop(num)					
				if(perg_4 == '2'):
					print("Serviço encerrado!")
					break
				if(perg_4 != '1' and perg_4 != '2'):
					print("Escolha uma opção válida! \n")
				
			else:
				print("Registro inexistente!!!")
				break


user = str(input("Se identifique: \n 1 - Solicitante \n 2 - Manutentor \n"))

while user != '1' and user != '2':
		user = str(input("Escolha uma opcao válida: \n"))	
	
if (user == '1'):
	login_e = str(input("Digite o seu login: \n"))
	senha_e = str(input("\nDigite sua senha: \n"))
	cont = 0

	for chave, valor in autenc_1.items():
		if (chave == login_e) and (valor == senha_e):
			cont += 1	
	while cont == 0:
		print("######## Serviço negado ########")
		print("Tente novamente \n\n")
		login_e = str(input("Digite o seu login: \n"))
		senha_e = str(input("Digite sua senha: \n"))
		for chave, valor in autenc_1.items():
			if (chave == login_e) and (valor == senha_e):
				cont += 1
	if (cont != 0):	
		print("######## Acesso Permitido ######## \n\n")
		while True:
			main_1()
			saida = str(input("Retornar ao menu inicial? 1-Sim  2-Não \n"))
			if(saida == '2'):
				print("Serviço encerrado!!")		
				break
			if(saida != '1' and saida != '2'):
				print("Escolha uma opção válida! \n")
	
	
				

else:
	login_e = str(input("Digite o seu login: \n"))
	senha_e = str(input("Digite sua senha: \n"))
	cont = 0

	for chave, valor in autenc_2.items():
		if (chave == login_e) and (valor == senha_e):
			cont += 1	
	while cont == 0:
		print("######## Serviço negado ########")
		print("Tente novamente")
		login_e = str(input("Digite o seu login: \n"))
		senha_e = str(input("Digite sua senha: \n"))
		for chave, valor in autenc_2.items():
			if (chave == login_e) and (valor == senha_e):
				cont += 1
	if (cont != 0):	
		print("######## Acesso Permitido ######## \n\n")
		while True:
			main_2()
			saida = str(input("Retornar ao menu inicial? 1-Sim  2-Não \n"))
			if(saida == '2'):
				print("Serviço encerrado!!")		
				break
			if(saida != '1' and saida != '2'):
				print("Escolha uma opção válida! \n")
	
