import streamlit as st
import pandas as pd
import json
from Ask_Ollama import perguntar

#Adiciona uma logo no canto superior esquerdo
st.logo("Images/V.png", size = "large")

# titulo
st.title(" VithorIA ")

#Explicação superficial do Vithor
st.write("a VithorIA é uma AI especializada em finanças e feita para auxiliar com organização financeira, orquestrar e cumprir metas")

#coluna lateral com planilha para checagem e atualização em tempo real
tabela = pd.DataFrame(pd.read_csv('./data/transacoes.csv'))
# sidebar é pra mostrar a tabela do cliente
with st.sidebar:
    
    #transações
    df = pd.read_csv('./data/transacoes.csv')

    #Agrupa por data e separa 'entrada' e 'saida' em colunas
    df_chart = df.pivot_table(
        index='data',       # Eixo X será a data
        columns='tipo',     # Cria uma coluna para 'entrada' e uma para 'saida'
        values='valor',     # Soma dos valores
        aggfunc='sum'
    ).fillna(0)             # Preenche dias sem movimentação com 0

    # Exibe o gráfico no Streamlit
    st.subheader("📈 Fluxo Entradas e saidas")
    st.line_chart(df_chart)

    #editor da tabela
    edited_df = st.data_editor(tabela, num_rows="dynamic", height=600)
    button = st.button("Atualizar planilha")
    if button:
        edited_df.to_csv('./data/transacoes.csv', index=False)
        st.toast(body="salvo",icon="🔥")
        st.rerun()

# Botão popover  
CAMINHO_PERFIL = "./data/perfil_investidor.json"
CAMINHO_CSV = "./data/transacoes.csv"

with open(CAMINHO_PERFIL, "r", encoding="utf-8") as f:
    perfil_data = json.load(f)


with st.popover("⚙️ Editar Perfil & Metas", use_container_width=True):
    st.subheader("Dados Pessoais")
    novo_nome = st.text_input("Nome", value=perfil_data["nome"])
    nova_renda = st.number_input("Renda Mensal", value=float(perfil_data["renda_mensal"]))
    
    if st.button("Salvar Dados Pessoais"):
        perfil_data["nome"] = novo_nome
        perfil_data["renda_mensal"] = nova_renda
        
        # Grava de volta no JSON
        with open(CAMINHO_PERFIL, "w", encoding="utf-8") as f:
            json.dump(perfil_data, f, ensure_ascii=False, indent=2)
            
        st.toast("Dados pessoais salvos!", icon="✅")
        st.rerun()

    st.divider()

    st.subheader("Metas Financeiras")
    metas_editadas = st.data_editor(perfil_data["metas"], num_rows="dynamic")
    
    if st.button("Salvar Metas"):
        perfil_data["metas"] = metas_editadas
        
        # Grava de volta no JSON
        with open(CAMINHO_PERFIL, "w", encoding="utf-8") as f:
            json.dump(perfil_data, f, ensure_ascii=False, indent=2)
            
        st.toast("Metas salvas!", icon="✅")
        st.rerun()

# historico de mensagem
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant" ,
            "avatar": "./Images/VithorIA.jpg",
            "content": '''
             Olá, como vai? sou a VithorIA, sua assistente Financeira em AI e osso. Como posso lhe auxiliar hoje?
             
             - Me mande seu historico de transações desse mês e posso categoriza-los 
             - Me diga uma meta e um prazo para cumpri-la e posso te auxiliar a formular o plano para tal
             - Me diga quanto gostaria de economizar por mês e posso te auxiliar com seus gastos
             
             Como começamos?''' 
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message["avatar"]):
        st.markdown(message["content"])

#Entrada do Usuario

if entrada := st.chat_input("Converse com o Vithor"):

    st.session_state.messages.append(
        {"role": "user", "content": entrada, "avatar": "user"}
    )

    with st.chat_message(name="Usuario", avatar="user"):
        st.markdown(entrada)

    with st.spinner("..."):
        resposta = perguntar(entrada)

    st.session_state.messages.append(
        {"role": "assistant", "content": resposta, "avatar": "./Images/VithorIA.jpg"}
    )        
    
    with st.chat_message(name="VithorIA", avatar="./Images/VithorIA.jpg"):
        st.markdown(resposta)


        




