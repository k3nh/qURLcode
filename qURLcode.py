import qrcode
import sys
from io import BytesIO
from qrcode.image.svg import SvgPathImage

def generate_qr_code(url, file_name):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image (PNG)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"{file_name}.png")

    # Save as SVG
    qr_svg = qrcode.make(url, image_factory=SvgPathImage)
    svg_buffer = BytesIO()
    qr_svg.save(svg_buffer)
    with open(f"{file_name}.svg", 'wb') as f:
        f.write(svg_buffer.getvalue())

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python generate_qr.py")
        sys.exit(1)
    
    url = input("Enter the URL: ")
    file_name = input("Enter the output file name (without extension): ")
    generate_qr_code(url, file_name)

