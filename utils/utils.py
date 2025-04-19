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

    for tag in soup.find_all(['h2']):
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
