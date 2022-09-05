from service.envvar import ensure_envvar_DB_xx_defined
#
from flask import Flask, jsonify
#
from service.db.mysql import dbsession
from service.db.model_class import Tel4vnCourse


ensure_envvar_DB_xx_defined()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # return GET_mock_tel4vn_course()
    return GET_tel4vn_course()


#region /tel4vn_course
def GET_tel4vn_course():
    r_all = dbsession.query(Tel4vnCourse).all()
    return jsonify(r_all)

@app.route('/tel4vn_course', methods=['GET'])
def tel4vn_course():
    return GET_tel4vn_course()


#region mock
@app.route('/mock/tel4vn_course', methods=['GET'])
def mock_tel4vn_course():
    return GET_mock_tel4vn_course()

mock_course_l = [
    {'name': 'Docker Container',  'fee': '2,500,000₫', 'desc': 'Khóa học trang bị nền tảng kiến thức về container và triển khai ứng dụng theo kiến trúc microservice', },
    {'name': 'Python for DevOps', 'fee': '5,500,000₫', 'desc': 'Tổng quan: Python hiện đang là 1 trong những ngôn ngữ lập trình phổ biến nhất cho người mới bắt đầu với CNTT nhờ…', },
]

def GET_mock_tel4vn_course():
    return jsonify(mock_course_l)
#endregion mock

#endregion /tel4vn_course


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
