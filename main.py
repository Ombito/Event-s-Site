from sqlalchemy import create_engine, Table, Integer, String, Column, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, backref

Base = declarative_base()

user_event = Table(
    'user_event',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('event_id', ForeignKey('events.id'), primary_key=True),
    extend_existing=True
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    events = relationship("Event", secondary=user_event, back_populates='users')
    reviews = relationship("Review", backref=backref('user'))

    def __repr__(self):
        return f"User {self.name}, id: {self.id}"

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    users = relationship("User", secondary=user_event, back_populates='events')
    reviews = relationship("Review", backref=backref('event'))

    def __repr__(self):
        return f"Event: {self.name}, Location: {self.location}"

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    user_id = Column(Integer(), ForeignKey("users.id"))
    event_id = Column(Integer(), ForeignKey("events.id"))

    def __repr__(self):
        return f"Review: Score {self.score}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///my_database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    userA = User(name='Alvin')
    userB = User(name='Becky')

    
