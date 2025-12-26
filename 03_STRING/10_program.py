#WAP to fill in a letter template input name and date by user using input function
x = input("Enetr your name :")
y = input("Enetr todays date :")
letter = '''Dear <|name|>
        you are selected
        <|date|>    '''

print(letter.replace("<|name|>",x).replace("<|date|>",y))