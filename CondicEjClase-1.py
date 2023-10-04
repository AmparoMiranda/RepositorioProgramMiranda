#Solicitar al usuario que ingrese la fecha actual en formato “día, DD/MM”
date = input("Ingrese la fecha actual (dia de la semana, DD/MM): ")
#Convertir a minusculas
date = date.lower()
#Separar la variable date en 3 variables diferentes
week_day = date[0:date.find(",")]
day = int(date[date.find(" ") + 1:date.find("/")])
month = int(date[date.find("/")+1:])
#Comprobar que la fecha ingresada sea correcto
if week_day == "lunes" or week_day == "martes" or week_day == "miercoles" or week_day == "jueves" or week_day == "viernes" or week_day == "sabado" or week_day == "domingo":
    if day > 0 and  day < 31:
        if(month>0 and month<13):
            print(" ")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")
#Indicar si ese dia se tomaron examenes en nivel inicial, intermedio y avanzado
if(week_day == "lunes" or week_day == "martes" or week_day == "miercoles"):
    condition = input("Hoy se tomaron examenes?(SI/NO): ")
    condition.lower()
    #Cantidad de alumnos aprobados/desaprobados
    if(condition == "si"):
        approved = input("Ingrese la cantidad de aprobados: ")
        disapproved = input("Ingrese la cantidad de desaprobados: ")
        #Porcentaje de alumnos aprobados
        percent = (approved + disapproved)/approved
        print("El porcentaje de alumnos aprobados es: "+percent)
    #Asistencia en porcentajes en la clase de practica hablada
elif week_day == "jueves":
    attendance = input("Ingrese el porcentaje de asistencia en la clase de practica hablada")
    if attendance > 50:
        print("Asistió la mayoría")
    else :
        print("No asistió la mayoría")
    #Nuevo ciclo en ingles para viajeros
elif week_day == "viernes":
    if (day == 1) and (month == 1 or month == 7):
        print("Comienzo de nuevo ciclo")
        #Cantidad de alumnos del curso
        students_number = input("Ingrese la cantidad de alumnos del nuevo ciclo: ")
        #Aranceles por alumno
        tariff = input("Ingrese el arancel por cada alumno: ")
        #Ingreso total
        total_revenue = students_number * tariff
        print("El ingreso total es: " + total_revenue)

