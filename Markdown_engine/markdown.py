import markdown

with open('markdown.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('markdown.html', 'w') as f:
    f.write(html)