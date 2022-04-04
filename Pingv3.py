import subprocess
#import repeat as repeat
word = input('Wybierz jaki test: G=Google.com X=IP')

#print(word.lower())
# word[0] - pierwsza litera, or lub
# == porównanie wartości
while True:
    if word[0] =='g' or word[0] =='G':
#    print('TAK')
        out = subprocess.run(['ping', 'google.com'], capture_output=True)
        print(out.stdout.decode())
        if input('Chcesz jeszcze raz powtorzyc to(y/n)') == 'n':
            break
    if word[0] =='x' or word[0] =='X':
        adres = input("Podaj własny adres:\n")
        adresy = open("adresy.txt", "r+")
        adresy_lista = adresy.read()
        adresy = open("adresy.txt", "a+")
        adresy_zapisz = adresy.write('\n' + adres)
        adresy.close()
        out = subprocess.run(['ping', adres], capture_output=True)
        print(out.stdout.decode())
        print("To na tyle")
        if input('Chcesz jeszcze raz powtorzyc to(y/n)') == 'n':
            break
else:
    print('Jeszcze nie znam :) Sorry, będzie w kolejnych wersjach.')



