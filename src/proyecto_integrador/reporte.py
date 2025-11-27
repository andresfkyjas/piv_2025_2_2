import streamlit as st
import pandas as pd

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

    # ------------------------
    # Cálculo de indicadores
    # ------------------------
    def _compute_kpis(self):
        df = self.df

        kpis = {
            "Valor total medio (R$)": df["valor_total"].mean(),
            "Precio medio por m² (R$/m²)": df["unit"].mean(),
            "Área útil media (m²)": df["area_util"].mean(),
            "Cuartos medios": df["quartos"].mean(),
            "Renta per cápita media (R$)": df["renda_percapita"].mean(),
        }
        return kpis

    # ------------------------
    # Sección de KPIs
    # ------------------------
    def render_kpis(self):
        st.subheader("Indicadores principales")

        kpis = self._compute_kpis()

        col1, col2, col3 = st.columns(3)
        col4, col5 = st.columns(2)
        cols = [col1, col2, col3, col4, col5]

        for col, (label, value) in zip(cols, kpis.items()):
            col.metric(label, f"{value:,.2f}")

        # Gráfico de barras con los indicadores
        st.markdown("### Comparación de indicadores")
        kpi_df = pd.DataFrame(
            {"Indicador": list(kpis.keys()), "Valor": list(kpis.values())}
        )
        st.bar_chart(kpi_df.set_index("Indicador"))

    # ------------------------
    # Gráficos exploratorios
    # ------------------------
    def render_exploratory_charts(self):
        df = self.df

        st.subheader("Exploración de los datos")

        # Scatter valor_total vs área_util
        if {"area_util", "valor_total"}.issubset(df.columns):
            st.markdown("**Valor total vs área útil**")
            st.scatter_chart(df, x="area_util", y="valor_total")

        # Mapa de propiedades si hay lat/lon
        if {"lat", "lon"}.issubset(df.columns):
            st.markdown("**Mapa de propiedades**")
            st.map(df[["lat", "lon"]].dropna())

    # ------------------------
    # Filtros (opcional)
    # ------------------------
    def render_filters(self):
        df = self.df

        st.sidebar.header("Filtros")

        # Ejemplo: filtrar por estación y línea de metro
        estacoes = ["(Todas)"] + sorted(df["estacao_prox"].dropna().unique().tolist())
        linhas = ["(Todas)"] + sorted(df["linha_prox"].dropna().unique().tolist())

        estacao_sel = st.sidebar.selectbox("Estación más próxima", estacoes)
        linha_sel = st.sidebar.selectbox("Línea más próxima", linhas)

        df_filtrado = df.copy()

        if estacao_sel != "(Todas)":
            df_filtrado = df_filtrado[df_filtrado["estacao_prox"] == estacao_sel]

        if linha_sel != "(Todas)":
            df_filtrado = df_filtrado[df_filtrado["linha_prox"] == linha_sel]

        # Actualizamos el df que usa el dashboard
        self.df = df_filtrado

        st.sidebar.write(f"Total de registros: {len(self.df)}")

    # ------------------------
    # Método principal
    # ------------------------
    def render(self):
        st.title("Dashboard Inmobiliario")

        # Filtros (modifican self.df)
        if {"estacao_prox", "linha_prox"}.issubset(self.df.columns):
            self.render_filters()

        # Secciones principales
        self.render_kpis()
        self.render_exploratory_charts()


# ------------------------
# Uso en app.py
# ------------------------
# Guarda este archivo como app.py, por ejemplo,
# y ejecuta: streamlit run app.py

#if __name__ == "__main__":
    # Aquí cargas tu df:
    # df = pd.read_csv("tus_datos.csv")
    # Para el ejemplo, simplemente creamos uno vacío:
    # df = pd.read_csv("datos_inmuebles.csv")

    # Ejemplo: si ya tienes df en otro archivo, solo lo importas
    # from datos import df

    #df = pd.read_csv("tus_datos.csv")  # ajusta ruta

    #st.set_page_config(page_title="Dashboard Inmobiliario", layout="wide")

    #dashboard = ImoveisDashboard(df)
    #dashboard.render()
