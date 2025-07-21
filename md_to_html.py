import re

def markdown_to_html(markdown_text):
    """
    Converts a markdown string to an HTML string.
    """
    lines = markdown_text.split('\n')
    html_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Code blocks
        if line.startswith('```'):
            code_block_content = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code_block_content.append(lines[i])
                i += 1
            html_lines.append('<pre><code>' + '\n'.join(code_block_content) + '</code></pre>')
            i += 1
            continue

        # Headings
        if line.startswith('#'):
            level = len(line.split(' ')[0])
            content = line[level:].strip()
            html_lines.append(f'<h{level}>{content}</h{level}>')
            i += 1
            continue

        # Bullet points
        if line.startswith('* ') or line.startswith('- '):
            html_lines.append('<ul>')
            while i < len(lines) and (lines[i].startswith('* ') or lines[i].startswith('- ')):
                html_lines.append(f'<li>{lines[i][2:].strip()}</li>')
                i += 1
            html_lines.append('</ul>')
            continue

        # Paragraphs
        if line.strip():
            html_lines.append(f'<p>{line.strip()}</p>')
        
        i += 1

    html_content = '\n'.join(html_lines)
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Markdown</title>
<style>
    body {{
        font-family: sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: #111;
    }}
    pre {{
        background: #f4f4f4;
        padding: 10px;
        border-radius: 5px;
        overflow-x: auto;
    }}
    code {{
        font-family: monospace;
    }}
    ul {{
        padding-left: 20px;
    }}
</style>
</head>
<body>
{html_content}
</body>
</html>
""".replace('{', '{{').replace('}', '}}').replace('{{html_content}}', '{html_content}')