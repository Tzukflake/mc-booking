from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()  # Bas för alla modeller, denna tas från Martinas sen


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
