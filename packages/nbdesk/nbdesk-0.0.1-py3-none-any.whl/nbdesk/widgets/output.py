""" TextOutput Widget """

import html
import ipywidgets


class TextOutput(ipywidgets.HTML):
    """ Text output widget with a print function but no context """

    def __init__(self, text: str = None, truncate: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.truncate = truncate
        self.contents = []
        if text is not None:
            self.print(text)

    def output_stdout(self, text: str):
        """ append stdout output """
        self.contents.extend(text.splitlines())

        if self.truncate and len(self.contents) > self.truncate:
            self.contents = self.contents[-self.truncate:]

        contents = "\n".join(self.contents)
        self.value = "<pre>%s</pre>" % html.escape(contents)

    def output_stderr(self, text: str):
        """ append stderr output (same as output_stdout) """
        self.output_stdout(text)

    def print(self, *objects, clear_output: bool = False):
        """ print objetcs in the output widget """
        if clear_output:
            self.contents = ""
        text = " ".join(str(obj) for obj in objects)
        self.output_stdout(text)

    def clear_output(self):
        """ clear output """
        self.contents = []
        self.value = ""
