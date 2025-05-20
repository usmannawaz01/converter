# app.py
from flask import Flask, render_template, request, send_file
import io, zipfile
import os, glob

app = Flask(__name__)

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
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    files = request.files.getlist('files[]')
    output_stream = io.BytesIO()
    with zipfile.ZipFile(output_stream, 'w') as z:
        for f in files:
            original = f.read().decode('utf-8')
            mapped = mapping_table(original)
            z.writestr(f.filename, mapped)
    output_stream.seek(0)
    return send_file(output_stream,
                     as_attachment=True,
                     download_name='converted.zip',
                     mimetype='application/zip')

if __name__ == '__main__':
    app.run(debug=True)

# templates/index.html
# Create a folder named 'templates' alongside app.py and add this file:
#
# <!DOCTYPE html>
# <html>
#   <head>
#     <meta charset="utf-8">
#     <title>PUA Handling System for Old Church Slavonic</title>
#   </head>
#   <body>
#     <h1>PUA Handling System for Old Church Slavonic</h1>
#     <p>Please select the folder containing your .txt files:</p>
#     <form action="/convert" method="post" enctype="multipart/form-data">
#       <input type="file"
#              name="files[]"
#              webkitdirectory
#              directory
#              multiple>
#       <br><br>
#       <button type="submit">Convert Folder</button>
#     </form>
#   </body>
# </html>
