import streamlit as st
import zipfile
import io

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
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

st.set_page_config(layout="wide", page_title="PUA Handling System")
st.title("PUA Handling System for Old Church Slavonic")
db = st.selectbox("Please select your desired option to convert text:", ["Cyrillomethodiana", "database 2", "database 3"])
st.markdown("**Welcome to the PUA Handling System for the Conversion of Text Corpora in Old Church Slavonic**")

st.write("Paste your text below:")
input_text = st.text_area("", height=200)
if st.button("Submit"):
    if db != "Cyrillomethodiana":
        st.info("Work in progress for the selected database.")
    else:
        st.write("Processed Text:")
        st.text_area("", mapping_table(input_text), height=200)

st.write("Convert multiple text files at once:")
uploaded = st.file_uploader("", type="txt", accept_multiple_files=True)
if st.button("Select Folder and Process"):
    if db != "Cyrillomethodiana":
        st.info("Work in progress for the selected database.")
    elif not uploaded:
        st.warning("Please select one or more .txt files.")
    else:
        out = io.BytesIO()
        with zipfile.ZipFile(out, "w") as z:
            for f in uploaded:
                data = f.read().decode("utf-8")
                z.writestr(f.name, mapping_table(data))
        out.seek(0)
        st.success("Files processed.")
        st.download_button("Download Processed ZIP", out.getvalue(), file_name="processed.zip")
