import csv
csv_file='dati.csv'
with open(csv_file, 'a') as f:
    f.close()
csv_otrais = 'trenina_dati.csv'

def ievade():
    global pietupienu_skaits,vienas_kajas_pietupienu_skaits,pievilksanas_skaits,muscle_up_skaits,atspiesanas_skaits,dimanta_atspiesanas_skaits,sedus_augsa_skaits,planka_ilgums
    with open(csv_file, 'r') as f:
        first_char = f.read(1)
        if not first_char: 
    
            while True: 
                try:
                    pietupienu_skaits = int(input("Ievadiet pietupienu skaitu: "))
                    if pietupienu_skaits<1001 and pietupienu_skaits>-1:
                        break
                    else:
                        print('Nepareiza ievade')
                except ValueError:
                    print('Nepareiza ievade')
            while True:
                try:
                    vienas_kajas_pietupienu_skaits = int(input("Ievadiet vienas kājas pietupienu skaitu: ")) 
                    if vienas_kajas_pietupienu_skaits<1001 and vienas_kajas_pietupienu_skaits>-1:
                        break
                    else:
                        print('Nepareiza ievade')
                except ValueError:
                    print('Nepareiza ievade')
            while True:
                try:
                    pievilksanas_skaits = int(input("Ievadiet pievilkšanās skaitu: "))
                    if pievilksanas_skaits<1001 and pievilksanas_skaits>-1:
                        break
                    else:
                        print('Nepareiza ievade')
                except ValueError:
                    print('Nepareiza ievade')
            while True:
                try:
                    muscle_up_skaits = int(input("Ievadiet muscle up skaitu: "))
                    if muscle_up_skaits<1001 and muscle_up_skaits>-1:
                        break
                    else:
                        print('Nepareiza ievade')
                except ValueError:
                    print('Nepareiza ievade')
            while True:
                try:
                    atspiesanas_skaits = int(input("Ievadiet atspiešanās skaitu: "))
                    if atspiesanas_skaits<1001 and atspiesanas_skaits>-1:
                        break
                    else:
                        print('Nepareiza ievade')
                except ValueError:
                        print('Nepareiza ievade')
            while True:
                try:
                    dimanta_atspiesanas_skaits = int(input("Ievadiet dimanta atspiešanās skaitu: "))
                    if dimanta_atspiesanas_skaits<1001 and dimanta_atspiesanas_skaits>-1:
                        break
                    else:
                        print('Nepareiza ievade')
                except ValueError:
                        print('Nepareiza ievade')
            while True:
                try:
                    sedus_augsa_skaits = int(input("Ievadiet sēdus augšā skaitu: "))
                    if sedus_augsa_skaits<1001 and sedus_augsa_skaits>-1:
                        break
                    else:
                        print('Nepareiza ievade')
                except ValueError:
                    print('Nepareiza ievade')
            while True:
                try:
                    planka_ilgums = float(input("Ievadiet planka ilgumu(sekundes): "))
                    if planka_ilgums<1001 and planka_ilgums>-1:
                        break
                    else:
                        print('Nepareiza ievade')
                except ValueError:
                    print('Nepareiza ievade')
        else:
            print("Tavi dati saglabāti dati.txt failā")

def saglabasana(): 
    rezultati=[
        {'pietupieni':pietupienu_skaits,'vienas_kajas_pietupieni':vienas_kajas_pietupienu_skaits,'pievilksanas':pievilksanas_skaits,"muscle_up":muscle_up_skaits,"atspiesanas":atspiesanas_skaits,"dimanta_atspiesanas":dimanta_atspiesanas_skaits,"sedus_augsa":sedus_augsa_skaits,"planka_ilgums":planka_ilgums}
    ]
    with open(csv_file,'w',encoding='utf8',newline='') as file:
        fieldnames=["pietupieni",'vienas_kajas_pietupieni',"pievilksanas","muscle_up","atspiesanas","dimanta_atspiesanas","sedus_augsa","planka_ilgums"]
        writer=csv.DictWriter(file,fieldnames)
        writer.writeheader() 
        writer.writerows(rezultati)

with open(csv_file,'r',encoding='utf8') as file:
    reader=csv.DictReader(file)
    for rinda in reader:
        pietupienu_skaits=int(rinda['pietupieni'])
        vienas_kajas_pietupienu_skaits=int(rinda['vienas_kajas_pietupieni'])
        pievilksanas_skaits=int(rinda['pievilksanas'])
        muscle_up_skaits=int(rinda['muscle_up'])
        atspiesanas_skaits=int(rinda['atspiesanas'])
        dimanta_atspiesanas_skaits=int(rinda['dimanta_atspiesanas'])
        sedus_augsa_skaits=int(rinda['sedus_augsa'])
        planka_ilgums=float(rinda['planka_ilgums'])        


