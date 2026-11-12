def chap_khat():
    for i in range(1, 41):
        print("-", end="")
    print()


list_adat = []
list_anjam = []
list_kol = []
list_streak = []
list_beststreak = []
list_akharin = []

print("be sistem modiriat adat ha khosh amadid")

while True:
    chap_khat()
    menu = input("1.adat jadid 2.namayesh adat ha 3.sabt emrooz 4.rooz haye motavali 5.adat haye anjam nashode 6.darsad paybandi 7.behtarin adat ha 8.hazf adat 9.exit:")

    match menu:
        case "1":
            esm = input("adat jadidet chiye? (masalan violon tamrin mikonam):")
            if len(esm) == 0:
                print("esm adat khali ast")
            elif list_adat.count(esm) > 0:
                print("in adat ghablan sabt shode")
            else:
                list_adat.append(esm)
                list_anjam.append(0)
                list_kol.append(0)
                list_streak.append(0)
                list_beststreak.append(0)
                list_akharin.append("hanooz")
                print("adat jadid sabt shod")

        case "2":
            if len(list_adat) == 0:
                print("hanooz adati sabt nashode")
            else:
                print(list_adat)
                print("tedad adat ha:", len(list_adat))

        case "3":
            if len(list_adat) == 0:
                print("aval yek adat sabt kon")
            else:
                for i in range(len(list_adat)):
                    print("emrooz", list_adat[i], "dar barname bood?")
                    javab = input("1.bale anjam dadam 2.bale ama anjam nadadam 3.dar barname nabood:")

                    match javab:
                        case "1":
                            list_anjam[i] = list_anjam[i] + 1
                            list_kol[i] = list_kol[i] + 1
                            list_streak[i] = list_streak[i] + 1
                            list_akharin[i] = "bale"
                            if list_streak[i] > list_beststreak[i]:
                                list_beststreak[i] = list_streak[i]
                            print("afarin")
                        case "2":
                            list_kol[i] = list_kol[i] + 1
                            list_streak[i] = 0
                            list_akharin[i] = "kheyr"
                            print("fardah bishtar talash kon")
                        case "3":
                            print("emrooz hesab nashod")
                        case _:
                            print("gozine eshtebah , emrooz hesab nashod")

        case "4":
            if len(list_adat) == 0:
                print("hanooz adati sabt nashode")
            else:
                for i in range(len(list_adat)):
                    print(list_adat[i], ": roozhaye motavali felli", list_streak[i], ", bishtarin", list_beststreak[i])

        case "5":
            if len(list_adat) == 0:
                print("hanooz adati sabt nashode")
            else:
                tedad_nashode = 0
                for i in range(len(list_adat)):
                    if list_akharin[i] != "bale":
                        print(list_adat[i], "anjam nashode")
                        tedad_nashode = tedad_nashode + 1
                if tedad_nashode == 0:
                    print("hame adat ha anjam shodan , afarin")

        case "6":
            if len(list_adat) == 0:
                print("hanooz adati sabt nashode")
            else:
                chap_khat()
                for i in range(len(list_adat)):
                    if list_kol[i] == 0:
                        print(list_adat[i], ": hanooz rooz i sabt nashode")
                    else:
                        darsad = list_anjam[i] * 100 / list_kol[i]
                        print(list_adat[i], ":", list_anjam[i], "bar anjam az", list_kol[i], "rooz ,", darsad, "darsad paybandi")
                chap_khat()
                print("jame anjam hame adat ha:", sum(list_anjam))

        case "7":
            if len(list_adat) == 0:
                print("hanooz adati sabt nashode")
            else:
                bishtarin_tekrar = list_anjam[0]
                shomare_tekrar = 0
                bishtarin_estemrar = list_beststreak[0]
                shomare_estemrar = 0

                for i in range(len(list_adat)):
                    if list_anjam[i] > bishtarin_tekrar:
                        bishtarin_tekrar = list_anjam[i]
                        shomare_tekrar = i
                    if list_beststreak[i] > bishtarin_estemrar:
                        bishtarin_estemrar = list_beststreak[i]
                        shomare_estemrar = i

                print("behtarin adat az nazar tekrar:", list_adat[shomare_tekrar], ",", bishtarin_tekrar, "bar")
                print("behtarin adat az nazar estemrar:", list_adat[shomare_estemrar], ",", bishtarin_estemrar, "rooz motavali")

        case "8":
            print(list_adat)
            esm = input("kodam adat hazf shavad?:")
            if list_adat.count(esm) == 0:
                print("in adat peyda nashod")
            else:
                shomare = list_adat.index(esm)
                list_adat.remove(esm)
                list_anjam.pop(shomare)
                list_kol.pop(shomare)
                list_streak.pop(shomare)
                list_beststreak.pop(shomare)
                list_akharin.pop(shomare)
                print("adat hazf shod")

        case "9":
            print("bye bye")
            break

        case _:
            print("gozine eshtebah ast")
