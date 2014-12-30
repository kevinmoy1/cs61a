-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

select "States adjacent to California:";
select * from adjacencies where s1='CA';
-- Finds lengths of possible paths between two states
create table distances as
  with
    distance(start, end, hops) as (
    select a.s1, a.s2, 1 from adjacencies as a union
    select a.start, b.s2, a.hops+1 from distance as a, adjacencies as b where a.end=b.s1 and a.hops+1<=15
    )
  select * from distance;

select "Lengths of paths between CA and WI:";
select * from distances where start = "CA" and end = "WI" order by hops;

select "States 3 hops from CA:";
select end from distances where hops=3 and start="CA";
select "Long alphabetical paths:";
with
  paths(s, n, last) as (
    select state, 1, state from states union
    select a.s||", "||b.s2, a.n+1, b.s2 from paths as a, adjacencies as b where b.s1=a.last and a.last<b.s2
  )
select s from paths where n > 6 order by -n;