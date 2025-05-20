import streamlit as st
import os
import glob
import zipfile
import io

# ——— Your mapping logic unchanged ———
def mapping_table(text):
    replacements = {
        '': 'и',
        '': '҃',  # update
        '': '҃',
        '': 'ч',  # updated U+0447
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
        '': '',  # maslay wala
        '': 'ꙩ́',
        'ѧ': 'уѧ',
        '': '҆',
        '': '',  # maslay wala
        '': 'Ю',
        '': 'ꙅ',
        'ⷤ': '',
    }
    for old_char, new_char in replacements.items():
        text = text.replace(old_char, new_char)
    return text

def process_folder(input_folder: str, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)
    for in_path in glob.glob(os.path.join(input_folder, '*.txt')):
        with open(in_path, 'r', encoding='utf-8') as f:
            content = f.read()
        mapped = mapping_table(content)
        out_path = os.path.join(output_folder, os.path.basename(in_path))
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(mapped)

# ——— UI ———
st.set_page_config(layout="wide", page_title="PUA Handling System")

st.title("PUA Handling System for Old Church Slavonic")

st.write("Please select your desired option to convert text:")
db = st.selectbox("", ["Cyrillomethodiana", "database 2", "database 3"])

st.markdown(
    "<div style='font-weight:bold; font-size:16px;'>"
    "Welcome to the PUA Handling System for the Conversion of Text Corpora in Old Church Slavonic"
    "</div>",
    unsafe_allow_html=True
)

st.write("Paste your text below:")
input_text = st.text_area("", height=200)

if st.button("Submit"):
    if db != "Cyrillomethodiana":
        st.info("Work in progress for the selected database.")
    else:
        st.write("Processed Text:")
        st.text_area("", mapping_table(input_text), height=200)

st.write("Convert an entire folder of text files:")
# We use a ZIP upload in lieu of folder selection
uploaded_zip = st.file_uploader("", type="zip")
if st.button("Select Folder and Process"):
    if db != "Cyrillomethodiana":
        st.info("Work in progress for the selected database.")
    elif uploaded_zip is None:
        st.warning("Please upload a ZIP file of .txt files.")
    else:
        z = zipfile.ZipFile(uploaded_zip)
        out_io = io.BytesIO()
        with zipfile.ZipFile(out_io, "w") as out_zip:
            for name in z.namelist():
                if name.lower().endswith(".txt"):
                    txt = z.read(name).decode("utf-8")
                    out_zip.writestr(name, mapping_table(txt))
        st.success("Files processed.")
        st.download_button("Download Processed ZIP", out_io.getvalue(), file_name="processed.zip")
