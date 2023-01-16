
import Operaciones

respuesta = 0

while respuesta != 10:
        
    print("\nSeleccione una opción:\n \n\t1) Realizar Suma \n\t2) Realizar Resta \n\t3) Realizar Multiplicación \n\t4) Realizar División \n\t5) Potencia de un número \n\t6) Obtener Raiz n de un número \n\t7) Obtener Sen(x) \n\t8) Obtener Cos(x) \n\t9) Obtener Tan(x) \n\t10) Salir\n") 

    respuesta = int(input())

    if respuesta >= 0 and respuesta <= 4:

        #print("ENTRA DE ESTE LADO ------->")

        print("\n+--------------------+")
        print("| PERACIONES BÁSICAS |")
        print("+--------------------+")

        num1 = float(input("\n\tIngresa el primer número: "))
        num2 = float(input("\n\tIngresa el segundo número: "))

        if respuesta == 1:

            print("\n+----------------+")
            print("| OPERACIÓN SUMA |")
            print("+----------------+")
            
            resultado = Operaciones.operacionSuma(num1, num2)
            print("\nLa suma de ", num1, " + ", num2, " es: ", resultado)

        if respuesta == 2:
            
            print("\n+-----------------+")
            print("| OPERACIÓN RESTA |")
            print("+-----------------+")

            resultado = Operaciones.operacionResta(num1, num2)
            print("\nLLa resta de ", num1, " - ", num2, " es: ", resultado)

        if respuesta == 3:

            print("\n+--------------------------+")
            print("| OPERACIÓN MULTIPLICACIÓN |")
            print("+--------------------------+")
            
            resultado = Operaciones.operacionMultiplicacion(num1, num2)
            print("\nLLa multiplicación de ", num1, " x ", num2, " es: ", resultado)

        if respuesta == 4:
            
            print("\n+--------------------+")
            print("| OPERACIÓN DIVISIÓN |")
            print("+--------------------+")

            resultado = Operaciones.operacionDivision(num1, num2)
            print("\nLLa división de ", num1, " / ", num2, " es: ", resultado)

    if respuesta == 5 or respuesta == 6:

        print("\n+--------------------+")
        print("| POTENCIAS Y RAICES |")
        print("+--------------------+")

        if respuesta == 5:
            num1 = float(input("\n\tIngresa el número: "))
            num2 = float(input("\n\tIngresa la base: "))
                
            print("\n+-----------+")
            print("| POTENCIA |")
            print("+-----------+")

            resultado = Operaciones.operacionPotencia(num1, num2)
            print("\n", num1, " Elevado a la potencia ", num2, " es: ", resultado)
                
        if respuesta == 6:

            num1 = float(input("\n\tIngresa el número: "))
            num2 = float(input("\n\tIngresa la base: "))
                
            print("\n+--------+")
            print("| RAÍZ |")
            print("+--------+")

            resultado = Operaciones.operacionRaiz(num1, num2)
            print("\nLa raíz ", num2, " de ", num1, " es: ", resultado)

    elif respuesta >= 7 and respuesta <= 9:
            
        #print("ENTRA DE ESTE OTRO LADO <-------")
        
        print("\n+-----------------------------+")
        print("| OPERACIONES TRIGONOMÉTRICAS |")
        print("+-----------------------------+")

        num1 = float(input("\n\tIngresa los grados: "))
        
        if respuesta == 7:
            
            print("\n+------------------+")
            print("| CÁLCULO DEL SENO |")
            print("+------------------+")

            resultado = Operaciones.operacionSen(num1)
            print("\nEl sen(", num1, ") es: ", resultado)

        if respuesta == 8:

            print("\n+--------------------+")
            print("| CÁLCULO DEL COSENO |")
            print("+--------------------+")
            
            resultado = Operaciones.operacionCos(num1)
            print("\nEl cos(", num1, ") es: ", resultado)

        if respuesta == 9:
            
            print("\n+------------------------+")
            print("| CÁLCULO DE LA TANGENTE |")
            print("+------------------------+")

            resultado = Operaciones.operacionTan(num1)
            print("\nLa tan(", num1, ") es: ", resultado)

    if respuesta == 10:

        print("\n+-----------------+")
        print("| FIN DEL PROGAMA |")
        print("+-----------------+\n")

        break