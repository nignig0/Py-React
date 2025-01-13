from index import Tag

class P(Tag):
    def __init__(self, text, id=None, className=None, children = []):
        super.__init__('Paragraph', 'html Paragraph tag')
        self.id = id
        self.className = className
        self.children = children
    
    def render(self):
        content = ''
        for child in self.children:
            if child.isinstance(Tag):
                content+=child.render()
            else:
                content+=child
        return f""" <p id= {self.id if self.id else ''} class = {self.className if self.ClassName else ''}> {content} </p>"""