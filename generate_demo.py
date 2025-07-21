from md_to_html import markdown_to_html

with open('demo/sample.md', 'r') as f:
    markdown = f.read()

html = markdown_to_html(markdown)

with open('demo/output.html', 'w') as f:
    f.write(html)
