# 🏙️ Proyecto Integrado 5 – Análisis de precios de apartamentos en São Paulo 🇧🇷

## 📘 1. Descripción del proyecto

El objetivo de este proyecto es **analizar los precios de venta de apartamentos en la ciudad de São Paulo (Brasil)** para identificar **patrones de valor por metro cuadrado** y **zonas con mejor costo-beneficio**.

El estudio busca responder la pregunta:

> 🏡 ¿En qué barrios de São Paulo los apartamentos son más caros o más baratos por metro cuadrado?

Este análisis permite ofrecer información útil para:
- Inversionistas inmobiliarios que buscan zonas de alta rentabilidad.  
- Constructoras que desean definir precios competitivos.  
- Ciudadanos que buscan vivienda o comparar precios de mercado.

---

## 📊 2. Dataset utilizado

**Fuente:** Kaggle  
**Nombre:** *Apartamentos à venda na cidade de São Paulo, SP*  
**Autor:** [@jlgrego](https://www.kaggle.com/jlgrego)  
**Enlace:** [https://www.kaggle.com/datasets/jlgrego/apartamentos-venda-na-cidade-de-sao-paulo-sp](https://www.kaggle.com/datasets/jlgrego/apartamentos-venda-na-cidade-de-sao-paulo-sp)  
**Archivo principal:** `dados_wgs.xlsx`  
**Licencia:** Según Kaggle, licencia abierta (normalmente *CC BY 4.0*).  
**Fecha de descarga:** Octubre de 2025  

El dataset contiene información sobre apartamentos en venta, con datos de ubicación, tamaño, precio, número de habitaciones y coordenadas geográficas.

---

## 🧩 3. Variables relevantes

| Variable | Descripción | Utilidad |
|-----------|--------------|----------|
| `bairro` | Barrio o zona de São Paulo | Permite agrupar por ubicación |
| `preco` | Precio total de venta del apartamento | Variable objetivo principal |
| `area_m2` | Área total en metros cuadrados | Permite calcular el valor por m² |
| `n_quartos` | Número de habitaciones | Segmenta el tipo de vivienda |
| `ano_construcao` | Año de construcción del inmueble | Permite analizar influencia de la antigüedad |
| `latitude` / `longitude` | Coordenadas geográficas | Facilita análisis geoespacial o visualización en mapas |

---

## 🧠 4. Caso de uso y justificación

El mercado inmobiliario de São Paulo es altamente competitivo y diverso.  
Los precios varían significativamente entre barrios, por lo que **la analítica de datos es clave** para:

- Identificar zonas subvaloradas (bajo precio por m²).  
- Detectar barrios premium o con alta valorización.  
- Apoyar decisiones de inversión y políticas de vivienda.

---

## 🧱 5. Flujo de datos implementado

El proyecto cumple con el flujo **dataset → SQLite → CSV** exigido:

