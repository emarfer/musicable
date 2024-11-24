with movida as (
select sc.id_can, sc.artist, sc.album, sc.title, art.genero, min(date(sc.fechahora)) as minfecha, max(date(sc.fechahora)) as maxfecha, count(sc.uts) as reps
from scrobbling sc left join artistas art on sc.artist = art.artist
-- where sc.fechahora >= "2023-10-27"
where -- sc.fechahora >= "2023-01-01" and
/*
sc.id_can in (Select id_can from biblioteca where folder like "%Metal, hard rock%" or folder like "%Rock Ibérico, punkarra y rock latino%"
or folder like "%Classic Punk, New Wave, Garage Rock y psicodeli%" or folder like "%Flamenco, Fusión, Música del mundo, ritmos latinos y Franci%"
or folder like "%Punky, rap metal, Ska y Reggae%" or folder like "%V.A%") and
*/
(genero like "%metal%" or genero like "%rock%" or genero like "%ska%" or genero like "%punk%" or genero like "%grunge%" or genero like "%glam%")
and sc.artist not in ("leiva","ariel rot","celtas cortos","Coque Malla","Pereza","Ska-P","Albert Pla","Andrés Calamaro","Despistaos","Firehouse","Ken Zazpi","La Maravillosa Orquesta del Alcohol",
"La Vela Puerca","Loquillo Y Los Intocables","Los Ronaldos","Molotov","Los Abuelos de la Nada","Los Nikis","Crazy Town","El Canijo de Jerez","Howe Gelb & A Band of Gypsies","Kiko Veneno",
"La Frontera","Los Delinqüentes","Los Fabulosos Cadillacs","Los Rodríguez","Migue Benítez","Minutemen","Ojos de Brujo","Raimundo Amador","The Living End","Veneno","Amy Macdonald", 
"Counting Crows","Danza Invisible","Eagle-Eye Cherry","Eric Carmen","Jerry Lee Lewis","Los de Abajo","Roxette","Texas","Texas","The Beatles","The Brian Setzer Orchestra","The Rapture",
"Train","Zenttric","Olé Olé","Amaral","Cadillac","Crowded House","El Último de la Fila","Howie Day","Dionysos","Jimmy Page","Los Piojos","Manfred Mann","Pabellón Psiquiátrico","Pata Negra",
"Pixies","Santana","Save Ferris","The Cranberries","The Bangles","Veruca Salt","Alaska","Del Shannon","Enanitos Verdes","Live","Rob Thomas","Rosario La Tremendita","The Electric Prunes",
"Los Secretos","Status Quo","The Black Ryder","Spin Doctors","Snuff","Nancy Sinatra","Los Auténticos Decadentes","Albertucho","Andy Chango","Bill Haley & His Comets","Flobots",
"Jah Wobble's Invaders of the Heart","Julieta Venegas","Plain White T's","Tam Tam Go!","XTC","091","Alanis Morissette","Alfie Zappacosta","Aterciopelados","Boston","Bruce Channel","Daniel Wesley",
"Fairground Attraction","Frankie Valli & the Four Seasons","Frankenstein Drag Queens from Planet 13","Goblin","Guaraná","Hall & Oates","Huey Lewis and the News","Jesús Cifuentes","Kambotes","Kevin Johansen","La Unión",
"Little Richard","Los Bravos","Los Electroduendes","Louise Attaque","Marcy Playground","Maria McKee","Mike Oldfield","New Radicals","No Doubt","Pavement","Nomy","Roy Orbison","Sixpence None the Richer",
"Starship","Stealers Wheel","Supertramp","The Box Tops","The Church","The Doobie Brothers","The Doobie Brothers","The Proclaimers","The Rembrandts","Third Eye Blind","Tom Johnston","Transvision Vamp","Urge Overkill",
"Vikxie","love","Melting Pot","Better Than Ezra","HAIM","Joe 90","Maroon 5","Marika Hackman","Matchbox Twenty","Moon Duo","Royal Blood","Shivaree","The Baseballs","The Break And Repair Method","The Cardigans","Vega",
"10cc","3 Doors Down","Aloha from Hell","4 Non Blondes","Andrés Calamaro y Fito & Fitipaldis","Beck","BeNuts","Billy Joel","Billy Idol","Black Country Communion","Black Label Society","Blue Swede","Brenda Lee",
"Bryan Adams","Buck Wild","Buckcherry","Butt First","Captain Beefheart & His Magic Band","Carpenters","Cavo","Chad Kroeger","Cheap Trick","Chesney Hawkes","Chevelle","Chicago","Chris Daughtry","Chris Rea","Cinema Bizarre",
"Class of '99","Cliff Richard","Comalcool","Cream","Creed","Creedence Clearwater Revival","Danzig","Die Toten Hosen","Dinosaur Jr.","Dire Straits","Dulce Venganza","Dynamite Boy","Edwyn Collins",
"Bad Company","Iron Butterfly","Jack Black","John Mayer","Mick Jagger","Moby Grape","Roger McGuinn","Ron Wood","The Animals","Gavin Rossdale","Goo Goo Dolls","Jane's Addiction","Joe Queer & The Nobodys","Nada Surf",
"Tito & Tarantula","Traffic","Reckless Drivers","Tabitha's Secret","Jefferson Airplane","CRIENIUM","Meat Puppets","Richard Hawley","Steely Dan","The Horrors","The La's","The Vines","Beth Hart","George Ezra","Paramore",
"Small Faces","Sonic Youth","The Soft Moon","Deep Blue Something","Lebanon Hanover","McNamara","Muse","Sugar Ray","Tracy Bonham","Almodóvar & McNamara","Alaska y Dinarama","Alaska y Los Pegamoides",
"Dream Wife","Duncan Dhu","Kaka de Luxe","Aerolíneas Federales","Fool's Garden","Soul Asylum","Steve Miller Band","John Lennon","Mikel Erentxun","The Doors","Gatas Negras","George Harrison","John Mellencamp",
"Judee Sill","EMF","Café Tacvba","Eagles","Foreigner","Gabinete Caligari","The Shins","The Stone Roses","The Smashing Pumpkins","The Rasmus","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",
"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""
)
and sc.id_Can in (Select distinct id_Can from biblioteca)
-- and year(sc.fechahora) = 2024
group by sc.id_can, sc.artist, sc.album, sc.title, art.genero
having reps = 9
-- order by artist, reps desc, minfecha
order by reps, minfecha desc, artist desc, album desc
 )
