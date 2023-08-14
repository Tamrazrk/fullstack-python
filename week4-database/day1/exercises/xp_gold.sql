-- tast 1
select first_name, last_name, birth_date
from students
order by last_name asc
limit 4;

-- task 2
select first_name, last_name, birth_date
from students
order by birth_date desc
limit 1;

-- task 3
select first_name, last_name, birth_date
from students
offset 2
limit 3;
