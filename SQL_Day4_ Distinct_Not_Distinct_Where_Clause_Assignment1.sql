Enter password: ********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 9.1.0 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> -- Create a database named BankAccount
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE DATABASE BankAccount;
Query OK, 1 row affected (0.01 sec)

mysql>
mysql> -- Use the created database
Query OK, 0 rows affected (0.00 sec)

mysql> USE BankAccount;
Database changed
mysql>
mysql> -- Create the BankAccount table with the specified columns
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE BankAccount (
    ->     account_id INT PRIMARY KEY,
    ->     account_holder_name VARCHAR(100) NOT NULL,
    ->     account_balance DECIMAL(10, 2) NOT NULL
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql>
mysql> -- Task 1: Insert 5 records into the BankAccount table
Query OK, 0 rows affected (0.00 sec)

mysql> INSERT INTO BankAccount (account_id, account_holder_name, account_balance) VALUES
    -> (101, 'John Doe', 25000.00),
    -> (102, 'Jane Smith', 50000.00),
    -> (103, 'Alice Johnson', 75000.00),
    -> (104, 'Bob Brown', 100000.00),
    -> (105, 'Charlie Davis', 125000.00);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql>
mysql> -- Task 2: Retrieve the account_holder_name and account_balance of all account holders
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT account_holder_name, account_balance
    -> FROM BankAccount;
+---------------------+-----------------+
| account_holder_name | account_balance |
+---------------------+-----------------+
| John Doe            |        25000.00 |
| Jane Smith          |        50000.00 |
| Alice Johnson       |        75000.00 |
| Bob Brown           |       100000.00 |
| Charlie Davis       |       125000.00 |
+---------------------+-----------------+
5 rows in set (0.00 sec)

mysql>
mysql> -- Task 3: Retrieve the account_holder_name and account_balance where the account_balance is more than 30,000
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT account_holder_name, account_balance
    -> FROM BankAccount
    -> WHERE account_balance > 30000;
+---------------------+-----------------+
| account_holder_name | account_balance |
+---------------------+-----------------+
| Jane Smith          |        50000.00 |
| Alice Johnson       |        75000.00 |
| Bob Brown           |       100000.00 |
| Charlie Davis       |       125000.00 |
+---------------------+-----------------+
4 rows in set (0.00 sec)

mysql>
mysql> -- Task 4: Update the account_balance of the account holder whose ID is 101
Query OK, 0 rows affected (0.00 sec)

mysql> UPDATE BankAccount
    -> SET account_balance = 60000.00
    -> WHERE account_id = 101;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
