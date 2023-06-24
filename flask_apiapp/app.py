from service.envvar import ensure_envvar_DB_xx_defined
#
from flask import Flask, jsonify
#
import pymysql; pymysql.install_as_MySQLdb()  # fix err > ModuleNotFoundError: No module named 'MySQLdb'  ref. https://stackoverflow.com/a/71730129/248616
#
from service.db.mysql import dbsession
from service.db.model_class import Tel4vnCourse


ensure_envvar_DB_xx_defined()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({})


#region /tel4vncourse
def GET_tel4vncourse():
    r_all = dbsession.query(Tel4vnCourse).all()
    return jsonify(r_all)

@app.route('/tel4vncourse', methods=['GET'])
def tel4vncourse():
    return GET_tel4vncourse()


#region mock
@app.route('/mock/tel4vncourse', methods=['GET'])
def mock_tel4vncourse():
    return GET_mock_tel4vncourse()

mock_course_l = [
    {'name': 'Docker Container',  'fee': '2,500,000₫', 'desc': 'Khóa học trang bị nền tảng kiến thức về container và triển khai ứng dụng theo kiến trúc microservice', },
    {'name': 'Python for DevOps', 'fee': '5,500,000₫', 'desc': 'Tổng quan: Python hiện đang là 1 trong những ngôn ngữ lập trình phổ biến nhất cho người mới bắt đầu với CNTT nhờ…', },
]

def GET_mock_tel4vncourse():
    return jsonify(mock_course_l)
#endregion mock

#endregion /tel4vncourse


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
