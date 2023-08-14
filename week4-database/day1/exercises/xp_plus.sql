-- task 1.1. create students table
create table students(
	id serial primary key,
	last_name varchar (100) not null,
	first_name varchar (50) not null,
	birth_date date not null
);

-- set date style to be able to insert date in format dd/mm/yyyy
SET DateStyle = 'European';

-- task 2.1. fill students table
insert into students
	(id, first_name, last_name, birth_date)
values
    (1, 'Marc', 'Benichou', '02/11/1998'),
    (2, 'Yoan', 'Cohen', '03/12/2010'),
    (3, 'Lea', 'Benichou', '27/07/1987'),
    (4, 'Amelia', 'Dux', '07/04/1996'),
    (5, 'David', 'Grez', '14/06/2003'),
    (6, 'Omer', 'Simpson', '03/10/1980');

-- task 2.2
insert into students
	(id, first_name, last_name, birth_date)
values
	(7, 'Tamar', 'Zarkhozashvili ', '20/07/1993');

-- task 3.1
select * from students;

-- task 3.2
select first_name, last_name
from students;

-- task 3.3.1
select first_name, last_name
from students
where id=2

-- task 3.3.2
select first_name, last_name
from students
where last_name='Benichou' and first_name='Marc'

-- task 3.3.3
select first_name, last_name
from students
where last_name='Benichou' or first_name='Marc'

-- task 3.3.4
select first_name, last_name
from students
where first_name like '%a%'

-- task 3.3.5
select first_name, last_name
from students
where first_name like 'a%'

-- task 3.3.6
select first_name, last_name
from students
where first_name like '%a'

-- task 3.3.7
select first_name, last_name
from students
where substring(first_name, length(first_name)-1, 1) = 'a'

-- task 3.3.8
select first_name, last_name
from students
where id in (1, 3)
