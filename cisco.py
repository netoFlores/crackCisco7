#!/usr/bin/python
"""
	Esta aplicacion puede ser modificada y distribuirla libremente 
	bajo la licencia GPLV2. Esta aplicacion descripta el algoritmo Cisco7.
	
	BY:	 Ernesto Flores.
	Email:	 ernesto.flores28@gmail.com
"""
cifrada = [0x41, 0x2c, 0x2e, 0x69, 0x79, 0x65, 0x77, 0x72, 0x6b, 0x6c, 0x64, 0x4a, 0x4b, 0x44, 0x48, 0x53, 0x55, 0x42, 0x73, 0x67, 0x76, 0x63, 0x61, 0x36, 0x39, 0x38, 0x33, 0x34, 0x6e, 0x63, 0x78]



cifrado = raw_input("Ingrese el password: ")
cifrado = cifrado[2:]
countCaracter = len(cifrado)
i = 2
ianterior = 0
lista = []
while i <= countCaracter:	
	lista.append(cifrado[ianterior:i])
	ianterior = i
	i += 2
totalElementos = len(lista)
o = 0
desecriptada = []
while o < totalElementos:	
	valor = cifrada[o] ^ int(lista[o], 16)
	desecriptada.append(hex(valor))
	o += 1
cadenaCifrada = ""
cadenaCifrada = cadenaCifrada.join(desecriptada)
cadenaCifrada = cadenaCifrada.replace("0x", "")
print cadenaCifrada.decode('hex')
