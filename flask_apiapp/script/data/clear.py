from service.envvar import ensure_envvar_DB_xx_defined
#
from service.db.model_class import Base, Tel4vnCourse
from service.db.mysql import scoped_engine, dbsession


ensure_envvar_DB_xx_defined()

# create table if not exist
Base.metadata.create_all(scoped_engine)  # ref. https://stackoverflow.com/a/70402756/248616


dbsession.query(Tel4vnCourse).delete()
dbsession.commit()


print(f'''
cleared all row
re-query {len( dbsession.query(Tel4vnCourse).all() )}
'''.rstrip())
