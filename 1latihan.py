import os
import random
import string
lanjut = "y"
id = []
mapel = []
guru = []
hari = []
jam = []
ruangan = []
# a = {"" : ""}
# ak = dict.fromkeys(a.keys())
ulang = 0
data = {
    "id" : "",
    "mapel" : "",
    "guru" : "",
    "hari" : "",
    "jam" : "",
    "ruangan" : ""
}
datas = dict.fromkeys( data.keys() )
while lanjut.lower() == "y":
    print("*"*10, "DAFTAR MAPEL", "*"*10)
    ulang += 1
    id = "MPL"+"".join(random.choice( string.ascii_uppercase ) for i in range ( 3 ) )
    mapel.append(input("Mapel\t : "))
    guru.append(input("guru\t : "))
    hari.append(input("hari\t : "))
    jam.append(input("jam\t : "))
    ruangan.append(input("ruangan\t : "))
    lanjut = input("lanjut (y/t) ? ")
    if lanjut.lower() == "y":
        os.system( "cls" )
    else:
        print("*"*50)
        print("ID \t MAPEL \t GURU \t HARI \t JAM \t RUANGAN")
        print("*"*50)
        for i in range(ulang):
            datas["id"] = "MPL"+"".join(random.choice( string.ascii_uppercase ) for i in range ( 3 ) )
            datas["mapel"] = mapel[i]
            datas["guru"] = guru[i]
            datas["hari"] = hari[i]
            datas["jam"] = jam[i]
            datas["ruangan"] = ruangan[i]
            print(f"{datas['id']}\t{datas['mapel']}\t{datas['guru']}\t{datas['hari']}\t{datas['jam']}\t{datas['ruangan']} ")
        break
    # datas["id"] = "MPL"+"".join(random.choice( string.ascii_uppercase ) for i in range ( 3 ) )
    # datas["mapel"] = mapel
    # datas["guru"] = guru
    # datas["hari"] = hari
    # datas["jam"] = jam
    # datas["ruangan"] = ruangan
    # else:
        # print("*"*50)
        # print("ID \t MAPEL \t GURU \t HARI \t JAM \t RUANGAN")
        # print("*"*50)
        # NewData = { data( i for i in range(4)) }
        # print( f"{NewData}")
        # print( f' id\t mapel\t guru\t hari\t jam \t ruangan ' )
        # print(f"{datas['id']}\t{datas['mapel']}\t{datas['guru']}\t{datas['hari']}\t{datas['jam']}\t{datas['ruangan']} ")
    # ulang = ulang + 1
# print("*"*50)
# print("ID \t MAPEL \t GURU \t HARI \t JAM \t RUANGAN")
# print("*"*50)
# for i in range (ulang):
#     datas["id"] = "MPL"+"".join(random.choice( string.ascii_uppercase ) for i in range ( 3 ) )
#     datas["mapel"] = mapel
#     datas["guru"] = guru
#     datas["hari"] = hari
#     datas["jam"] = jam
#     datas["ruangan"] = ruangan
    # NewData = { data( i for i in range(4)) }
    # print( f"{NewData}")
    # print( f' id\t mapel\t guru\t hari\t jam \t ruangan ' )
    # print(f"{datas['id']}\t{datas['mapel']}\t{datas['guru']}\t{datas['hari']}\t{datas['jam']}\t{datas['ruangan']} ")
# print( f"ulang = {ulang}")