from abc import ABC, abstractmethod

# 1. Single Responsibility Principle (SRP):

class BookingService:
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def book_room(self, room_type, guest_name, nights):
        total_price = room_type.get_price() * nights
        if self.payment_service.process_payment(total_price):
            return f"Booking successful for {guest_name} in {room_type.get_name()} for {nights} nights."
        return "Booking failed due to payment error."

# 2. Open/Closed Principle (OCP):

class Room(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

class StandardRoom(Room):
    def get_price(self):
        return 100  

    def get_name(self):
        return "Standard Room"

class DeluxeRoom(Room):
    def get_price(self):
        return 200  

    def get_name(self):
        return "Deluxe Room"

# 3. Liskov Substitution Principle (LSP):

class SuiteRoom(Room):
    def get_price(self):
        return 300

    def get_name(self):
        return "Suite Room"

# 4. Interface Segregation Principle (ISP):
class PaymentService(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class Payment(ABC):
    @abstractmethod
    def process_info(self, amount):
        pass

class CreditCardPayment(PaymentService):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"Processing credit card payment amount: ${amount}")
        return True

class PayPalPayment(PaymentService,Payment):
    def __init__(self, email, currency):
        self.email = email
        self.currency = currency

    def process_payment(self, amount):
        print("Processing PayPal payment is Success")
        return True
    def process_info(self, amount):
        print(f"Processing PayPal payment for {self.email}, amount: {amount} {self.currency}")
        return True

# 5. **Dependency Inversion Principle (DIP)**:
class HotelBookingApp:
    def __init__(self, booking_service):
        self.booking_service = booking_service

    def make_booking(self, room_type, guest_name, nights):
        return self.booking_service.book_room(room_type, guest_name, nights)


credit_card_payment = CreditCardPayment("1234-5678-9876-5432")
paypal_payment = PayPalPayment("ahmed@example.com",'USD')

booking_service_credit = BookingService(credit_card_payment)
booking_service_paypal = BookingService(paypal_payment)

standard_room = StandardRoom()
deluxe_room = DeluxeRoom()

hotel_app_credit = HotelBookingApp(booking_service_credit)
hotel_app_paypal = HotelBookingApp(booking_service_paypal)

print(hotel_app_credit.make_booking(standard_room, "Mohamed", 3))
print(hotel_app_paypal.make_booking(deluxe_room, "Ahmed", 2))
