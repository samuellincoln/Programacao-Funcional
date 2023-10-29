#Abaixo a gente ve o exemplo da implementacao do diagrama de maquina de estados para o exemplo das estacoes do ano...
nextstate = lambda state : "Primavera" if state == "Inverno" else "Verao" if state == "Primavera" else "Outono" if state == "Verao" else "Inverno"

#nextpdca = lambda state : "Action" if state == "Check" else "Plan" if state == "Action" else 

#print (nextstate ("Primavera"))
#print (nextstate ("Inverno"))

#Abaixo a gente ve a implementacao do simulador do protocolo OAuth 2.0

PR = "Protected Resource"
GR = "Grant"
AT = "Access Token"
SUC = "SUCCESS"
ER = "ERROR"

crry = lambda f : (lambda p : f (p))
deccry = lambda f, p : f (p)
client = lambda msg : SUC if msg == PR else crry (auth_server) if msg == GR else resource_server () if msg == AT else ER
cl_rec = lambda msg, rec : crry (client) if msg == rec else ER
resource_owner = lambda msg : cl_rec (msg, GR)
auth_server = lambda msg : cl_rec (msg, AT)
resource_server = lambda msg : cl_rec (msg, PR)

cll = client ("Grant") ("Access Token") ("Protected Resource")
cll2 = client ("Grant") ("Protected Resource")
cll3 = client ("Grant") ("Access Token") ("Grant") ("Protected Resource")
print (cll)
print (cll2)
print (cll3)
