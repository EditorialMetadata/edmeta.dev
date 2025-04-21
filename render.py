import markdown
from jinja2 import Environment, FileSystemLoader
import os

def render_markdown_to_html(markdown_files, template_path, output_path):
    """
    Renders a dictionary of markdown files into a Jinja template.

    Args:
        markdown_files (dict): A dictionary where keys are output file names and values are paths to markdown files.
        template_path (str): Path to the Jinja template file.
        output_path (str): Path to the directory where HTML files will be saved.
    """

    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path))) 
    template = env.get_template(os.path.basename(template_path))

    for output_filename, markdown_filepath in markdown_files.items():
        with open(markdown_filepath, 'r') as f:
            markdown_content = f.read()

        # Remove the front matter if present
        if markdown_content.startswith('---'):
            end_of_front_matter = markdown_content.find('---', 3) + 3
            markdown_content = markdown_content[end_of_front_matter:].strip()

        # Enable common markdown extensions including tables and fenced code blocks
        html_content = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code', 'codehilite', 'toc'])

        # Render the HTML content using the Jinja template
        rendered_html = template.render(content=html_content)

        with open(os.path.join(output_path, output_filename), 'w') as f:
            f.write(rendered_html)

# Example usage (you would replace this with your actual data):
if __name__ == "__main__":
    markdown_files = {
        "index.html": "content/index.md",
    }
    template_path = "templates/base.html"
    output_path = "output"

    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    render_markdown_to_html(markdown_files, template_path, output_path)
