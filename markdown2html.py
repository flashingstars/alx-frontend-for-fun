#!/usr/bin/python3
"""
Creating a markdown to html
"""
import sys
import os
import markdown


def parse_heading(line):
    """
    Parses the heading line and generates HTML.

    Arguments:
              line (str): The heading line in Markdown format.

    Returns:
            str: The corresponding HTML for the heading.
    """
    level = line.count('#')
    if level > 6:
        level = 6
    return '<h{}>{}</h{}>\n'.format(level, line.strip('# ').strip(), level)


def parse_list(lines, list_type):
    """
    Parses the list lines and generates HTML.

    Arguments:
              lines (list): The list of lines in Markdown format.
              list_type (str): The type of the list: 'unordered' or 'ordered'.

    Returns:
            str: The corresponding HTML for the list.
    """
    html = '<{}l>\n'.format('u' if list_type == 'unordered' else 'o')
    for line in lines:
        line = line.strip()
        if line.startswith('- ') or line.startswith('* '):
            html += '    <li>{}</li>\n'.format(line[2:])
    html += '</{}l>\n'.format('u' if list_type == 'unordered' else 'o')
    return html


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
        markdown_content = md_file.readlines()
        html_content = ''

        # Group consecutive list lines
        list_lines = []
        list_type = None

        for line in markdown_content:
            line = line.strip()
            if line.startswith('- ') or line.startswith('* '):
                if not list_type:
                    list_type = 'unordered' if line.startswith('- ') else 'ordered'
                list_lines.append(line)
            elif list_lines:
                html_content += parse_list(list_lines, list_type)
                list_lines = []
                list_type = None
            elif line.startswith('#'):
                html_content += parse_heading(line)
            else:
                html_content += markdown.markdown(line)


        # Handle remaining list lines if any
        if list_lines:
            html_content += parse_list(list_lines, list_type)

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
