import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
    
)

qr="https://www.linkedin.com/in/iamrohanraj/"
ro=qrcode.make(qr)
ro.save("QR CODE.jpg")