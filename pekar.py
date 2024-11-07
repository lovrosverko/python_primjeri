def izracunaj_vrijeme_pecenja(veliki, srednji, mali):
    """
    Izračunava minimalno vrijeme potrebno za pečenje kruha 
    različitih veličina u tri pećnice.

    Argumenti:
      veliki: Broj velikih kruhova.
      srednji: Broj srednjih kruhova.
      mali: Broj malih kruhova.

    Return:
      Minimalno vrijeme pečenja u minutama.
    """
    vrijeme = 0  # Inicijalizacija varijable za ukupno vrijeme pečenja
    pecnica1 = pecnica2 = pecnica3 = 0  # Inicijalizacija varijabli za broj turnusa svake pećnice

    while veliki > 0 or srednji > 0 or mali > 0:  # Petlja se izvršava dok postoje kruhovi za pečenje
        # Pećnica 1 (veliki, srednji, mali) - kapacitet 3
        if pecnica1 >= 0:  # Provjera je li pećnica dostupna (uvijek je true u ovom slučaju)
            if veliki > 2:  # Ako ima dovoljno velikih kruhova, peći samo velike
                veliki -= min(veliki, 3)  # Smanji broj velikih kruhova za maksimalno 3
                pecnica1 += 1  # Povećaj broj turnusa za pećnicu 1
            elif srednji > 0:  # Ako nema dovoljno velikih, a ima srednjih, peći kombinaciju
                veliki -= min(veliki, 3)  # Smanji broj velikih kruhova
                srednji -= min(srednji, 3-veliki)  # Smanji broj srednjih kruhova, uzimajući u obzir preostali prostor
                pecnica1 += 1  # Povećaj broj turnusa za pećnicu 1
            elif mali > 0:  # Ako nema dovoljno velikih i srednjih, a ima malih, peći kombinaciju
                veliki -= min(veliki, 2)  # Smanji broj velikih kruhova (maksimalno 2)
                srednji -= min(srednji, 3-veliki)  # Smanji broj srednjih kruhova, uzimajući u obzir preostali prostor
                mali -= min(mali,3-veliki-srednji)  # Smanji broj malih kruhova, uzimajući u obzir preostali prostor
                pecnica1 += 1  # Povećaj broj turnusa za pećnicu 1

        print("pecnica 1: ", pecnica1)  # Ispis stanja pećnice 1
        print("veliki: ", veliki)  # Ispis broja preostalih velikih kruhova
        print("srednji: ", srednji)  # Ispis broja preostalih srednjih kruhova
        print("mali: ", mali)  # Ispis broja preostalih malih kruhova
        print()

        # Pećnica 2 (srednji, mali) - kapacitet 4
        if pecnica2 >= 0:  # Provjera je li pećnica dostupna (uvijek je true u ovom slučaju)
            if srednji > 0 and mali > 0:  # Ako ima i srednjih i malih kruhova, peći kombinaciju
                srednji -= min(srednji, 2)  # Smanji broj srednjih kruhova (maksimalno 2)
                mali -= min(mali, 2)  # Smanji broj malih kruhova (maksimalno 2)
            elif srednji > 0:  # Ako ima samo srednjih kruhova, peći samo srednje
                srednji -= min(srednji, 4)  # Smanji broj srednjih kruhova (maksimalno 4)
            elif mali > 0:  # Ako ima samo malih kruhova, peći samo male
                mali -= min(mali, 4)  # Smanji broj malih kruhova (maksimalno 4)
            pecnica2 += 1  # Povećaj broj turnusa za pećnicu 2

        print("pecnica 2: ", pecnica2)  # Ispis stanja pećnice 2
        print("veliki: ", veliki)  # Ispis broja preostalih velikih kruhova
        print("srednji: ", srednji)  # Ispis broja preostalih srednjih kruhova
        print("mali: ", mali)  # Ispis broja preostalih malih kruhova
        print()

        # Pećnica 3 (mali) - kapacitet 2
        if pecnica3 >= 0 and mali > 0:  # Provjera je li pećnica dostupna i ima li malih kruhova
            mali -= min(mali, 2)  # Smanji broj malih kruhova (maksimalno 2)
            pecnica3 += 1  # Povećaj broj turnusa za pećnicu 3

        print("pecnica 3: ", pecnica3)  # Ispis stanja pećnice 3
        print("veliki: ", veliki)  # Ispis broja preostalih velikih kruhova
        print("srednji: ", srednji)  # Ispis broja preostalih srednjih kruhova
        print("mali: ", mali)  # Ispis broja preostalih malih kruhova
        print()

    print (pecnica1, pecnica2, pecnica3)  # Ispis broja turnusa za svaku pećnicu
    max_turnus = max (pecnica1, pecnica2, pecnica3)  # Odredi maksimalan broj turnusa među svim pećnicama
    vrijeme = max_turnus*5  # Izračunaj ukupno vrijeme pečenja (svaki turnus traje 5 minuta)
    return vrijeme  # Vrati izračunato vrijeme

# Ispis minimalnog vremena pečenja
print("Minimalno vrijeme pečenja:", izracunaj_vrijeme_pecenja(5, 10, 7), "minuta")