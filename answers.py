import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import math


# =========================================================
# FUNÇÃO AUXILIAR
# =========================================================

def create_km_class(km_driven):
    return math.ceil(km_driven / 5000)


# =========================================================
# PRIMEIRA RODADA
# =========================================================

def rd1_question_1(df):
    st.subheader("1. Quantas motos temos no dataset?")
    st.metric("Total de Motos", df.shape[0])


def rd1_question_2(df):
    st.subheader("2. Ano da moto mais antiga")
    st.write(df["year"].min())


def rd1_question_3(df):
    st.subheader("3. Ano da moto mais nova")
    st.write(df["year"].max())


def rd1_question_4(df):
    st.subheader("4. Valor da moto mais cara")
    st.write(f"U$ {df['selling_price'].max():,.2f}")


def rd1_question_5(df):
    st.subheader("5. Maior quilometragem")
    st.write(f"{df['km_driven'].max():,.0f} Km")


def rd1_question_6(df):
    st.subheader("6. Menor quilometragem")
    st.write(f"{df['km_driven'].min():,.0f} Km")


def rd1_question_7(df):
    st.subheader("7. Maior valor ex_showroom_price")
    st.write(f"U$ {df['ex_showroom_price'].max():,.2f}")


def rd1_question_8(df):
    st.subheader("8. Menor valor ex_showroom_price")
    st.write(f"U$ {df['ex_showroom_price'].min():,.2f}")


def rd1_question_9(df):
    st.subheader("9. Quantidade por tipo de vendedor")

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
    st.write(f"U$ {df['selling_price'].mean():,.2f}")


def rd1_question_11(df):
    st.subheader("11. Média de ano")
    st.write(round(df["year"].mean()))


def rd1_question_12(df):
    st.subheader("12. Média de quilometragem")
    st.write(f"{df['km_driven'].mean():,.2f} Km")


def rd1_question_13(df):
    st.subheader("13. Motos de único dono")
    total = df[df["owner"] == "1st owner"].shape[0]
    st.metric("Quantidade", total)


def rd1_question_14(df):
    st.subheader("14. Quilometragem vs Preço")

    df["km_class"] = df["km_driven"].apply(create_km_class)

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

    grouped = df.groupby("owner")["selling_price"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="owner", y="selling_price", ax=ax)

    st.pyplot(fig)


def rd2_question_2(df):
    st.subheader("2. Quilometragem média por tipo de dono")

    grouped = df.groupby("owner")["km_driven"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="owner", y="km_driven", ax=ax)

    st.pyplot(fig)


def rd2_question_3(df):
    st.subheader("3. Idade média por tipo de dono")

    grouped = df.groupby("owner")["age"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="owner", y="age", ax=ax)

    st.pyplot(fig)


def rd2_question_4(df):
    st.subheader("4. Preço médio por tipo de vendedor")

    grouped = df.groupby("seller_type")["selling_price"].mean().reset_index()

    fig, ax = plt.subplots()
    sns.barplot(data=grouped, x="seller_type", y="selling_price", ax=ax)

    st.pyplot(fig)


def rd2_question_7(df):
    st.subheader("7. Fabricantes com mais motos")

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

    grouped = (
        df.groupby("company")["selling_price"]
        .mean()
        .reset_index()
        .sort_values("selling_price", ascending=False)
    )

    st.dataframe(grouped.head(10))


def rd3_question_7(df):
    st.subheader("7. Motos recomendadas para compra")

    df_selected = df.loc[
        (df["age"] <= 3) &
        (df["km_driven"] <= 40000) &
        (df["owner"] == "1st owner") &
        (df["seller_type"] == "Individual") &
        (df["selling_price"] < df["ex_showroom_price"]),
        ["name", "selling_price", "km_driven", "year"]
    ].sort_values("selling_price", ascending=False)

    st.dataframe(df_selected)

    st.download_button(
        label="📥 Baixar Relatório CSV",
        data=df_selected.to_csv(index=False),
        file_name="bikes_selected.csv",
        mime="text/csv"
    )