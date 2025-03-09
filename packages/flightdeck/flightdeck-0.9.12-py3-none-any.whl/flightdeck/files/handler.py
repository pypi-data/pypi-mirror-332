import pathlib
import .files.picture as picture
import .files.markdown as markdown

def read_file(file):
    print(f"Reading file: {file}")
    extension = pathlib.Path(file).suffix.lower()
    print("Extension:", extension)

    image = [".jpg", ".jpeg", ".png"]
    
    if extension in image:
        picture.print_image(file)
    elif extension == ".md":
        markdown.print_markdown_fancy(file)

