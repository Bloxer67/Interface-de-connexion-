Identifiant = "Nabil"
Mot_de_passe = "Bahit"

connecté("False")

print("interface de connexion")
print("")

while connecté == "False":
    Identifiant2 = input("Entrez votre indentifiant > " )
    Mot_de_passe2 = input("Entrez votre mot de passe > ")

    if Identifiant == Identifiant2 and Mot_de_passe == Mot_de_passe2 :
        print ("vous êtes connecté , Bienvuenue ")
        connecté == "True"

    elif Identifiant == Identifiant2 or Mot_de_passe != Mot_de_passe2 :
        print("Identifiants incorrect, veuillez réessayer")
