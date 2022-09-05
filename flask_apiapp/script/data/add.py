from service.envvar import ensure_envvar_DB_xx_defined
#
from service.db.model_class import Base, Tel4vnCourse
from service.db.mysql import scoped_engine, dbsession


ensure_envvar_DB_xx_defined()

# create table if not exist
Base.metadata.create_all(scoped_engine)  # ref. https://stackoverflow.com/a/70402756/248616

l = [
    {'name': 'Docker Container',  'fee': '2,500,000₫', 'desc': 'Khóa học trang bị nền tảng kiến thức về container và triển khai ứng dụng theo kiến trúc microservice', },
    {'name': 'Python for DevOps', 'fee': '5,500,000₫', 'desc': 'Tổng quan: Python hiện đang là 1 trong những ngôn ngữ lập trình phổ biến nhất cho người mới bắt đầu với CNTT nhờ…', },
]

for i,m in enumerate(l):  # m aka model_obj_dict, i aka index
    d = {
        **m,

        # add suffix clone#i from i=1,2,...
        'name': m['name']+f' clone#{i}' if i>0 else \
                m['name'],
    }
    r = Tel4vnCourse(**d)
    dbsession.add(r) ; dbsession.commit()

print(f'''
added row {len(l)}
total row {len(dbsession.query(Tel4vnCourse).all())}
'''.rstrip())