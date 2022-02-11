# Musicable
# _Análisis de datos basados en la música que escucho_
(Nunca pensé que me pudiera molar tanto hacerle requests a una api...)


![](imagenes/headphones.jpg)


# Last.fm: 
![## Last.fm:](imagenes/lastlogodos.png)

 ### Es una [red social](https://www.last.fm/), una radio vía Internet y además un sistema de recomendación de música que construye perfiles y estadísticas sobre gustos musicales, basándose en los datos enviados por los usuarios registrados

## MySQL:
![](imagenes/mysqltrans.png)

### [MySQL](https://www.mysql.com/) es un sistema de gestión de bases de datos relacional 

# ¿Qué es lo que hago con este repositorio?
Desde hace tiempo tengo una base de datos creada en MySQL que se llama "musicablecero": recoge los metadatos de mis archivos musicales del pc y también las reproducciones de last.fm de mi usuario: "[sinatxester](https://www.last.fm/user/sinatxester)". Con estos datos me genero listas de reproducción musicales en función de diversos parámetros, que no soy he sido capaz de encontrar en ninún repoductor musical, por muy personalizables que puedan hacer estas listas.

## Objetivos principales:
- Automatizar procesos de insercción de datos tanto de metadatos de mis archivos como reproducciones de last.fm usando su [api](https://www.last.fm/api).
- Generar visualizaciones de las estadísticas de reproducción más allá de las que brinda last.fm a sus usuarios (tanto los de pago como los que no nos gastamos ni un duro)
- Usar apis de otros proveedore de datos musicales como [discogs](https://www.discogs.com/es/) para enriquecer la base que ya tengo
- Crear una base de datos más amplia que recoga los datos de otros usuarios de lastfm para mostrarles las estadísticas de reproducción que deseen y generales listados de reproducción con los parámetros que deseen

### <u>Conseguido</u>: :sunglasses:
- Automatizo el proceso de insercción en musicablecero de las reproducciones registrradas en last.fm
<!-- 
<p align="center">
  <img src=imagenes/lastlogodos.png width="350" title="hover text">
  <img src=imagenes/lastlogodos.png width="350" alt="accessibility text">
</p> -->