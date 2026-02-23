# Lets start
# heyyyy 








# import qrcode
# This imports the qrcode library, which is a Python package used to generate QR codes.

# The [pil] installs Pillow, which is required to generate image files.

# def generate_simple_qr(data, filename="simple_qr.png"):
# This defines a function named generate_simple_qr.
# Parameters:
# data → The information that will be encoded inside the QR code.
# filename="simple_qr.png" → The name of the file where the QR image will be saved.
# If no filename is provided, it defaults to "simple_qr.png".
# This makes the function reusable.
# God abeg 😭🤧


# text = "Hello"
# print(text)
# print("-" * len(text))


# Creating a QR Code Object
        # qr = qrcode.QRCode(
        #     version=1,
        #     box_size=10,
        #     border=5
        # )

# a QRCode instance:
# explanation for each parameter:

# version=1
# Controls the size of the QR code.
# Version 1 is the smallest QR code.
# QR versions range from 1 to 40.
# Higher version → more data capacity → larger QR pattern.
# If you set fit=True later (which i have done), Python can automatically adjust the version if needed.

# box_size=10
# Controls how big each square (pixel block) is.
# Larger number = bigger image.
# Does NOT affect data capacity.
# Only affects visual size.

# border=5
# Controls the thickness of the white border.
# QR codes require a white margin called the “quiet zone.”
# Minimum recommended border is 4.


# Adding Data
# ---------qr.add_data(data)--------
# This adds whatever string is passed into the function in the QR code.
# Examples: Website URL, Text, Phone number, Contact info, Contact info 
# WiFi credentials
# Any string





















import qrcode

# Simple QR code
def generate_simple_qr(data, filename="simple_qr.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    
    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")
    return img

# Example usage
generate_simple_qr("https://www.example.com", "website_qr.png")
generate_simple_qr("Contact: John Doe\nPhone: 123-456-7890", "contact_qr.png")
