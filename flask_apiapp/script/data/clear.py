from service.db.model_class import Base, Tel4vnCourse
from service.db.mysql import scoped_engine, dbsession


# create table if not exist
Base.metadata.create_all(scoped_engine)  # ref. https://stackoverflow.com/a/70402756/248616


dbsession.query(Tel4vnCourse).delete()
dbsession.commit()


print(f'''
cleared all row
re-query {len( dbsession.query(Tel4vnCourse).all() )}
'''.rstrip())
