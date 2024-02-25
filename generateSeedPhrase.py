'''
    MIT License

    Copyright (c) 2024 José Luis Alvarez Gago

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
'''

import random as rn

sel = (input("Elija el tipo de frase semilla, [0] De 12 palabras o [1] De 24 palabras o cualquier otra tecla para abandonar: "))
if sel == '0':
    print("Ha elegido generar una frase semilla de 12 palabras")
elif sel == '1':
    print("Ha elegido generar una frase semilla de 24 palabras")
else:
    print("...Abandonando el programa...")

def artx():
    arch = open("bip39.txt", mode="r")
    est = arch.readable()
    if est == True:
        print("El archivo 'bip39.txt' está OK!")
    else:
        print("Problemas accediendo al archivo 'bip39.txt'. Resuelva la incidencia...")

semen = list()

def genBit():
    global pala
    global semen
    pabi = ''
    for ejecucion in range (11):
        bito = str(rn.randint(0,1))
        pabi = pabi + bito
    bibi = ('0b' + pabi)
    bide = int(pabi, 2)
    with open ("bip39.txt") as arch:
        pala = arch.readlines()[bide]

def doce():
    for eje in range (12):
        genBit()
        semen.append(pala.rstrip())
    print(semen)

def vcua():
    for eje in range (24):
        genBit()
        semen.append(pala.rstrip())
    print(semen)

if sel == '0':
    artx()
    doce()
elif sel == '1':
    artx()
    vcua()
else:
    print("Not your keys, not your cryptos!")
