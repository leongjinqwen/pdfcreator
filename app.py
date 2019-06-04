import os
import subprocess
from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Why so easy</h1>'

def _get_pdfkit_config():
    if os.getenv('FLASK_ENV') == 'production':
        WKHTMLTOPDF_CMD = subprocess.Popen(
            ['which', os.environ.get(
                'WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')],
            stdout=subprocess.PIPE).communicate()[0].strip()
        return pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
    else:
        return pdfkit.configuration()

@app.route("/pdf")
def show():
    import pdfkit
    pdf = pdfkit.from_url('http://google.com',False,configuration=_get_pdfkit_config())
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f"inline; filename = hello.pdf"
    return response

if __name__ == '__main__':
   app.run()