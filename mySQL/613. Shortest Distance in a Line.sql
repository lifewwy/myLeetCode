

-- Table point holds the x coordinate of some points on x-axis in a plane, which are all integers.
-- Write a query to find the shortest distance between two points in these points.
-- | x   |
-- |-----|
-- | -1  |
-- | 0   |
-- | 2   |
-- The shortest distance is '1' obviously, which is from point '-1' to '0'. So the output is as below:
-- | shortest|
-- |---------|
-- | 1       |
-- Note: Every point is unique, which means there is no duplicates in table point.
-- Follow-up: What if all these points have an id and are arranged from the left most to the right most of x axis?



-- 选择数据库
use WWY1;

DROP TABLE IF EXISTS point;

-- 数据库中创建数据表 table1 ：
CREATE TABLE IF NOT EXISTS `point`(
   `x_id` INT UNSIGNED AUTO_INCREMENT,
   `x` INT NOT NULL,
   PRIMARY KEY ( `x_id` )
);


-- 插入数据
INSERT INTO point (x) VALUES (-1);
INSERT INTO point (x) VALUES (0);
INSERT INTO point (x) VALUES (2);

SELECT * FROM WWY1.point;


-- MySQL的连接查询: JION
-- SELECT
--     p1.x, p2.x, ABS(p1.x - p2.x) AS distance
-- FROM
--     point p1
--         JOIN
--     point p2 ON p1.x != p2.x
-- ;

-- MySQL的连接查询: JION
SELECT
    MIN(ABS(p1.x - p2.x)) AS shortest
FROM
    point p1  -- point is the table name 
        JOIN
    point p2 ON p1.x != p2.x
;

-- 查询数据的 SELECT语句 并不改变原表  
SELECT * FROM WWY1.point;




































