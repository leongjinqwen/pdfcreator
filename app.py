from flask import Flask, make_response
import pdfkit

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Why so easy</h1>'

@app.route("/pdf")
def show():
    pdf = pdfkit.from_url('http://google.com',False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f"inline; filename = hello.pdf"
    return response

if __name__ == '__main__':
   app.run()