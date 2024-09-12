# Entero a cadena
num = 10
num_str = str(num)
print(num_str)  # "10"

# Cadena a entero
num_str = "20"
num = int(num_str)
print(num)  # 20

# Decimal a cadena
decimal = 3.14
decimal_str = str(decimal)
print(decimal_str)  # "3.14"

# Cadena a decimal
decimal_str = "2.718"
decimal = float(decimal_str)
print(decimal)  # 2.718

multilinea = """Esta es una cadena de múltiples líneas en Python."""
print(multilinea)

cadena = "Hola, ivan"
print(len(cadena))

cadena = "Hola, ivan"
n = 5
print(cadena[:n])

cadena = "Hola, ivan"
inicio = 5
fin = 10
print(cadena[inicio:fin])

cadena = "Hola, ivan"
n = 5
print(cadena[-n:])

cadena = "Hola, ivan"
print(cadena.upper())

cadena = "Hola, ivan"
print(cadena.lower())

multilinea = """Esta es otra cadena de múltiples líneas en Python."""
print(multilinea)

cadena = "   Hola, ivan   "
print(cadena.strip())

cadena = "Hola, ivan"
print(cadena.replace("ivan", "Python"))

cadena = "Hola, ivan"
print(cadena.replace("ivan", "Python"))

nombre = "Santiago"
edad = 20
print(f"Me llamo {nombre} y tengo {edad} años.")

