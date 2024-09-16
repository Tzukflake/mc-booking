# mc-booking system made in python


This is a Motorcycle Service Booking System implemented using Python and SQLAlchemy ORM. The system allows users to manage various aspects of motorcycle services such as customer management, service bookings, payments, logistics, and inventory management.

Features
- Customer Management: Add and manage customer information.
- Service Management: Add and manage available services.
- Booking Management: Create, update, and track service bookings for customers.
- Order Management: Track orders for service-related inventory.
- Inventory Management: Manage service parts and track inventory status.
- Payment Management: Record and manage payments for services.
- Logistics: Manage pickup and drop-off logistics related to bookings.


Technologies Used
- Python 3.x: Programming language.
- SQLAlchemy: ORM (Object Relational Mapping) for database interaction.
- SQLite: Database backend (easily changeable to other SQL-based databases).
- Datetime: For date and time management.
- Database Models
- The system contains several interrelated models:

- Customer: Stores customer information like name, address, phone, and motorcycle details.
- Booking: Represents a service booking made by a customer, linking to service, mechanic, and customer.
- Service: Stores available services with cost and description.
- Mechanic: Stores information about the mechanics who perform the services.
- Order: Tracks service-related orders from inventory.
- Inventory: Manages the availability and details of parts and items used for services.
- Payment: Records payment details related to bookings.
- Logistics: Tracks pickup and drop-off logistics related to service bookings.
