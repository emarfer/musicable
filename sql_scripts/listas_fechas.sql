DROP procedure  IF EXISTS listas_fechas;

delimiter //
create procedure listas_fechas(_finicio date, _ffin date)
begin

declare _megas float;
    declare _sumt int;
    declare _summ float;
    declare _otrot int;
    declare _otrom float;
    
    set _megas = 0;

 DROP TEMPORARY TABLE IF EXISTS base;
 create temporary table base (id_base int primary key auto_increment,
								id_can int, fechahora datetime, reps int, duracion int, tamaño float, gender varchar(10), id_art int);
	insert into base (id_can, fechahora, reps, duracion, tamaño, gender, id_art)
		select sc.id_can, min(Sc.fechahora) as fechahora, count(sc.uts) as reps,
				bib.secs as duracion, bib.kbs as tamaño,
				a.sexo as gender, a.id_Art
		from scrobbling sc
			left join biblioteca bib on bib.id_CAn = sc.id_Can
			left join temas t on t.id_Can = sc.id_can
				left join artistas a on a.id_art = t.id_Art
		where date(sc.fechahora) between _finicio and _ffin
		group by sc.id_can
		order by reps desc, date(fechahora) desc, sexo;  
    drop table if exists dosanualidades;
    
				create table dosanualidades (id_base int, id_can int, fechahora datetime, reps int, megas int, id_Art int);
				
                While _megas < 716800 do
					insert into dosanualidades 
						select min(id_base), id_can, fechahora, reps, tamaño, id_Art 
						from base
                        where id_Art not in (select id_Art from dosanualidades)
						group by id_Art
                        limit 1;
					select sum(megas) into _summ from dosanualidades;
                    set _otrom = (select duracion from base
								 where id_Art not in (select id_Art from dosanualidades)
								group by id_Art
								limit 1                    
								);
					set _megas = _summ + _otrom;
				end while;
    
    
    
    end //
 delimiter ;   
set @fechafinal = date(now());

call listas_fechas( '2021-09-28', '2022-09-27');


create table segundanualidadesdeamor as (select * From dosanualidades);
select dosanualidadesdeamor.*, t.artist, t.album, t.title

 From dosanualidadesdeamor join total t on t.id_can = dosanualidadesdeamor.id_can;
 
 select base.* , t.artist, t.album, t.title
 from base  join total t on t.id_can = base.id_can
 where base.id_art not in (Select id_art from dosanualidades);
 
 
 
 
 
select dos.id_base, dos.id_can, t.artist, t.album, t.title, t.folder, t.archivo, t.ruta
from dosanualidadesdeamor dos join total t on t.id_can = dos.id_can
order by dos.id_base desc ;

select * from unaanualidadesdeamor