from flask import Flask, Response
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/qr/<string:data>')
def qr_code(data):
    # génération du QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    response = Response(img_io.getvalue(), content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='QR-Code.png')
    return response

if __name__ == "__main__":
    app.run(debug=True)
