import unittest
from md_to_html import markdown_to_html

class TestMarkdownToHtml(unittest.TestCase):

    def test_renderer(self):
        with open('test.md', 'r') as f:
            markdown = f.read()
        
        html = markdown_to_html(markdown)

        self.assertIn('<h1>This is a heading</h1>', html)
        self.assertIn('<p>This is a paragraph.</p>', html)
        self.assertIn('<ul>', html)
        self.assertIn('<li>list item 1</li>', html)
        self.assertIn('<li>list item 2</li>', html)
        self.assertIn('</ul>', html)
        self.assertIn('<pre><code>this is a\ncode block</code></pre>', html)

if __name__ == '__main__':
    unittest.main()
