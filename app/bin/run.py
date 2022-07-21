from flask import Flask, request, render_template, send_file, jsonify
import os
import base64


template_dir = '/app/html/templates'
static_dir = '/app/html/static'
app = Flask(__name__, template_folder=template_dir, static_url_path='/static', static_folder=static_dir)


@app.route('/edah_api', methods=['POST'])
def run_edah_api():
    json_list = []
    if request.method == 'POST':
        if 'filename' not in request.files:
            json_list = [{'image': 'there is no filename in form!'}]
        img = request.files['filename']
        img_string = base64.b64encode(img.read())
    json_list = [{'image': img_string.decode('utf-8')}]
    return jsonify(json_list)

@app.route('/', methods=['GET'])
def run_app():
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0', port=5555, ssl_context='adhoc')
    app.run(debug=True, host='0.0.0.0', port=15588, ssl_context=('/app/html/ssl/openaifab.com/fullchain4.pem', '/app/html/ssl/openaifab.com/privkey4.pem'))
