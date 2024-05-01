import os
import datetime, calendar

# Uso de algunas funciones del modulo: os
os.system("cls")
print("Sistema operativo ,", os.uname())
print("Carpeta actual ", os.getcwd())
os.chdir("/")
print(os.listdir())
print("\nVariables de entorno:", os.environ)
print("\nRuta:", os.getenv("PATH"))

# Uso de algunas funciones del modulo: datetime
ahora = datetime.datetime.now()
print("\nFecha y hora actuales", ahora)
print("\nLa fecha actual:", ahora.strftime("%b / %d / %Y"))
print("La hora actual:", ahora.strftime("%H:%M"))

# Uso de algunas funciones del modulo: calendar
print("\nCalendario anual 2024:\n")
calendar.prcal(2024)
print("Calendario de un mes especifico:\n")
calendar.prmonth(2024,4)
