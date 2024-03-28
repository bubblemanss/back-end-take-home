import re
from airium import Airium

class MarkdownToHTML:
    def __init__(self) -> None:
        self.a = Airium()
        self.body = []

    def addMarkdown(self, line) -> None:
        line = line.strip()
        
        # blank line
        if len(line) == 0:
            return
        
        config = {
            'func': None,
            'link': False
        }
        args = []

        # heading
        if re.match(r'(#+)\s(.*)', line):
            match = re.match(r'(#+)\s(.*)', line)

            # more than 6 #s
            n = len(match.group(1))
            heading = match.group(2).strip()
            if n > 6:
                config['func'] = self.a.p
                args = self.getNestedHTML(line, config)
            else:
                args = self.getNestedHTML(heading, config)
                if n == 6:
                    config['func'] = self.a.h6
                elif n == 5:
                    config['func'] = self.a.h5
                elif n == 4:
                    config['func'] = self.a.h4
                elif n == 3:
                    config['func'] = self.a.h3
                elif n == 2:
                    config['func'] = self.a.h2
                elif n == 1:
                    config['func'] = self.a.h1
        else:
            config['func'] = self.a.p
            args = self.getNestedHTML(line, config)

        self.body.append((args, config))

    def getNestedHTML(self, line, config):
        if re.search(r'\[(.*?)\]\((.*?)\)', line):
            config['link'] = True
            match = re.match(r'(.*)\[(.*?)\]\((.*?)\)(.*)', line)
            return {
                'start_text': match.group(1).strip(),
                'link_text': match.group(2).strip(),
                'link': match.group(3),
                'end_text': match.group(4).strip()
            }
        else:
            return {
                'text': line
            }

    def toHTMLBody(self) -> None:
        a = self.a
        for args, config in self.body:
            if config['link']:
                with config['func']():
                    a(args['start_text'])
                    with a.a(href=args['link']):
                        a(args['link_text'])
                    a(args['end_text'])
            else:
                with config['func']():
                    a(args['text'])

    def toHTML(self) -> None:
        a = self.a
        a('<!DOCTYPE html>')
        with a.html(lang="pl"):
            with a.head():
                a.meta(charset="utf-8")
                a.title(_t="Intuit Project")
            with a.body():
                self.toHTMLBody()

    def toString(self) -> str:
        self.toHTML()
        return str(self.a)
    
    def toBytes(self) -> bytes:
        self.toHTML()
        return bytes(self.a)
    
    def convert(self, line) -> str:
        self.addMarkdown(line)
        self.toHTMLBody()
        return str(self.a)
    
    def printBody(self) -> None:
        self.toHTMLBody()
        print(str(self.a))
    
    def clear(self) -> None:
        self.body = []
        self.a = Airium()
