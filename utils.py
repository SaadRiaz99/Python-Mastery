import string
import random
from datetime import datetime


THEMES = {
    "mehndi": {
        "id": "mehndi",
        "name": "Mehndi",
        "description": "Elegant green aesthetic with floral patterns and gold details",
        "colors": {
            "primary": "#166534",
            "secondary": "#15803d",
            "accent": "#d4a843",
            "background": "#f0fdf4",
            "text": "#14532d",
            "cardBg": "rgba(255, 255, 255, 0.95)",
            "gradient": "linear-gradient(135deg, #166534 0%, #15803d 50%, #d4a843 100%)",
        },
    },
    "barat": {
        "id": "barat",
        "name": "Barat",
        "description": "Deep maroon with luxury gold typography and royal elegance",
        "colors": {
            "primary": "#7f1d1d",
            "secondary": "#991b1b",
            "accent": "#d4a843",
            "background": "#fef2f2",
            "text": "#7f1d1d",
            "cardBg": "rgba(255, 255, 255, 0.95)",
            "gradient": "linear-gradient(135deg, #7f1d1d 0%, #991b1b 50%, #d4a843 100%)",
        },
    },
    "nikah": {
        "id": "nikah",
        "name": "Nikah",
        "description": "Ivory and white with Islamic geometric patterns, minimal and elegant",
        "colors": {
            "primary": "#1c1917",
            "secondary": "#44403c",
            "accent": "#b8860b",
            "background": "#fafaf9",
            "text": "#1c1917",
            "cardBg": "rgba(255, 255, 255, 0.98)",
            "gradient": "linear-gradient(135deg, #1c1917 0%, #44403c 50%, #b8860b 100%)",
        },
    },
    "walima": {
        "id": "walima",
        "name": "Walima",
        "description": "White and pastel aesthetic with modern luxury design",
        "colors": {
            "primary": "#5b21b6",
            "secondary": "#7c3aed",
            "accent": "#c4b5fd",
            "background": "#faf5ff",
            "text": "#3b0764",
            "cardBg": "rgba(255, 255, 255, 0.95)",
            "gradient": "linear-gradient(135deg, #5b21b6 0%, #7c3aed 50%, #c4b5fd 100%)",
        },
    },
}


def get_theme(theme_id: str) -> dict:
    return THEMES.get(theme_id, THEMES["barat"])


def generate_slug(length: int = 8) -> str:
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choices(chars, k=length))


def format_date(date_str: str) -> str:
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%A, %B %d, %Y")
    except (ValueError, TypeError):
        return date_str


def format_time(time_str: str) -> str:
    try:
        parts = time_str.split(":")
        h = int(parts[0])
        m = parts[1] if len(parts) > 1 else "00"
        ampm = "PM" if h >= 12 else "AM"
        h12 = h % 12 or 12
        return f"{h12}:{m} {ampm}"
    except (ValueError, TypeError):
        return time_str


def get_whatsapp_url(guest_name: str, contact: str, invitation_link: str) -> str:
    clean_contact = "".join(c for c in contact if c.isdigit() or c == "+")
    message = (
        f"Assalam-o-Alaikum {guest_name}!\n\n"
        f"You are warmly invited to celebrate our special day.\n\n"
        f"View your personal wedding invitation here:\n\n"
        f"{invitation_link}"
    )
    import urllib.parse
    encoded = urllib.parse.quote(message)
    return f"https://wa.me/{clean_contact}?text={encoded}"
