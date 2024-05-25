# Control de jugadores de la academia de futbol Santos Laguna
import os

class Jugador:
    def __init__(self, nombre, añoNac, sexo, becado):
        self.nombre = nombre
        self.añoNac = añoNac
        self.sexo   = sexo
        self.becado = becado
    def __str__(self):
        return f"Nombre: {self.nombre:<20} AñoNac: {self.añoNac:<10} Sexo: {self.sexo:<10} Becado: {self.becado}"
    
class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre    = nombre
        self.rango     = rango
        self.costo     = costo 
        self.jugadores = list()
    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)
    def totalCategoria(self):
        total = 0
        for jugador in self.jugadores:
            if jugador.becado.upper() == "SIN BECA":
                total += self.costo
        return total

    def __str__(self):
        return f"Nombre: {self.nombre:<15} Rango: {self.rango:<20} Costo: ${self.costo:,.2f}"
    
class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre      = nombre
        self.propietario = propietario 
        self.domicilio   = domicilio
        self.categorias  = list()
    def agregarCategoria(self, categoria):
        self.categorias.append(categoria)
    def totalHombres(self):
        total = 0
        for categoria in self.categorias:
            for jugador in categoria.jugadores:
                if jugador.sexo.upper() == "HOMBRE":
                    total += 1
        return total
    def totalMujeres(self):
        total = 0
        for categoria in self.categorias:
            for jugador in categoria.jugadores:
                if jugador.sexo.upper() == "MUJER":
                    total += 1
        return total
    def totalIngresos(self):
        total = 0
        for categoria in self.categorias:
            total += categoria.totalCategoria()
        return total
    def __str__(self):
        return f"Nombre:       {self.nombre} \nPropietario:  {self.propietario} \nDomicilio:    {self.domicilio}"

def Reporte(academia):
    os.system("cls")
    print("REPORTE DEL CLUB DEPORTIVO \n")
    print(academia)
    print(f"\nTotal de Categorias: {len(academia.categorias)}")
    print(f"Total de Hombres:    {academia.totalHombres()}")
    print(f"Total de Mujeres:    {academia.totalMujeres()}")
    
    print("\n\n>> Datos Generales de las Categorias \n")
    for categoria in academia.categorias:
        print(categoria)
    
    print("\n\n>> Jugadores por Categoria: ")
    for categoria in academia.categorias:
        print(f"\n> {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})\n")
        for jugador in categoria.jugadores:
            print(jugador)
        print(f"\n- Subtotal: ${categoria.totalCategoria():,.2f}\n")
    print(f"\n-> Total: ${academia.totalIngresos():,.2f}")

# el programa le da la opcion al usuario de agregar nuevos jugadores y nuevas categorias 
categorias = ["Junior A", "Junior B", "Pony A"]
def LeerCategoria(academia):
    print("\nIngrese los datos de la categoria: ")
    nombre = input("Nombre ? ")
    if nombre not in categorias:
        rango = input("Rango ? ")
        costo = float(input("Costo ? "))
        categoria = Categoria(nombre, rango, costo)
        categorias.append(nombre)
        academia.agregarCategoria(categoria)
    cat = nombre
    return cat

def LeerJugador(categoria, academia):
    print("\nIngrese los datos del jugador: ")
    nombre = input("nombre ? ")
    añoNac = input("Año de nacimiento ? ")
    sexo = input("Sexo ? ")
    becado = input("Becado ? ")
    jugador = Jugador(nombre, añoNac, sexo, becado)
    academia.categorias[categorias.index(categoria)].agregarJugador(jugador)

def main():
    os.system("cls")
    
    academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")
    academia.agregarCategoria(Categoria(nombre = "Junior A", rango = "2006/2007/2008", costo = 1250))
    academia.agregarCategoria(Categoria(nombre = "Junior B", rango = "2009/2010/2011", costo = 850))
    academia.agregarCategoria(Categoria(nombre = "Pony A",   rango = "2012/2013/2014", costo = 700))

    academia.categorias[0].agregarJugador(Jugador(nombre = "Alexander Lopez", añoNac = 2006, sexo = "Hombre", becado = "Sin Beca"))
    academia.categorias[0].agregarJugador(Jugador(nombre = "Uriel Puga", añoNac = 2007, sexo = "Hombre", becado = "Becado"))
    academia.categorias[0].agregarJugador(Jugador(nombre = "Alejandra Escalona", añoNac = 2008, sexo = "Mujer", becado = "Sin Beca"))
    
    academia.categorias[1].agregarJugador(Jugador(nombre = "Armando Santana", añoNac = 2009, sexo = "Hombre", becado = "Sin Beca"))
    academia.categorias[1].agregarJugador(Jugador(nombre = "Daniel Mijares", añoNac = 2010, sexo = "Hombre", becado = "Sin Beca"))
    academia.categorias[1].agregarJugador(Jugador(nombre = "Antonia Hernandez", añoNac = 2011, sexo = "Mujer", becado = "Becado"))
    
    academia.categorias[2].agregarJugador(Jugador(nombre = "Andrea Solis", añoNac = 2012, sexo = "Mujer", becado = "Becado"))
    academia.categorias[2].agregarJugador(Jugador(nombre = "Marissa Hernandez", añoNac = 2013, sexo = "Mujer", becado = "Becado"))
    academia.categorias[2].agregarJugador(Jugador(nombre = "Diana Soto", añoNac = 2014, sexo = "Mujer", becado = "Sin Beca"))
    
    #Reporte(academia)

    # Menu de seleccion de operaciones entre impresion del reporte o añadir jugadores y categorias  
    while True:
        os.system("cls")
        print("Bienvenido a la base de datos de la academia Santos Laguna\n")
        print("[ A ] Añadir un nuevo jugador\n[ C ] Consultar información existente")

        op = input("Seleccione una opcion ? ").upper()
        if op == "A":  
            cat = LeerCategoria(academia)
            LeerJugador(cat, academia)

        if op == "C":
            Reporte(academia)
        
        res = input("\nDesea continuar (S/N) ? ").upper()
        if res == "N": break
            

if __name__ == "__main__":
    main()