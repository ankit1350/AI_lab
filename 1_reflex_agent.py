def agent(rooms, loc):
    print("....Initial Environment:....")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Vacuum Location:", loc)

    print("....Actions Performed:....")
    while True:
        if rooms[loc]=="Dirty":
            print("Location :", loc)
            print("Percept :", loc, "is Dirty.")
            print("Action: Suck")
            rooms[loc]="Clean"
        else:
            if loc=="A":
                print("Location :", loc)
                print("Percept :", loc, "is Clean.")
                print("Action: Move Right")
                loc="B"
            elif loc=="B":
                print("Location :", loc)
                print("Percept :", loc, "is Clean.")
                print("Action: Move Left")
                loc="A"
        if rooms["A"]=="Clean" and rooms["B"]=="Clean":
            print("Both rooms are clean.")
            print("Agent goal achieved.")
            break
    print("......Final Environment:......")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Vacuum Location:", loc)


rooms = {"A": "Clean", "B": "Dirty"}
loc = "B"

agent(rooms, loc)