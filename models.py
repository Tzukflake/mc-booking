from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, VARCHAR, DateTime
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()

# class Booking(Base):
#     __tablename__ = 'bookings'
    
#     booking_id = Column(Integer, primary_key=True)
#     customer_id = Column(Integer, ForeignKey('customers.customer_id'))
#     service_id = Column(Integer, ForeignKey('services.service_id'))
#     booking_date = Column(DateTime)
#     status = Column(String)
    
#     customer = relationship("Customer", back_populates="bookings")
#     service = relationship("Service", back_populates="bookings")
#     payments = relationship("Payment", back_populates="booking")

class Service(Base):
    __tablename__ = 'services'

    service_id = Column(Integer, primary_key=True)
    service_name = Column(VARCHAR(255), nullable=False)
    description = Column(VARCHAR(255), nullable=False)
    cost = Column(Integer, nullable=False)

    bookings = relationship('Booking', back_populates='service')

class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    address = Column(VARCHAR(255), nullable=False)
    phone = Column(String(20), nullable=False)  # Phone numbers should be stored as strings
    email = Column(VARCHAR(255), nullable=False)
    motorcycle_model = Column(VARCHAR(255), nullable=False)

    bookings = relationship('Booking', back_populates='customer')

class Payment(Base):
    __tablename__ = 'payments'

    payment_id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'), nullable=False)
    amount = Column(Integer, nullable=False)
    payment_date = Column(DateTime, nullable=False)
    payment_method = Column(VARCHAR(50), nullable=False)

    booking = relationship('Booking', back_populates='payments')

def create_database():
    engine = create_engine('sqlite:///mc_booking.sqlite', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == '__main__':
    session = create_database()
    print('Creation successful')


def add_service(service_name, description, cost):
    # Skapa en ny tjänst
    new_service = Service(
        service_name=service_name,
        description=description,
        cost=cost
    )

    # Lägg till tjänsten i sessionen
    session.add(new_service)
    
    # Spara ändringar i databasen
    session.commit()
    
    print("Tjänsten har lagts till framgångsrikt!")

def add_customer(first_name, last_name, address, phone, email, motorcycle_model):
    # Skapa en ny kund
    new_customer = Customer(
        first_name=first_name,
        last_name=last_name,
        address=address,
        phone=phone,
        email=email,
        motorcycle_model=motorcycle_model
    )

    # Lägg till kunden i sessionen
    session.add(new_customer)
    
    # Spara ändringar i databasen
    session.commit()
    
    print("Kunden har lagts till framgångsrikt!")


def add_payment(booking_id, amount, payment_date, payment_method):
    # Skapa en ny betalning
    new_payment = Payment(
        booking_id=booking_id,
        amount=amount,
        payment_date=payment_date,
        payment_method=payment_method
    )

    # Lägg till betalningen i sessionen
    session.add(new_payment)
    
    # Spara ändringar i databasen
    session.commit()
    
    print("Betalningen har lagts till framgångsrikt!")



# Example: Adding a new service
service_name = "Oil Change"
description = "Full oil change with synthetic oil"
cost = 120
add_service(service_name, description, cost)

# Example: Adding a new customer
first_name = "John"
last_name = "Doe"
address = "1234 Elm Street"
phone = "123-456-7890"
email = "john.doe@example.com"
motorcycle_model = "Harley Davidson"
add_customer(first_name, last_name, address, phone, email, motorcycle_model)

# Example: Adding a new payment
booking_id = 1  # Assuming the booking with ID 1 already exists
amount = 120
payment_date = datetime.strptime("2024-08-31", "%Y-%m-%d")
payment_method = "Credit Card"
add_payment(booking_id, amount, payment_date, payment_method)


