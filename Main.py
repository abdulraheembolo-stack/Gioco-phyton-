print("Benvenuto nel mio primo gioco mobile!")
punti = 0
risposta = input("Quanto fa 2 + 2? ")

if risposta == "4":
    print("Esatto! Hai guadagnato 10 punti.")
    punti = punti + 10
else:
    print("Sbagliato!")

print(f"Punteggio totale: {punti}")

