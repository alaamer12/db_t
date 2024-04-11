from sqlalchemy import create_engine, ForeignKey, Column, Integer, String , CHAR, join
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    ssn = Column("ssn", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)

    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first_name, last_name, gender, age):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return "Person({}, {}, {}, {}, {})".format(self.ssn, self.first_name, self.last_name, self.gender, self.age)



class Thing(Base):
    __tablename__ = 'things'

    tid = Column("tid", Integer, primary_key=True)
    name = Column("name", String)
    description = Column("description", String)
    owner = Column("owner", Integer, ForeignKey('people.ssn'))

    def __init__(self, tid, name, description, owner):
        self.tid = tid
        self.name = name
        self.description = description
        self.owner = owner

    def __repr__(self):
        return "Thing({}, {}, {}, {})".format(self.tid, self.owner, self.name, self.description)



engine = create_engine('sqlite:///orm.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# person = Person(ssn=123, first_name="John", last_name="Doe", gender="M", age=30)
# person2 = Person(ssn=456, first_name="Jane", last_name="Doe", gender="F", age=25)
# person3 = Person(ssn=789, first_name="Bob", last_name="Smith", gender="M", age=40)
# session.add(person)
# session.add(person2)
# session.add(person3)
session.commit()


# Querying all of them
# people = session.query(Person).all()
# print(people)

# t1 = Thing(tid=1, name="thing1", description="description1", owner=123)
# t2 = Thing(tid=2, name="thing2", description="description2", owner=456)
# t3 = Thing(tid=3, name="thing3", description="description3", owner=789)
# session.add(t1)
# session.add(t2)
# session.add(t3)
session.commit()

# Get filtered results from Thing and Person
results = session.query(Thing, Person).join(Person, Thing.owner == Person.ssn).all()
print(results)