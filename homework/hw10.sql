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
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------
create table sizedDogs as
  select name, size from dogs, sizes where height > min and height <= max;

with ancestors(ancestor, descendant) as (
    select parent, child from parents union
    select ancestor, child from ancestors, parents where parent = descendant
) select * from ancestors; 
-- The names of all "toy" and "mini" dogs
select name from sizedDogs where size == 'toy' or size == 'mini';
-- Expected output:
--   abraham
--   eisenhower
--   fillmore
--   grover
--   herbert

-- All dogs with parents ordered by decreasing height of their parent
select child from dogs, parents  where parent = name order by height desc;
  
-- Expected output:
--   herbert
--   fillmore
--   abraham
--   delano
--   grover
--   barack
--   clinton

-- Sentences about siblings that are the same size
with bros(first, second) as (
  select a.child, b.child from parents as a, parents as b where a.parent=b.parent and a.child!=b.child and a.child < b.child
)
select (s.first || " and " || s.second || " are " || a.size || " siblings") from bros as s, sizedDogs as a, sizedDogs as b 
  where s.first=a.name and s.second=b.name and a.size=b.size;
-- Expected output:
--   barack and clinton are standard siblings
--   abraham and grover are toy siblings
with
  h(names, totala, totalb, last, count) as
  (select name, height, 1, name, 1 from dogs union
      select a.names || ", " || b.name, a.totala+b.height, a.totalb+1, b.name, count+1 from h as a, dogs as b, dogs as c  where a.last=c.name and c.height < b.height )
select names, totala from h where totala>=170 and count = 4  order by totala;
-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
-- Expected output:
--   abraham, delano, clinton, barack|171
--   grover, delano, clinton, barack|173
--   herbert, delano, clinton, barack|176
--   fillmore, delano, clinton, barack|177
--   eisenhower, delano, clinton, barack|180

-- All non-parent relations ordered by height difference


