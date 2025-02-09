with selection as (
select 
	t.id_can,
    t.id_art,
    t.id_alb,
    t.artist,
    t.genero,
    t.album,
    t.title,
    t.secs,
    t.kbs,
    t.released,
    min(date(sc.fechahora)) as min_fecha,
    max(date(sc.fechahora)) as max_fecha,
    count(sc.uts) as reps
from 
	scrobbling sc
	left join total t
    on t.id_can = sc.id_can
-- where date(sc.fechahora) >= '2023-10-28'
-- and date(sc.fechahora) <= '2024-10-27'
group by t.id_can,
    t.id_art,
    t.id_alb,
    t.artist,
    t.album,
    t.title
    ),
ranked as (
select
	id_can,
    id_art,
    id_alb,
    artist,
    genero,
    album,
    title,
    min_fecha,
    max_fecha,
    reps,
    secs,
    kbs,
    released,
    row_number() over(partition by id_art order by reps desc,min_fecha desc, max_fecha) as rank_pos
from selection
),
cumulative_data AS (
    select 
    
	id_can,
    id_art,
    id_alb,
    artist,
    album,
    title,
    min_fecha,
    max_fecha,
    reps,
    secs,
    kbs,
    genero,
    released,
    rank_pos,
    SUM(kbs) OVER(ORDER BY reps desc,min_fecha desc, max_fecha ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) / 1024 AS cumulative_megas,
    SUM(secs) OVER (ORDER BY reps desc, min_fecha desc, max_fecha ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) / 60 AS cumulative_mins ,
    row_number() over() as cumulative_ranked_pos
    from ranked
    where rank_pos = 1 
    order by reps desc)
-- select * from ranked;
SELECT
	*
FROM
	cumulative_data
WHERE 
	cumulative_megas <= 800
ORDER BY
	cumulative_ranked_pos desc
;
select artist, title, year(fechahora), count(uts)
from scrobbling
where id_can = 3328
group by year(fechahora)
;