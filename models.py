from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()  # Bas för alla modeller, denna tas från Martinas sen

# Ta bort denna sen
# class Booking(Base):
    # __tablename__ = 'bookings'
    
    # booking_id = Column(Integer, primary_key=True)
    # customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    # service_id = Column(Integer, ForeignKey('services.service_id'))
    # mechanic_id = Column(Integer, ForeignKey('mechanics.mechanic_id'))
    # booking_date = Column(DateTime)
    # status = Column(String)
    
    # customer = relationship("Customer", back_populates="bookings")
    # service = relationship("Service", back_populates="bookings")
    # mechanic = relationship("Mechanic", back_populates="bookings")
    # orders = relationship("Order", back_populates="booking")
    # payments = relationship("Payment", back_populates="booking")
    # logistics = relationship("Logistic", back_populates="booking")


# Klass för logistik
class Logistics(Base):
    __tablename__ = 'logistics'

    logistics_id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'), nullable=False)
    pickup_location = Column(String, nullable=False)
    dropoff_location = Column(String, nullable=False)
    pickup_date = Column(DateTime, nullable=False)
    dropoff_date = Column(DateTime, nullable=False)

    bookings = relationship('Booking', back_populates='logistics')

# Klass för inventarie
class Inventory(Base):
    __tablename__ = 'inventory'

    inventory_id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)

    orders = relationship('Order', back_populates='inventory')  # Se till att Order-klass är korrekt definierad

# Klass för mekaniker
class Mechanics(Base):
    __tablename__ = 'mechanics'

    mechanic_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialization = Column(String)

    bookings = relationship('Booking', back_populates='mechanic')


# Funktion för att skapa databasen och sessionen
def create_database():
    engine = create_engine('sqlite:///mc_booking.sqlite', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == '__main__':
    session = create_database()
    print('Databasen och tabellerna har skapats framgångsrikt')
