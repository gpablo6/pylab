"""
Utility functions for displaying long strings and text files
in Jupyter Notebooks.
"""

from IPython.display import HTML, display
import json
import html


class DisplayHelper:
    
    def __init__(self):
        pass

    def wrap(self, long_string, pre=False):
        escaped_string = html.escape(long_string)
        html_string = escaped_string.replace("\n", "<br>")
        if pre:
            display(
                HTML(
                    f"<div style='width: 600px; word-wrap: break-word;'>{html_string}</div>"  # noqa
                )
            )
        else:
            display(
                HTML(
                    f"<div style='width: 600px; word-wrap: break-word;'><pre>{html_string}</pre></div>"  # noqa
                )
            )

    def text_file(self, file_path):
        try:
            # Open the file and read its contents into a string
            with open(file_path, 'r', encoding='utf-8') as file:
                text_string = file.read()
            # Print the contents (optional)
            print(f"{file_path}:")
            self.wrap(text_string)
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def json_file(self, file_path):
        try:
            # Open the file and read its contents into a string
            with open(file_path, 'r', encoding='utf-8') as file:
                text_string = file.read()
            text_string = json.dumps(
                json.loads(
                    text_string
                ),
                indent=4
            )
            # Print the contents (optional)
            print(f"{file_path}:")
            # self.wrap(text_string, True)
            print(text_string)
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
