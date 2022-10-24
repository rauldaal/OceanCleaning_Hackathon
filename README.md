# E21---DATAERS

## Web Page
[Ocean Litter Tracker Platform](https://sergigarriga.website/)


## Index
En este proyecto hemos implemnetado varios algoritmos para la ayuda del seguimiento de plásticos en los oceanos.
1. Visualización de las trayectorias de plásticos según las corrientes marítimas.
2. Detección de plásticos en las playas con un modelo de deep learning U-Net
3. Tracking de los plásticos según el destino y el origen.

## 1. Trayectorias de plásticos según las corrientes marítimas.

A través del dataset [Global Lagrangian dataset of Marine litter](https://zenodo.org/record/6310460) hemos podido hacer un tracking de las corrinetes marinas.
Estos datos representan el movimiento de las particulas al curso de los años. En nuestro caso lo hemos aplicado solamente para el año 2021 debido al gran volumen de datos.

En __Track_and_country.ipynb__ está disponible el tracking para *20000* trayectorias del año 2021.
> Los datos son cargados a partir del archivo __data.csv__ generado con __convert_dataset.ipynb__.

![alt text](https://github.com/BIHackathon/E21---DATAERS/blob/main/img/20000_muestras.png "20000 tracks")

## 2. Detección de plásticos con U-Net.
A partir del dataset de imagenes de playas contaminadas [The BeachLitter Dataset 2022](https://www.seanoe.org/data/00743/85472/) se ha podido crear un modelo de Deep Learning tipo U-Net, con la que se han obtenido unas mascaras las cuales nos han permitido situar residos en playas. 
En __UNET_BeachLitter (1).ipynb__, donde se explica los fundamentos de la misma, se encuentra el modelo creado.
Este modelo nos permite a partir de una imagen como esta:

![alt text](https://github.com/BIHackathon/E21---DATAERS/blob/main/img/imagen.jpg "Imagen Inicial")


Crear una mascara:

![alt text](https://github.com/BIHackathon/E21---DATAERS/blob/main/img/mascara.jpg "Imagen de la Mascara")


Que al aplicarla a la imagen inicial queda de la siguiente manera:

![alt text](https://github.com/BIHackathon/E21---DATAERS/blob/main/img/substract.jpg "Resultado")

## 3. Tracking de plásticos según origen/destino.

Mediante el dataset generado con los archivos __convert_dataset.ipynb__ y __dataset_cleaning.ipynb__ se ha generado el archivo __cleande_data.csv__, el cual contiene la cordenadas iniciales y finales de cada muestra es decir tiene la dimension (n_samples, 4).
Gracias a este dataset podemos entrenar un [Regressor Lineal](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) que predice tanto la posición final a partir de la inicial, como la posición inicial a partir de la final.
Prediccion posición Inicial

![alt text](https://github.com/BIHackathon/E21---DATAERS/blob/main/img/lr_ini.png "Prediccion Inicial (Rojo)")
![alt text](https://github.com/BIHackathon/E21---DATAERS/blob/main/img/lr.png "Prediccion Final (Rojo)")

![alt text](https://github.com/BIHackathon/E21---DATAERS/blob/main/img/spain_out.png "20000 tracks")

## 4. Base de datos geocalizada con PostgresSQL.

Hemos creado una base de datos en PostgresSQL con datos  geolocalizados  para poder almacenar información sobre la contaminación maritima. 
En el estado actual del proyecto, hemos guardado en la BD las coordenadas de los movimientos de las mareas del mar para poder almacenarlas y poder trabajar con ellas en las diferentes herramientas desarrolladas. 
Esta base de datos nos aporta escalabilidad al proyecto, ya que en un futuro podríamos aumentar los datos, es decir, guardar más información útil en dicha BD. Por ejemplo, podríamos guardar coordenadas de diferentes residuos localizados en el mar, información sobre acciones de saneado del mar, etc. Estos nuevos datos  actualmente no los podríamos añadir porque necesitaríamos recolectarlos, ya que nadie lo hizo o  no consta en internet. 
