import streamlit as st
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Elementos
elementos = ["Fogo", "Terra", "Vento", "Agua"]
ganha_de = {
    "Fogo": "Terra",
    "Terra": "Vento",
    "Vento": "Agua",
    "Agua": "Fogo"
}
elemento_cod = {e: i for i, e in enumerate(elementos)}
cod_elemento = {i: e for e, i in elemento_cod.items()}

# Caminho do CSV
csv_path = "partidas.csv"

# Carrega ou cria base
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=["meu_1", "meu_2", "oponente_1", "oponente_2", "escolha_oponente"])

# --- Função de treino ---
def treinar_modelo(df):
    if len(df) < 5:
        return None  # Evita treinar com pouquíssimos dados
    X = df[["meu_1", "meu_2", "oponente_1", "oponente_2"]]
    y = df["escolha_oponente"]
    modelo = RandomForestClassifier(random_state=42, 
                                n_estimators=1100, 
                                n_jobs=-1, 
                                min_samples_leaf=2)
    modelo.fit(X, y)
    return modelo

# --- Inicializa estados ---
if "meus" not in st.session_state:
    st.session_state.meus = []
if "oponente" not in st.session_state:
    st.session_state.oponente = []
if "real" not in st.session_state:
    st.session_state.real = None

# --- Interface ---
st.set_page_config(page_title="Previsão de jogada", layout="centered")
st.title("🔥 Previsão de Elementos com ML (Aprendizado Contínuo)")

# Seletor dos elementos
st.session_state.meus = st.multiselect("Escolha seus dois elementos:", elementos, default=st.session_state.meus, max_selections=2)
st.session_state.oponente = st.multiselect("Escolha os dois elementos do oponente:", elementos, default=st.session_state.oponente, max_selections=2)

if len(st.session_state.meus) == 2 and len(st.session_state.oponente) == 2:
    modelo = treinar_modelo(df)
    entrada = [[
        elemento_cod[st.session_state.meus[0]],
        elemento_cod[st.session_state.meus[1]],
        elemento_cod[st.session_state.oponente[0]],
        elemento_cod[st.session_state.oponente[1]],
    ]]

    if modelo:
        pred = modelo.predict(entrada)[0]
        previsao = cod_elemento[pred]
        st.success(f"🎯 Oponente provavelmente escolherá: **{previsao}**")
        op_derrotado_por = [k for k, v in ganha_de.items() if v == previsao]
        melhores = [e for e in st.session_state.meus if e in op_derrotado_por]
        if melhores:
            st.info(f"✅ Sugestão: Jogue com **{melhores[0]}**")
        else:
            st.warning("⚠️ Nenhum dos seus elementos vence o previsto.")
    else:
        st.warning("⚠️ Modelo ainda está aprendendo. Registre mais partidas.")

    # Escolha real do oponente
    st.session_state.real = st.selectbox(
        "Agora selecione o que o oponente REALMENTE escolheu:",
        st.session_state.oponente,
        index=0 if st.session_state.real is None else st.session_state.oponente.index(st.session_state.real)
    )

    if st.button("✅ Registrar partida"):
        nova_linha = {
            "meu_1": elemento_cod[st.session_state.meus[0]],
            "meu_2": elemento_cod[st.session_state.meus[1]],
            "oponente_1": elemento_cod[st.session_state.oponente[0]],
            "oponente_2": elemento_cod[st.session_state.oponente[1]],
            "escolha_oponente": elemento_cod[st.session_state.real]
        }
        df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("🎉 Partida registrada com sucesso! O modelo foi atualizado.")

        # Limpa os campos
        st.session_state.meus = []
        st.session_state.oponente = []
        st.session_state.real = None
        st.rerun()
else:
    st.info("Selecione exatamente 2 elementos seus e 2 do oponente para continuar.")