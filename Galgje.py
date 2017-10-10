geheimwoord = "cola"
geheimlijst = ["c", "o", "l", "a"]
einde = len(geheimlijst)*("_")
geraden = ""

print ("Welkom het spel hangman de bedoeling is dat je niet word opgehangen en dit moet je doen door 1 letter in te typen en als je een woord wil intypen dan moet je het vraagteken invoeren.")
aantalgoed = 0
aantalletters = ""
aantalFouten = 0
figuur1 = "==================="
figuur2 = "|"
galg = "( )"
galg1 ="/|\ "
galg2 = "/ \ "
alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","?"]

while aantalFouten < 5:
    letter = input ("Type een letter.")
    Lijst = letter
    print ("Dit is de letter die je hebt gebruikt:" + " " + Lijst)

    if letter == "quit":
        print("het spel is gestopt het woord was" + " " + geheimwoord)
        break

    if letter in alfabet:
        if letter in geheimlijst:
                tijdelijk = geheimlijst.index(letter)
                list1 = list(einde)
                list1[tijdelijk] = letter
                einde2 = "".join(list1)
                geraden += letter
                print(geraden)
                if geraden == geheimwoord:
                    print("Goedzo je hebt het woord geraden!")
                    break
        print ("")
    else:
        print("als je een woord wil intypen dan moet je het vraagteken invoeren")


    if letter == "?":
        school = input ("Type een woord")
        Lijst = school
        print ("Dit is het woord die je hebt gebruikt:" + " " + Lijst)
        if school == geheimwoord:
            print ("Yee je hebt het woord geraden.")
            break

    if letter in geheimwoord:
        aantalletters = aantalletters + letter
        print("je hebt het goed")

    elif letter in aantalletters:
        print("je hebt de letter al geraden")

    else:
        print ("je hebt het verkeerd")
        aantalFouten = aantalFouten + 1

    if aantalFouten == 1:
        print (figuur1)
        print ("je hebt nu 1 fout")

    if aantalFouten == 2:
        print (figuur1)
        for i in range (5):
                print (figuur2)
        print ("je hebt nu twee fouten")


    if aantalFouten == 3:
    print (figuur1)
    for i in range (5):
            print (figuur2)
    print (figuur1)
    print ("je hebt nu drie fouten")


    if aantalFouten == 4:
        print (figuur1)
        print("|" + " " + " "+ " " + " "+ " " + " "+ " " + " " + " " + " "+ " " + " " + "|")
        for i in range (5):
                print (figuur2)
        print (figuur1)
        print ("je hebt nu vier fouten")


    if aantalFouten == 5:
        print (figuur1)
        print("|" + " " + " "+ " " + " "+ " " + " "+ " " + " " + " " + " "+ " " + " " + "|")
        print("|" + " " + " "+ " " + " "+ " " + " "+ " " + " " + " " + " "+ " " + galg)
        print("|" + " " + " "+ " " + " "+ " " + " "+ " " + " " + " " + " "+ " " + galg1)
        print("|" + " " + " "+ " " + " "+ " " + " "+ " " + " " + " " + " "+ " " + galg2)
        for i in range (5):
                print (figuur2)
        print (figuur1)
        print ("je hebt nu vijf fouten")
        print ("GAME OVER")
        print ("je bent opgehangen het woord was :(" + " " + geheimwoord)
