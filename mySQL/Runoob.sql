
-- MySQL 菜鸟教程

-- MySQL Workbench
-- 注释快捷键 Command + / 

-- 创建数据库
-- CREATE DATABASE WWY1; 

-- 删除数据库
-- drop database WWY1;

-- 选择数据库
use WWY1;

-- 数据库中创建数据表 table1 ：
/*CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;*/

-- MySQL 删除数据表
-- 以下为删除MySQL数据表的通用语法：
-- DROP TABLE table_name ;
-- drop table runoob_tbl

-- 插入数据
/*INSERT INTO runoob_tbl 
    (runoob_title, runoob_author, submission_date)
     VALUES
     ("学习 PHP", "菜鸟教程", NOW());
     
INSERT INTO runoob_tbl
    (runoob_title, runoob_author, submission_date)
    VALUES
    ("学习 MySQL", "菜鸟教程", NOW());

INSERT INTO runoob_tbl
    (runoob_title, runoob_author, submission_date)
    VALUES
    ("JAVA 教程", "RUNOOB.COM", '2016-05-06');*/

/*查询数据
MySQL 数据库使用 SELECT 语句来查询数据。
语法
MySQL数据库中查询数据通用的 SELECT 语法：
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]*/

-- 注释快捷键 Command + / 
-- SELECT 
--     *
-- FROM
--     runoob_tbl;
-- 
-- SELECT 
--     runoob_author
-- FROM
--     runoob_tbl;
 
SELECT 
    runoob_title, submission_date
FROM
    runoob_tbl
WHERE
    runoob_author = '菜鸟教程';
  
  




































