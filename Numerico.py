def puntos_millar(cifra):
    xxx = str(print('{:,}'.format(cifra).replace(',', '.'), "- ", end=""))

def Varia_Ord(m, n):
    import math
    print("Variaciones en grupos de", n, "en una población de", m, "= ", end="")
    var = int(math.factorial(m) / (math.factorial(m - n)))
    print(var)
def Varia_Rep(m, n):
    print("Variaciones con repetición en grupos de", n, "en una población de", m, "= ", end="")
    var = m ** n
    print(var)
def Permuta(m):
    import math
    var = math.factorial(m)
    print("Permutaciones en una población de", m, "= ", end="")
    print(var)
def Permuta_Cir(m):
    import math
    var = math.factorial(m - 1)
    print("Permutaciones circulares en una población de", m, "= ", end="")
    print(var)
def Permuta_Rep(p, q):
    import math
    denominador = 1
    numerador = math.factorial(p)
    for x in range(q):
        print(x + 1, "ª serie, ", end="")
        d = int(input("repeticiones:"))
        denominador = denominador * math.factorial(d)
    permuta = int(numerador / denominador)
    print("Permutaciones con repetición entre", p, "elementos:", permuta)
def N_Combinatorio(m, n):
    import math
    N_combi = int(math.factorial(m) / (math.factorial(n) * math.factorial(m - n)))
    print(N_combi)
def Combinaciones(pob, elem):
    import math
    combi = int(math.factorial(pob) / (math.factorial(elem) * math.factorial(pob - elem)))
    print(combi)


###########################################3 Mínimo común múltiplo

def MinComMul():
    n = int(input("Número:"))

    diccio = {}
    valor = 0  # repeticiones de n
    x = 2  # divisor empieza con valor 2
    while n > 1:
        if n % x == 0:
            n = n / x
            valor += 1
            diccio[x] = valor
        else:
            x = x + 1
            valor = 0
    for klave, valor in diccio.items():
        print(klave, "^", valor, "=", klave ** valor)

    n2 = 1
    while n2 != 0:
        n2 = int(input("\nNúmero (0 para salir):"))
        diccio2 = {}
        valor2 = 0  # repeticiones de n
        x2 = 2  # divisor empieza con valor 2
        while n2 > 1:
            if n2 % x2 == 0:
                n2 = n2 / x2
                valor2 += 1
                diccio2[x2] = valor2
            else:
                x2 = x2 + 1
                valor2 = 0
        for k, v in diccio2.items():
            print(k, "^", v, "=", k ** v)

        for c in diccio.keys():  # compara coincidencias con primer diccionario
            if c in diccio2:
                if diccio2[c] > diccio[c]:
                    diccio.pop(c)
                    diccio[c] = diccio2[c]

        for c in diccio2.keys():  # agrega nuevos múltiplos al diccionario
            if not c in diccio:
                diccio[c] = diccio2[c]

    # import operator													#
    # resultado = sorted(diccio.items(), key=operator.itemgetter(0))	# ordena diccio como lista

    mcm = 1
    print("\nMúltiplos:")
    for klave, valor in diccio.items():
        print(klave, "^", valor, "=", klave ** valor)
        mcm = mcm * klave ** valor
    print("Mínimo común múltiplo:", mcm)


###########################################3 Máximo común divisor

def MaxComDiv(numeros):
    lista = []
    divisores = []
    mcd = 0
    for veces in range(numeros):  # entrada de números limitada por usuario
        num = int(input("Número:"))
        lista.append(num)
        lista.sort()  # ordena números de menor a mayor

    for x in lista:
        for n in range(2, x + 1):
            if x % n == 0:
                divisores.append(n)  # agrega todos los divisores a la lista

    # evita duplicaciones en lista de divisores
    lista_div = []
    [lista_div.append(key) for key in divisores if key not in lista_div]
    #
    lista_div.sort()
    lista_div.reverse()

    lista_mcd = lista_div[:]  # impide que la nueva lista copie cambios en lista original

    lista_ok = []
    for y in lista_div:  # recorre divisores para exluir mayores que números introducidos
        chivato = 0
        for x in lista[:]:  # comprueba divisor entre números de lista
            if y > x:
                chivato = 1
        if chivato == 0:
            lista_ok.append(y)

    lista_fin = []
    excluidos = []

    for a in lista_ok:
        for b in lista:
            if b % a != 0:
                if a not in excluidos:
                    excluidos.append(a)

    incluidos = []
    for c in lista_ok:
        if c not in excluidos:
            incluidos.append(c)
    if len(incluidos) != 0:
        print("Divisores comunes:", incluidos)

    for z in incluidos:  # busca divisores entre lista divisores de todos los números, descarta menores
        for sig in incluidos[-1::-1]:
            if z > sig and z % sig == 0:
                excluidos.append(sig)

    for a in incluidos:
        if a not in excluidos:
            lista_fin.append(a)

    if len(lista_fin) == 0:
        lista_fin.append(1)
        print("Único divisor común: 1")
    else:
        print("MCD:", lista_fin)


