select alb.id_alb, a.artist, alb.album, sc.album_mbid
from albums alb join  artistas a on alb.id_art = a.id_art
join temas t on t.id_alb = alb.id_alb
join scrobbling sc on sc.id_can = t.id_can
where alb.album is not null
and a.artist <> 'Varios Artistas'
-- and sc.album_mbid <> ''
group by artist, id_alb
;

-- id_alb	country	year	genre	style	id	resource_url
drop table gen_alb;

create table gen_alb (id_ga int primary key auto_increment,
					id_alb int UNIQUE,
                    country varchar(100),
                    year_date year,
                    genre varchar(255),
                    style varchar(255),
                    id int,
                    resource_url text,
                    lindex int,
                    FOREIGN KEY (id_alb) REFERENCES albums(id_alb)
                    );


select * from gen_alb;
describe gen_alb;

select * from albums where id_alb not in (select id_alb from gen_alb);

select id_alb, count(id_alb) as cu, year_date, genre, style, id, resource_url
from gen_alb group by id_alb having cu > 1;
select * from gen_alb where id_alb = 1;
-- truncate gen_alb;

SELECT * FROM gen_alb
WHERE id_alb in (SELECT id_alb FROM gen_alb GROUP BY id_alb HAVING count(id_alb) > 1)
ORDER BY id_alb;

