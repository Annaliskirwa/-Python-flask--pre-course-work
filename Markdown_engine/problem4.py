# Converting markdown to HTML
# Store the markdown content in a file named markdown.md

#Create a virtual environment, activate it and install markdown.
import markdown

# Open the markdown.md file in read mode
with open('markdown.md', 'r') as f:
    # Then you store the file contents in a variable f
    text = f.read() 
    # Convert the text to html
    html = markdown.markdown(text)
# Opens a html file and writes the contents on the f variable
with open('markdown.html', 'w') as f:
    f.write(html)

#On the terminal run python3 problem4.py to run and compile with virtual env active





# Converting markdown to Latex
# Store the markdown content in a file named markdown.md

#Create a virtual environment, activate it and install markdown.
import markdown

# Open the markdown.md file in read mode
with open('markdown.md', 'r') as f:
    # Then you store the file contents in a variable f
    text = f.read() 
    # Convert the text to latex
    latex = markdown.Markdown(None, extensions=['latex'])
    latex_out = latex.convert(text)

    #Outputs the latex
    print(latex_out)

#On the terminal run python3 problem4.py to run and compile with virtual env active


