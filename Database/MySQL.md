<!-- TOC -->

- [基础命令 base](#base)
- [流程 Process](#process)
- [注释 Comments](#comments)
- [数据库结构 database struct](#database-struct)
  - [库相关 database](#database)
    - [创建数据库 create database](#create-database)
    - [修改数据库 update database](#update-database)
    - [删除数据库 drop database](#drop-database)
  - [表相关 table struct](#table-struct)
    - [新建表 create table](#create-table)
    - [修改表 update table](#update-table)
    - [删除表 drop table](#drop-table)
- [记录 record](#record)
  - [新增 insert](#insert)
  - [删除 delete](#delete)
  - [修改 update record](#update-record)
  - [查询 query](#query)
    - [基础 query base](#query-base)
      - [distinct 唯一](#distinct)
    - [top 前几行](#top)
    - [offset 移位](#offset)
    - [排序](#)
      - [order by](#order-by)
- [函数 func](#func)
  - [Drop](#drop)
  - [where](#where)
- [fatal](#fatal)
- [参考 reference](#reference)

<!-- /TOC -->

# 基础命令 base
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

# 流程 Process
| 工序           | 语句                                                                 |
| -------------- | -------------------------------------------------------------------- |
| 创建新数据库   | `create database database_name`                                      |
| **使用数据库** | `use table_name`                                                     |
| 创建新表       | `create table table_name ()`                                         |
| **插入记录**   | `INSERT INTO table_name VALUES ();`                                  |
| **查询记录**   | `SELECT distinct column_name from table_name;`                       |
| 修改记录       | `ALTER TABLE table_name MODIFY COLUMN column_name datatype`          |
| 删除记录       | `DELETE FROM table_name WHERE some_column=some_value;`               |
| 修改表         | `UPDATE table_name SET column1=value1 WHERE some_column=some_value;` |
| 删除表         | `DROP TABLE table_name`                                              |

# 注释 Comments
```SQL
# abc
SELECT * -- abc
from table_name;
/*abc*/
```

# 数据库结构 database struct
## 库相关 database
### 创建数据库 create database
```sql
CREATE DATABASE dbname;
```
### 修改数据库 update database
MySQL不提供

### 删除数据库 drop database
```sql
DROP DATABASE database_name
```
## 表相关 table struct
### 新建表 create table
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
### 修改表 update table
- 添加列
```sql
ALTER TABLE table_name
ADD column_name datatype
```
- SQL Server / MS Access：
```sql
ALTER TABLE table_name
ALTER COLUMN column_name datatype
```
- My SQL / Oracle：
```slq
ALTER TABLE table_name
MODIFY COLUMN column_name datatype
```
- 清空表记录
```sql
TRUNCATE TABLE table_name
```
### 删除表 drop table
```sql
DROP TABLE table_name
```
# 记录 record
## 新增 insert
- 第一种形式无需指定要插入数据的列名，只需提供被插入的值即可：
  ```sql
  INSERT INTO table_name
  VALUES (value1,value2,value3,...);
  ```
- 第二种形式需要指定列名及被插入的值：
  ```sql
  INSERT INTO table_name (column1,column2,column3,...)
  VALUES (value1,value2,value3,...);
  ```
## 删除 delete
```sql
DELETE FROM table_name
WHERE some_column=some_value;
```
## 修改 update record
```sql
UPDATE table_name
SET column1=value1,column2=value2,...
WHERE some_column=some_value;
```
## 查询 query
### 基础 query base
#### distinct 唯一
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
### offset 移位
```SQL
SELECT column_name
from table_name
limit 5 offset 5;
```
> 从第5行开始取5行数据，第一个检索行是第0行

### 排序
#### order by
取一个或多个列的名字，据此对输出进行排序，默认字母顺序。
order by子句必须位于最后一条子句
```SQL
SELECT column_name
from table_name
order by column_name;
```
# 函数 func
## Drop
DROP 用于删除[索引](#)、[表](#drop-table)和[数据库](#drop-database)
## where

| 运算符  | 描述                                                   |
| ------- | ------------------------------------------------------ |
| =       | 等于                                                   |
| <>      | 不等于。注释：在 SQL 的一些版本中，该操作符可被写成 != |
| >       | 大于                                                   |
| <       | 小于                                                   |
| >=      | 大于等于                                               |
| <=      | 小于等于                                               |
| BETWEEN | 在某个范围内                                           |
| LIKE    | 搜索某种模式                                           |
| IN      | 指定针对某个列的多个可能值                             |
# fatal
- SQL 对大小写不敏感
  - `set names utf8;` 命令用于设置使用的字符集。
# 参考 reference
[SQL 教程 | 菜鸟教程](http://www.runoob.com/sql/sql-tutorial.html)