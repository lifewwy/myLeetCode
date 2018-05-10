-- There is a table World
-- 
-- +-----------------+------------+------------+--------------+---------------+
-- | name            | continent  | area       | population   | gdp           |
-- +-----------------+------------+------------+--------------+---------------+
-- | Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
-- | Albania         | Europe     | 28748      | 2831741      | 12960000      |
-- | Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
-- | Andorra         | Europe     | 468        | 78115        | 3712000       |
-- | Angola          | Africa     | 1246700    | 20609294     | 100990000     |
-- +-----------------+------------+------------+--------------+---------------+
-- A country is big if it has an area of bigger than 3 million square km or a population of more than 25 million.
-- 
-- Write a SQL solution to output big countries' name, population and area.
-- 
-- For example, according to the above table, we should output:
-- 
-- +--------------+-------------+--------------+
-- | name         | population  | area         |
-- +--------------+-------------+--------------+
-- | Afghanistan  | 25500100    | 652230       |
-- | Algeria      | 37100000    | 2381741      |
-- +--------------+-------------+--------------+

-- 请记住...
-- SQL 对大小写不敏感：SELECT 与 select 是相同的

-- 选择数据库
use WWY1;

DROP TABLE IF EXISTS World;

-- 数据库中创建数据表 table1 ：
CREATE TABLE IF NOT EXISTS `World`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `name` VARCHAR(100) NOT NULL,
   `continent` VARCHAR(100) NOT NULL,
   `area` INT UNSIGNED ,
   `population` INT UNSIGNED,
   `gdp` INT UNSIGNED,
   PRIMARY KEY ( `id` )
);

INSERT INTO World 
    (name, continent, area, population, gdp)
     VALUES
     ("Afghanistan", "Asia", 652230, 25500100, 20343000);

-- mysql中一条insert语句批量插入多条记录
INSERT INTO World 
    (name, continent, area, population, gdp)
     VALUES
     ("Albania", "Europe", 28748, 2831741, 12960000),
     ("Algeria", "Africa", 2381741, 37100000,188681000),
	 ("Andorra", "Europe", 468, 78115, 3712000),
	 ("Angola", "Africa", 1246700, 20609294, 100990000);

SELECT * from World;
     
-- MySQL 数据库使用SQL SELECT 语句来查询数据。
SELECT 
    name, population, area
FROM
    World
WHERE
    area > 3000000 OR population > 25000000
    
    
    
    
    
    
    