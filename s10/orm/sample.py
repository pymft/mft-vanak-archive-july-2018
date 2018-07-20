from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///mydb.sqlite', echo=True)
Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)

    def __init__(self, fn, ln, a):
        self.firstname = fn
        self.lastname = ln
        self.age = a

    def __repr__(self):
        return "{i}) {fn} {ln} : {a}".format(
            i=self.id, fn=self.firstname, ln=self.lastname, a=self.age)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

s1 = Employee("John", "Smith", 21)
session.add(s1)

session.commit()   

