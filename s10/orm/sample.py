from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('postgresq1:///:memory:', echo=True)    # psycopg2
engine = create_engine('sqlite:///mydb.sqlite', echo=True)
Base = declarative_base()

# CREATE TABLE employee (id INTEGER PRIMARY KEY,
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
    #
    # def __repr__(self):
    #     return "{i}) {fn} {ln} : {a}".format(
    #         i=self.id, fn=self.firstname, ln=self.lastname, a=self.age)

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)

    def __init__(self, fn, ln, a):
        self.firstname = fn
        self.lastname = ln
        self.age = a

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

res = session.query(Employee).filter_by(firstname='John2').all()
print(res)
print ('end')

# s1 = Employee("John", "Smith", 21)
# s2 = Employee("John2", "Smith2", 22)
# s3 = Employee("John3", "Smith3", 24)
# # print (s1)
# session.add(s1)
# session.add(s2)
# session.add(s3)
# #
# session.commit()

