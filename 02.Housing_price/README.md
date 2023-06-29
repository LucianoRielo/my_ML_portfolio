# 02. Housing Price

## Creación de **entorno virtual**

```bash
cd machine_learning_practice
mkdir 02.Housing_Price
virtualenv safe_house

source safe_house/bin/activate

pip3 install --upgrade jupyter matplotlib numpy pandas scipy scikit-learn
```

## Análisis

- Se descarga el dataset mediante ***fetch_data*** y ***load_data***
- Se analiza el dataset con .info(), .describe(), .value_counts(), .hist(bins=50,figsize(20,15)) y se hacen observaciones:
- [x]  No existe median_income por encima de 15 y debajo de 0.5
- [x]  asimetría en varios histogramas
- [x]  ocean_proximity son categorias de strings
- [x]  en total_bedrooms faltan datos
- [x]  hay una concentracion de districtos con median_house_value = 500001.0
- [x]  hay una concentracion de districtos con housing_median_age = 52.0
- Se crea el ****************test_set**************** mediante *******************stratified sampling******************* considerando al ingreso medio como variable importante
- Se plotea el mapa (latitud, longitud) de california y se hacen **observaciones.**
- Se buscan correlaciones mediante el coeficiente de correlación estandar, se hacen **observaciones:**
- [x]  median_house_value tiene una gran correlacion con los ingresos medios
- [x]  la latitud tiene una correlacion negativa, es decir, cuando es mayor a menor tienden los ingresos
- Se prueban nuevos atributos, como rooms_per_holdhouse, bedrooms_per_holdhouse, y population_per_holdhouse. ********************************************************************Todas obtuvieron mejor factor de correlación.********************************************************************

## Preprocesado

- Se reemplazan las celdas vacias en total_bedrooms por la mediana
- OneHotEncoder para reemplazar los datos strings por 0 o 1
- Se crea un transformador de data en nuevas features creando una clase que hereda BaseEstimator y TransformerMixin para ser compatible con pipelines de sklearn
- Escaleo de valores con standarization
- Creacion de pipelines con FeatureUnion (combina varias pipelines, una para procesar valores numericos, y otra para transformar las categorias de strings en one-hot vectors)

## Entrenamiento del Modelo

Se prueban distintos modelos:

- Regresion lineal
- Arbol de decisiones
- RandomForest