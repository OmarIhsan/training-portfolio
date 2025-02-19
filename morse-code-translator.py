def trans_morse(str):
    t_morse = ""
    for letter in str:
        if letter in "Aa":
            t_morse = t_morse + ".- "
        elif letter in "Bb":
            t_morse = t_morse + "-... "
        elif letter in "Cc":
            t_morse = t_morse + "-.-. "
        elif letter in "Dd":
            t_morse = t_morse + "-.. "
        elif letter in "Ee":
            t_morse = t_morse + ". "
        elif letter in "Ff":
            t_morse = t_morse + "..-. "
        elif letter in "Gg":
            t_morse = t_morse + "--. "
        elif letter in "Hh":
            t_morse = t_morse + ".... "
        elif letter in "Ii":
            t_morse = t_morse + ".. "
        elif letter in "Jj":
            t_morse = t_morse + ".--- "
        elif letter in "Kk":
            t_morse = t_morse + "-.- "
        elif letter in "Ll":
            t_morse = t_morse + ".-.. "
        elif letter in "Mm":
            t_morse = t_morse + "-- "
        elif letter in "Nn":
            t_morse = t_morse + "-. "
        elif letter in "Oo":
            t_morse = t_morse + "--- "
        elif letter in "Pp":
            t_morse = t_morse + ".--. "
        elif letter in "Qq":
            t_morse = t_morse + "--.- "
        elif letter in "Rr":
            t_morse = t_morse + ".-. "
        elif letter in "Ss":
            t_morse = t_morse + "... "
        elif letter in "Tt":
            t_morse = t_morse + "- "
        elif letter in "Uu":
            t_morse = t_morse + "..- "
        elif letter in "Vv":
            t_morse = t_morse + "...- "
        elif letter in "Ww":
            t_morse = t_morse + ".-- "
        elif letter in "Xx":
            t_morse = t_morse + "-..- "
        elif letter in "Yy":
            t_morse = t_morse + "-.-- "
        elif letter in "Zz":
            t_morse = t_morse + "--.. "
        elif letter in "1":
            t_morse = t_morse + ".---- "
        elif letter in "2":
            t_morse = t_morse + "..--- "
        elif letter in "3":
            t_morse = t_morse + "...-- "
        elif letter in "4":
            t_morse = t_morse + "....- "
        elif letter in "5":
            t_morse = t_morse + "..... "
        elif letter in "6":
            t_morse = t_morse + "-.... "
        elif letter in "7":
            t_morse = t_morse + "--... "
        elif letter in "8":
            t_morse = t_morse + "---.. "
        elif letter in "9":
            t_morse = t_morse + "----. "
        elif letter in "0":
            t_morse = t_morse + "----- "
    return t_morse

CODES_LIST = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----'
}

def re_t_morse(message):
   global i
   message += ' '
   decipher = ''
   mytext = ''
   for myletter in message:
      if (myletter != ' '):
         i = 0
         mytext += myletter
      else:
         i += 1
         if i == 2 :
            decipher += ' '
         else:
            decipher += list(CODES_LIST.keys())[list(CODES_LIST
            .values()).index(mytext)]
            mytext = ''
   return decipher
def main():
    print("1.Translate A sentence to Morse code ")
    print("2.Translate Morse code to English sentence ")

    while True:
        choice = input("enter choice(1/2)  ")
        if choice in ('1', '2'):


            if choice == '1':
                print(trans_morse(input("Type your sentence: ")))
            elif choice == '2':
                print(re_t_morse(input("Type your Morse code: ")))
        else:
                print("invailed choice")
if __name__ == '__main__':
   main()
