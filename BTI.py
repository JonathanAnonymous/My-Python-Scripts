#!/usr/bin/python3

while True:

	try:
		bits = input('Bits> ')

		if bits == "quit":
			print ('Bye!')
			exit(0)

		elif bits.isdigit():
			calculo = 2 ** int(bits)
			resultado = list(str(calculo))
			c = len(resultado)

			while c > 3:
				c -= 3
				resultado.insert(c, '.')

			print (''.join(resultado))

		else:
			continue

	except EOFError:
		print ('Bye!')
		exit(0)

	except KeyboardInterrupt:
		print ('Bye!')
		exit(0)
