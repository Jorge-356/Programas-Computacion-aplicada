# -------------------------------------------------------------
# Tercer examen Parcial                                       -
# Materia: Computacion Aplicada                               -
# Programa: Maestria en ingenieria y tecnologia aplicada      -  
# Maestro: Dr. Carlos Héctor Castañeda Ramírez                -
# Alumno: Ing. Jorge Murillo Dominguez                        -
# -------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# Programacion orientada a objetos                                                                        -
# Este código implementa una estructura de clases en Python para gestionar los jugadores y categorías     -
# de la Academia de Fútbol Santos Laguna.                                                                 -
# Utiliza programación orientada a objetos para organizar la información y generar un reporte con formato -
# mostrando detalles de la academia, sus categorías y los jugadores en cada una                           -
# ---------------------------------------------------------------------------------------------------------

class Jugador:
    def __init__(self, nombre, anio_nac, sexo, becado):
        self.nombre = nombre
        self.anio_nac = anio_nac
        self.sexo = sexo
        self.becado = becado  # True si está becado, False si no

    def __str__(self):
        beca_estado = "Becado" if self.becado else "Sin Beca"
        return f"{self.nombre:<20} {self.anio_nac:<10} {self.sexo:<10} {beca_estado}"


class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango  # Rango en formato de años, e.g., "2006/2007/2008"
        self.costo = costo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def subtotal_categoria(self):
        # Calcula el subtotal considerando solo los jugadores no becados
        return sum(self.costo for jugador in self.jugadores if not jugador.becado)

    def __str__(self):
        return f"{self.nombre:<10} Rango: {self.rango:<15} Costo: ${self.costo:,.2f}"


class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def total_categorias(self):
        return len(self.categorias)

    def total_hombres(self):
        return sum(jugador.sexo == "Hombre" for categoria in self.categorias for jugador in categoria.jugadores)

    def total_mujeres(self):
        return sum(jugador.sexo == "Mujer" for categoria in self.categorias for jugador in categoria.jugadores)

    def total_ingresos(self):
        return sum(categoria.subtotal_categoria() for categoria in self.categorias)

    def reporte(self):
        # Imprime el reporte de la academia, categorías y jugadores con formato
        print("REPORTE DEL CLUB DEPORTIVO".center(50, "="))
        print(f"Nombre:      {self.nombre}")
        print(f"Propietario: {self.propietario}")
        print(f"Domicilio:   {self.domicilio}")
        print(f"Total de Categorías: {self.total_categorias()}")
        print(f"Total de Hombres:   {self.total_hombres()}")
        print(f"Total de Mujeres:   {self.total_mujeres()}")
        print("\n>> Datos generales de las Categorías")
        for categoria in self.categorias:
            print(" " * 4 + str(categoria))  # Indentado para claridad
        print("\n>> Jugadores por Categoría:")
        for categoria in self.categorias:
            print(f"\n> {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})")
            print(f"{'Nombre':<20} {'AñoNac':<10} {'Sexo':<10} {'Becado'}")
            print("-" * 50)
            for jugador in categoria.jugadores:
                print(jugador)
            print(f"- SubTotal : ${categoria.subtotal_categoria():,.2f}")
        print(f"\n-> Total : ${self.total_ingresos():,.2f}")
        print("=" * 50)


# --- Datos de prueba ---
def main():
    academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")

    # Creando categorías y jugadores
    categoria1 = Categoria("Junior A", "2006/2007/2008", 1250.00)
    categoria1.agregar_jugador(Jugador("Alexander Lopez", 2006, "Hombre", False))
    categoria1.agregar_jugador(Jugador("Uriel Puga", 2007, "Hombre", True))
    categoria1.agregar_jugador(Jugador("Alejandra Escalona", 2008, "Mujer", False))

    categoria2 = Categoria("Junior B", "2009/2010/2011", 850.00)
    categoria2.agregar_jugador(Jugador("Armando Santana", 2009, "Hombre", False))
    categoria2.agregar_jugador(Jugador("Daniel Mijares", 2010, "Hombre", False))
    categoria2.agregar_jugador(Jugador("Antonio Hernandez", 2011, "Mujer", True))

    categoria3 = Categoria("Pony A", "2012/2013/2014", 700.00)
    categoria3.agregar_jugador(Jugador("Andrea Solis", 2012, "Mujer", True))
    categoria3.agregar_jugador(Jugador("Marissa Hernandez", 2013, "Mujer", True))
    categoria3.agregar_jugador(Jugador("Diana Soto", 2014, "Mujer", False))

    # Agregando categorías a la academia
    academia.agregar_categoria(categoria1)
    academia.agregar_categoria(categoria2)
    academia.agregar_categoria(categoria3)

    # Generando el reporte
    academia.reporte()


if __name__ == "__main__":
    main()
