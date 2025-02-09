with scrobbles as (
select sc.id_can, sc.title, t.id_alb, sc.album, t.num_track, sc.artist, date(sc.fechahora) as fecha
from scrobbling sc
join total t
on t.id_can = sc.id_can
where folder not like '%V.A%'
), agrupado as (
select id_alb, fecha, year(fecha) as año, num_track, artist, album, count(distinct id_can) as canciones, count(*) as reproducciones
from scrobbles
group by fecha, año, id_alb
having canciones >= num_track -1
), ranked as (
select año, fecha, id_alb, artist, album, canciones, reproducciones, num_track,
row_number() over(partition by id_alb order by año) as first_year
from agrupado
)
-- select * from ranked;
-- select * from ranked where num_track != canciones;
select * from ranked where first_year = 1;
select año, count(distinct id_alb) as nuevodisco from ranked where first_year = 1 group by año ;
select * from ranked where first_year = 1 and año = 2016 order by fecha;
select fecha, count(distinct id_alb) as nuevodisco, min(id_alb) from ranked where first_year = 1 group by fecha ;
select * from total where id_alb = 4516;

select * from scrobbling where date(fechahora) = '2016-01-04';


select distinct sc.id_can
from scrobbling sc
join total t
on t.id_can = sc.id_can
where t.num_track >= 3
and sc.album = 'warcry';
select * from total where album = 'Warcry';

select distinct id_alb, album, id_art, artist, released, num_track, folder from total where num_Track <= 4 
and folder not like '%V.A%';

select * from total where num_track = 1;
select * from total where id_alb = 117;
selec