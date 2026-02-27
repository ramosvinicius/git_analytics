import streamlit as st
import answers as asw
from extraction import load_data

# ---------------------------------------------------
# Configuração da página
# ---------------------------------------------------
st.set_page_config(
    page_title="Kobe Bikes - Business Analysis",
    layout="wide"
)

# ---------------------------------------------------
# Seção de visualização do Dataset
# ---------------------------------------------------
def create_dataframe_section(df):

    st.title("🏍️ Kobe Bikes - Dataset Overview")

    col_1, col_2 = st.columns(2)

    with col_1:
        st.subheader("📊 Database")
        st.dataframe(df, height=500)

    with col_2:
        st.subheader("📘 Data Description")

        st.markdown("""
        | Coluna | Descrição |
        |:-------|:-----------|
        | id | Identificador da linha |
        | name | Fabricante e Modelo |
        | selling_price | Preço de Venda |
        | year | Ano de Fabricação |
        | seller_type | Individual ou Dealer |
        | owner | Número de donos |
        | km_driven | Quilometragem total |
        | ex_showroom_price | Preço sem taxas |
        | age | Idade da moto |
        | km_class | Classe por km |
        | km_per_year | Km por ano |
        | km_per_month | Km por mês |
        | company | Fabricante |
        """)

# ---------------------------------------------------
# Seção das Perguntas com 3 Abas
# ---------------------------------------------------
def create_answers_section(df):

    st.title("📈 Business Questions")

    tab1, tab2, tab3 = st.tabs([
        "🔹 Primeira Rodada",
        "🔹 Segunda Rodada",
        "🔹 Terceira Rodada"
    ])

    # ====================================================
    # PRIMEIRA RODADA
    # ====================================================
    with tab1:
        st.header("Primeira Rodada")

        asw.rd1_question_1(df)
        asw.rd1_question_2(df)
        asw.rd1_question_3(df)
        asw.rd1_question_4(df)
        asw.rd1_question_5(df)
        asw.rd1_question_6(df)
        asw.rd1_question_7(df)
        asw.rd1_question_8(df)
        asw.rd1_question_9(df)
        asw.rd1_question_10(df)
        asw.rd1_question_11(df)
        asw.rd1_question_12(df)
        asw.rd1_question_13(df)
        asw.rd1_question_14(df)

    # ====================================================
    # SEGUNDA RODADA
    # ====================================================
    with tab2:
        st.header("Segunda Rodada")

        asw.rd2_question_1(df)
        asw.rd2_question_2(df)
        asw.rd2_question_3(df)
        asw.rd2_question_4(df)
        asw.rd2_question_7(df)

    # ====================================================
    # TERCEIRA RODADA
    # ====================================================
    with tab3:
        st.header("Terceira Rodada")

        asw.rd3_question_2(df)
        asw.rd3_question_7(df)


# ---------------------------------------------------
# Função Principal
# ---------------------------------------------------
def main():

    df = load_data()

    create_dataframe_section(df)

    st.divider()

    create_answers_section(df)


if __name__ == "__main__":
    main()