chaine = "abcdefghijklmnopqrstuvwxyz"
index = 1  
while True:  
    if index <= 26: 
        print(chaine[:index])  
        index += 1  
    elif index > 26:  
        break  
    else:
      print("Erreur: Index non valide.")  
