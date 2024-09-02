from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime, VARCHAR
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship,declarative_base

Base = declarative_base()

# Tabellen för bokningar
class Booking(Base):
    __tablename__ = 'bookings'
    
    booking_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    service_id = Column(Integer, ForeignKey('services.service_id'))
    mechanic_id = Column(Integer, ForeignKey('mechanics.mechanic_id'))
    booking_date = Column(DateTime)
    status = Column(String)
    
    customer = relationship("Customer", back_populates="bookings")
    service = relationship("Service", back_populates="bookings")
    mechanic = relationship("Mechanic", back_populates="bookings")
    orders = relationship("Order", back_populates="booking")
    payments = relationship("Payment", back_populates="booking")
    logistics = relationship("Logistic", back_populates="booking")

# Tabellen för beställningar
class Order(Base):
    __tablename__ = 'orders'
    
    order_id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'))
    inventory_id = Column(Integer, ForeignKey('inventory.inventory_id'))
    item_name = Column(String)
    quantity = Column(Integer)
    status = Column(String)

    booking = relationship("Booking", back_populates="orders")
    inventory = relationship("Inventory", back_populates="orders")

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
    

class Logistics(Base):
    __tablename__ = 'logistics'

    logistics_id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'), nullable=False)
    pickup_location = Column(String, nullable=False)
    dropoff_location = Column(String, nullable=False)
    pickup_date = Column(DateTime, nullable=False)
    dropoff_date = Column(DateTime, nullable=False)

    bookings = relationship('Booking', back_populates='logistics')

class Inventory(Base):
    __tablename__ = 'inventory'

    inventory_id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)

    orders = relationship('Order', back_populates='inventory')  # Se till att Order-klass är korrekt definierad

class Mechanics(Base):
    __tablename__ = 'mechanics'

    mechanic_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialization = Column(String)

    bookings = relationship('Booking', back_populates='mechanic')

#skapa databas och engine
db = "sqlite:///bokningssystem.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

#skapa session
Session = sessionmaker(bind=engine)
session = Session()


#Lägg till ny bokning i Booking-tabellen
def add_booking(customer_id, service_id, mechanic_id, booking_date, status):
    # Skapa en ny bokning
    new_booking = Booking(
        customer_id=customer_id,
        service_id=service_id,
        mechanic_id=mechanic_id,
        booking_date=booking_date,
        status=status
    )

    # Lägg till bokningen i sessionen
    session.add(new_booking)
    
    # Spara ändringar i databasen
    session.commit()
    
    print("Bokningen har lagts till framgångsrikt!")

#Lägg till en ny beställning i Order-tabellen
def add_order(booking_id, inventory_id, item_name, quantity, status):
    # Skapa en ny beställning
    new_order = Order(
        booking_id=booking_id,
        inventory_id=inventory_id,
        item_name=item_name,
        quantity=quantity,
        status=status
    )
    
    # Lägg till beställningen i sessionen
    session.add(new_order)
    
    # Spara ändringar i databasen
    session.commit()
    
    print("Beställningen har lagts till framgångsrikt!")

#Lägg till data

#lägg till bokning
customer_id= 1
service_id= 1
mechanic_id= 1 
booking_date= "2024-08-30" #format?
status= "pågående"
add_booking(customer_id, service_id, mechanic_id, booking_date, status, session)


#Lägg till order
booking_id= 1
inventory_id= 1
item_name= "avgasrör"
quantity= 1
status= "skickad"
add_order(booking_id, inventory_id, item_name, quantity, status, session)




