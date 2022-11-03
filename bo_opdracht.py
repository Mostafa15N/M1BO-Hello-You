import time
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "J" ,"j" ,"ja"]
no = ["N", "n", "no","nee"]
required1 = ("\nUse only A, B\n")
required = ("\nUse only A, B, or C\n")
eind_1 = ("Jij en je hele familie zijn dood gegaan. Jullie hadden een heel moeilijk leven. Je kent nu rusten met je familie in het paradijs.")
eind_2 = ("De soldaten schieten je niet en nemen je mee in het leger en je werkt nu met hen.")
eind_3 = ("Je woont samen met je broertje in vredes.")
eind_4 = ("Je gaat met je broertje met hen wonnen en leven samen en gelukkig.")

print("Het verhaal van een vluchteling")
def start():
    choice = input("Wil je het spel starten? J/N ")
    if choice in yes:
        intro()
    elif choice in no:
        print()
    else:
        start()

def intro():
    print("\nOpeens zit je opgesloten in huis: naar buiten gaan was veel te gevaarlijk. Je hebt geen water. Geen elektriciteit en amper eten.")
    print("Uit verveling telden mijn vrienden en jij de bommen. Eén keer vielen er 101 achterelkaar. In de tuin vond ik 96 kogels.")
    print("Zo dichtbij was de oorlog. Voor het slapen was je bang: zou je morgen weer wakker worden? Als dat gebeurde.")
    print("Was je nog steeds bang: wie was er vandaag aan de beurt?")
    print("Je hebt al veel vrienden en kennissen verloren. Voor de oorlog leefde je een luxeleven.")
    print("Je had veel vrienden, een grote familie en zelfs een eigen chauffeur die je naar school bracht.")
    print("Nooit had je gedacht dat het oorlog kon worden in jouw land. In jouw stad. Eigenlijk kan ik het nog steeds niet geloven.")
    print("Je stad werd omsingeld. Er konden geen mensen meer in en uit.")
    print("Toch maakte je vader stiekem gevaarlijke reizen naar andere steden om aan eten te komen.\n")
    time.sleep(1)
    stuk_1()


