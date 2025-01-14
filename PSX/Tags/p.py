from PSX.Tags.Component import Component

class P(Component):
    def __init__(self, text = None, id=None, className=None, children = []):
        super().__init__('Paragraph', 'html Paragraph tag', children)
        self.id = id
        self.className = className
        if text:
            self.children = [text]+self.children

    def addChild(self, childComponent):
        super().children.append(childComponent)
    
    def render(self):
        content = super().render()
        return f""" <p id= {self.id if self.id else ''} class = {self.className if self.className else ''}> {content} </p>"""