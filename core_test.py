import unittest
from markdownToHTML import core

'''
Note: airium does 2 space indent by default

Doesn't handle case with additional square brackets or regular brackets in text with link
'''
class TestMarkdownToHTML(unittest.TestCase):
    def test_convert_heading1(self):
        md = core.MarkdownToHTML()
        markdown_text = "# Hello, World!"
        expected_html = "<h1>\n  Hello, World!\n</h1>"
        converted_html = md.convert(markdown_text)
        self.assertEqual(converted_html, expected_html)
    
    def test_convert_heading6(self):
        md = core.MarkdownToHTML()
        markdown_text = "###### Hello, World!"
        expected_html = "<h6>\n  Hello, World!\n</h6>"
        converted_html = md.convert(markdown_text)
        self.assertEqual(converted_html, expected_html)

    def test_convert_heading_too_many_hashtags(self):
        md = core.MarkdownToHTML()
        markdown_text = "####### Hello, World!"
        expected_html = "<p>\n  ####### Hello, World!\n</p>"
        converted_html = md.convert(markdown_text)
        self.assertEqual(converted_html, expected_html)

    def test_convert_paragraph(self):
        md = core.MarkdownToHTML()
        markdown_text = "This is a paragraph."
        expected_html = "<p>\n  This is a paragraph.\n</p>"
        converted_html = md.convert(markdown_text)
        self.assertEqual(converted_html, expected_html)
    
    def test_convert_link(self):
        md = core.MarkdownToHTML()
        markdown_text = "[Link text](https://www.example.com)"
        expected_html = '<p>\n  \n  <a href="https://www.example.com">\n    Link text\n  </a>\n  \n</p>'
        converted_html = md.convert(markdown_text)
        self.assertEqual(converted_html, expected_html)
    
    def test_convert_inline_link(self):
        md = core.MarkdownToHTML()
        markdown_text = "This is sample markdown for the [Mailchimp](https://www.mailchimp.com) homework assignment."
        expected_html = '<p>\n  This is sample markdown for the\n  <a href="https://www.mailchimp.com">\n    Mailchimp\n  </a>\n  homework assignment.\n</p>'
        converted_html = md.convert(markdown_text)
        self.assertEqual(converted_html, expected_html)
    
    def test_convert_blank_line(self):
        md = core.MarkdownToHTML()
        markdown_text = " "
        expected_html = ""
        converted_html = md.convert(markdown_text)
        self.assertEqual(converted_html, expected_html)

if __name__ == '__main__':
    unittest.main()
