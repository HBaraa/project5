def test_number(nb1, nb2, entered_number):
    choice = 0
    print("Entrez un nombre entre {} et {}", format(nb1, nb2))
    if choice < nb1 or choice > nb2:
        choice = input(entered_number)
        choice = int(choice)
    else
        print("vous avez entré un mauvais nombre, merci d'entrer un nombre entre {} et {}".format(nb1, nb2))
        choice = 0
    return choice
    