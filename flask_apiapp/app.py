from flask import Flask, jsonify


mock_course_l = [
    {'name': 'Docker Container',  'fee': '2,500,000₫', 'desc': 'Khóa học trang bị nền tảng kiến thức về container và triển khai ứng dụng theo kiến trúc microservice', },
    {'name': 'Python for DevOps', 'fee': '5,500,000₫', 'desc': 'Tổng quan: Python hiện đang là 1 trong những ngôn ngữ lập trình phổ biến nhất cho người mới bắt đầu với CNTT nhờ…', },
]

app = Flask(__name__)

@app.route('/tel4vn_course', methods=['GET'])
def tel4vn_course():
    return jsonify(mock_course_l)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
