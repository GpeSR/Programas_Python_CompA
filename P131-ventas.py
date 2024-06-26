# Control de ventas orientado a objetos
class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio
        self.total = cantidad * precio
    def __str__(self):
        return f"Articulo: {self.articulo:<15} Cantidad: {self.cantidad:>10,.2f} Precio: {self.precio:>10,.2f} Total: {self.total:>10,.2f}"
    
class Cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc = rfc
        self.nombre = nombre
        self.domicilio = domicilio
        self.correo = correo 
        self.ventas = list()
    def agregarVenta(self, venta):
        self.ventas.append(venta)
    def totalVentas(self):
        total = 0
        for venta in self.ventas:
            total += venta.total
        return total
    def __str__(self):
        return f"Cliente -> [ Nombre: {self.nombre:<15} RFC: {self.rfc:<12} Domicilio: {self.domicilio:<20} Correo: {self.correo:<30} ]" 
    
class Tienda:
    def __init__(self, nombre, domicilio, propietario):
        self.nombre = nombre
        self.domicilio = domicilio
        self.propietario = propietario
        self.clientes = list()
    def agregarCliente(self, cliente):
        self.clientes.append(cliente)
    def totalVentas(self):
        total = 0
        for cliente in self.clientes:
            total += len(cliente.ventas)
        return total 
    def totalImportVentas(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.totalVentas()
        return total
    def __str__(self):
        return f"Tienda [ Nombre: {self.nombre} Domicilio: {self.domicilio} Propietario: {self.propietario} ]"

def Reporte(mitienda):
    print("\nReporte de Ventas ", mitienda)
    print(f"Total de clientes: {len(mitienda.clientes)}")
    print(f"Total Ventas     : {mitienda.totalVentas()}")
    print("\nClientes:")
    for cliente in mitienda.clientes:
        print(cliente)
        for venta in cliente.ventas:
            print(venta)
        print(f"Total Ventas: {cliente.totalVentas():,.2f}\n")
    print(f"\nTotal General: {mitienda.totalImportVentas():,.2f}")

def LeerCliente(mitienda):
    print("\nIngrese los datos del Cliente")
    rfc       = input("RFC      : ")
    nombre    = input("Nombre   : ")
    domicilio = input("Domicilio: ")
    correo    = input("Correo   : ")
    cliente = Cliente(rfc, nombre, domicilio, correo)
    mitienda.agregarCliente(cliente)

def LeerVenta(cliente):
    print("\nLeer venta")
    articulo = input("Articulo : ")
    cantidad = float(input("Cantidad : "))
    precio   = float(input("Precio   : "))
    venta = Venta(articulo, cantidad, precio)
    cliente.agregarVenta(venta)


def main():
    import os
    os.system("cls")
    mitienda = Tienda(nombre = "Ferreteria las Lomas", domicilio = "Av Luis Moya 345", propietario = "Carlos Castañeda")
    print(mitienda)
    v1 = Venta(articulo = "Martillo", cantidad = 10, precio = 60.5)
    #print(v1)
    v2 = Venta(articulo = "Pala", cantidad = 2, precio = 1170.55)
    #print(v2)
    c1 = Cliente(rfc="JELI20240", nombre = "Felipe Calderón", domicilio = "Las Lomas 123", correo = "calderon.com")
    c1.agregarVenta(v1)
    c1.agregarVenta(v2)
    mitienda.agregarCliente(c1)
    mitienda.agregarCliente( Cliente(rfc='PEÑA121250',nombre='Enrique Peña',domicilio='5 de Mayo 321',correo='quique@gmail.com') )
    mitienda.agregarCliente( Cliente(rfc='AMLO101145',nombre='Andres Lopez',domicilio='Palacio Nacional 321',correo='peje@yahoo.com') )
    mitienda.agregarCliente( Cliente(rfc='GELA666666',nombre='Xochitl Gelatinas',domicilio='Danone 123',correo='xochitl@precidencia.gob.mx') )
    mitienda.clientes[1].agregarVenta( Venta(articulo='Clavo',cantidad=2.5,precio=160.34) )
    mitienda.clientes[1].agregarVenta( Venta(articulo='Cinta de Aislar',cantidad=5,precio=71.34) )
    mitienda.clientes[1].agregarVenta( Venta(articulo='Pinzas',cantidad=10,precio=650.33) )
    mitienda.clientes[2].agregarVenta( Venta(articulo='Thiner',cantidad=50,precio=65.00) )
    mitienda.clientes[3].agregarVenta( Venta(articulo='Gelatinas',cantidad=150,precio=165.00) )
    LeerCliente(mitienda)
    LeerVenta(mitienda.clientes[4])
    Reporte(mitienda)
    #print(c1)
    #print(c1.ventas[0])
    #print(c1.ventas[1])
    #print(c1.totalVentas())

if __name__ == "__main__" :
    main()