import json
with open("alumnos.json") as archivo:
    datos = json.load(archivo)
    print("Datos JSON:")
    print(type(archivo))
    for alumno in datos["alumnos"]:
        print(" ")
        print("Edad: ", alumno["edad"])
        print("Carné: ", alumno["carne"])
        print("Semestre: ", alumno["semestre"])
        print("Nota: ", alumno["nota"])
print(" ")