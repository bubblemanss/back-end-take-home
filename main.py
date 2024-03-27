from markdownToHTML import core

filename = 'sample'
markdownToHTML = core.MarkdownToHTML()
with open(f'back-end-take-home/resources/input/{filename}.md') as file:
    for line in file:
        markdownToHTML.addMarkdown(line)

with open(f'back-end-take-home/resources/output/{filename}.html', 'wb') as f:
    f.write(markdownToHTML.toBytes())