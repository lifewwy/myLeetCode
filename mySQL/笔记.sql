

-- Order by
-- 按照字段值进行排序，默认升序(asc)。
-- order by 字段 升序|降序（asc|desc）

-- limit
-- 限制获得的记录数量。 
-- limit的语法： 
-- limit offset, row count 
-- offset 偏移量，可以省略，默认从0开始。 
-- row count 总记录数，如果数量大于余下的记录数，则获取剩余的记录数即可。

	

-- 选择数据库
use WWY1;


DROP TABLE IF EXISTS test;

create table IF NOT EXISTS test(
id int primary key not null auto_increment,
name varchar(10),
group_id int 
);

insert into test values(null,'jason',5);
insert into test values(null,'mark',3);
insert into test values(null,'jason',4);
insert into test values(null,'ivy',3);
insert into test values(null,'jason',3);
insert into test values(null,'mark',5);
insert into test values(null,'mark',5);
insert into test values(null,'jason',4);


select * from test ;

-- -------------------------------------------------------------------------- 
SELECT 
    *
FROM
    test
ORDER BY group_id ASC , id DESC
LIMIT 100;

-- -------------------------------------------------------------------------- 
SELECT 
    group_id
FROM
    test
group BY group_id ASC
LIMIT 100;

-- -------------------------------------------------------------------------- 



































