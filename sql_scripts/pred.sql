use musicablecero;
#call proxima_lista(
	-- primer parámetro hay que incluir anual o cumple según si la lista anual de datos que queremos hacer desde septiembre o desde enero.
    -- segundo parámetro anual o estación si la primera lista la queremos de año o de esatción. normalmente seleccionaremos estación.

#lista de datos es de cumple o de año    
 -- set @datos = 'cumple'; 
set @datos = 'anual';     

#estamos baremando primero la estación o el año
set @estacional = 'estacion';
-- set @estacional = 'anual';

call proxima_lista(@datos, @estacional);


select * from prediction;
select * from prediction where veces > 0;
select * from prediction where veces = 0;

select min(rep) into @minrep from prediction;
select @minrep; -- 2

select * from prediction where rep = @minrep;



select id_can, artist, album, title, genero, sexo, rep, veces from prediction
	where veces > 0
union
select id_can, artist, album, title, genero, sexo, rep, veces from base_pred
	where id_art in (select id_art from prediction where veces > 0) and veces = 0
		 and rep > (@minrep - 3)
order by artist, rep desc;
-- -2: 49 // -3: 25 46 29 30 39 11 7 4 0!!!

select id_can, artist, album, title, genero, sexo, rep, veces from base_pred 
where id_art not in (Select id_art from prediction
					-- where veces = 0
													)
	and rep >= (@minrep - 2)
	-- and sexo = 'fem'
	and veces = 0
  --  and id_can not in (select id_can from prediction_dos)
  ; -- 


-- -------------------------------------------------------
select * from prediction_dos;
select * from prediction_dos where veces > 0 or prec is true;
select * from prediction_dos where veces = 0 and prec is false; -- 25 33 35

select min(rep) into @minrepdos from prediction_dos;
select @minrepdos; -- 6
select * from prediction_dos where rep = @minrepdos; 
select sum(secs)/60 from prediction_dos where rep = @minrepdos;
select * from prediction_dos where rep = @minrepdos and veces = 0 and prec = 0; 
select sum(secs)/60 from prediction_dos where rep = @minrepdos and veces = 0 and prec = 0; 
select * from prediction_dos where rep = @minrepdos and (veces > 0 or prec > 0);  

select id_can, artist, album, title, genero, sexo, rep, veces,prec from prediction_dos
	where veces > 0 or prec is True
UNION
select id_can, artist, album, title, genero, sexo, rep, veces,prec  from base_pred_dos
	where id_art in (select id_art from prediction_dos where veces > 0 or prec is true )
		and veces = 0
        and prec is false
		and rep >= (@minrepdos - 1)
order by artist, rep desc, prec desc; 
-- -1:139 127 125 119 118 113 112 113


select id_can, artist, album, title, genero, sexo, rep, veces, prec from base_pred_dos 
where id_art not in (Select id_art from prediction_dos 
				-- where veces = 0
					)
    and prec is false
	 and rep >= (@minrepdos -2)
   -- and sexo = 'fem'
and veces = 0;


-- ----------------------------
select artist into @artist from artistas where artist = 'luis ramiro';

call artista_lista (@artist);
call temas_lista (@artist);


-- --------------------------------
set @reptot = 50;
call albums_sin_rep (@reptot); -- 40:10 30:21 40:9 30:19




select a.artist, count(l.id_can) as cuenta from artistas a left join temas t on t.id_art = a.id_art left join temasenlistados l on l.id_can = t.id_can
where a.id_art in (select id_art from temas where id_can in (select id_can from temasenlistados))
group by a.artist order by cuenta desc;

select count(*) from biblioteca;
select * From biblioteca
;
select 22243 -22389;
