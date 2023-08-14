
-- create items table
CREATE TABLE items(
	item_id serial primary key,
	title varchar (50) not null,
	price integer not null
);

-- task 1
insert into items
	(item_id, title, price)
values
	(1, 'Small Desk', 100),
	(2, 'Large desk', 300),
	(3, 'Fan', 80);

-- create customers table
create table customers(
	customer_id serial primary key,
	first_name varchar (50) not null,
	last_name varchar (100) not null
);

-- task 2
insert into customers
	(customer_id, first_name, last_name)
values
	(1, 'Greg', 'Jones'),
	(2, 'Sandra', 'Jones'),
	(3, 'Scott', 'Scott'),
	(4, 'Trevor', 'Green'),
	(5, 'Melanie', 'Johnson');


-- task 3.1
select * from items;

-- task 3.2
select * from items where price > 80;

-- task 3.3
select * from items where price <= 300;

-- task 3.4 (empty outcome)
select * from customers where last_name = 'Smith';

-- task 3.5
select * from customers where last_name = 'Jones';

-- task 3.6
select * from customers where first_name != 'Scott';
