-- select* from planes;
-- select* from airports;
-- select* from airlines;
-- select* from flights;
-- select* from weather;

select count(*) from planes where speed is not NULL;
-- There are 23 planes with speeds listed

select min(speed) from planes where speed is not NULL;
-- Minimum speed is 90

select max(speed) from planes where speed is not NULL;
-- Max speed is 432

select sum(distance) from flights where year = 2013;
-- Total distance flown in 2013 is 350,217,607 miles

select sum(distance) from flights where year = 2013 and tailnum = '';
-- Total distance flown in 2013 by flights without tailnum is 1,784,167 miles

select manufacturer, sum(distance) from planes p
inner join flights f on f.tailnum = p.tailnum
where f.month = 7 and f.day = 5 and f.year = 2013
group by manufacturer;

select manufacturer, sum(distance) from planes p
left join flights f on f.tailnum = p.tailnum
where f.month = 7 and f.day = 5 and f.year = 2013
group by manufacturer;
-- Inner and left joins are the same results for this data