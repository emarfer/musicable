select * from total
where concat(artist,title) in 
(select concat(artist,title) as arttit from total group by arttit having count(id_can) > 1)
order by artist,title
;
select * from temas where id_Can in (
173,18310,24772,23022,4764,26000,12011,18662,12006,9269
)