while 1 == 1:
    prueba = open("/home/pi/pitando/Lista_usuarios.csv","a")
    print("Introduce el numero de empleado\n")
    Num = str(input())
    import time
    hora = time.strftime("%H:%M:%S")
    fecha = time.strftime("%d/%m/%y")
    prueba.write(Num)
    prueba.write(",")
    prueba.write(hora)
    prueba.write(",")
    prueba.write(fecha)
    prueba.write("\n")
    prueba.close()
        
