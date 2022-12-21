select * from biblioteca;
select folder, count(*) as archivos
from biblioteca
group by folder
order by archivos desc
;
select replace(folder,'H:\\','D:\\') from biblioteca;
select folder,replace(folder,'H:\\','D:\\') from biblioteca;
update biblioteca set folder = replace(folder,'H:\\','D:\\');

alter table biblioteca add column id_ruta int;

drop table ruta_total;
create table ruta_total (
	id_ruta int primary key, 
    folder varchar(190), 
    unidad varchar(5), 
    raiz varchar(10),
    genero varchar(70), 
    artista varchar(70),
    disco  varchar(100), 
    sub1 varchar(50)
)
;

select * from ruta_total;

alter table biblioteca add column idr_ruta int;
alter table biblioteca drop column idr_ruta;
alter table biblioteca add column id_ruta int;
alter table biblioteca drop column id_ruta;



update biblioteca b join ruta_total r on r.folder = b.folder
set b.id_ruta = r.id_ruta
;

select * from biblioteca;

select * From ruta_total;