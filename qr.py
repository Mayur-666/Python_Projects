from qrcode.main import QRCode

qr = QRCode(version=1, box_size=20, border=5)
data = str(input("Enter any text :"))
qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')

img.save('img.png')