def Narciso(y, z):
    print("Serie de NÚMEROS DE NARCISO entre", y, "y", z, ":")
    for x in range(y, z):
        pot = 0
        for n in range(0, len(str(x))):
            pot += int(str(x)[n]) ** len(str(x))
            if pot == x and n + 1 == len(str(x)):
                puntos_millar (pot)
#                print(pot, "· ", end="")

def Narciso_halla(narciso_pos):
    pot = 0
    chiva = 0
    for n in range(0, len(str(narciso_pos))):
        pot += int(str(narciso_pos)[n]) ** len(str(narciso_pos))
        if pot == narciso_pos and n + 1 == len(str(narciso_pos)):
            print(narciso_pos, "es narcisista")
            chiva=1
    if chiva==0:
        print(narciso_pos, "no es narcisista")

def Fibonacci(limite):
    print("Sucesión DE FIBONACCI")
    previo, fibo = 0, 1
    while fibo < fin:
        fibo += previo
        if fibo <= fin:
            puntos_millar (fibo)
            #print(fibo, "· ", end="")
        previo += fibo
        if previo <= fin:
            puntos_millar(previo)
            #print(previo, "· ", end="")

def Primos(inicio, limite):
    print("Serie de NÚMEROS PRIMOS entre", inicio, "y", limite, ":")
    contador = 0
    for n in range(inicio, limite + 1):
        chiva = 0
        for d in range(1, n):
            if n % d == 0:
                chiva = chiva + 1
            if n == d + 1 and chiva == 1:
                puntos_millar(n)        # llama a la función que pone los puntos de millar
                contador+=1
    print("\n", contador, "números primos en total")


def Primos_halla(primus):
    # falta implementar números a partir de 2 ####################################
    chiva = 0
    divisores=[]
    for d in range(2, primus):
        if primus % d == 0:
            chiva = 1
            divisores.append(d)
    if chiva == 0:
        print(primus, "es PRIMO")
    else:
        print(primus, "no es PRIMO, tiene los siguientes divisores:", divisores)

def Fermat(a, b):
        for n in range(a, b + 1):
            #print("( n =", n,")", 2 ** (2 ** n) + 1)

            print("\n( n =", n, ") ", end="")
            puntos_millar(2 ** (2 ** n) + 1)
































            #if n == 2 ** (2 ** n) + 1:
             #   print(n)

#################################### MENÚ PRINCIPAL ###################################
opcion = ()
while opcion != 0:
    opcion = int(input("\n1 - Combinatoria y probabilidad\n2 - Mínimo común múltiplo y máximo común divisor\n3 - Series y curiosidades numéricas\n0 - Salir\n "))

    if opcion == 1:
        opc = ()
        while opc != 0:
            opc = int(input(
                "1 - Variaciones\n2 - Variaciones con repetición\n3 - Permutaciones\n4 - Permutaciones circulares\n5 - Permutaciones con repetición\n6 - Número combinatorio\n7 - Combinaciones\n0 - Salir"))
            if opc == 1:
                x = int(input("Población: "))
                y = int(input("Grupos: "))
                Varia_Ord(x, y)
            elif opc == 2:
                x = int(input("Población: "))
                y = int(input("Grupos: "))
                Varia_Rep(x, y)
            elif opc == 3:
                x = int(input("Población: "))
                Permuta(x)
            elif opc == 4:
                x = int(input("Población: "))
                Permuta_Cir(x)
            elif opc == 5:
                x = int(input("Población ="))
                y = int(input("Grupos de repeticiones"))
                Permuta_Rep(x, y)
            elif opc == 6:
                x = int(input("Elementos:"))
                y = int(input("Orden:"))
                N_Combinatorio(x, y)
            elif opc == 7:
                x = int(input("Población:"))
                y = int(input("en grupos de:"))
                Combinaciones(x, y)

    if opcion == 2:
        opm = ()
        while opm != 0:
            opm = int(input("\n1 - Mínimo común multiplo\n2 - Máximo común divisor\n0 - Salir\n "))
            if opm == 1:
                MinComMul()
            elif opm == 2:
                nmcd = int(input("¿Cuántos números intervienen para hallar el Máximo común divisor? "))
                MaxComDiv(nmcd)

    if opcion == 3:
        op = ()
        while op != 0:
            op = int(
                input("\n1 - Serie de Números de Narciso o de Armstrong\n2 - Halla si un número es narcisista\n3 - Sucesión de Fibonacci\n4 - Serie de Números Primos\n5 - Hallar si un número es Primo\n6 - Números de Fermat\n0 - Salir\n "))
            print()
            if op == 1:
                a = int(input("Número inicio"))
                b = int(input("Número límite"))
                Narciso(a, b)
            elif op == 2:
                posible = int(input("Posible Narciso"))
                Narciso_halla(posible)
            elif op == 3:
                fin = int(input("Número límite"))
                Fibonacci(fin)
            elif op == 4:
                fin = 10 ** 2
                ini = int(input("Número inicio"))
                fin = int(input("Número límite"))
                Primos(ini, fin)
            elif op == 5:
                primo = int(input("Posible Primo")) # tiene que ser mayor que 0
                Primos_halla(primo)
            elif op == 6:
                x, y = 0, 7
                Fermat(x, y)