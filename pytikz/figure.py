import os


def _write_file(file_name, contents):
    with open(file_name, "w") as f:
        f.write(contents)


class Figure:
    def __init__(self, name, target_directory=None):
        # defines the file names and initializes the data string
        self.name = name
        self.path_target_directory = (
            target_directory if target_directory is not None else os.getcwd()
        )
        self._string = ""

    def append_string(self, data):
        self._string += data

    def draw(self, drawable):
        self.append_string(f"{drawable}\n")

    def path_target_file(self, suffix):
        return os.path.join(self.path_target_directory, f"{self.name}_{suffix}")

    @property
    def path_data(self):
        return self.path_target_file("data.tex")

    @property
    def path_include(self):
        return self.path_target_file("include.tex")

    @property
    def path_standalone(self):
        return self.path_target_file("standalone.tex")

    @property
    def contents_data(self):
        return self._string

    @property
    def contents_include(self):
        return (
            "\\begin{tikzpicture}\n"
            f"\\input{{{self.path_data}}}\n"
            "\\end{tikzpicture}\n"
        )

    @property
    def contents_standalone(self):
        return (
            "\\documentclass[preview]{standalone}\n"
            "\\usepackage{tikz}\n"
            "\\begin{document}\n"
            "\\begin{tikzpicture}\n"
            f"\\input{{{self.path_data}}}\n"
            "\\end{tikzpicture}\n"
            "\\end{document}\n"
        )

    def write_data(self):
        _write_file(self.path_data, self.contents_data)

    def write_include(self):
        _write_file(self.path_include, self.contents_include)

    def write_standalone(self):
        _write_file(self.path_standalone, self.contents_standalone)

    def write_all(self, include=False):
        self.write_data()
        self.write_standalone()
        self.write_include() if include else None

    def process(self):
        os.system(
            f"pdflatex -output-directory={self.path_target_directory} {self.path_standalone}"
        )
