from flask import Flask, render_template, request
from temp import *

app = Flask('NetArt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        image = request.files['image']
        ascii_str = convert_image_to_ascii(image)
        ascii_json = json.dumps({"ascii_str": ascii_str})
        ascii_dict = json.loads(ascii_json)
        return render_template('index.html', ascii_dict=ascii_dict)