__version__ = "0.1"
app_name = "Ask Your PDF"

import streamlit as st
import css

## setup pages


st.set_page_config(layout='centered', page_title=f'{app_name} {__version__}')
ss = st.session_state
if 'debug' not in ss: ss['debug'] = {}
st.write(f'<style>{css.v1}</style>', unsafe_allow_html=True)
header1 = st.empty()  # for errors / messages
header2 = st.empty()  # for errors / messages
header3 = st.empty()  # for errors / messages


def ui_spacer(n=2, line=False, next_n=0):
    for _ in range(n):
        st.write('')
    if line:
        st.tabs([' '])
    for _ in range(next_n):
        st.write('')


def ui_info():
    st.markdown(f"""
	# Ask Your PDF
	version {__version__}

	Question answering system built on top of GPT3.5.
	""")
    ui_spacer(1)
    st.write("Made by Fluent-QA",
             unsafe_allow_html=True)
    ui_spacer(1)
    st.markdown("""
		Thank you for your interest in this PDF application.
		""")
    ui_spacer(1)


if __name__ == '__main__':
    ui_info()
