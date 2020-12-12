import os,re
print("A l’aide, tous aux abris ! ")
pas,mineur,majeur,lines,arbres = [0,0,0,0],0,0,[],[]
def wopen(text):
    with open (text) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        return lines
for line in wopen("messagePourSauverLeMonde.txt"):
    getvolcan = re.findall('volcan', line)
print(getvolcan)
for line in wopen("livreDeLaNatureEtDesLacs.txt"):
    getarbre = re.findall('arbre suspendu', line)
    if getarbre != arbres:
        print("GPS ACTIVER")
        break
for line in wopen("desProjectilesEtDesDodos.txt"):
    getarbre = re.findall('arbre', line)
    getrocher = re.findall('rocher', line)
    getdodo = re.findall('Dodo', line)
    getlac = re.findall('lac', line)
    if getarbre != "":
        pas[1] += 10
        pas[0] += 10
    elif getrocher != "":
        pas[2] += 5
        pas[0] += 5
    elif getdodo != "":
        pas[3],pas[0] = pas[3]+6,pas[0]+6
    if pas[0] > 100 and getlac == ["lac"]:
        print("lac trouver")
        if pas[3] > pas[2] and pas[3] > pas[1]:
            print("on a fait plus de pas a droite")
        elif pas[2] > pas[3] and pas[2] > pas[1]:
            print("on a fait plus de pas a droite")
        elif pas[1] > pas[2] and pas[1] > pas[3]:
            print("on a fait plus de pas a droite")
        print("Vous avez fait : " + str(pas[0]) + " pas")
        break
with open("lafamilleDodo.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
        num = line.split(', ')
        num_sansdoubl = []
        for i in num:
            if i not in num_sansdoubl:
                if i == " ":
                    pass
                else:
                    num_sansdoubl.append(i)
num_sansdoubl = [int(x) for x in num_sansdoubl]
num_sansdoubl.sort()
print(num_sansdoubl)
with open("ageDodo.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
        num = line.split(', ')
        for i in num:
            if int(i) < 5:
                mineur += 1
            elif int(i) >= 5:
                majeur += 1
print("majeur : ", str(majeur)," + mineur : ", str(mineur))
