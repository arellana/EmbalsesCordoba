# 🌊 EmbalsesCordoba

## 🛰️ Análisis del Estado Trófico de los Embalses de Córdoba  
**Basado en imágenes satelitales ópticas Sentinel-2.**

Repositorio destinado al análisis del estado trófico de diversos embalses en la provincia de Córdoba, Argentina, utilizando herramientas de **teledetección, análisis espacial y machine learning**.

---

## 📂 Contenido del Repositorio

### 🗂️ Carpetas
- 📐 **Fajas_Gauss_Kruger_Argentina**  
  Conversión y datos geoespaciales en coordenadas **Gauss-Krüger** para Argentina.  

- 📊 **Plots**  
  Gráficos generados para visualizar resultados del análisis.  

- 🗺️ **Poligonos**  
  Polígonos vectoriales de los límites de embalses.  

- ✏️ **geometrias-corregidas**  
  Versiones corregidas o ajustadas de geometrías originales.  

- 🧩 **polsembalses**  
  Polígonos específicos para cada embalse. *(No hace falta modificar)*  

---

### 📑 Archivos principales
- 📘 **Estadistica_ROIs.ipynb**  
  Notebook que analiza estadísticas de las **Regiones de Interés (ROIs)**:  
  - Firma Espectral  
  - Índices Ópticos  
  - Brightness, Greeness, Wetness  

- 🌲 **RandomForest.ipynb**  
  Implementación de un modelo **Random Forest** para clasificar o predecir el estado trófico.  

- ⚙️ **funciones.py**  
  Funciones auxiliares para:  
  - Cargar datos  
  - Preprocesamiento  
  - Graficado  

- 📙 **Presentacion1.ipynb** y **Presentacion2.ipynb**  
  - Métodos de clasificación **KMeans** aplicados a las ROIs.  
  - Métodos de **Machine Learning** aplicados a las ROIs junto con análisis de firmas espectrales:  
    - Tasseled Cap  
    - Clasificadores Supervisados y No Supervisados  

---

## ▶️ Ejecución del Proyecto

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/arellana/EmbalsesCordoba.git
   cd EmbalsesCordoba
   

2. **Preparar el entorno**
   Instalar dependencias desde el archivo **YAML**:

   ```bash
   conda env create -f dependencies.yml
   ```

3. **Explorar los notebooks**

   * 📘 `Estadistica_ROIs.ipynb`: estadísticas de las ROIs.
   * 📙 `Presentacion1.ipynb` y `Presentacion2.ipynb`: análisis visual y métodos de ML.
   * 🌲 `RandomForest.ipynb`: modelo supervisado aplicado.

4. **Inspeccionar datos geoespaciales**

   * Las carpetas con geometrías (`Poligonos`, `geometrias-corregidas`, `polsembalses`) y mapas (`Plots`) contienen la información principal de interés.
   * 🔧 Se pueden modificar las **Regiones de Interés (ROIs)** para estudiar nuevos sitios.

---

## 📝 Cosas por Hacer

* 🌐 Traducir todo el repositorio al inglés.
* 🛰️ Incluir una **imagen Sentinel-2 de prueba**.
* 📖 Documentar cada notebook con descripciones claras.

---

## 👨‍🔬 Créditos

Desarrollado por **Javier Arellana**

📍 Instituto de Astronomía y Física del Espacio (IAFE), **UBA – CONICET**
📍 Departamento de Física, Facultad de Ciencias Exactas y Naturales, **Universidad de Buenos Aires**

---

