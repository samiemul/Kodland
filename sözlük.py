word_list = {"CRINGE" : "garip yada utandirici olan bir sey icin bir sifat",
             "LOL" : "komik yada sacma bir seye verilen bir cevap",
             "AGGRO":"agresiflesmek/sinirlenmek"}

print(" Ben akilli bir kelime sözlügyüm")
print("bana 3 farkli kelimenin anlamini sora bilirsin")

for i in range(3):
    word = input("anlamadiginiz bir kelime yazin : ").upper() 

    if word in word_list.keys():

        print(word_list[word])

    else:
        print("Girdiginiz gelimeyi tanimiyorum, sorry")
