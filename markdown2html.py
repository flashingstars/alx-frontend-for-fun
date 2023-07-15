#!/usr/bin/python3
"""
Creating a markdown to html
"""
import sys
import os
import markdown


def markdown_to_html(md, html):
    """
    Converting a markdown to HTML.

    Arguments:
               md (str): Path to the input Markdown file.
               html (str): Path to the output HTML file.
    """

    # Checking if the markdown file exists
    if not os.path.exists(md):
        sys.stderr.write('Missing {}\n'.format(md))
        sys.exit(1)

    # Converting the Markdown file to HTML
    with open(md, 'r') as md_file:
        markdown_content = md_file.read()
        html_content = markdown.markdown(markdown_content)

    # Write the HTML content to the output file
    with open(html, 'w') as html_file:
        html_file.write(html_content)


if __name__ == '__main__':
    # Check if the correct number of arguments is given
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py <input_file> '
                         '<output_file>\n')
        sys.exit(1)

    # Extract the input and output file names from the arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to html
    markdown_to_html(input_file, output_file)

    sys.exit(0)
