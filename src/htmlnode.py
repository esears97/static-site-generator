class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = {}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props is None:
            return ""
        string = ""
        for prop in self.props:
            string += f' {prop}="{self.props[prop]}"'
        return string

    def __repr__(self):
        return f"TAG={self.tag} VALUE={self.value} CHILDREN={children} PROPS={props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = {}):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError("value cannot be None")
        if self.tag is None:
            return f"{self.value}"
        else:
          return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
