def chape_khat():
    for i in range(1, 41):
        print("-", end="")
    print()

list_daramad = []
list_hazine = []
list_hazine_daste = []

daste_ha = ["khorak", "raft o amad", "tafrih", "ghabz", "sayer"]

print("be sistem modiriat hazine khosh amadid")

while True:
    chape_khat()
    menu = input("1.sabt daramad 2.sabt hazine 3.jam daramad va hazine 4.mojoodi 5.bishtarin hazine 6.gozaresh dasteh ha 7.jostojoo 8.hazf akharin hazine 9.exit:")

    match menu:
        case "1":
            mablagh = int(input("mablagh daramad (toman):"))
            if mablagh <= 0:
                print("mablagh bayad bishtar az 0 bashad")
            else:
                list_daramad.append(mablagh)
                print("daramad sabt shod")

        case "2":
            mablagh = int(input("mablagh hazine (toman):"))
            print("1.khorak 2.raft o amad 3.tafrih 4.ghabz 5.sayer")
            entekhab = input("dasteh bandi ra entekhab kon:")

            match entekhab:
                case "1":
                    dasteh = "khorak"
                case "2":
                    dasteh = "raft o amad"
                case "3":
                    dasteh = "tafrih"
                case "4":
                    dasteh = "ghabz"
                case "5":
                    dasteh = "sayer"
                case _:
                    dasteh = ""

            mojoodi = sum(list_daramad) - sum(list_hazine)

            if dasteh == "":
                print("dasteh bandi eshtebah ast")
            elif mablagh <= 0:
                print("mablagh bayad bishtar az 0 bashad")
            elif mablagh > mojoodi:
                print("mojoodi kafi nist , mojoodi shoma:", mojoodi)
            else:
                list_hazine.append(mablagh)
                list_hazine_daste.append(dasteh)
                print("hazine sabt shod")

        case "3":
            print("jame daramad:", sum(list_daramad), "toman")
            print("jame hazine:", sum(list_hazine), "toman")
            print("tedad daramad ha:", len(list_daramad))
            print("tedad hazine ha:", len(list_hazine))

        case "4":
            mojoodi = sum(list_daramad) - sum(list_hazine)
            print("mojoodi hesab shoma:", mojoodi, "toman")

        case "5":
            if len(list_hazine) == 0:
                print("hanooz hazine i sabt nashode")
            else:
                bishtarin = list_hazine[0]
                shomare = 0
                for i in range(len(list_hazine)):
                    if list_hazine[i] > bishtarin:
                        bishtarin = list_hazine[i]
                        shomare = i
                print("bishtarin hazine:", bishtarin, "toman")
                print("babate:", list_hazine_daste[shomare])

        case "6":
            if len(list_hazine) == 0:
                print("hanooz hazine i sabt nashode")
            else:
                jam_kol = sum(list_hazine)
                bishtarin_jam = 0
                bishtarin_dasteh = ""

                chape_khat()
                for dasteh in daste_ha:
                    jam_dasteh = 0
                    for i in range(len(list_hazine)):
                        if list_hazine_daste[i] == dasteh:
                            jam_dasteh = jam_dasteh + list_hazine[i]

                    tedad = list_hazine_daste.count(dasteh)
                    darsad = jam_dasteh * 100 / jam_kol
                    print(dasteh, ":", tedad, "ta hazine , jam", jam_dasteh, "toman ,", darsad, "darsad")

                    if jam_dasteh > bishtarin_jam:
                        bishtarin_jam = jam_dasteh
                        bishtarin_dasteh = dasteh

                chape_khat()
                print("bishtarin hazine shoma dar dasteh", bishtarin_dasteh, "ast")

        case "7":
            nooe = input("1.jostojoo ba mablagh 2.jostojoo ba dasteh bandi:")

            if nooe == "1":
                mablagh_jostojoo = int(input("che mablaghi ra donbal mikoni:"))
                peyda_shod = 0
                for i in range(len(list_hazine)):
                    if list_hazine[i] == mablagh_jostojoo:
                        print(mablagh_jostojoo, "toman kharj shode baraye:", list_hazine_daste[i])
                        peyda_shod = peyda_shod + 1
                if peyda_shod == 0:
                    print("hazine i ba in mablagh peyda nashod")

            elif nooe == "2":
                print("1.khorak 2.raft o amad 3.tafrih 4.ghabz 5.sayer")
                entekhab = input("dasteh bandi ra entekhab kon:")
                match entekhab:
                    case "1":
                        dasteh_jostojoo = "khorak"
                    case "2":
                        dasteh_jostojoo = "raft o amad"
                    case "3":
                        dasteh_jostojoo = "tafrih"
                    case "4":
                        dasteh_jostojoo = "ghabz"
                    case "5":
                        dasteh_jostojoo = "sayer"
                    case _:
                        dasteh_jostojoo = ""

                if dasteh_jostojoo == "":
                    print("dasteh bandi eshtebah ast")
                else:
                    peyda_shod = 0
                    for i in range(len(list_hazine)):
                        if list_hazine_daste[i] == dasteh_jostojoo:
                            print(dasteh_jostojoo, ":", list_hazine[i], "toman")
                            peyda_shod = peyda_shod + 1
                    if peyda_shod == 0:
                        print("hazine i dar in dasteh nist")
            else:
                print("gozine eshtebah ast")

        case "8":
            if len(list_hazine) == 0:
                print("hanooz hazine i sabt nashode")
            else:
                mablagh_hazf = list_hazine.pop()
                dasteh_hazf = list_hazine_daste.pop()
                print("akharin hazine hazf shod:", mablagh_hazf, "toman ,", dasteh_hazf)

        case "9":
            print("bye bye")
            break

        case _:
            print("gozine eshtebah ast")
