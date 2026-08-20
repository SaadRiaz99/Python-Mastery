import string
import random
from datetime import datetime


THEMES = {
    "royal": {
        "id": "royal",
        "name": "Royal Pakistani",
        "description": "Deep maroon with gold Mughal-inspired royal elegance",
        "colors": {
            "primary": "#5B0E1A",
            "secondary": "#8B1A2B",
            "accent": "#D4A843",
            "background": "#3D0A10",
            "text": "#F5E6D0",
            "cardBg": "rgba(91, 14, 26, 0.95)",
            "gradient": "linear-gradient(135deg, #3D0A10 0%, #5B0E1A 30%, #8B1A2B 60%, #D4A843 100%)",
        },
    },
    "modern": {
        "id": "modern",
        "name": "Modern Elegant",
        "description": "Ivory and champagne with clean modern luxury",
        "colors": {
            "primary": "#C9B99A",
            "secondary": "#E8DCC8",
            "accent": "#B8963E",
            "background": "#FAF8F5",
            "text": "#3A3530",
            "cardBg": "rgba(255, 255, 255, 0.98)",
            "gradient": "linear-gradient(135deg, #FAF8F5 0%, #E8DCC8 50%, #C9B99A 100%)",
        },
    },
    "mehndi": {
        "id": "mehndi",
        "name": "Mehndi Celebration",
        "description": "Emerald green and yellow with traditional Pakistani floral patterns",
        "colors": {
            "primary": "#0D5E2E",
            "secondary": "#1A7A42",
            "accent": "#E8B830",
            "background": "#F0FDF4",
            "text": "#0A3D1C",
            "cardBg": "rgba(255, 255, 255, 0.95)",
            "gradient": "linear-gradient(135deg, #0D5E2E 0%, #1A7A42 50%, #E8B830 100%)",
        },
    },
    "barat": {
        "id": "barat",
        "name": "Barat (Legacy)",
        "description": "Deep maroon with luxury gold",
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
        "name": "Nikah (Legacy)",
        "description": "Ivory and white minimalism",
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
        "name": "Walima (Legacy)",
        "description": "Purple pastel luxury",
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


CARD_DESIGNS = ["royal", "modern", "mehndi"]

DESIGN_TEMPLATE_MAP = {
    "royal": "invite_royal.html",
    "modern": "invite_modern.html",
    "mehndi": "invite_mehndi.html",
    "barat": "invite_royal.html",
    "nikah": "invite_modern.html",
    "walima": "invite_mehndi.html",
}


def get_theme(theme_id: str) -> dict:
    return THEMES.get(theme_id, THEMES["royal"])


def get_template_for_theme(theme_id: str) -> str:
    return DESIGN_TEMPLATE_MAP.get(theme_id, "invite_royal.html")


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
