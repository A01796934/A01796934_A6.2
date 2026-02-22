"""
Main entry point for the Reservation System.
"""
from src.hotel import Hotel
from src.customer import Customer
from src.reservation import Reservation


def run_demo():
    """
    Demonstrates the basic functionality of the system.
    """
    print("--- Inciando Sistema de Reservaciones ---")

    # 1. Crear un Hotel
    hotel = Hotel(1, "Hotel Maya", "Cancun", 50)
    hotel.save_to_file()
    print(f"Hotel '{hotel.name}' guardado con éxito.")

    # 2. Crear un Cliente
    cliente = Customer(101, "Fernando Perez", "fer@mail.com")
    cliente.save_to_file()
    print(f"Cliente '{cliente.name}' registrado.")

    # 3. Crear una Reservación
    reserva = Reservation(5001, 101, 1)
    reserva.save_to_file()
    print(f"Reservación {reserva.reservation_id} creada.")

    # 4. Mostrar información (Usando los métodos estáticos)
    print("\n--- Consultando Datos ---")
    Customer.display_customer(101)

    print("\n--- Proceso Terminado ---")


if __name__ == "__main__":
    run_demo()
