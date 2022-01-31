   
-- 
select max(id_tag) into @maxtag from tag where id_can is not null;
select * from tag where id_tag > @maxtag;

#updates:

update tag join artistas a on a.artist = tag.artist
	set tag.id_art = a.id_art 
    where a.artist = tag.artist and tag.id_Art is null;
    
update tag join albums a on a.album = tag.album
	set tag.id_alb = a.id_alb
    where a.album = tag.album and tag.id_Alb is null 
		and a.id_art = tag.id_art
    -- and tag.id_tag > @maxtag; -- 
    ;

update tag join temas t on t.title = tag.title
 set tag.id_Can = t.id_Can
 where t.id_Art = tag.id_art and t.id_alb = tag.id_alb and tag.id_Can is null;
 
update tag join biblioteca b on b.id_Can = tag.id_Can
set tag.id_bib = b.id_bib
where tag.id_bib is null
 ;

#inserts:

 insert into artistas (artist, sexo, genero, band, id_p)
select distinct artist, 'fem', 'folk', 's', (select id_p from paises where nombre = 'Estados Unidos') from tag where id_tag > @maxtag;
 
insert into albums (album, released, num_track, id_art)
select album, released, max(track), id_art from tag where id_tag > @maxtag and id_alb is null  group by album
;

insert into temas (title, track, id_alb, id_art)
select title, track, id_alb, id_art from tag where id_tag > @maxtag and id_can is null;

 insert into biblioteca (id_Can, secs, kbs, folder, archivo, creado, tipo, bitrate)
select id_Can, secs, replace(kbs,',','.'), folder, archivo, creado, tipo, bitrate 
	from tag where id_tag > @maxtag;


-- 

select max(id_tag) into @maxtag from tag where id_can is not null;
select * from tag where id_tag > @maxtag;

select * from total where title in (Select title from tag where id_tag > @maxtag);
select * from albums where id_alb in (Select id_alb from tag where id_tag > @maxtag);

select released, max(track) into @rel, @tr from tag where id_tag > @maxtag;
select @rel, @tr;
update albums set released = @rel, num_track = @tr 
	where id_alb = (Select distinct id_alb from tag where id_tag > @maxtag);

select * from temas where id_can in (Select id_can from tag where id_tag > @maxtag);
update temas t join tag on tag.id_can = t.id_can
	set t.track = tag.track
    where t.id_can in (select id_Can from tag where id_tag > @maxtag) and t.track is null
    ;

select * from total where id_can in (Select id_can from tag where id_tag > @maxtag);
select * from total where artist = 'traffic';
select * from temas where id_Can = 14190;
select * From albums where album like '%garage i%';
select * from biblioteca order by id_bib desc;
select * from temas where title like '%manuel%';

select * from biblioteca;

select * from total where album in (select album from tag where id_tag > @maxtag);
select * from temas where id_can = 7314;




