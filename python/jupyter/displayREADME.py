from IPython.display import display, Markdown

with open('Readme.md', 'r') as fh:
    content = fh.read()

display(Markdown(content))
