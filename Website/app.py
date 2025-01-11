from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/download-page')
def download_page():
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True)
