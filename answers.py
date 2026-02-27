import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import math


# =========================================================
# FUNÇÃO AUXILIAR
# =========================================================

def create_km_class(km_driven):
    return math.ceil(km_driven / 5000)


def col_missing(df, col):
    """Exibe aviso e retorna True se a coluna não existir no DataFrame."""
    if col not in df.columns:
        st.warning(f"Coluna '{col}' não encontrada no dataset. Colunas disponíveis: {list(df.columns)}")
        return True
    return False


# =========================================================
# PRIMEIRA RODADA
# =========================================================

def rd1_question_1(df):
    st.subheader("1. Quantas motos temos no dataset?")
    st.metric("Total de Motos", df.shape[0])


def rd1_question_2(df):
    st.subheader("2. Ano da moto mais antiga")
    if col_missing(df, "year"): return
    st.write(df["year"].min())


def rd1_question_3(df):
    st.subheader("3. Ano da moto mais nova")
    if col_missing(df, "year"): return
    st.write(df["year"].max())


def rd1_question_4(df):
    st.subheader("4. Valor da moto mais cara")
    if col_missing(df, "selling_price"): return
    st.write(f"U$ {df['selling_price'].max():,.2f}")


def rd1_question_5(df):
    st.subheader("5. Maior quilometragem")
    if col_missing(df, "km_driven"): return
    st.write(f"{df['km_driven'].max():,.0f} Km")


def rd1_question_6(df):
    st.subheader("6. Menor quilometragem")
    if col_missing(df, "km_driven"): return
    st.write(f"{df['km_driven'].min():,.0f} Km")


def rd1_question_7(df):
    st.subheader("7. Maior valor ex_showroom_price")
    if col_missing(df, "ex_showroom_price"): return
>>>>>>> 39722dc (fix: Refactor analytics logic for improved readability and performance)
    st.write(f"U$ {df['ex_showroom_price'].max():,.2f}")


def rd1_question_8(df):
    st.subheader("8. Menor valor ex_showroom_price")
    if col_missing(df, "ex_showroom_price"): return
>>>>>>> 39722dc (fix: Refactor analytics logic for improved readability and performance)
    st.write(f"U$ {df['ex_showroom_price'].min():,.2f}")


def rd1_question_9(df):
    st.subheader("9. Quantidade por tipo de vendedor")
    if col_missing(df, "seller_type"): return

    grouped = (
        df.groupby("seller_type")["seller_type"]
        .count()
        .reset_index(name="count")
    )

    st.dataframe(grouped)

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="seller_type", y="count", ax=ax)

    st.pyplot(fig)


def rd1_question_10(df):
    st.subheader("10. Média de preço")
    if col_missing(df, "selling_price"): return
    st.write(f"U$ {df['selling_price'].mean():,.2f}")


def rd1_question_11(df):
    st.subheader("11. Média de ano")
    if col_missing(df, "year"): return
    st.write(round(df["year"].mean()))


def rd1_question_12(df):
    st.subheader("12. Média de quilometragem")
    if col_missing(df, "km_driven"): return
    st.write(f"{df['km_driven'].mean():,.2f} Km")


def rd1_question_13(df):
    st.subheader("13. Motos de único dono")
    if col_missing(df, "owner"): return
    total = df[df["owner"] == "1st owner"].shape[0]
    st.metric("Quantidade", total)


def rd1_question_14(df):
    st.subheader("14. Quilometragem vs Preço")
    if col_missing(df, "km_driven") or col_missing(df, "selling_price"): return

    df_temp = df.copy()
    df_temp["km_class"] = df_temp["km_driven"].apply(create_km_class)
>>>>>>> 39722dc (fix: Refactor analytics logic for improved readability and performance)

    grouped = (
        df.groupby("km_class")["selling_price"]
        .mean()
        .reset_index()
    )

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="km_class", y="selling_price", ax=ax)

    st.pyplot(fig)


# =========================================================
# SEGUNDA RODADA
# =========================================================

def rd2_question_1(df):
    st.subheader("1. Preço médio por tipo de dono")
    if col_missing(df, "owner") or col_missing(df, "selling_price"): return

    grouped = df.groupby("owner")["selling_price"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="owner", y="selling_price", ax=ax)

    st.pyplot(fig)


def rd2_question_2(df):
    st.subheader("2. Quilometragem média por tipo de dono")
    if col_missing(df, "owner") or col_missing(df, "km_driven"): return

    grouped = df.groupby("owner")["km_driven"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="owner", y="km_driven", ax=ax)

    st.pyplot(fig)


def rd2_question_3(df):
    st.subheader("3. Idade média por tipo de dono")
    if col_missing(df, "owner") or col_missing(df, "age"): return

    grouped = df.groupby("owner")["age"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="owner", y="age", ax=ax)

    st.pyplot(fig)


def rd2_question_4(df):
    st.subheader("4. Preço médio por tipo de vendedor")
    if col_missing(df, "seller_type") or col_missing(df, "selling_price"): return

    grouped = df.groupby("seller_type")["selling_price"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="seller_type", y="selling_price", ax=ax)

    st.pyplot(fig)


def rd2_question_7(df):
    st.subheader("7. Fabricantes com mais motos")
    if col_missing(df, "company"): return

    grouped = (
        df.groupby("company")["company"]
        .count()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    st.dataframe(grouped.head(10))


# =========================================================
# TERCEIRA RODADA
# =========================================================

def rd3_question_2(df):
    st.subheader("2. Fabricante com maior preço médio")
    if col_missing(df, "company") or col_missing(df, "selling_price"): return

    grouped = (
        df.groupby("company")["selling_price"]
        .mean()
        .reset_index()
        .sort_values("selling_price", ascending=False)
    )

    st.dataframe(grouped.head(10))


def rd3_question_7(df):
    st.subheader("7. Motos recomendadas para compra")

    required = ["age", "km_driven", "owner", "seller_type", "name", "selling_price", "year"]
    for col in required:
        if col_missing(df, col): return

    filtros = (
        (df["age"] <= 3) &
        (df["km_driven"] <= 40000) &
        (df["owner"] == "1st owner") &
        (df["seller_type"] == "Individual")
    )

    if "ex_showroom_price" in df.columns:
        filtros = filtros & (df["selling_price"] < df["ex_showroom_price"])

    colunas = ["name", "selling_price", "km_driven", "year"]

    df_selected = (
        df.loc[filtros, colunas]
        .sort_values("selling_price", ascending=False)
    )
>>>>>>> 39722dc (fix: Refactor analytics logic for improved readability and performance)

    st.dataframe(df_selected)

    st.download_button(
        label="📥 Baixar Relatório CSV",
        data=df_selected.to_csv(index=False),
        file_name="bikes_selected.csv",
        mime="text/csv"
    )
