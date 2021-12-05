nev = input("Mi a kutyája neve: ")
fajta = input("Mi a kutyájának a fajtája: ")
kor = input("Hány éves a kutyája : ")
igazolas = input("van e védettségi oltása a kutyájának: ")

lista = [nev, fajta, kor, igazolas]
print(lista)
print("")
kutya = {
    "neve": nev,
    "eddig eltelt ideje": kor,
    "igazolvany": igazolas,
    "faj": fajta
    }
print(kutya)