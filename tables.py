from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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




