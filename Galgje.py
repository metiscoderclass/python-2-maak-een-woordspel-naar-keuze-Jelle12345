geheimwoord = "banaan"

print ("Welkom het spel hangman de bedoeling is dat je niet word opgehangen en dit moet je doen door 1 letter in te typen.")

aantalFouten = 0
while aantalFouten < 5:
    letter = input("Type een letter")
    if letter == "quit":
        break

    if letter in geheimwoord:
        print("je hebt het goed")
    else:
        print ("je hebt het verkeerd")
        print ("figuur1")
