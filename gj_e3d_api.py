import ips
from py_gjapi import *
def usr_data():
	auth = open("User.ini", "r")
	auth2 = open("Token.ini", "r")
	User = auth.readline()
	Token = auth2.readline()
	placeholder = GameJoltTrophy(User, Token, "Aqui va la id de tu juego", "aqui va la llave de tu juego")
	return placeholder
	auth.close()
	auth2.close()
	#Establece la informacion del usuario
def Get_key():
	k_in = open("Key.ini", "r")
	key = k_in.readline()
	return key
	#Establece la key
def login():
	usrdata = usr_data()
	Output = open("Output.txt", "a")
	if  usrdata.authenticateUser() == True:
		Output.write('True')
		return True
	if  usrdata.authenticateUser() == False:
		Output.write('False')
		return False
	Output.close()
	#inicia la sesion del usuario
def give_trophy():
	usrdata = usr_data()
	trophy_id = open("Trophy.ini", "r")
	E3d_output = open("Message.txt", "a")
	ID = trophy_id.readline()
	if login() == True:
		usrdata.addAchieved(ID)
		E3d_output.write('Archieved')
		return True
	if login() == False:
		E3d_output.wirte('Auth Error')
		return False
	trophy_id.close()
	E3d_output.close()
	#Le da un logro al usuario previamente definido
def start_game():
	usrdata = usr_data()
	usrdata.openSession()
	#Inicia la sesión del usuario
def keep_active():
	usrdata = usr_data()
	usrdata.pingSession(active=True)
	#Mantiene activo al usuario, invocar cada 30 seg o se cerrará la sesión.
def keep_logged():
	usrdata = usr_data()
	usrdata.pingSession(active=False)
	#Mantiene en stand-by al usuario, invocar cada 30 seg o se cerrará la sesión.
def save_server_score():
	usrdata = usr_data()
	s_in = open("Score.ini", "r")
	sr_in = open("Sort.ini", "r")
	ed_in = open("Extra_data.ini", "r")
	type = open("Table.ini", "r")
	MAIN = type.readline()
	EData = ed_in.readline()
	score = s_in.readline()
	sort = sr_in.readline()
	usrdata.addScores(score, sort, table_id=MAIN, extra_data=EData, guest=False, guestname='')
	#Guarda una puntuación para el jugador servidor.
def save_clients_score(Name1,MAIN1):
	usrdata = usr_data()
	s_in1 = open("C1Score.ini", "r")
	sr_in1 = open("C1Sort.ini", "r")
	ed_in1 = open("C1Extra_data.ini", "r")
	EData1 = ed_in1.readline()
	score1 = s_in1.readline()
	sort1 = sr_in1.readline()
	usrdata.addScores(score1, sort1, table_id=MAIN1, extra_data=EData1, guest=True, guestname=Name1)
	#Guarda una puntuación para los jugadores cliente.
def get_max_scores():
	usrdata = usr_data()
	result = usrdata.scoreTable()
	return result
	#Obtiene las puntuaciones máximas de tu juego.
def get_data():
	usrdata = usr_data()
	key = Get_key()
	reut = usrdata.fetchData(key, user_info_only=False)
	return reut
	#Obtiene informacion alojada en una key
def store_Data(User): #User debe ser True o False
	dat = open("Data.ini", "r")
	key = Get_key()
	data = dat.readline()
	if User==True:
		usrdata = usr_data()
		usrdata.storeData(key, data, user_info_only=True)
	if User==False:
		storeData(key, data, user_info_only=False)
	#Guarda información en la nube de GameJolt
def get_scores():
	usrdata = usr_data()
	Tb_in = open("Table.ini", "r")
	TableX = Tb_in.readline()
	result = usrdata.fetchScores(limit=10, table_id=TableX, user_info_only=False)
	return result
	#Obtiene las puntuaciones globales de tu juego
def get_tables(input,numt) #input indica qué dato deseas consultar (1-id,2-descripcion,3-nombre,4-primario(boolean),5-numero de tablas
	userdata=usr_data()
	u = userdata.scoreTable()
	if input=1:
		idmain=u['tables'][numt]['id']
		return idmain
	if input=2:	
		descmain=u['tables'][numt]['description']
		return descmain
	if input=3:	
		namemain=u['tables'][numt]['name']
		return namemain
	if input=4:
		ismain=u['tables'][numt]['primary']
		return ismain
	if input=5	
		nummer=len(u['tables'])
		return nummer
def 