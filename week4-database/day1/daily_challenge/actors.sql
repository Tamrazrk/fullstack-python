-- count actors
select count(*) from actors;

-- try to add actor with some blank fields
insert into actors (first_name, last_name, age, number_oscars)
values ('Tamar', '', '05/05/2008', 6);

-- in my understanding, 'first_name' and 'last_name' can be left blank,
-- as an empty string is still a valid string. 'age' can not be blank,
-- because it will not be valid date string, so it will raise an error.
