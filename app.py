import streamlit as st
import os
import glob

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

def process_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for in_path in glob.glob(os.path.join(input_folder, '*.txt')):
        with open(in_path, 'r', encoding='utf-8') as f:
            content = f.read()
        mapped = mapping_table(content)
        out_path = os.path.join(output_folder, os.path.basename(in_path))
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(mapped)

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

st.markdown("---")
st.write("Convert an entire folder of text files:")

input_folder = st.text_input("Input folder path")
output_folder = st.text_input("Output folder path")

if st.button("Select Folder and Process"):
    if db != "Cyrillomethodiana":
        st.info("Work in progress for the selected database.")
    else:
        if not input_folder or not output_folder:
            st.warning("Please specify both input and output folder paths.")
        else:
            try:
                process_folder(input_folder, output_folder)
                st.success(f"Files have been processed and saved to: {output_folder}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
