select alb.id_alb, a.artist, alb.album, sc.album_mbid
from albums alb join  artistas a on alb.id_art = a.id_art
join temas t on t.id_alb = alb.id_alb
join scrobbling sc on sc.id_can = t.id_can
where alb.album is not null
and a.artist <> 'Varios Artistas'
-- and sc.album_mbid <> ''
group by artist, id_alb
;

drop table gen_discog;

create table gen_discog (id_ga int primary key auto_increment,
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


select * from gen_discog;
describe gen_discog;

select * from albums where id_alb not in (select id_alb from gen_discog);