-- select * from movida
select distinct genero from movida
-- select distinct artist from movida order by artist
;

select * from total where artist = "alice cooper";

select distinct genero from artistas
where genero like "%metal%" or genero like "%rock%" or genero like "%ska%" or genero like "%punk%" or genero like "%grunge%" or genero like "%glam%"
order by genero;

select * from artistas where genero like "%glam%";

select distinct genero from artistas order by genero;

with seleccion as (
select sc.id_can, sc.artist, sc.album, sc.title, art.genero, min(date(sc.fechahora)) as minfecha, max(date(sc.fechahora)) as maxfecha, count(sc.uts) as reps
from scrobbling sc left join artistas art on sc.artist = art.artist
where art.genero in ("art rock","black metal","blues","blues rock","folk rock","garage","glam rock","gothic metal","grunge","hard rock","hardcore","heavy metal","oi!","power metal","pop rock",
"power metal","punk","punk pop","punk rock","riot grrrl","rock","rock alternativo","rock ibérico","rock latino","rock progresivo","rock psicodélico","ska","ska punk","thrash metal", "new wave", "rock andaluz",
"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","")
and sc.id_can in (select id_can from biblioteca)
and art.artist not in ("091","4 Non Blondes","Alanis Morissette","Alaska y Dinarama","Alaska y Los Pegamoides","Aerolíneas Federales","Alaska","Alfie Zappacosta","Allah-Las","Almodóvar & McNamara","Amaral",
"Amy Macdonald","Andrés Calamaro","Andy Chango","Anouk","Ariel Rot","Aterciopelados","Bad Company","Beck","Belinda Carlisle","Berlin","Beth Hart","Better Than Ezra","Beverly McClellan","Billy Joel","Blues Brothers",
"Bonnie Raitt","Bonnie Tyler","Boston","Buckcherry","Cadillac","Café Tacvba","Bunbury","Celtas Cortos","Chrissie Hynde","Counting Crows","CRIENIUM","Creedence Clearwater Revival","Crowded House","Danza Invisible","Dead Or Alive",
"Deep Blue Something","Derek and the Dominos","Despistaos","Dionysos","Dire Straits","Dog Eat Dog","Dream Wife","Duncan Dhu","Eagle-Eye Cherry","Eagles","Elvis Costello","Elvis Costello & The Attractions","El Último de la Fila",
"Eric Carmen","Eric Clapton","Faces","Fairground Attraction","Flobots","Fool's Garden","Free","Gabinete Caligari","Gatas Negras","Gavin Rossdale","George Harrison","Goblin","Goo Goo Dolls","Guaraná","HAIM",
"Hall & Oates","Happy Mondays","Hidrogenesse","Howie Day","Huey Lewis and the News","Iron Butterfly","Incubus","Jack Black","Jane's Addiction","Jefferson Airplane","Jesús Cifuentes","Jimmy Page","Joe 90",
"Joe Queer & The Nobodys","John Lennon","John Mayer","John Mellencamp","Jonny Lang","Julieta Venegas","Kaka de Luxe","Kambotes","Keb' Mo'","Kevin Johansen","La Guardia","La Unión","Lebanon Hanover","Los Bravos",
"Los Electroduendes","Los Fabulosos Cadillacs","Los Piojos","Los Rodríguez","Los Romeos","Los Secretos","Louise Attaque","Love","Manfred Mann","Marcy Playground","Maria McKee","Maroon 5","Matchbox Twenty",
"McNamara","Meat Puppets","Melting Pot","Men at Work","Michael Sembello","Mick Jagger","Mike Oldfield","Mikel Erentxun","Minutemen","Missing Persons","Moby Grape","Moon Duo","Muddy Waters",
"Nacha Pop","Mürfila","Nada Surf","Nena","New Order","New Radicals","Nick Lowe","Nickelback","No Doubt","Nomy","Olé Olé","Opus","Paramore","Patti Scialfa","Pavement","Pereza","Plain White T's","Queens of the Stone Age",
"Reckless Drivers", "Rob Thomas","Roger McGuinn","Ron Wood","Roy Orbison","Royal Blood","Ryan Adams","Santana","Shannon Shaw","Sixpence None the Richer","Small Faces","Sonic Youth","Soul Asylum","Spandau Ballet","Spin Doctors",
"Starship","Status Quo","Stealers Wheel","Steely Dan","Sugar Ray","Supertramp","Tears for Fears","Texas","The Animals","The Black Ryder","The Beatles","The Blow Monkeys","The Box Tops","The Break And Repair Method",
"The Church","The Cramps","The Dollyrots","The Doobie Brothers","The Electric Prunes","The Kingsmen","The Kinks","The Living End","The Monkees","The Police","The Pretenders","The Primitives","The Proclaimers","The Rasmus",
"The Refrescos","The Rembrandts","The Rolling Stones","The Shins","The Stone Roses","The Stooges","The Stranglers","The Vines","The White Stripes","Third Eye Blind","Tito & Tarantula","Tom Johnston","Tom Tom Club",
"Tracy Bonham","Traffic","Train","U2","Vega","Veruca Salt","Vikxie","Zenttric",
"Daniel Wesley","EMF","Enanitos Verdes","Foreigner","Joe Cocker & Jennifer Warnes","Journey","Ken Zazpi","Ram Jam","Steve Miller Band","The Presidents of the United States of America","The Smashing Pumpkins",
"Steppenwolf","Bryan Adams","R.E.M.","The La's","Television","Alice in Chains","Marika Hackman","The Mighty Mighty Bosstones","Kiko Veneno","Veneno","El Barrio","Joe Esposito","Sting","Live","Molotov","Tam Tam Go!",
"Tino Casal","El Niño de La Hipoteca","Pabellón Psiquiátrico","Perfect Pussy","Pixies","Pink Floyd","Roxette","Shivaree","Skunk Anansie","Tabitha's Secret","The Cult","The Goops", "INXS",
"David Bowie","Bruce Springsteen","Muse","Kate Bush",
"Elvis Presley","Leiva","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","")
group by sc.id_can, sc.artist, sc.album, sc.title, art.genero
)
-- select distinct artist, genero, count(distinct id_Can) as canciones from seleccion group by artist order by canciones asc, artist
select * from seleccion where reps = 9 order by artist, reps desc
;
select genero, count(*) from artistas group by genero;

select * From artistas;