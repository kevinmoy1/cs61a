-- CS 61A Fall 2014
-- Name: Arani Bhattacharyay
-- Login: cs61a-aoy

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore"        union
  select "delano"           , "jackson";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31           union
  select "jackson"        , "long"       , 43;

-- All triples of dogs with the same fur that have increasing heights

select "=== Question 1 ===";
select first.name, second.name, third.name from dogs as first, dogs as second, dogs as third where first.fur = second.fur and first.fur = second.fur and second.fur = third.fur and 
  first.name != second.name and first.name != third.name and second.name != third.name and first.height < second.height and second.height < third.height;

-- Expected output:
--   abraham|delano|clinton
--   abraham|jackson|clinton
--   abraham|jackson|delano
--   grover|eisenhower|barack
--   jackson|delano|clinton

-- The sum of the heights of at least 3 dogs with the same fur, ordered by sum

select "=== Question 2 ===";
with
  h(furs, totala, count, last) as
  (select name, height, 1, name from dogs union
      select b.fur, a.totala+b.height, count+1, b.name from h as a, dogs as b, dogs as c  where a.last=c.name and b.name < c.name and b.fur = c.fur )
select furs, totala from h where count >= 3  order by totala;
-- Expected output:
--   long|115
--   short|115
--   long|116
--   long|119
--   long|136
--   long|162

-- The terms of g(n) where g(n) = g(n-1) + 2*g(n-2) + 3*g(n-3) and g(n) = n if n <= 3

select "=== Question 3 ===";
with
  setter(third, second, first, current, count) as (
    select 3,2,1,10,4 union
    select current, third, second, current+ 2*third + 3*second, count+1 from setter where count <= 20)
select first from setter union select second from setter union select third from setter;

-- Expected output:
--   1
--   2
--   3
--   10
--   22
--   51
--   125
--   293
--   696
--   1657
--   ...
--   9426875