'''        
class Trenini(): 
    def __init__(self,pietupieni, vienas_kajas_pietupieni,atspiesanas, dimanta_atspiesanas,pievilksanas,muscle_up,sedus_augsa) :
        self.pietupieni = pietupieni
        self.vienas_kajas_pietupieni = vienas_kajas_pietupieni
        self.atspiesanas = atspiesanas
        self.dimanta_atspiesanas = dimanta_atspiesanas
        self.pievilksanas = pievilksanas
        self.muscle_up = muscle_up
        self.sedus_augsa = sedus_augsa
    def prints(self):
        print('----------------------------------')
        print('Jūsu šodienas treniņu plāns:')
class Kajas(Trenini): 
    def __init__(self):
        super().__init__()
    def trenet_kajas(self): 
        print(f'Pietupienu skaits: {round(self.pietupieni*0.75+5)}')
        print(f'Vienas kājas pietupienu skaits: {round(self.vienas_kajas_pietupieni*0.75+1)}')
        print('----------------------------------')
    def prints(pietupieni,vienas_kajas_pietupieni):
         return super().prints + f'Pietupienu skaits: {round(pietupieni*0.75+5)}'+'\n'+f'Vienas kājas pietupienu skaits: {round(vienas_kajas_pietupieni*0.75+1)}'+'\n'+'----------------------------------'
    
class Kruskurvis(Trenini):
    def trenet_kruskurvi(atspiesanas,dimanta_atspiesanas):
        print(f'atspiešanās skaits: {round(atspiesanas*0.75+1)}')
        print(f'dimanta atspiešanās skaits: {round(dimanta_atspiesanas*0.75+1)}')
        return super().prints + f'atspiešanās skaits: {round(atspiesanas*0.75+1)}' + '\n' + f'dimanta atspiešanās skaits: {round(dimanta_atspiesanas*0.75+1)}'+ '\n'+'----------------------------------'
        
class Mugura(Trenini):
    def __init__(self):
        super().__init__()
    def prints(pievilksanas,muscle_up):
        return super().prints + f"Pievilkšanās skaits: {round(pievilksanas*0.75+1)}"+'\n'+f"Muscle up skaits: {round(muscle_up*0.75+1)}"+'\n'+"----------------------------------"
class Vedera_presite(Trenini):
    def __init__(self):
        super().__init__()
    def prints(self,sedus_augsa,planks):
        return super().prints + f'Sedus augšā skaits: {round(sedus_augsa*0.75+5)}'+'\n'+ f'Planka ilgums (sekundēs): {round(planks*0.75+3)}'+'\n'+"----------------------------------"
class Atputa(Trenini):
    def prints():
        return super().prints +"Šodien treniņš nav, atpūtas diena." + '----------------------------------'
'''
def trenet_kajas(pietupienu_skaits, vienas_kajas_pietupienu_skaits):
    print('----------------------------------')
    print('Jūsu šodienas treniņu plāns:')
    print(f'Pietupienu skaits: {round(pietupienu_skaits*0.75+5)}')
    print(f'Vienas kājas pietupienu skaits: {round(vienas_kajas_pietupienu_skaits*0.75+1)}')
    print('----------------------------------')
def trenet_kruskurvi(atspiesanas,dimanta_atspiesanas):
    print('----------------------------------')
    print("Jūsu šodienas treniņu plāns: ")
    print(f'atspiešanās skaits: {round(atspiesanas*0.75+1)}')
    print(f'dimanta atspiešanās skaits: {round(dimanta_atspiesanas*0.75+1)}')
    print('----------------------------------')
def trenet_muguru(pievilksanas, muscle_up):
    print('----------------------------------')
    print('Jūsu šodienas treniņu plāns:')
    print(f"Pievilkšanās skaits: {round(pievilksanas*0.75+1)}")
    print(f"Muscle up skaits: {round(muscle_up*0.75+1)}")
    print('----------------------------------')
def trenet_presiti(sedus_augsa,planks):
    print('Jūsu šodienas treniņu plāns:')
    print(f"Sedus augšā skaits: {round(sedus_augsa*0.75+5)}")
    print(f'Planka ilgums (sekundēs): {round(planks*0.75+3)}')
    print('----------------------------------')
def atputas_diena():
    print("Jūsu šodienas treniņu plāns:")
    print("Šodien treniņš nav, atpūtas diena.")
    print('----------------------------------')


def parakstit_otra():
    with open(csv_file,'r') as firstfile, open(csv_otrais,'w') as secondfile:
    # read content from first file
        for line in firstfile:
             # append content to second file
             secondfile.write(line)
             
def treninu_saksana():
    global treneties
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
    return treneties

def treninu_izpilde():
    global izpilde
    while True:
        izpilde = input("Vai jūs izpildījāt šodienas treniņu? (J/N):")
        if izpilde == "J":
            izpilde=1
            break
        elif izpilde == "N":
            izpilde = 0
            break
        else:   
            print("Nepareiza ievade.")
    return izpilde
        
def galvena():
    ievade()
    with open(csv_file, 'r') as f:
        first_char = f.read(1)
        if not first_char: 
            saglabasana()
        else:
            print('Nav dati ievadīti!')
    with open(csv_otrais, 'r') as f:
        first_char = f.read(1)
        if not first_char: 
            parakstit_otra()
        else:
            print()
   
    treninu_saksana() 
    if treneties =='1':
        trenet_kajas(pietupienu_skaits,vienas_kajas_pietupienu_skaits)

    elif treneties == '0':
        exit()

galvena()

