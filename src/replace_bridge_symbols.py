from md2pdf.core import md2pdf

# Define the replacement symbols
symbols = {
  "!C": "<font color=green class=club>&clubs;</font>", 
  "!D": "<font color=orange class=diam>&diams;</font>", 
  "!H": "<font color=red class=heart>&hearts;</font>", 
  "!S": "<font color=blue class=spade>&spades;</font>",
  "!M": "<font color=magenta class=major>M</font>",
  "!m": "<font color=grassgreen class=minor>m</font>"
}

filename = "Kevin-Zach"
# Open the file in read and write mode
with open(f"src/{filename}.md", "r+") as file:
  # Read the input string from the file
  input_string = file.read()

  # Loop through the symbols and replace them in the input string
  for key, value in symbols.items():
    input_string = input_string.replace(key, value)

  # Move the file pointer to the beginning of the file
  # file.seek(0)

  # Write the output string to the file
  # with open(f"src/System Card {filename}.md", "w") as output:
  #   output.write(input_string)
  
  md2pdf(f"System Card {filename}.pdf",
        md_content=input_string,
        css_file_path="src/markdownhere.css")
