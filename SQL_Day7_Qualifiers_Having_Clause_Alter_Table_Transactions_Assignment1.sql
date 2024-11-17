LAB31:SQL:Day-7(Qualifiers,Having Caluse,Alter Table,Transactions) 


mysql> use anpc8905;
Database changed

/*Task1: Create a table Person with PersonID int, FirstName varchar(255), LastName varchar(255) and age (int). Make PersonID PRIMARY KEY. */

mysql> CREATE TABLE Person (PersonID INT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), age INT);
Query OK, 0 rows affected (0.06 sec)

/* Task 3: Insert data to Person table*/
mysql> INSERT INTO Person (PersonID, FirstName, LastName, age) VALUES (1, 'Swapnali', 'Wagh', 25), (2, 'Sonali', 'Thule', 23), (3, 'Kunal', 'Gupta', 26), (4, 'Janhavi', 'Mane', 24), (5, 'Ismail', 'Khan', 23), (6, 'Sneha', 'Shukla', 21);
Query OK, 6 rows affected (0.01 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> select*from Person;
+----------+-----------+----------+------+
| PersonID | FirstName | LastName | age  |
+----------+-----------+----------+------+
|        1 | Swapnali  | Wagh     |   25 |
|        2 | Sonali    | Thule    |   23 |
|        3 | Kunal     | Gupta    |   26 |
|        4 | Janhavi   | Mane     |   24 |
|        5 | Ismail    | Khan     |   23 |
|        6 | Sneha     | Shukla   |   21 |
+----------+-----------+----------+------+
6 rows in set (0.00 sec)

/*Task2: Create a table Employee with emp_id int, first_name varchar(255), last_name varchar(255) and age (int ) Make emp_id PRIMARY KEY.*/

mysql> CREATE TABLE Employee (emp_id INT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), age INT);
Query OK, 0 rows affected (0.02 sec)

/* Task 4: Insert data to Employee table */

mysql> INSERT INTO Employee (emp_id, first_name, last_name, age) VALUES (101, 'Kunal', 'Dhamal', 28), (102, 'Tanaya', 'Shete', 24), (103, 'Anchal', 'Saini', 23), (104, 'Fairaaz', 'Ahmed', 21), (105, 'Rutuja', 'Vilankar', 25), (106, 'Akansha', 'Kotian', 30);
Query OK, 6 rows affected (0.01 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> select*from Employee;
+--------+------------+-----------+------+
| emp_id | first_name | last_name | age  |
+--------+------------+-----------+------+
|    101 | Kunal      | Dhamal    |   28 |
|    102 | Tanaya     | Shete     |   24 |
|    103 | Anchal     | Saini     |   23 |
|    104 | Fairaaz    | Ahmed     |   21 |
|    105 | Rutuja     | Vilankar  |   25 |
|    106 | Akansha    | Kotian    |   30 |
+--------+------------+-----------+------+
6 rows in set (0.00 sec)

/*Task 5: Create Union of two tables */

mysql> SELECT PersonID AS ID, FirstName AS First_Name, LastName AS Last_Name, Age FROM Person UNION SELECT emp_id AS ID, first_name AS First_Name, last_name AS Last_Name, age FROM Employee;
+-----+------------+-----------+-----+
| ID  | First_Name | Last_Name | Age |
+-----+------------+-----------+-----+
|   1 | Swapnali   | Wagh      |  25 |
|   2 | Sonali     | Thule     |  23 |
|   3 | Kunal      | Gupta     |  26 |
|   4 | Janhavi    | Mane      |  24 |
|   5 | Ismail     | Khan      |  23 |
|   6 | Sneha      | Shukla    |  21 |
| 101 | Kunal      | Dhamal    |  28 |
| 102 | Tanaya     | Shete     |  24 |
| 103 | Anchal     | Saini     |  23 |
| 104 | Fairaaz    | Ahmed     |  21 |
| 105 | Rutuja     | Vilankar  |  25 |
| 106 | Akansha    | Kotian    |  30 |
+-----+------------+-----------+-----+
12 rows in set (0.00 sec)