import qrcode
from qrcode.image.pure import PyPNGImage
import sys

def create_phishing_qr(site_url: str, output_file: str = "phishing_qr.png") -> None:
    """
    Generates a QR code image that encodes the given URL.

    Args:
        site_url (str): The URL to encode in the QR code.
        output_file (str): Filename to save the QR code image (default: phishing_qr.png).

    Raises:
        ValueError: If the site_url is empty or invalid.
        IOError: If the file cannot be written.
    """
    if not site_url.strip():
        raise ValueError("URL cannot be empty.")

    try:
        img = qrcode.make(site_url, image_factory=PyPNGImage)
        with open(output_file, "wb") as f:
            img.save(f)
        print(f"[+] QR code successfully saved as '{output_file}'")
    except Exception as e:
        print(f"[!] Failed to create QR code: {e}")
        sys.exit(1)

def main():
    try:
        url = input("Enter the phishing URL to embed in the QR code: ").strip()
        create_phishing_qr(url)
    except ValueError as ve:
        print(f"[!] Input error: {ve}")
    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
