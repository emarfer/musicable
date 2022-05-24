use sakila;
SELECT * FROM ACTOR;
DESCRIBE actor;
DESCRIBE FILM_ACTOR;
DESCRIBE FILM;

select concat(a1.first_name,' ',a1.last_name) as firs_actor,
concat(a2.first_name,' ',a2.last_name) as second_act,
f.title as title
from actor a1
join actor a2 on a2.actor_id = a1.actor_id
join film_actor fa on fa.actor_id = a1.actor_id
join film f on f.film_id = fa.film_id
order by title
;

select a1.actor_id, a2.actor_id,count(a1.film_id),group_concat(a1.film_id)
from film_actor a1 join film_actor a2 on a2.actor_id =a1.actor_id
join film f on f.film_id = a1.film_id
group by a1.actor_id, a2.actor_id;

with top_name (actor1, actor2, starts) as
    (select tp.actor_id, fa.actor_id as costar, count(fa.actor_id) as starts
    from film_actor fa, film_actor tp
    where fa.film_id = tp.film_id
    and fa.actor_id <> tp.actor_id
    group by tp.actor_id, fa.actor_id
    order by starts desc, tp.actor_id
    limit 1) -- the most co-star
-- join with actor and film tables
select a1.first_name||' '||a1.last_name as "first_actor",
       a2.first_name||' '||a2.last_name as "second_actor",
       f.title
from
     actor a1, actor a2, film f, top_name tt
     where tt.actor1 = a1.actor_id
     and tt.actor2 = a2.actor_id
     and f.film_id in 
     (select fa1.film_id from film_actor fa1, film_actor fa2
     where fa1.film_id = fa2.film_id
     and fa1.actor_id = a1.actor_id
     and fa2.actor_id = a2.actor_id);
     
    
   
    
    select a1.actor_id as actor1, a2.actor_id as actor2, count(a1.actor_id) as pelis
    from film_actor a1, film_actor a2
    where a1.film_id = a2.film_id and a1.actor_id != a2.actor_id
    group by a1.actor_id, a2.actor_id
    order by pelis desc, a1.actor_id
    limit 10;
    
    
    
    
    with resumen (uno,dos,pelis) as (
    select a1.actor_id, a2.actor_id, count(a2.actor_id)
    from film_actor a1, film_actor a2
    where a1.film_id = a2.film_id and a1.actor_id != a2.actor_id
    group by a1.actor_id, a2.actor_id
    order by count(a2.actor_id) desc, a1.actor_id
    limit 1) 
    select concat(a1.first_name,' ',a1.last_name) as first_actor,
    concat(a2.first_name,' ',a2.last_name) as second_actor,
    f.title as title
    from resumen res
    join film_actor fa1 on fa1.actor_id = res.uno
    join film_actor fa2 on fa2.actor_id = res.dos
    join film f on f.film_id = fa1.film_id and f.film_id = fa2.film_id
    join actor a1 on a1.actor_id = res.uno
    join actor a2 on a2.actor_id = res.dos
    order by title;
    
    
with casting (uno,dos,pelis) as (
	select a1.actor_id, a2.actor_id, count(a2.actor_id)
	from film_actor a1
	join film_actor a2 on a1.film_id = a2.film_id and a1.actor_id != a2.actor_id
	group by a1.actor_id, a2.actor_id
	order by count(a2.actor_id) desc, a1.actor_id
	limit 1) 
select concat(a1.first_name,' ',a1.last_name) as first_actor,
	concat(a2.first_name,' ',a2.last_name) as second_actor,
	f.title as title
from casting as c
	join film_actor fa1 on fa1.actor_id = c.uno
	join film_actor fa2 on fa2.actor_id = c.dos
	join film f on f.film_id = fa1.film_id and f.film_id = fa2.film_id
	join actor a1 on a1.actor_id = c.uno
	join actor a2 on a2.actor_id = c.dos
order by title;


CREATE TEMPORARY TABLE hola as
    (select * from scrobbling where id_can > 12000);
select * from hola;
drop temporary table hola;
    