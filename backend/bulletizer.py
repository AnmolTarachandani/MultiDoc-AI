import re

def convert_to_bullets(text):
    lines = text.strip().split('.')
    bullets = [line.strip() + '.' for line in lines if line.strip()]
    return bullets
