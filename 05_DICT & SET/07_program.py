#WAP to creat a dictionary of hindii words with value English translation.provide user an option to look it up.

animal = {
            "kutta":"dog",
            "haati":"elephat",
            "sugar":"pig",
            "billi":"cat"
}

word = input("Emter animal name in hindi :")
print(animal.get(word))