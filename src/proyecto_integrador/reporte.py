# reporte.py
import streamlit as st
import pandas as pd
from logger_config import get_logger

class Reporte:
    def __init__(self, df: pd.DataFrame):
        """
        df: DataFrame con las columnas, por ejemplo:
        ['id', 'valor_total', 'unit', 'area_util', 'quartos', 'vagas',
         'condominio', 'suites', 'banheiros', 'piscina', ...,
         'qtd_dados_bairro', 'media_idh', 'media_gini', 'expectativa_vida',
         'renda_percapita', 'estacao_prox', 'linha_prox', 'dist', 'lat', 'lon']
        """
        self.df = df
        self.logger = get_logger(self.__class__.__name__)
        # Logeamos información básica del DF de visualización
        self.logger.info(
            "Reporte inicializado con DataFrame de shape: %s y columnas: %s",
            self.df.shape,
            list(self.df.columns),
        )

    # ------------------------
    # Cálculo de indicadores
    # ------------------------
    def _compute_kpis(self):
        df = self.df

        kpis = {
            "valor_total_medio": df["valor_total"].mean(),
            "precio_m2_medio": df["unit"].mean(),
            "area_util_media": df["area_util"].mean(),
            "cuartos_medios": df["quartos"].mean(),
            "renta_percapita_media": df["renda_percapita"].mean(),
        }

        # Log de las variables de visualización (KPIs)
        self.logger.info("KPIs calculados para visualización: %s", kpis)

        # Devolvemos en formato legible para la UI
        labels = {
            "valor_total_medio": "Valor total medio (R$)",
            "precio_m2_medio": "Precio medio por m² (R$/m²)",
            "area_util_media": "Área útil media (m²)",
            "cuartos_medios": "Cuartos medios",
            "renta_percapita_media": "Renta per cápita media (R$)",
        }

        kpis_mostrados = {labels[k]: v for k, v in kpis.items()}
        return kpis_mostrados

    def render_kpis(self):
        st.subheader("Indicadores principales")

        kpis = self._compute_kpis()

        col1, col2, col3 = st.columns(3)
        col4, col5 = st.columns(2)
        cols = [col1, col2, col3, col4, col5]

        for col, (label, value) in zip(cols, kpis.items()):
            col.metric(label, f"{value:,.2f}")

        # Log de datos usados en el gráfico de barras
        self.logger.info("Mostrando KPIs en dashboard: %s", kpis)

        kpi_df = pd.DataFrame(
            {"Indicador": list(kpis.keys()), "Valor": list(kpis.values())}
        )

        st.markdown("### Comparación de indicadores")
        st.bar_chart(kpi_df.set_index("Indicador"))

    # ------------------------
    # Gráficos exploratorios
    # ------------------------
    def render_exploratory_charts(self):
        df = self.df

        st.subheader("Exploración de los datos")

        # Scatter valor_total vs área_util
        if {"area_util", "valor_total"}.issubset(df.columns):
            self.logger.info(
                "Renderizando scatter valor_total vs area_util con %d filas",
                len(df),
            )
            st.markdown("**Valor total vs área útil**")
            st.scatter_chart(df, x="area_util", y="valor_total")
        else:
            self.logger.warning(
                "No se puede crear scatter: faltan columnas 'area_util' o 'valor_total'"
            )

        # Mapa de propiedades si hay lat/lon
        if {"lat", "lon"}.issubset(df.columns):
            df_mapa = df[["lat", "lon"]].dropna()
            self.logger.info(
                "Renderizando mapa de propiedades con %d puntos", len(df_mapa)
            )
            st.markdown("**Mapa de propiedades**")
            st.map(df_mapa)
        else:
            self.logger.warning(
                "No se puede crear mapa: faltan columnas 'lat' o 'lon'"
            )

    # ------------------------
    # Filtros
    # ------------------------
    def render_filters(self):
        df = self.df

        st.sidebar.header("Filtros")

        estacoes = ["(Todas)"]
        linhas = ["(Todas)"]

        if "estacao_prox" in df.columns:
            estacoes += sorted(df["estacao_prox"].dropna().unique().tolist())
        if "linha_prox" in df.columns:
            linhas += sorted(df["linha_prox"].dropna().unique().tolist())

        estacao_sel = st.sidebar.selectbox("Estación más próxima", estacoes)
        linha_sel = st.sidebar.selectbox("Línea más próxima", linhas)

        df_filtrado = df.copy()

        if estacao_sel != "(Todas)" and "estacao_prox" in df.columns:
            df_filtrado = df_filtrado[df_filtrado["estacao_prox"] == estacao_sel]

        if linha_sel != "(Todas)" and "linha_prox" in df.columns:
            df_filtrado = df_filtrado[df_filtrado["linha_prox"] == linha_sel]

        # Log de variables de visualización relacionadas con filtros
        self.logger.info(
            "Filtros aplicados - estacao_prox: %s, linha_prox: %s, filas resultantes: %d",
            estacao_sel,
            linha_sel,
            len(df_filtrado),
        )

        self.df = df_filtrado
        st.sidebar.write(f"Total de registros: {len(self.df)}")

    # ------------------------
    # Método principal
    # ------------------------
    def render(self):
        st.title("Dashboard Inmobiliario")

        # Log de inicio de render
        self.logger.info("Renderizando dashboard principal")

        # Filtros (modifican self.df)
        self.render_filters()

        # Secciones principales
        self.render_kpis()
        self.render_exploratory_charts()

        self.logger.info("Render de dashboard completado")
