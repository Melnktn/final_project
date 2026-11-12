def chape_khat():
    for i in range(1, 41):
        print("-", end="")
    print()

user_name = input("esm sandoghdar ra bezan:")

while True:
    pasword = input("password bezan (hadeaghal 4 character dashte bashe):")
    if len(pasword) >= 4:
        print("salam", user_name, "khoshomadiii")
        break
    else:
        print("password unvalid")
        continue

rooz = input("emrooz che rozi ast? (shanbe, yekshanbe, doshanbe, seshanbe, charshanbe, panjshanbe, jome):")

if rooz == "panjshanbe" or rooz == "jome":
    darsad_takhfif = 30
    print("emrooz 30 darsad takhfif rooye nooshidani ha darim")
else:
    darsad_takhfif = 0
    print("emrooz takhfif nadarim")

gheymat_pofak = 175000
gheymat_nooshabe = 100000
gheymat_abmive = 30000
gheymat_nan = 40000

factor = []

while True:
    menu = input("1.afzoodan kala 2.kam kardan kala 3.hazf akharin kala 4.namayesh factor 5.chap factor va pardakht 6.exit:")

    match menu:
        case "1":
            print("65.pofak namaki minoo 175000 , 10.nooshabe khanevade pepsi 100000 , 20.ab miveh 30000 , 30.nan sangak 40000")
            shenase = input("shenase kala ra bezan:")
            if shenase == "65" or shenase == "10" or shenase == "20" or shenase == "30":
                tedad = int(input("chanta ezafe konam?:"))
                for i in range(tedad):
                    factor.append(shenase)
                print("ezafe shod")
                print(factor)
            else:
                print("shenase eshtebah ast")

        case "2":
            shenase = input("shenase kala ra bezan:")
            tedad = int(input("chanta kam konam?:"))
            if tedad > factor.count(shenase):
                print("inghadr az in kala dar factor nist")
            else:
                for i in range(tedad):
                    factor.remove(shenase)
                print("kam shod")
                print(factor)

        case "3":
            if len(factor) == 0:
                print("factor khali ast")
            else:
                kala_hazf = factor.pop()
                print("akharin kala hazf shod:", kala_hazf)
                print(factor)

        case "4":
            print(factor)
            print("tedad kol kala ha:", len(factor))

        case "5":
            num_pofak = factor.count("65")
            num_nooshabe = factor.count("10")
            num_abmive = factor.count("20")
            num_nan = factor.count("30")

            jam_pofak = gheymat_pofak * num_pofak
            jam_nooshabe = gheymat_nooshabe * num_nooshabe
            jam_abmive = gheymat_abmive * num_abmive
            jam_nan = gheymat_nan * num_nan

            jam_kol = jam_pofak + jam_nooshabe + jam_abmive + jam_nan

            if jam_kol == 0:
                print("factor khali ast")
                continue

            tedad_nooshidani = num_nooshabe + num_abmive
            jam_nooshidani = jam_nooshabe + jam_abmive
            takhfif = jam_nooshidani * darsad_takhfif / 100

            pas_az_takhfif = jam_kol - takhfif
            maliyat = pas_az_takhfif * 10 / 100
            mablagh_nahaii = pas_az_takhfif + maliyat

            chape_khat()
            print("factor forooshgah - cashier:", user_name)
            chape_khat()

            if num_pofak > 0:
                print("pofak namaki minoo (65):", num_pofak, "ta bood , ", num_pofak, "ta shod", jam_pofak, "toman")
            if num_nan > 0:
                print("nan (30):", num_nan, "ta bood , ", num_nan, "ta shod", jam_nan, "toman")
            if tedad_nooshidani > 0:
                print("nooshidani ha:", tedad_nooshidani, "ta bood , ", tedad_nooshidani, "ta shod", jam_nooshidani, "toman")
                if num_nooshabe > 0:
                    print("    nooshabe (10):", num_nooshabe, "ta shod", jam_nooshabe, "toman")
                if num_abmive > 0:
                    print("    ab miveh (20):", num_abmive, "ta shod", jam_abmive, "toman")

            chape_khat()
            print("jame kol:", jam_kol, "toman")
            print("takhfif", darsad_takhfif, "darsad rooye nooshidani:", takhfif, "toman")
            print("maliyat 10 darsad:", maliyat, "toman")
            print("mablagh nahaii:", mablagh_nahaii, "toman")
            chape_khat()

            while True:
                daryafti = int(input("mablagh daryafti az moshtari:"))
                if daryafti < mablagh_nahaii:
                    print("pool kam ast , dobare bezan")
                    continue
                else:
                    baghi_mande = daryafti - mablagh_nahaii
                    print("mablagh daryafti:", daryafti)
                    print("baghi mande pool:", baghi_mande)
                    print("mamnoon az kharid shoma")
                    break

            factor = []

        case "6":
            print("bye bye")
            break

        case _:
            print("gozine eshtebah ast")
