import streamlit as st

def mapping_table(text):
    replacements = {
        '': 'и',
        '': '҃',
        '': '҃',
        '': 'ч',
        '': 'ѥ',
        '': 'н',
        '': '҇',
        '': '҃',
        '': '~',
        '': 'ⷦ҇',
        '': ' ⷮ',
        '': '҆̀',
        '': '҆̀',
        '': 'ⷹ',
        '': 'ч',
        '': 'ⷹ',
        '': ':',
        '': 'Чⷹ',
        '': 'о',
        '': 'с',
        '': 'е',
        '': '͠',
        '': '·̀',
        '': '·̀',
        'ⷭⷭ': '҇',
        '': '҇',
        '': '҆',
        '': 'ⷩ',
        '': 'ꙶ',
        '': 'оу',
        '': 'ꙁ',
        '': 'ⷿ',
        '': 'ⷿ',
        '': 'ѧ',
        ' ': 'с',
        '': 'ѱ',
        '': 'ѥ',
        '': 'р҃',
        '꙳': 'у',
        '꙯': '҃',
        '': '͡',
        '': '͠',
        'ъ': 'уъ',
        '': 'у',
        'ⷣ': 'ⷣ͡',
        'ⷮ': 'ⷣ͡',
        'ⷯ': '̈͠',
        '': '',
        '': 'ꙩ́',
        'ѧ': 'уѧ',
        '': '҆',
        '': '',
        '': 'Ю',
        '': 'ꙅ',
        'ⷤ': '',
    }
    for old_char, new_char in replacements.items():
        text = text.replace(old_char, new_char)
    return text

st.set_page_config(layout="wide", page_title="PUA Handling System for OCS")

st.title("PUA Handling System for Old Church Slavonic")

st.write("Please select your desired option to convert text:")
db = st.selectbox("", ["Cyrillomethodiana", "database 2", "database 3"], key="db_select")

st.markdown(
    "<div style='font-weight:bold; font-size:16px;'>"
    "Welcome to the PUA Handling System for the Conversion of Text Corpora in Old Church Slavonic"
    "</div>",
    unsafe_allow_html=True
)

st.write("Paste your text below:")
input_text = st.text_area("Input Text", height=200, key="input_text_area")
if st.button("Submit", key="submit_button"):
    if db != "Cyrillomethodiana":
        st.info("Work in progress for the selected database.")
    else:
        st.write("Processed Text:")
        st.text_area("Output Text", mapping_table(input_text), height=200, key="output_text_area")

st.markdown("---")

st.write("Convert an entire folder of text files (select all .txt files at once):")

uploaded_files = st.file_uploader(
    "Select .txt files", 
    type="txt", 
    accept_multiple_files=True, 
    key="file_uploader"
)

if st.button("Select Folder and Process", key="folder_process_button"):
    if db != "Cyrillomethodiana":
        st.info("Work in progress for the selected database.")
    elif not uploaded_files:
        st.warning("Please select one or more .txt files.")
    else:
        for idx, f in enumerate(uploaded_files):
            text = f.read().decode("utf-8")
            mapped = mapping_table(text)
            st.write(f"**{f.name}**")
            st.download_button(
                label="Download Processed File",
                data=mapped,
                file_name=f.name,
                mime="text/plain",
                key=f"download_{idx}"
            )
