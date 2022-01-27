print("Velkommen til IM1A Quiz!")

playing = input("Vil du spille? ")

if playing.lower() != "ja":
    quit()

print("Supert! La oss starte :)")
score = 0

answer = input("Hva heter UTV læreren våres? ")
if answer.lower() == "tor":
    print('Riktig!')
    score += 1
else:
    print("Feil, klarer du ikke å huske navn?!")

answer = input("Hvor kommer Haidas fra? ")
if answer.lower() == "litauen":
    print('Riktig!')
    score += 1
else:
    print("Feil!")

answer = input("Hvor høy er Maziu? ")
if answer.lower() == "167":
    print('Riktig!')
    score += 1
else:
    print("Feil, ta med en linjal i morgen og prøv på nytt!")

answer = input("Hvilke pcer har vi på skolen? ")
if answer.lower() == "mac":
    print('Riktig!')
    score += 1
else:
    print("Feil! Se på logoen bak pcen din")

answer = input("Hvor mange er vi i klasse IM2A? ")
if answer.lower() == "13":
        print('Riktig!')
        score += 1
else:
        print("Feil, Klarer du ikke å telle!?")

answer = input("Hvor gammel er Romandus? ")
if answer.lower() == "17":
            print('Riktig!')
            score += 1
else:
            print("Feil!? Hvordan ka du få feil på dette?")

answer = input("Hva heter hovedlæreren våres? ")
if answer.lower() == "stein":
                print('Riktig!')
                score += 1
else:
                print("Feil, Du må huske bedre!?")

answer = input("Hva måned har Deimantas bursdag? ")
if answer.lower() == "juni":
                    print('Riktig!')
                    score += 1
else:
                    print("Feil, Vet ikke du din klassekammerat sin bursdag?!?")

answer = input("Hvor høy er Bendik? ")
if answer.lower() == "186":
                        print('Riktig!')
                        score += 1
else:
                        print("Feil, He is a tall man!?")

answer = input("Hva er Bendik og Eirik? ")
if answer.lower() == "venner":
                            print('Riktig!')
                            score += 1
else:
                            print("Feil, are you diry minded!?")


print("Du fikk " + str(score) + " spørsmål riktig!")
print("Du fikk " + str((score / 10) * 100) + "% korrekt.")