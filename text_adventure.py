rummet = [ ["Du vaknar upp står på en mörk återvändsgränd som leder norr.\nHuvudet värker och du vill hem.", "soptunna", "trasig cykel", "spindel"],
          ["Du är i en park med gröna fina träd.", "nyckel", "stenbumling"],
          ["Du står framför ditt hus", "vattenkanna", "låst dörr"] ]
korg = []
rum = 0

def skriv ():
    global rum, rummet, korg
    print ("\nPlats", rum)
    print (rummet[rum][0]) # Skriv ut beskrivningen av rummet
    print ("Här finns: ", end="")
    for i in range (1, len(rummet[rum])):
        print (rummet[rum][i], end = "")
        if i != len(rummet[rum]) - 1:
            print (", ", end = "")
    print ("\nI din ficka har du:", korg)

def ta_upp (sak):
    global rum, rummet, korg
    try:
        plats_i_listan = rummet[rum].index (sak.lower())
    except:
        print ("Det finns inget sånt här.")
        return
    korg.append (rummet[rum][plats_i_listan])
    rummet[rum].pop (plats_i_listan)

while rum < len(rummet):
    skriv ()
    sak = input ("Gå norr eller söder? Något du vill ta upp?")
    if (sak.lower() == "norr"):
        if (rum == 2 and not "nyckel" in korg):
            print ("Du kan inte låsa upp dörren och gå norr.")
            continue
        rum += 1

    elif (sak.lower() == "söder"):
        rum -= 1
        if (rum < 0):
            print ("Du kan inte gå längre söder ut.")
            rum = 0
    else:
        ta_upp (sak)

print ("Du har kommit hem!\nGrattis du har klarat spelet!")