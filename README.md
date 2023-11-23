# OR-Generator

Specifications:
* QR Code Version: Used the version parameter set to 1, indicating the size and data capacity of the QR code.
* Error Correction Level: Set the error correction level to qrcode.constants.ERROR_CORRECT_L to provide low error correction.
*Box Size: The box_size parameter is set to 5, determining the size of each box (pixel) in the QR code.
*Border Size: The border parameter is set to 4, defining the size of the border around the QR code.
*QR Code Data: The variable qr holds the URL for which the QR code is generated. In this example, it contains a LinkedIn profile URL.
* QR Code Generation: Uses the qrcode.QRCode class to configure the QR code with the specified parameters.
* QR Code Image Creation: The qrcode.make() function is then called with the configured QR code, and the resulting image is stored in the variable ro.
* Image Saving: The generated QR code image (ro) is saved as a JPEG file named "QR CODE.jpg" using the save() method.

HOW TO RUN:

Install the required library:

* pip install qrcode[pil]
* Modify the 'qr' variable with the desired URL.
* Run the script.
*The QR code will be generated and saved as "QR CODE.jpg" in the same directory.

Example:
For a LinkedIn profile, the script generates a QR code pointing to "https://www.linkedin.com/in/iamrohanraj/".