def stuk_1():
    print("\nOpeens zegt je vader dat jullie weg moeten vluchten, omdat het niet meer veilig is in het land en dat jullie naar Turkije moeten vluchten.")
    print("Jullie gaan laat in de nacht verterekken. Je wil niet weg van je land gaan maar je weet niet wat je moet doen.")
    time.sleep(1)
    print("\n[A] je besluit om te verstoppen tot dat je ouders weggaan")
    print("[B] je gaat met hen en verlaat je land voor een veilig en beter leven\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_2()
    elif choice in answer_B:
        stuk_3()
    else:
      print (required1)
      stuk_1()

def stuk_2():
    print("\nJe verstopt in een kast. Je ouders vinden je niet en willen snel gaan voordat iemand hun ziet.")
    print("Ze roepen je naam en willen je niet achterlaten, maar je weet niet wat je moet doen je land verlaten of heer blijven.")
    print(" _______________________________________ ")
    print("|    | _______ | _______ |  |           |")
    print("|    ||       |||       ||  |           |")
    print("|    ||       |||       ||  |           |")
    print("|    ||       |||       ||  |           |")
    print("|    ||       |||       ||  |           |")
    print("|    ||     O ||| O     ||  |           |")
    print("|    ||       |||       ||  |___________|")
    print("|    ||       |||       ||  |___________|")
    print("|   /||_______|||_______|| /            |")
    print("|  / |_________|_________|/             |")
    print("| / /                                   |")
    print("|/ /                                    |")
    print("| /                                     |")
    print("|/______________________________________|")
    time.sleep(1)
    print("\n[A] Je komt uit de kast en gaat met hen en verlaat je land voor een veilig leven")
    print("[B] Je blijft in de kast en besluit om daar te blijven\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_3()
    elif choice in answer_B:
        stuk_4()
    else:
     print (required1)
     stuk_2()

def stuk_3():
    print("\nJullie nemen het overige eten mee en een baar klieren. Jullie nemen niet te veen spullen me om ")
    print("beter te kunnen rijzen. Buiten staat een auto geparkeerd. Je vader zegt dat hij deze auto heeft ")
    print("gekocht en dat jullie er mee gaan rijzen. Jullie stappen erin en zetten jullie spullen in de achterbak je ")
    print("vader start de auto en hier begint je rijs.\n")
    print("Op de grens van het land komen jullie soldaten tegen ze vragen wie we jullie zijn en waar jullie ")
    print("naartoe gaan. Opeens stapt je vader uit de auto en spreekt met de agent en komt weer terug.")
    print("Je vader zegt dat jullie uit moeten stappen.")
    print(" _______________________________________ ")
    print("|                                       |")
    print("|     ____                   _____      |")
    print("|    /    \              ___/     \___  |")
    print("|    \____/     ___     /_____________\ |")
    print("|           ___/   \_                   |")
    print("|          /__________\                 |")
    print("|                                       |")
    print("|          ______________               |")
    print("|         / /    |||    \ \             |")
    print("|    ____/||_____|||_____\ \________    |")
    print("|  /  ____| -     | -      |  ____  \   |")
    print("|  |_//   \_______|________|_//   \_|   |")
    print("|____\ __//__________________\ __//_____|")
    print("|_______________________________________|")
    time.sleep(1)
    print("\n[A] Je gaat uit stappen ")
    print("[B] je blijft in de auto zitten omdat je bang bent\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_5()
    elif choice in answer_B:
        stuk_6()
    else:
     print (required1)
     stuk_3()

def stuk_4():
    print("\nJe ouder konden je helemaal niet vinden en besluiten om niet weg te gaan en thuis te blijven. Maar ")
    print("de volgende dag is een bom op dicht bij jullie huis gevallen jullie huis is helemaal neergestort. ")
    print(" _______________________________________ ")
    print("|                                       |")
    print("|                                       |")
    print("|                                       |")
    print("|                     \                 |")
    print("|              /     /  \               |")
    print("|             / \   /    \              |")
    print("|      \    /    \ (      )   /         |")
    print("|      / \  |    |  )    (  /  \        |")
    print("|     |   \ \     \/     / |    |       |")
    print("|     \    \/            \/    /        |")
    print("|      |        ______        |         |")
    print("|      |       |      |       |         |")
    print("|      |       |O     |       |         |")
    print("|______|_______|______|_______|_________|")
    time.sleep(1)
    print("\n", eind_1)
    time.sleep(.5)
    eind()

def stuk_5():
    print("\nJe stapt uit de auto maar je moeder is bang om uit te stappen. Je vader vertelt haar dat ze eruit moet ")
    print("stappen anders gaan de agenten haar dood schieten.")
    time.sleep(1)
    print("\n[A] Je vertelt je moeder dat ze van de auto af moet anders wordt ze dood ")
    print("[B] Je wordt bang en stapt nog een keer in de auto\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_7()
    elif choice in answer_B:
        stuk_6()
    else:
      print (required1)
      stuk_5()

def stuk_6():
    print("\nJe wordt doodgeschoten in de auto met je hele familie \n")
    print(" _______________________________________ ")
    print("|                     \                 |")
    print("|              /     /  \               |")
    print("|             / \   /    \              |")
    print("|      \    /    \ (      )   /         |")
    print("|      / \  |    |  )    (  /  \        |")
    print("|     |   \ \     \/     / |    |       |")
    print("|     \    \/            \/    /        |")
    print("|     |   / /    |||    \ \    \        |")
    print("|    __\ /||_____|||_____\ \___/____    |")
    print("|  /  ____| -     | -      |  ____  \   |")
    print("|  |_//   \_______|________|_//   \_|   |")
    print("|____\ __//__________________\ __//_____|")
    print("|_______________________________________|")
    print(eind_1)
    eind()

def stuk_7():
    print("\nJe moeder stapt uit de auto. De agent zegt dat jullie weg moeten rennen. En dat de agenten jullie ")
    print("van achter gaan schieten en wie er overleeft. Laten ze hem met rust en mag uit het land vluchten")
    print("Jullie hebben geen keuze meer en rennen zo snel weg. De soldaten schieten jullie. Je klein broertje ")
    print("wordt op zijn been geschoten.")
    print(" _______________________________________ ")
    print("|                                       |")
    print("|     ____                   _____      |")
    print("|    /    \              ___/     \___  |")
    print("|    \____/     ___     /_____________\ |")
    print("|           ___/   \_                   |")
    print("|          /__________\                 |")
    print("|_______________________________________|")
    print("|  /﹋\                     /﹋\        |")
    print("|           /﹋\                 /﹋\   |")
    print("|   _/﹋\_           _/﹋\_             |")
    print("|   ( `_`)           (҂`_`)             |")
    print("|   <,︻╦╤─ ҉ - -    <,︻╦╤─ ҉ - -        |")
    print("|   _/﹋\_           _/﹋\_             |")
    print("|_______________________________________|")
    time.sleep(1)
    print("\n[A] Je gaat naar je broertje om hem te reden")
    print("[B] Je laat je broertje achter en rent om te overleven\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_8()
    elif choice in answer_B:
        stuk_9()
    else:
      print (required1)
      stuk_7()

def stuk_8():
    print("\nJe vader ziet je en rent naar je toe om je te reden. Hij tilt je en je broertje en rent weg. Hij krijgt een ")
    print("baar kogels in zijn rug, maar hij blijft nog rennen. Hij zet jullie achter een grote steen. En gaat terug ")
    print("om je moeder te zoeken. Na een tijdje komt je vader niet.")
    print(""" _______________________________________
|                                       |
|     ____                   _____      |
|    /    \              ___/     \___  |
|    \____/     ___     /_____________\ |
|           ___/   \_                   |
|          /__________\                 |
|_______________________________________|
|  /﹋\                     /﹋\        |
|           /﹋\                 /﹋\   |
|﹋﹋﹋﹋﹋\       _/﹋\_               |
|        ☻/ \      (o-o )               |
|   ☻   /▌   \     /\  /\               |
|  /▌_  / \   \    _/﹋\_               |
|_______________________________________|""")
    time.sleep(1)
    print("\n[A] Je komt achter het steen om je vader te zoeken ")
    print("[B] Je besluit om te wachten tot dat je vader komt. ")
    print("[C] Je besluit om weg te gaan om je broertje te reden, omdat hij veel bloed kwijt heeft geraakt\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_10()
    elif choice in answer_B:
        stuk_11()
    elif choice in answer_C:
        stuk_12()
    else:
      print (required)
      stuk_8()

def stuk_9():
    print("\nJe blijft rennen. Je vader weet niet dat je broertje is neergeschoten en blijft rennen. Daarna wordt je ")
    print("vader ook op zijn been geschoten, maar hij blijft rennen. Je ziet een grote steen.")
    print(" _______________________________________ ")
    print("|                                       |")
    print("|     ____                   _____      |")
    print("|    /    \              ___/     \___  |")
    print("|    \____/     ___     /_____________\ |")
    print("|           ___/   \_                   |")
    print("|          /__________\                 |")
    print("|_______________________________________|")
    print("|  /﹋\                     /﹋\        |")
    print("|      /﹋\                      /﹋\   |")
    print("|         /﹋﹋﹋﹋﹋\                  |")
    print("|        /            \                 |")
    print("|       /              \                |")
    print("|      /                \               |")
    print("|_______________________________________|")
    time.sleep(1)
    print("\n[A] je gaat achter het steen schuilen")
    print("[B] je blijft door rennen\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_13()
    elif choice in answer_B:
        stuk_14()
    else:
      print (required1)
      stuk_9()

def stuk_10():
    print("\nJe ziet je vader en moeder dood op de grond liggen.")
    print(" _______________________________________ ")
    print("|                                       |")
    print("|     ____                   _____      |")
    print("|    /    \              ___/     \___  |")
    print("|    \____/     ___     /_____________\ |")
    print("|           ___/   \_                   |")
    print("|          /__________\                 |")
    print("|_______________________________________|")
    print("|      /﹋\               /﹋\          |")
    print("|                 /﹋\                  |")
    print("|                                       |")
    print("|                                       |")
    print("|         O-|--<                        |")
    print("|                  O-|--<               |")
    print("|_______________________________________|")
    time.sleep(1)
    print("\n[A] Je besluit om weg te gaan om je broertje te reden, omdat hij veel bloed kwijt heeft geraakt ")
    print("[B] Je rent naar je ouders \n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_12()
    elif choice in answer_B:
        stuk_15()
    else:
      print (required1)
      stuk_10()

def stuk_11():
    print("\nJe vader komt niet")
    time.sleep(1)
    print("\n[A] Je komt achter het steen om je vader te zoeken ")
    print("[B] Je besluit om weg te gaan om je broertje te reden, omdat hij veel bloed kwijt heeft geraakt \n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_10()
    elif choice in answer_B:
        stuk_12()
    else:
      print (required1)
      stuk_11()

def stuk_12():
    print("\nJe zet je broertje op je rug en loopt tot dat je huizen en mensen ziet. De mensen zien jullie en pellen ")
    print("de ambulance om je broertje te reden. De kogel in je broertje been wordt weggehaald maar hij kan ")
    print("niet meer lopen. Je hoeft niets voor het ziekenhuis te betalen, maar jullie weten niet waar jullie heen moeten.")
    print(" _______________________________________ ")
    print("|                                       |")
    print("|       ______________________          |")
    print("|      |       ________        |        |")
    print("|      |      |  _| |_  |      |        |")
    print("|      |      | |_   _| |      |        |")
    print("|      |      |___|_|___|      |        |")
    print("|      |_______________________|        |")
    print("|      |        ______         |        |")
    print("|      |       ||----||        |        |")
    print("|      |       ||----||        |        |")
    print("|______|_______||----||________|________|")
    time.sleep(1)
    print("\n[A] je gaat naar de gemeente ")
    print("[B] je zoekt werk\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_16()
    elif choice in answer_B:
        stuk_17()
    else:
      print (required1)
      stuk_12()

def stuk_13():
    print("\nJe schuilt achter het steen. Je kijkt achter je en je ziet je ouders dood op de grond liggen.")
    print("De soldaten zijn gestopt met schieten.")
    print(" _______________________________________ ")
    print("|                                       |")
    print("|     ____                   _____      |")
    print("|    /    \              ___/     \___  |")
    print("|    \____/     ___     /_____________\ |")
    print("|           ___/   \_                   |")
    print("|          /__________\                 |")
    print("|_______________________________________|")
    print("|      /﹋\               /﹋\          |")
    print("|                 /﹋\                  |")
    print("|                                       |")
    print("|                                       |")
    print("|     ☻   O-|--<                        |")
    print("|    /▌_            O-|--<              |")
    print("|_______________________________________|")
    time.sleep(1)
    print("\n[A] Je besluit om je broertje te reden, omdat hij veel bloed kwijt heeft geraakt en snel weg gaan.")
    print("[B] Je rent naar je ouder\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_12()
    elif choice in answer_B:
        stuk_15()
    else:
      print (required1)
      stuk_13()

def stuk_14():
    print("\nJe wordt doodgeschoten en je hele familie wordt dood")
    print(" _______________________________________ ")
    print("|                                       |")
    print("|     ____                   _____      |")
    print("|    /    \              ___/     \___  |")
    print("|    \____/     ___     /_____________\ |")
    print("|           ___/   \_                   |")
    print("|          /__________\                 |")
    print("|_______________________________________|")
    print("|      /﹋\               /﹋\          |")
    print("|                 /﹋\                  |")
    print("|                                       |")
    print("|                       O-|--<          |")
    print("|         O-|--<                        |")
    print("|   O-|-<         O-|--<                |")
    print("|_______________________________________|")
    print(eind_1)
    time.sleep(.5)
    eind()

def stuk_15():
    print("\nDe soldaten zien je, maar ze schieten je niet. Ze zegen dat ze je dood gaan schieten als je niet weg rent.")
    time.sleep(1)
    print("\n[A] je rent weg en gaat naar je broertje")
    print("[B] je blijft staan\n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_12()
    elif choice in answer_B:
        print(eind_2)
        eind()
    else:
      print (required1)
      stuk_15()

def stuk_16():
    print("\nDe gemeente stuurt je naar een vluchtelingenkamp, maar je vindt het niet leuk daar en wilt een normaal leven.")
    print(""" _______________________________________ 
|                                       |
|     ____                   _____      |
|    /    \              ___/     \___  |
|    \____/     ___     /_____________\ |
|           ___/   \_                   |
|          /__________\                 |
|_______________________________________|
|           ____________________        |
|         / \                   \       |
|        / | \                   \      |
|       /  |  \                   \     |
|      /   |   \                   \    |
|     /    |    \                   \   |
|    /     |     \                   \  |
|_______________________________________|
    """)
    time.sleep(1)
    print("\n[A] Je blijft in het vluchtelingenkamp met je broertje")
    print("[B] Je gaat werk zoeken ")
    print("[C] je vraagt de gemeente of je naar school kan \n")
    choice = input(">>> ")
    if choice in answer_A:
        stuk_18()
    elif choice in answer_B:
        stuk_19()
    elif choice in answer_C:
        stuk_20()
    else:
      print (required)
      stuk_16()

def stuk_17():
    print("\nJe gaat voor werk zoeken wat wil je werken")
    time.sleep(1)
    print("\n[A] schoonmaken ")
    print("[B] Bij bakkerij ")
    print("[C] Bij supermarkt \n")
    choice = input(">>> ")
    if choice in answer_A or answer_B or answer_C:
        stuk_23()
    else:
      print (required)
      stuk_17()

def stuk_18():
    print("\nNa een tijdje komt een Turkse familie om je en je broertje te adopteren en bij hen te wonnen.")
    time.sleep(1)
    print("\n[A] je gaat met hen mee ")
    print("[B] je wil niet met hun leven en wil alleen met je broertje leven\n")
    choice = input(">>> ")
    if choice in answer_A:
        print(eind_4)
        time.sleep(.5)
        eind()
    elif choice in answer_B:
        stuk_21()
    else:
      print (required1)
      stuk_18()

def stuk_19():
    print("\nJe gaat voor werk zoeken wat wil je werken")
    time.sleep(1)
    print("\n[A] schoonmaken ")
    print("[B] Bij bakkerij ")
    print("[C] Bij supermarkt \n")
    choice = input(">>> ")
    if choice in answer_A or answer_B or answer_C:
        stuk_22()
    else:
      print (required)
      stuk_19()

def stuk_20():
    print("\nDe gemeente schrijft je en je broertje in op school en na een tijdje komt een Turkse familie om je en ")
    print("je broertje te adopteren en bij hen te wonnen.")
    print(""" _______________________________________ 
|                                       |
|     ____                   _____      |
|    /    \              ___/     \___  |
|    \____/     ___     /_____________\ |
|           ___/   \_                   |
|          /__________\                 |
|          ____________________         |
|         /                    \        |
|        /______________________\       |
| ________|      |School|      |_______ |
|/________| _    _      _    _ |_______\|
| _    _  || |  | |    | |  | || _    _ |
|| |  | | |        ___         || |  | ||
|_________|       |   |        |________|
|_________|_______|___|________|________|
    """)
    time.sleep(1)
    print("\n[A] je gaat met hen mee ")
    print("[B] je wil niet met hun leven en wil alleen met je broertje leven \n")
    choice = input(">>> ")
    if choice in answer_A:
        print(eind_4)
        time.sleep(.5)
        eind()
    elif choice in answer_B:
        stuk_21()
    else:
      print (required1)
      stuk_20()

def stuk_21():
    print("\nNa een tijde geeft de gemeente jullie een Wooning. ")
    print("""____________^v^_____^v^
    _________¶¶¶¶___^v^
    _______¶¶¶¶¶¶¶_____^v^
    ______¶¶¶¶¶¶¶¶¶¶_________/
    ____¶¶¶¶¶¶¶¶¶¶¶¶¶_____--- ---
    __¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____/_
    ___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____^v^
    ____¶¶¶¶¶¶¶¶¶¶¶¶¶________^v^
    _______¶¶I_I¶¶¶¶_______¶¶¶¶
    _________I_I___________¶¶¶¶
    ___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    __¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    _¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ___¶_________________________¶
    ___¶__¶¶¶¶¶¶__¶¶¶¶¶__¶¶¶¶¶___¶
    ___¶__¶¶¶¶¶¶__¶¶¶¶¶__¶¶¶¶¶___¶
    ___¶__¶¶¶¶¶¶__¶¶¶¶¶__¶¶¶¶¶___¶
    ___¶__¶¶¶¶¶¶_________________¶__o
    ___¶__¶¶¶¶¶¶_________________¶_(|/)
    ___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    """)
    time.sleep(1)
    print(eind_3)
    time.sleep(.5)
    eind()

def stuk_22():
    print("\nJe hebt nu werk en na een tijdje komt een Turkse familie om je en je broertje te adopteren en bij hen te wonnen.")
    time.sleep(1)
    print("\n[A] je gaat met hen mee ")
    print("[B] je wil niet met hun leven en wil alleen met je broertje leven \n")
    choice = input(">>> ")
    if choice in answer_A:
        print(eind_3)
        time.sleep(2)
        eind()
    elif choice in answer_B:
        stuk_21()
    else:
      print (required1)
      stuk_22()

def stuk_23():
    print("\nJe helpt nu werk maar geen blek om te wonnen, dus je huurt een huis en schrijft je broertje op school. ")
    time.sleep(1)
    print(eind_3)
    time.sleep(.5)
    eind()

def eind():
    print("\nDit is het eind van het spel\n")
    choice = input("Wil je nog een keer spelen? J/N ")
    if choice in yes:
        intro()
    elif choice in no:
        print()
    else:
        eind()

start()
