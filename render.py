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

        # Remove and parse the front matter if present - this is a common pattern in markdown files
        # that use YAML front matter (e.g., Jekyll, Hugo)
        # This assumes the front matter is enclosed in triple dashes (---)
        # and is at the beginning of the file.
        if markdown_content.startswith('---'):
            end_of_front_matter = markdown_content.find('---', 3)
            if end_of_front_matter != -1:
                front_matter = markdown_content[3:end_of_front_matter].strip()
                markdown_content = markdown_content[end_of_front_matter + 3:].strip()
            else:
                front_matter = None
        else:
            front_matter = None

        # Extract title from front matter if available
        title = None
        if front_matter:
            for line in front_matter.splitlines():
                if line.lower().startswith('title:'):
                    title = line.split(':', 1)[1].strip()
                    break
        if title is None:
            # Fallback to the filename without extension if no title is found
            title = os.path.splitext(os.path.basename(markdown_filepath))[0].replace('_', ' ').title()
        # Add title to the context for rendering
        context = {
            'title': title,
            'content': markdown_content,
        }

        # Enable common markdown extensions including tables and fenced code blocks
        html_content = markdown.markdown(markdown_content, extensions=['extra', 'smarty', 'tables', 'fenced_code'])
        # Add the HTML content to the context
        context['content'] = html_content
        # Add the front matter to the context if available
        if front_matter:
            context['front_matter'] = front_matter

        # Debug: dump the context to see what is being passed to the template
        # print(context)

        rendered_html = template.render(content=html_content, title=title, front_matter=front_matter)

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
