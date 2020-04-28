import os


class LatexFigure:
    def __init__(self, fig_name: str, directory: str=os.getcwd()):
        # defines the file names and initializes the data string
        self.fig_name = fig_name
        self.directory = directory
        self.paths = {
            'dir': directory,
            'data':       os.path.join(directory, fig_name + '_data.tex'),
            'standalone': os.path.join(directory, fig_name + '_standalone.tex'),
            'include':    os.path.join(directory, fig_name + '_include.tex'),
            'standalone_aux': [
                os.path.join(directory, fig_name + '_standalone.aux'),
                os.path.join(directory, fig_name + '_standalone.log')
            ]
        }
        self._string = ''

    def append_string(self, data: str):
        # appends data to the data.tex file
        self._string += data

    def draw(self, drawable):
        # parse drawable object and appends it to the string
        self.append_string('{data}\n'.format(data=drawable.draw()))

    def update(self, hard=False, cleanup=True):
        # creates the tex files and runs latexmk on the standalone tex file
        # if hard=True then all files are overwritten
        # if cleanup=True then .aux and .log files are removed
        f = open(self.paths['data'], 'w')
        f.write(self._string)
        f.close()

        if hard or not os.path.isfile(self.paths['standalone']):
            f = open(self.paths['standalone'], 'w')
            f.write(
                """
                \\documentclass[preview]{{standalone}}
                \\usepackage{{tikz}}
                \\begin{{document}}
                \\begin{{tikzpicture}}
                \\input{{{file}}}
                \\end{{tikzpicture}}
                \\end{{document}}
                """.format(file=self.paths['data'])
            )
            f.close()

        if hard or not os.path.isfile(self.paths['include']):
            f = open(self.paths['include'], 'w')
            f.write(
                """
                \\begin{{tikzpicture}}
                \\input{{{file}}}
                \\end{{tikzpicture}}
                """.format(file=self.paths['data'])
            )
            f.close()

        os.system('pdflatex -output-directory={dir} {tex_file}'.format(
            tex_file=self.paths['standalone'],
            dir=self.paths['dir']
        ))

        if cleanup:
            for file_name in self.paths['standalone_aux']:
                os.remove(file_name)
