# 🔮 API de Previsão utilizando RandomForestClassifier

Este projeto implementa uma aplicação interativa em Python que utiliza machine learning para prever a escolha do adversário em um mini game presente em Slayer Legend baseado em 4 elementos com ciclo de força:

**Fogo > Terra > Vento > Água > Fogo**

A cada partida registrada, o modelo aprende continuamente utilizando um **RandomForestClassifier** da biblioteca `scikit-learn`, e sugere a melhor jogada com base no padrão de comportamento do oponente.

A interface é construída com **Streamlit**, permitindo interações locais de forma simples e visual.

---

## ⚙️ Funcionalidades

- ✅ Registro de partidas (elementos do jogador e do oponente)
- 🤖 Previsão da jogada mais provável do adversário
- 🎯 Sugestão da jogada ideal para vencer
- 📈 Aprendizado contínuo com base no histórico salvo em `partidas.csv`
- 💻 Executável `.exe` gerado com PyInstaller para rodar localmente com duplo clique

---

## 🚀 Como executar o projeto

### 1. Instale as dependências

```bash
pip install streamlit pandas scikit-learn
```

### 2. Execute o aplicativo localmente

```bash
start_app.exe
```

O navegador será aberto automaticamente com a interface.

---

## 📁 Estrutura do projeto

```
API ML Elemental/
├── main.py          # Aplicação Streamlit com RandomForest
├── start_app.exe    # Script para iniciar o Streamlit com um clique
├── partidas.csv     # Gerado automaticamente com o histórico de jogadas
└── README.md
```

---

## 📚 Tecnologias utilizadas

- Python 3
- [Streamlit](https://streamlit.io)
- [Scikit-learn](https://scikit-learn.org)
- Pandas
- PyInstaller

---

## 📌 Autor

**Ronaldo Esteves Ianelli**  
Projeto feito com fins de estudo, aprendizado de ML e experimentação com interfaces web locais.
