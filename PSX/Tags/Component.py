class Component():
    def __init__(self, name=None, description=None, children = []):
        self.name = name
        self.description = description
        self.children = children
    
    def render(self):
        content = ''
        for child in self.children:
            if isinstance(child, Component):
                content+=child.render()
            else:
                content+=child
        return content