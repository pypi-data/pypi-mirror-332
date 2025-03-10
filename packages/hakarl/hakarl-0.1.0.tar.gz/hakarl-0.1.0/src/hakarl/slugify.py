import re
import unicodedata


def slugify(text):
    # Convert to lowercase
    text = text.lower()

    # Convert accented characters to ASCII equivalents
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])

    # Replace spaces with hyphens
    text = text.replace(' ', '-')

    # Remove all non-alphanumeric characters (except hyphens)
    text = re.sub(r'[^\w\-]', '', text)

    # Replace multiple consecutive hyphens with a single hyphen
    text = re.sub(r'-+', '-', text)

    # Remove leading and trailing hyphens
    text = text.strip('-')

    return text
