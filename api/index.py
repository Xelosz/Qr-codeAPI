print("starting")
import io
import qrcode
from flask import Flask, make_response

app = Flask(__name__)

@app.route("/qr/<path:url>")
def qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    with io.BytesIO() as output:
        img.save(output, format='PNG')
        output.seek(0)
        data = output.read()

    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'attachment; filename=qr_code.png'
    return response

if __name__ == "__main__":
    app.run()