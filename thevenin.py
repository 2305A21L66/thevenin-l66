import streamlit as st
st.title("Thevenin's Theorem - 2305A21L166")

def output(vth,rth,rl):
    il=vth/(rth+rl)
    pl=il*il*rl
    return il,pl
tab1,tab2=st.tabs(["Compute","Explain"])
with tab1:
    col1,col2=st.columns(2)
    with col1:
        with st.container(border=True):
            vth=st.number_input("Vth (V)", value=10)
            rth=st.number_input("Rth (Ohms)", value=100)
            rl=st.number_input("Rl (Ohms)", value=100)
            
            compute=st.button("compute")

    with col2:
        with st.container(border=True):
            if compute:
              il,pl=output(vth,rth,rl)
              st.write(f"load current={il:.2f} A")
              st.write(f"Load Power={pl:.2f} Watts")