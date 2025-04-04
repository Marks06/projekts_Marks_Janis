def ievade():
    while True:
        try:
            pietupienu_skaits = int(input("Ievadiet pietupienu skaitu: "))
            break
        except ValueError:
            print('Nepareiza ievade')
    while True:
        try:
            vienas_kajas_pietupienu_skaits = int(input("Ievadiet vienas kājas pietupienu skaitu: ")) 
            break
        except ValueError:
            print('Nepareiza ievade')
    while True:
        try:
            pievilksanas_skaits = int(input("Ievadiet pievilkšanās skaitu: "))
            break
        except ValueError:
            print('Nepareiza ievade')
    while True:
        try:
            muscle_up_skaits = int(input("Ievadiet muscle up skaitu: "))
            break
        except ValueError:
            print('Nepareiza ievade')
    while True:
        try:
            atspiesanas_skaits = int(input("Ievadiet atspiešanās skaitu: "))
            break
        except ValueError:
            print('Nepareiza ievade')
    while True:
        try:
            dimanta_atspiesanas_skaits = int(input("Ievadiet dimanta atspiešanās skaitu: "))
            break
        except ValueError:
            print('Nepareiza ievade')
    while True:
        try:
            sedus_augsa_skaits = int(input("Ievadiet sēdus augšā skaitu: "))
            break
        except ValueError:
            print('Nepareiza ievade')
    while True:
        try:
            planka_ilgums = float(input("Ievadiet planka ilgumu(sekundes): "))
            break
        except ValueError:
            print('Nepareiza ievade')

        
def trenini():
    while True:
        treneties=input("Vai vēlaties redzēt šodienas treniņa plānu? (J/N):")
        if treneties == "J":
            treneties=1
            break
        elif treneties =="N":
            treneties=0
            break
        else:
            print("Nepareiza ievade.")


def galvena():
    #parbauda, vai ir jau dati, ko izmantot
    #ja ir, tad:
    trenini()
    #ja nav, tad
    ievade()
    
'''lists = []

with open("rezultati.txt", "r") as file:
	lines = file.readlines()
for i in lines:
	as_list = i.split(", ")
	lists.append(as_list)
	print(lists)'''


'''with open('rezultati.txt', 'r') as f:
    myNames = [line.strip() for line in f]
    print(myNames)'''
lines = []
with open("rezultati.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!
    print(lines)

def trenet_kajas(pietupieni, vienas_kajas_pietupieni):
    print('Tavs šodienas treniņš:')
    print(f'Pietupienu skaits: {pietupieni*0.75+5}')
    print(f"Vienas kājas pietupienu skaits: {vienas_kajas_pietupieni*0.75+1}")
def trenet_krutis(atspiesanas,dimanta_atspiesanas):
    print('Tavs šodienas treniņš:')
    print(f'atspiešanās skaits: {atspiesanas*0.75+1}')
    print(f"Dimanta atspiešanās skaits: {dimanta_atspiesanas*0.75+1}")
def trenet_muguru(pievilksanas,muscle_up):
    print('Tavs šodienas treniņš:')
    print(f'Pievilkšanās skaits: {pievilksanas*0.75+1}')
    print(f'Muscle ups skaits: {muscle_up*0.75+1}')
def trenet_presiti(planks,sedus_augsa):
    print("Tavs šodienas treniņš:")
    print(f"Planka ilgums (sec): {planks*0.75+3}")
    print(f"Sēdus augšā skaits: {sedus_augsa*0.75+5}")
    