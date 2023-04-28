DROP TABLE if exists BinhLuan;

CREATE TABLE tel4vn_courses (
    `id` int AUTO_INCREMENT,

    name   text,
    fee    text,
    `desc` text,

    PRIMARY KEY(id)
);

INSERT INTO tel4vn_courses (`name`, `fee`, `desc`)
                    VALUES ('Docker Container',  '2,500,000₫', 'Khóa học trang bị nền tảng kiến thức về container và triển khai ứng dụng theo kiến trúc microservice'),
                           ('Python for DevOps', '5,500,000₫', 'Tổng quan: Python hiện đang là 1 trong những ngôn ngữ lập trình phổ biến nhất cho người mới bắt đầu với CNTT nhờ…')
;
