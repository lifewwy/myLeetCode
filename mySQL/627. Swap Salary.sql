-- SQL stands for Structured Query Language

-- Given a table salary, such as the one below, that has m=male and f=female values. 
-- Swap all f and m values (i.e., change all f values to m and vice versa) with a 
-- single update query and no intermediate temp table.
-- For example:
-- | id | name | sex | salary |
-- |----|------|-----|--------|
-- | 1  | A    | m   | 2500   |
-- | 2  | B    | f   | 1500   |
-- | 3  | C    | m   | 5500   |
-- | 4  | D    | f   | 500    |
-- 
-- After running your query, the above salary table should have the following rows:
-- | id | name | sex | salary |
-- |----|------|-----|--------|
-- | 1  | A    | f   | 2500   |
-- | 2  | B    | m   | 1500   |
-- | 3  | C    | f   | 5500   |
-- | 4  | D    | m   | 500    |


-- SQL UPDATE 语句
-- UPDATE 语句用于更新表中已存在的记录。
-- 
-- SQL UPDATE 语法

-- UPDATE table_name
-- SET column1=value1,column2=value2,...
-- WHERE some_column=some_value;
-- 
-- 请注意 SQL UPDATE 语句中的 WHERE 子句！
-- WHERE 子句规定哪条记录或者哪些记录需要更新。
-- 如果您省略了 WHERE 子句，所有的记录都将被更新！

-- 选择数据库
use WWY1;

DROP TABLE IF EXISTS salary;

create table if not exists salary(id int, name varchar(100), sex char(1), salary int);
Truncate table salary;
insert into salary (id, name, sex, salary) values ('1', 'A', 'm', '2500');
insert into salary (id, name, sex, salary) values ('2', 'B', 'f', '1500');
insert into salary (id, name, sex, salary) values ('3', 'C', 'm', '5500');
insert into salary (id, name, sex, salary) values ('4', 'D', 'f', '500');

select * from salary;

set sql_safe_updates=off;  
show variables like 'sql_safe%'; 

-- UPDATE salary 
-- SET 
--     sex = CASE sex
--         WHEN 'm' THEN 'f'
--         ELSE 'm'
--     END;

UPDATE salary 
SET 
    sex = IF(sex = 'm', 'f', 'm');
    
-- IF 表达式
-- IF( expr1 , expr2 , expr3 )
-- expr1 的值为 TRUE，则返回值为 expr2 
-- expr1 的值为FALSE，则返回值为 expr3

select * from salary;






























