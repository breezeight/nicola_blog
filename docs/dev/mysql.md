---
layout: post
title: "MySql"
date: 2014-03-16 19:59:15 +0100
comments: true
categories:
---
# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Refernce

* [Mysql 5.0 manual](http://dev.mysql.com/doc/refman/5.1/en/user-account-management.html)

# Install

## Ubuntu

sudo apt-get install mysql-server

## OSX

* `brew install mysql`
* `brew info mysql`
* To connect: `mysql -uroot`

# MISC

mysql is the command line client utility provide with the default installation.

Change the root password: `mysql mysqladmin -u root password 'new-password'`

To connect to a database: `mysql -h host -u user -p`

To show databases: `show databases;`

To show tables: `SHOW TABLES;`

To select a database for use: `USE dbname;`

To show the schema of table:

~~~
mysql> use depot_development;
mysql> show tables;
mysql> desc table_name;
~~~


drop db: `DROP DATABASE <db_name>;`

# Create a database with permission

To create a database as root and add user eventum:

~~~
    create database eventum
    # Permission only to localhost or:  grant all privileges on eventum.* to eventum identified by 'password!'         # ...all host
    grant all privileges on eventum.* to eventum@localhost identified by 'password!'      
    flush privileges
~~~

To dump/restore a database:

~~~
    mysqldump --add-drop-table --add-drop-database --opt -u root -p DigitalSignageServer_development >cip.sql
    mysql -u root -p DigitalSignageServer_development -e 'source cip.sql'
~~~

To grant permission on a db to a user (and create the user):

~~~
    use mysql
    grant CREATE, DROP on LoyaltyProgram_production.* to LoyaltyUser@localhost;
    or
    grant all on LoyaltyProgram_production.* to LoyaltyUser@localhost;
~~~

NB: syntax namedb.* means: all database's table.

To change password (attention there are different password for each host )

~~~
    mysql> use mysql
    mysql> update user set Password=PASSWORD('ciccia') where User="LoyaltyUser";

    mysql> flush privileges;

~~~


# Dump 

You can add drop tables and drop databases command to backup database scripts. Dump Content using mysqldump

Add the -e option for extended insert statements. This will make running the sql dump much faster.

Example: mysqldump -e -u fred -p FredsAddresses > /tmp/addresses.sql

## Restore

~~~
create database  kenwood_club;
grant all privileges on kenwood_club.* to kenwood@localhost identified by 'kenwood';
GRANT SUPER ON *.* TO kenwood@localhost;
flush privileges;

mysql -p -u kenwood  kenwood_club < ../kenwoodclub2013_it.sql
~~~

# Export CSV

MySQL provides an easy mechanism for writing the results of a select statement into a text file on the server. Using extended options of the INTO OUTFILE nomenclature, it is possible to create a comma separated value (CSV) which can be imported into a spreadsheet application such as OpenOffice or Excel or any other applciation which accepts data in CSV format.
    
Given a query such as: `SELECT order_id,product_name,qty FROM orders` 

which returns three columns of data, the results can be placed into the file /tmo/orders.txt using the query:

~~~
    SELECT order_id,product_name,qty
        FROM orders
        INTO OUTFILE '/tmp/orders.txt'
~~~

This will create a tab-separated file, each row on its own line. To alter this behavior, it is possible to add modifiers to the query:

~~~
    SELECT order_id,product_name,qty
        FROM orders
        INTO OUTFILE '/tmp/orders.csv'
            FIELDS TERMINATED BY ','
            ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
~~~


In this example, each field will be enclosed in "double quotes," the fields will be separated by commas, and each row will be output on a new line separated by a newline (\n). Sample output of this command would look like:

~~~
    "1","Tech-Recipes sock puppet","14.95"
    "2","Tech-Recipes chef's hat","18.95"
    ...
~~~

Keep in mind that the output file must not already exist and that the user MySQL is running as has write permissions to the directory MySQL is attempting to write the file to.




Import / Export


