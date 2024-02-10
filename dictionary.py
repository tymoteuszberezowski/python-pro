meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "IMO": "moim zdaniem",
            "TL:DR": "Too long don't read: krotki opis",
            "Long story short": "krotko mowiac",
            "FYI": "for you information, dla Twojej informacji"
            "XD": "smianie sie"
            
}
word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")



if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("slowo nie zostalo dodane, spytaj sie o dodanie")
