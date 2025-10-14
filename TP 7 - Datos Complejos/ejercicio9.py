agenda:dict = {("Lunes", "14:30"): "Arquitectura y Sistemas Operativos", 
               ("Martes","15:00"): "Matemática",  
               ("Miercoles", "14:45"): "Programación I",
               ("Jueves", "14:00"): "Organización Empresarial",
               ("Viernes", "16:00"): "Programación I (Consulta)"
               }

print(f"""
------------------------------------------------------      
                 Agenda Facultativa.
------------------------------------------------------          
      """)
dia:str = str(input("Ingrese el día a consultar: ")).capitalize()
hora:str = str(input("Ingrese la hora a consultar (formato 24hs, ej: 14:30): "))

if (dia, hora) in agenda:
    print(f"La actividad para el {dia} a las {hora} es: {agenda.get((dia, hora))}")
else:
    print(f"No hay ninguna actividad registrada para el {dia} a las {hora}.")    