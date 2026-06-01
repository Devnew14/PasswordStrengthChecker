from zxcvbn import zxcvbn


#J'entre un mot de passe !
password = input("Entrez votre mot de passe : ")


#je stocke la variable 
result = zxcvbn(password)



print("\n Analyse du mot de passe ")
print(f"Score : {result['score']} / 4")



#je presente ici les differents résultats en fonciton de la longueur du mot de passe 
if result["score"] == 0:
    print("Très faible")
elif result["score"] == 1:
    print("Faible")
elif result["score"] == 2:
    print("Moyen")
elif result["score"] == 3:
    print("Fort")
else:
    print("Très fort")



#represente le temps estimé pour trouve le mot de passe 
print(f"\nTemps estimé pour le casser :")
print(result["crack_times_display"]["offline_slow_hashing_1e4_per_second"])

if result["feedback"]["warning"]:
    print("\nAvertissement :")
    print(result["feedback"]["warning"])

if result["feedback"]["suggestions"]:
    print("\nSuggestions :")
    for suggestion in result["feedback"]["suggestions"]:
        print("-", suggestion)
