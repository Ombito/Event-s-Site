from faker import Faker
from main import Base, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


fake = Faker()
engine = create_engine('sqlite:///my_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session= Session()

print("seeding user data")

users = [ 
    User(
        name=fake.name
    )
    for i in range (10)]

session.bulk_save_objects(users)
session.commit()