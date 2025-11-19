from entradas import General, VIP, Estudiante, Grupo
from decoradores import DescuentoEstudiante, PromocionEspecial, VIPDecorador

def main():
    # Entrada General simple
    print("\n1. Entrada General (3 personas):")
    entrada1 = General(cant_personas=3, evento="Concierto de Rock")
    print(f"{entrada1.obtener_descripcion()}")
    print(f"Precio Total: {entrada1.calcular_precio()}")

    # Entrada VIP simple
    print("\n2. Entrada VIP (2 personas):")
    entrada2 = VIP(cant_personas=2, evento="Obra de Teatro")
    print(f"{entrada2.obtener_descripcion()}")
    print(f"Precio Total: {entrada2.calcular_precio()}")

    # Estudiante con descuento
    print("\n3. Entrada Estudiante con Descuento:")
    entrada3 = Estudiante(cant_personas=2, evento="Exposición de Arte")
    entrada3_decorada = DescuentoEstudiante(entrada3)
    print(f"{entrada3_decorada.obtener_descripcion()}")
    print(f"Precio Original: {entrada3.calcular_precio()}")
    print(f"Precio Final: {entrada3_decorada.calcular_precio()}")

    # Entrada General con Promoción Especial
    print("\n4. Entrada General con Promoción Especial:")
    entrada4 = General(cant_personas=5, evento="Festival de Danza")
    entrada4_decorada = PromocionEspecial(entrada4, descuento=0.25)
    print(f"{entrada4_decorada.obtener_descripcion()}")
    print(f"Precio Original: {entrada4.calcular_precio()}")
    print(f"Precio Final: {entrada4_decorada.calcular_precio()}")

    # Varios decoradores (Estudiante + Promoción)
    print("\n5. Estudiante con Promoción Especial (Decoradores Anidados):")
    entrada5 = Estudiante(cant_personas=1, evento="Concierto Sinfónico")
    entrada5_decorada = PromocionEspecial(DescuentoEstudiante(entrada5, descuento=0.10),descuento=0.15)
    print(f"{entrada5_decorada.obtener_descripcion()}")
    print(f"Precio Original: {entrada5.calcular_precio()}")
    print(f"Precio Final: {entrada5_decorada.calcular_precio()}")

    # Entrada de Grupo con upgrade VIP
    print("\n6. Entrada Grupal con Upgrade VIP:")
    entrada6 = Grupo(cant_personas=10, evento="Concierto")
    entrada6_decorada = VIPDecorador(entrada6, precio_adicional=15000)
    print(f"{entrada6_decorada.obtener_descripcion()}")
    print(f"Precio Base: {entrada6.calcular_precio()}")
    print(f"Precio Final: {entrada6_decorada.calcular_precio()}")

if __name__ == "__main__":
    main()
