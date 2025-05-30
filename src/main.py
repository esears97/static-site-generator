from textnode import TextNode, TextType

def main():
    my_node = TextNode("hello world", TextType.NORMAL,"http://google.com")
    print(my_node)

main()
