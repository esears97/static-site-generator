from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, node2):
        text_eq = self.text == node2.text
        text_type_eq = self.text_type == node2.text_type
        url_eq = self.url == node2.url
        return (text_eq and text_type_eq and url_eq)
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}"
