#eliminar columna fecha hora de scrobbling
#vista reproducciones usa fechahora... ver cómo se create
#vista scro_sin_reg usa fecha, hora y fechahora + tabmién scrob_sin_actualizar
/*
fehcahora de scrobbling se actuliza en el proc. "insert_scro" y se hace con la columna uts (podemos eliminar columna hora)
*/
/*
hemos usado las siguientes querys para analizar la funcionalidad el cambio de uts a hora con FROM_UNIXTIME de la función insert_scro
hemos comprobado que sí se modifica teniendo en cuenta horas de verano y demás a horario español
drop table probando_hora;
create table probando_hora as
select fecha, hora, FROM_UNIXTIME(uts,'%Y-%m-%d %H:%i:%s') as unix from scrobbling;

describe probando_hora;
ALTER TABLE `musicablecero`.`probando_hora` 
CHANGE COLUMN `unix` `unix` DATETIME NULL DEFAULT NULL ;

select Hour(hora), Hour(unix), Hour(unix)-Hour(hora) as dif from probando_hora;
*/
#ahora comprobado: pasamos a eliminar fecha hora de las vistas y luego de la tabla... 

#elimnamos de scrob_sin_actualizar y de scro_sin_reg

ALTER TABLE `musicablecero`.`scrobbling` 
DROP COLUMN `Hora`,
DROP COLUMN `Fecha`,
DROP INDEX `idx_fecha` ;
;

set @minuts = 0;

select * From scrobbling order by uts desc limit 30;
select min(uts) into @minuts From scrobbling order by uts asc limit 2000;
select @minuts;
select min(uts) from scrobbling;
select * from scrobbling where uts = 1642350684;

describe scrobbling;



select * from scrobbling where uts >= 1639842671;
delete from scrobbling where uts > 1639842671;

select * from scrobbling where uts >= 1642016142;
SELECT * FROM scrobbling ORDER BY uts desc;

select * From scrobbling where uts >= 1642152224;

delete from scrobbling where uts > 1642152224;



call insert_scro();
delete from scrobbling where uts = 1640351615;
update scrobbling set artist = 'Juan Luis Guerra y 4.40' where album = 'Bachata Rosa' and artist = 'Juan Luis Guerra';
update scrobbling set artist = 'Robe' where artist = 'Robe.';
update scrobbling set title = "Can't Hold Us Down (ft. Lil' Kim)" where artist = 'Christina Aguilera' and title = "Can't Hold Us Down";
update scrobbling set title = 'Satisfaction' where title = "(I Can't Get No) Satisfaction" and album = 'Out of Our Heads';

select * From total where album = 'out of our heads'; #Satisfaction

update scrobbling set artist = 'Robe' where artist = 'Robe.';

select * from scrobbling where id_Can is null and fechahora is null;

delete from scrobbling where uts >= 1639843825;
