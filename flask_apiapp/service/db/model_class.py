from sqlalchemy import Column, Text, Integer

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Tel4vnCourse(Base):
    __tablename__ = 'tel4vn_courses'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(Text)
    fee  = Column(Text)
    desc = Column(Text)
