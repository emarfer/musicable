select id_can, artist, album, title, count(uts) as total, min(fechahora) as minfechahora, max(fechahora) as maxfechahora
from scrobbling
where date(fechahora) >= '2024-01-01'
group by id_can, artist, album, title
having total >= 8
order by total asc
;

Select 
	id_can, artist, album, title, count(uts) as reps, min(fechahora) as minfechahora, max(fechahora) as maxfechahora
from 
	scrobbling
where
	date(fechahora) > '2023-12-31'
    and id_can not in (select distinct id_Can from repeticiones_lista_datos)
    and artist like '%porreta%'
group by
	id_can, artist, album, title
-- having reps in(18,19,20)
;

Select 
	id_can, artist, album, title, count(uts) as reps, year(fechahora)
from 
	scrobbling
where
	month(fechahora)= 1 and day(fechahora) = 18
group by id_can, artist, album, title,year(fechahora)
-- having reps > 1
order by year(fechahora), reps desc
;
Select 
	year(fechahora), count(uts) as total, count(distinct id_Can) as temas
from 
	scrobbling
where
	month(fechahora) = 1
    and day(fechahora) = 18
group by year(fechahora)
-- having reps > 1
order by year(fechahora), total desc
;
with sucumple as (
Select 
	id_can, artist, album, title, count(uts) as reps, year(fechahora) as anual, "sucumple" as "cumple"
from 
	scrobbling
where
    month(fechahora)= 1 and day(fechahora) = 18
group by id_can, artist, album, title, anual
-- having reps > 1
order by year(fechahora), reps desc)
, micumple as (
Select 
	id_can, artist, album, title, count(uts) as reps, year(fechahora) as anual, "micumple" as "cumple"
from 
	scrobbling
where
	month(fechahora)= 9 and day(fechahora) = 1
group by id_can, artist, album, title, anual
-- having reps > 1
order by year(fechahora), reps desc
)
select s.id_can, s.artist, s.album, s.title, s.reps as susreps, sum(m.reps) as misreps, (s.reps + m.reps) as repstot, s.anual as suanual, min(m.anual) as mianual-- , s.cumple as sucumple, m.cumple as micumple
from sucumple s
join micumple m
on s.id_can = m.id_can
and s.anual = m.anual
group by s.id_can, s.artist, s.album, s.title, s.anual
;

select * from scrobbling
where date(fechahora) = '2014-01-18'
and id_can in (select id_Can from scrobbling where date(fechahora) = '2014-09-01')
;
with todosmiscumples as (
select
id_can, artist, album, title, year(fechahora) as año
from scrobbling
where day(fechahora) = 1 and month(fechahora) = 9
)
select id_can, artist, album, title, count(distinct año) as cumpleaños, count(id_can) as reps
from todosmiscumples
group by id_can, artist, album, title
having cumpleaños > 1
;


select 
year(fechahora) as año, month(fechahora) as mes, count(uts) as plays
from scrobbling
group by año, mes
order by plays desc
;

With otrocumple as (
select 
year(fechahora) as año, count(uts) as plays
from scrobbling
where day(fechahora) = 18 
and month(fechahora) = 1
group by año
),
micumple as (select 
year(fechahora) as año, count(uts) as plays
from scrobbling
where day(fechahora) = 1 
and month(fechahora) = 9
group by año
)
select oc.año, mc.año, oc.plays, mc.plays
from otrocumple oc
left join micumple mc
on oc.año = mc.año
;