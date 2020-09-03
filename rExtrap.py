#!/usr/bin
#coding: utf-8
from random import randint
try:
    from colorama import init
    from termcolor import colored
except ImportError:
    print("""
    Tienes que instalar primero los requisitos,
    esto lo logras escribiendo el siguiente comando:
    pip install -r req.txt
    """)

def option1(card):
	card = card[0] + card[1] + card[2] + card[3] + card[4] + card[5] + card[6] + card[7] + card[8] + card[9] + card[10] + card[11] + card[12] + card[13] + 'x' + 'x'
	return card

def option2(card):
	card = card[0] + card[1] + card[2] + card[3] + card[4] + card[5] + card[6] + card[7] + card[8] + card[9] + card[10] + card[11] + 'x' + 'x' + 'x' + 'x'
	return card

def option3(card):
	card = card[0] + card[1] + card[2] + card[3] + card[4] + card[5] + card[6] + card[7] + card[8] + card[9] + card[10] + card[11] + 'x' + 'x' + card[14] + 'x'
	return card

def option4(card):
	card = card[0] + card[1] + card[2] + card[3] + card[4] + card[5] + card[6] + card[7] + card[8] + card[9] + 'x' + card[11] + 'x' + 'x' + card[14] + 'x'
	return card

def option5(card):
	card = card[0] + card[1] + card[2] + card[3] + card[4] + card[5] + card[6] + card[7] + card[8] + card[9] + 'x' + 'x' + 'x' + 'x' + 'x' + 'x'
	return card

def option6(card):
	card = card[0] + card[1] + card[2] + card[3] + card[4] + card[5] + 'x' + 'x' + 'x' + 'x' + card[10] + card[11] + card[12] + card[13] + 'x' + 'x'
	return card

def option7(card):
	card = card[0] + card[1] + card[2] + card[3] + card[4] + card[5] + card[6] + 'x' + card[8] + card[9] + 'x' + 'x' + card[12] + card[13] + 'x' + card[15]
	return card

def option8(card):
	card = card[0] + card[1] + card[2] + card[3] + card[4] + card[5] + 'x' + card[7] + card[8] + 'x' + 'x' + 'x' + 'x' + card[13] + card[14] + 'x'
	return card

####################################################################
def cardLuhnChecksumIsValid(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

def ccgen(bin_format):
    out_cc = ""
    if len(bin_format) == 16:
        for i in range(15):
            if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                out_cc = out_cc + bin_format[i]
                continue
            elif bin_format[i] in ("x"):
                out_cc = out_cc + str(randint(0,9))
            else:
                print("\nCaracter no valido en el formato: {}\n".format(bin_format))
                print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
                print("Ayuda: python2 rGen.py -h \n")
                sys.exit()

        for i in range(10):
            checksum_check = out_cc
            checksum_check = checksum_check + str(i)

            if cardLuhnChecksumIsValid(checksum_check):
                out_cc = checksum_check
                break
            else:
                checksum_check = out_cc

    else:
        print("\033[1;32m")
        print("\nERROR: Inserta un bin valido\n")
        print("SOLUCION: El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        print("AYUDA: python2 ccgenR.py -h\n")
        exit()
        
    return(out_cc)

#########################################################
def show(opt, card):
	if opt == '1':
		value = option1(card)
		print "Extrapolacion:   " + value
		print("")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("|Tarjetas generadas|")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("")
		for i in range(0, 10):
			print(" " + ccgen(value))

	if opt == '2':
		value = option2(card)
		print "Extrapolacion:   " + value
		print("")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("|Tarjetas generadas|")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("")
		for i in range(0, 10):
			print(" " + ccgen(value))

	if opt == '3':
		value = option3(card)
		print "Extrapolacion:   " + value
		print("")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("|Tarjetas generadas|")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("")
		for i in range(0, 10):
			print(" " + ccgen(value))

	if opt == '4':
		value = option4(card)
		print "Extrapolacion:   " + value
		print("")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("|Tarjetas generadas|")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("")
		for i in range(0, 10):
			print(" " + ccgen(value))

	if opt == '5':
		value = option5(card)
		print "Extrapolacion:   " + value
		print("")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("|Tarjetas generadas|")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("")
		for i in range(0, 10):
			print(" " + ccgen(value))

	if opt == '6':
		value = option6(card)
		print "Extrapolacion:   " + value
		print("")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("|Tarjetas generadas|")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("")
		for i in range(0, 10):
			print(" " + ccgen(value))

	if opt == '7':
		value = option7(card)
		print "Extrapolacion:   " + value
		print("")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("|Tarjetas generadas|")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("")
		for i in range(0, 10):
			print(" " + ccgen(value))

	if opt == '8':
		value = option8(card)
		print "Extrapolacion:   " + value
		print("")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("|Tarjetas generadas|")
		print(" ~~~~~~~~~~~~~~~~~~")
		print("")
		for i in range(0, 10):
			print(" " + ccgen(value))
#########################################################
embl =  """
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ? _____________________      ?
 ?| Hello member,       |     ?
 ?| welcome to          |     ?
 ?| RESET Extrapolation |     ?
 ? ---------------------      ?
 ?                    \       ?
 ?                     (oo)   ?
 ?                     (__)   ?
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 |Created by: Durd3n & Guarc0n|
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 """
init()
print(colored(embl, 'red'))

print ("Escribe la opcion deseas ejecutar en tu extrapolacion:")
print ("[1] -> " + colored("0000 0000 0000 00", "yellow") + colored("xx", "cyan"))
print ("[2] -> " + colored("0000 0000 0000 ", "yellow") + colored("xxxx", "cyan"))
print ("[3] -> " + colored("0000 0000 0000 ", "yellow") + colored("xx", "cyan") + colored("0", "yellow") + colored("x", "cyan"))
print ("[4] -> " + colored("0000 0000 00", "yellow") + colored("x", "cyan") + colored("0 ", "yellow") + colored("xx", "cyan") + colored("0", "yellow") + colored("x", "cyan"))
print ("[5] -> " + colored("0000 0000 00", "yellow") + colored("xx xxxx", "cyan"))
print ("[6] -> " + colored("0000 00", "yellow") + colored("xx xx", "cyan") + colored("00 00", "yellow") + colored("xx", "cyan"))
print ("[7] -> " + colored("0000 000", "yellow") + colored("x ", "cyan") + colored("00", "yellow") + colored("xx ", "cyan") + colored("00", "yellow") + colored("x", "cyan") + colored("0", "yellow"))
print ("[8] -> " + colored("0000 00", "yellow") + colored("x", "cyan") + colored("0 0", "yellow") + colored("xxx", "cyan") +  colored("x ", "cyan") + colored("00", "yellow") + colored("x", "cyan"))

def main():
	print("")
	opt = raw_input("Ingrese la opcion que desea: ")
	print("")
	card = raw_input("Inserte tarjeta: ")
	print("")
	if len(card) != 16:
		print "Escribe una tarjeta valida de 16 digitos"
		exit()
	show(opt, card)
main()