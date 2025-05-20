# app.py
from flask import Flask, render_template, request, send_file, abort, Response, url_for
import io, os, glob

app = Flask(__name__)
processed_files = {}

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

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    global processed_files
    processed_files.clear()
    files = request.files.getlist('files[]')
    for f in files:
        content = f.read().decode('utf-8')
        processed_files[f.filename] = mapping_table(content)
    return render_template('results.html', files=processed_files)

@app.route('/download/<path:filename>')
def download(filename):
    if filename not in processed_files:
        abort(404)
    data = processed_files[filename]
    return Response(
        data,
        mimetype='text/plain',
        headers={'Content-Disposition': f'attachment; filename="{filename}"'}
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# templates/index.html
# <!DOCTYPE html>
# <html>
#   <head><meta charset="utf-8"><title>PUA Handling System</title></head>
#   <body>
#     <h1>PUA Handling System for Old Church Slavonic</h1>
#     <p>Select a folder of .txt files to convert:</p>
#     <form action="/convert" method="post" enctype="multipart/form-data">
#       <input type="file" name="files[]" webkitdirectory directory multiple>
#       <br><br>
#       <button type="submit">Convert Folder</button>
#     </form>
#   </body>
# </html>

# templates/results.html
# <!DOCTYPE html>
# <html>
#   <head><meta charset="utf-8"><title>Conversion Results</title></head>
#   <body>
#     <h1>Conversion Results</h1>
#     {% for name, content in files.items() %}
#       <h2>{{ name }}</h2>
#       <textarea rows="10" cols="80" readonly>{{ content }}</textarea><br>
#       <a href="{{ url_for('download', filename=name) }}">Download {{ name }}</a>
#       <hr>
#     {% endfor %}
#   </body>
# </html>
