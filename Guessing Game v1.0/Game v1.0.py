import random
RandomNumber = int(random.randint(1,100))
HigherNumber = ["Mas alto amiga","Mas arriba podria estar","Hasta el infinito y mas alla","Arriba el america","Estas cerca (creo), apunta mas alto",
                "Tal vez si incrementas un poco...","MAAAAAAAS","Ay no, mejor ni juegues, dale mas","Estas frio, dale mas","Una pista:mas",
                "Tres metros sobre el cielo","Subele un poquito","Sin miedo","Incrementale, no pasa nada","Estas debajo, sube","Andas bajo mi rey"]
LowerNumber = ["Te pasaste un poco","No es competencia, baja","Dale pa bajo mi rey","Cerca, pero de tocar el techo","Nop, baja","Ya fuiste, te pasaste",
              "Cerca estas(creo), dale un poco menos","MENOOOOOOS","Mucha potencia tilin, menos","Andas muy arriba apa","Le diste de mas",
              "Intenta decrementar","Tambien puedes disminuir","Que malo eres, te pasaste","Uno poquito menos potencia amor","Ya mero, solo baja"]
tries = 5
print("-Adivina el numero en el que la computadora esta pensando")
print("-El numero esta entre 1 y 100")
print("-El simbolo + significa que el numero es mayor")
print("-El simbolo - significa que el numero es menor")
print("-Tienes 5 intentos, buena suerte!")
guess = int(input("Ingresa un numero que creas correcto: "))
boolean1 = True
while boolean1 == True:
#the 3 if's for the guess, if they are above or below, and if they win#
  #if in case they go below the random number#
  if guess < RandomNumber and tries != 1:
    tries -= 1
    print("-",random.choice(HigherNumber),"(+)")
    if tries < 2:
      print("Solo te queda un intento, usalo bien!")
    else:
      print("Te quedan",tries,"intentos")
    guess = int(input("Nuevo acierto: "))
  #if in case they go above the random number
  if guess > RandomNumber and tries != 1:
    tries -= 1
    print("-",random.choice(LowerNumber),"(-)")
    if tries < 2:
      print("Solo te queda un intento, usalo bien!")
    else:
      print("Te quedan",tries,"intentos")
    guess = int(input("Nuevo acierto: "))
  #if in case they guess the random number
  if guess == RandomNumber:
    tries = 1
    print("-Adivinaste el numero correcto, Felicidades!")
#replay or not if they win
  if tries == 1 and guess == RandomNumber:
    answer = input("-Te gustaria un doble o nada (si/no): ")
    if answer == "si":
      tries = 5
      RandomNumber = int(random.randint(1,100))
      print("-Me gusta como piensas, vas con todo tilin")
      print("-El numero ha cambiado, ya no es el mismo")
      guess = int(input("Ingresa un nuevo acierto: "))
    else:
      print("-Esta bien. Gracias por jugar!")
      boolean1 = False
#replay or not if they lost
  if tries == 1 and guess != RandomNumber:
    print("-Perdiste, te quedaste sin intentos, el numero correcto era",RandomNumber)
    answer = input("-Te gustaria intentarlo otra vez (si/no): ")
    if answer == "si":
      print("-Esa es la actitud, rendirse no es una opcion")
      tries = 5
      RandomNumber = int(random.randint(1,100))
      print("-El numero ha cambiado, ya no es el mismo")
      guess = int(input("Ingresa un nuevo acierto: "))
    else:
      print("-Te rendiste, no vales nada, pero gracias por jugar!")
      boolean1 = False