from sqlalchemy import Column, Text, Integer

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from dataclasses import dataclass

@dataclass  # fix error > not JSON serializable ref. https://stackoverflow.com/a/57732785/248616
class Tel4vnCourse(Base):
    __tablename__ = 'tel4vn_courses'

    # nedd  :int added or jsonify() returns null ref. https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json#comment103005318_57732785
    id      :int = Column(Integer, primary_key=True, autoincrement=True)

    # nedd  :str added or jsonify() returns null ref. https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json#comment103005318_57732785
    name    :str = Column(Text)
    fee     :str = Column(Text)
    desc    :str = Column(Text)
