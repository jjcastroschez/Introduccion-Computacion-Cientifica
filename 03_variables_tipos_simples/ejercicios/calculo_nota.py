PESO1PRUEBA=0.1
PESO2PRUEBA=0.15
PESO3PRUEBA=0.1

califPrimeraPrueba=float(input("Dame la calificación de la primera prueba: "))
califSegundaPrueba=float(input("Dame la calificación de la segunda prueba: ")) 
califTerceraPrueba=float(input("Dame la calificación de la tercera prueba: "))  

calif1=califPrimeraPrueba*PESO1PRUEBA
calif2=califSegundaPrueba*PESO2PRUEBA
calif3=califTerceraPrueba*PESO3PRUEBA

notaPruebasProgreso=calif1 + calif2 + calif3   
print(f"La calificación obtenida es: {notaPruebasProgreso:.2f} sobre 4")
