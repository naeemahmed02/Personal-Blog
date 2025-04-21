import re
from bs4 import BeautifulSoup

def slugify(text):
    # Remove emojis and special characters
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace whitespace with hyphens and make lowercase
    return re.sub(r'[\s]+', '-', text.strip().lower())

def generate_toc_and_content(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    toc = []

    for tag in soup.find_all(['h2', 'h3']):
        if not tag.get('id'):
            tag_id = slugify(tag.text)
            tag['id'] = tag_id
        toc.append({
            'level': tag.name,
            'title': tag.text,
            'id': tag['id']
        })

    return {
        'content': str(soup),
        'toc': toc
    }


def validate_passwords(password, confirm_password, min_length=8):
    """
    Validates that:
    - Both passwords match
    - Password is strong: min length, uppercase, lowercase, digit, special character
    returns (bool, message)
    """

    if password != confirm_password:
        return False, "Passwod do not match."
    
    if len(password) < min_length:
        return False, f"Password must be at least {min_length} characters long."
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    
    return True, "Password is valid."