# from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, VARCHAR, DateTime
# from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Base = declarative_base()

# # class Booking(Base):
# #     __tablename__ = 'bookings'
    
# #     booking_id = Column(Integer, primary_key=True)
# #     customer_id = Column(Integer, ForeignKey('customers.customer_id'))
# #     service_id = Column(Integer, ForeignKey('services.service_id'))
# #     booking_date = Column(DateTime)
# #     status = Column(String)
    
# #     customer = relationship("Customer", back_populates="bookings")
# #     service = relationship("Service", back_populates="bookings")
# #     payments = relationship("Payment", back_populates="booking")

# class Service(Base):
#     __tablename__ = 'services'

#     service_id = Column(Integer, primary_key=True)
#     service_name = Column(VARCHAR(255), nullable=False)
#     description = Column(VARCHAR(255), nullable=False)
#     cost = Column(Integer, nullable=False)

#     bookings = relationship('Booking', back_populates='service')

# class Customer(Base):
#     __tablename__ = 'customers'

#     customer_id = Column(Integer, primary_key=True)
#     first_name = Column(String(255), nullable=False)
#     last_name = Column(String(255), nullable=False)
#     address = Column(VARCHAR(255), nullable=False)
#     phone = Column(String(20), nullable=False)  # Phone numbers should be stored as strings
#     email = Column(VARCHAR(255), nullable=False)
#     motorcycle_model = Column(VARCHAR(255), nullable=False)

#     bookings = relationship('Booking', back_populates='customer')

# class Payment(Base):
#     __tablename__ = 'payments'

#     payment_id = Column(Integer, primary_key=True)
#     booking_id = Column(Integer, ForeignKey('bookings.booking_id'), nullable=False)
#     amount = Column(Integer, nullable=False)
#     payment_date = Column(DateTime, nullable=False)
#     payment_method = Column(VARCHAR(50), nullable=False)

#     booking = relationship('Booking', back_populates='payments')
    

# class Logistics(Base):
#     __tablename__ = 'logistics'

#     logistics_id = Column(Integer, primary_key=True)
#     booking_id = Column(Integer, ForeignKey('bookings.booking_id'), nullable=False)
#     pickup_location = Column(String, nullable=False)
#     dropoff_location = Column(String, nullable=False)
#     pickup_date = Column(DateTime, nullable=False)
#     dropoff_date = Column(DateTime, nullable=False)

#     bookings = relationship('Booking', back_populates='logistics')

# class Inventory(Base):
#     __tablename__ = 'inventory'

#     inventory_id = Column(Integer, primary_key=True)
#     item_name = Column(String, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     unit_price = Column(Integer, nullable=False)

#     orders = relationship('Order', back_populates='inventory')  # Se till att Order-klass är korrekt definierad

# class Mechanics(Base):
#     __tablename__ = 'mechanics'

#     mechanic_id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     specialization = Column(String)

#     bookings = relationship('Booking', back_populates='mechanic')


# def create_database():
#     engine = create_engine('sqlite:///mc_booking.sqlite', echo=True)
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session


# if __name__ == '__main__':
#     session = create_database()
#     print('Creation successful')

