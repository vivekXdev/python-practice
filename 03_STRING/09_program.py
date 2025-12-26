#WAP to fill in a letter template given below with name and date.
letter = '''Dear <|name|>
        you are selected
        <|date|>    '''
new_letter = letter.replace("<|name|>","Ankit").replace("<|date|>","15/11/26")
print(new_letter)