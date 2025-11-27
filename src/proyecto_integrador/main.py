# main.py
import streamlit as st
from ingestar import Ingestar
from reporte import Reporte
from logger_config import get_logger


logger = get_logger(__name__)


def run_app():
    """
    Ejecuta el flujo completo:
    1. Descarga el dataset desde Kaggle
    2. Extrae archivos si es necesario
    3. Carga los datos en un DataFrame
    4. Renderiza el Dashboard
    """
    kaggle = "jlgrego/apartamentos-venda-na-cidade-de-sao-paulo-sp"

    logger.info(">>> INICIANDO PROCESO DE EJECUCIÓN DE LA APLICACIÓN <<<")
    logger.info("Dataset origen Kaggle: %s", kaggle)

    ingestar = Ingestar()

    archivo = ingestar.download_dataset_zip(kaggle)
    zip_kaggle = ingestar.extract_zip_files(archivo)
    df = ingestar.load_dataset_as_dataframe(zip_kaggle)

    logger.info("DataFrame final para visualización con shape: %s", df.shape)

    st.set_page_config(page_title="Dashboard Inmobiliario", layout="wide")

    dashboard = Reporte(df)
    dashboard.render()

    logger.info(">>> APLICACIÓN EJECUTADA CORRECTAMENTE <<<")


# Este bloque evita ejecución accidental cuando se importa desde otro archivo
if __name__ == "__main__":
    run_app()
