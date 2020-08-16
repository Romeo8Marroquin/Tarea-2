import csv
with open("alumnos.csv") as archivo:
    datos = csv.reader(archivo, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
    print(" ")
    print("Datos CSV:")
    print(type(archivo))
    for alumno in datos:
        print(" ")
        print("Edad: ", alumno[0])
        print("Carné: ", alumno[1])
        print("Semestre: ", alumno[2])
        print("Nota: ", alumno[3])
input()