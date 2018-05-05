# 目录
[toc]

# 基础命令
- SELECT - 从数据库中提取数据
- UPDATE - 更新数据库中的数据
- DELETE - 从数据库中删除数据
- INSERT INTO - 向数据库中插入新数据
- CREATE DATABASE - 创建新数据库
- ALTER DATABASE - 修改数据库
- CREATE TABLE - 创建新表
- ALTER TABLE - 变更（改变）数据库表
- DROP TABLE - 删除表
- CREATE INDEX - 创建索引（搜索键）
- DROP INDEX - 删除索引

# 注释
```SQL
# abc
SELECT * -- abc
from table_name;
/*abc*/
```
# 流程
- 创建数据库
- 使用数据库
- 新建表

# 数据库结构
## 库相关
### 创建数据库
```sql
CREATE DATABASE dbname;
```
## 表相关
### 新建表
```sql
CREATE TABLE table_name
(
column_name1 data_type(size),
column_name2 data_type(size),
column_name3 data_type(size),
....
);
```

- NOT NULL - 指示某列不能存储 NULL 值。
- UNIQUE - 保证某列的每行必须有唯一的值。
- PRIMARY KEY - NOT NULL 和 UNIQUE 的结合。
确保某列（或两个列多个列的结合）有唯一标识，有助于更容易更快速地找到表中的一个特定的记录。
  - 初始主键
  ```sql
  PRIMARY KEY (P_Id)
  或 P_Id int NOT NULL PRIMARY KEY,
  ```
  - ADD PRIMARY KEY
  ```sql
  ALTER TABLE Persons
  ADD PRIMARY KEY (P_Id)
  ```
  - DROP PRIMARY KEY
  ```sql
  ALTER TABLE Persons
  DROP PRIMARY KEY
  ```
- FOREIGN KEY - 保证一个表中的数据匹配另一个表中的值的参照完整性。
  - 一个表中的 FOREIGN KEY 指向另一个表中的 PRIMARY KEY
  ```sql
  FOREIGN KEY (P_Id) REFERENCES Persons(P_Id)
  或 P_Id int FOREIGN KEY REFERENCES Persons(P_Id)
  ```
  - ADD FOREIGN KEY
  ```sql
  ALTER TABLE Orders
  ADD FOREIGN KEY (P_Id)
  REFERENCES Persons(P_Id)
  ```
  - DROP FOREIGN KEY
  ```sql
  ALTER TABLE Orders
  DROP FOREIGN KEY fk_PerOrders
  ```
- CHECK - 保证列中的值符合指定的条件。
- DEFAULT - 规定没有给列赋值时的默认值。

# 新增记录
```sql
INSERT ()
into table_name;
```
# 查询
## 基础
### distinct 唯一值
去除重复值，必须放在列名的前面，作用于所有列，不仅仅作用于其后的那一列
```sql
SELECT distinct column_name
from table_name;
```
### top 前几行
```SQL
SELECT top 5 column_name
from table_name;
```
### offset
```SQL
SELECT column_name
from table_name
limit 5 offset 5;
```
从第5行开始取5行数据，第一个检索行是第0行

## 排序
### order by
取一个或多个列的名字，据此对输出进行排序，默认字母顺序。
order by子句必须位于最后一条子句
```SQL
SELECT column_name
from table_name
order by column_name;
```
# 参考
[SQL 教程 | 菜鸟教程](http://www.runoob.com/sql/sql-tutorial.html)

`
