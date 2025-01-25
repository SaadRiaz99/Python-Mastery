import string
import random
from datetime import datetime

THEMES = {
    'royal': {'id': 'royal', 'name': 'Royal Pakistani', 'colors': {'primary': '#5B0E1A', 'accent': '#D4A843'}},
    'modern': {'id': 'modern', 'name': 'Modern Elegant', 'colors': {'primary': '#C9B99A', 'accent': '#B8963E'}},
    'mehndi': {'id': 'mehndi', 'name': 'Mehndi Celebration', 'colors': {'primary': '#0D5E2E', 'accent': '#E8B830'}},
}

CARD_DESIGNS = ['royal', 'modern', 'mehndi']
DESIGN_TEMPLATE_MAP = {'royal': 'invite_royal.html', 'modern': 'invite_modern.html', 'mehndi': 'invite_mehndi.html'}

def get_theme(theme_id):
    return THEMES.get(theme_id, THEMES['royal'])

def get_template_for_theme(theme_id):
    return DESIGN_TEMPLATE_MAP.get(theme_id, 'invite_royal.html')

def generate_slug(length=8):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=length))

def format_date(date_str):
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        return dt.strftime('%A, %B %d, %Y')
    except:
        return date_str

def format_time(time_str):
    try:
        parts = time_str.split(':')
        h = int(parts[0])
        m = parts[1] if len(parts) > 1 else '00'
        ampm = 'PM' if h >= 12 else 'AM'
        h12 = h % 12 or 12
        return f'{h12}:{m} {ampm}'
    except:
        return time_str
