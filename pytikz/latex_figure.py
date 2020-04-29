import os


class LatexFigure:
    def __init__(self, fig_name: str, save_dir: str = os.getcwd()):
        # defines the file names and initializes the data string
        self.fig_name = fig_name
        self.save_dir = save_dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        self.paths = {
            'dir': save_dir,
            'data':       os.path.join(save_dir, fig_name + '_data.tex'),
            'standalone': os.path.join(save_dir, fig_name + '_standalone.tex'),
            'include':    os.path.join(save_dir, fig_name + '_include.tex'),
            'standalone_aux': [
                os.path.join(save_dir, fig_name + '_standalone.aux'),
                os.path.join(save_dir, fig_name + '_standalone.log')
            ]
        }
        self._string = ''

    def append_string(self, data: str):
        # appends data to the data.tex file
        self._string += data

    def draw(self, drawable):
        # parse drawable object and appends it to the string
        self.append_string('{data}\n'.format(data=drawable.build_tikz_string()))

    def write_data(self):
        f = open(self.paths['data'], 'w')
        f.write(self._string)
        f.close()

    def write_standalone(self):
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

    def write_include(self):
        f = open(self.paths['include'], 'w')
        f.write(
            """
            \\begin{{tikzpicture}}
            \\input{{{file}}}
            \\end{{tikzpicture}}
            """.format(file=self.paths['data'])
        )
        f.close()

    def cleanup(self):
        for file_name in self.paths['standalone_aux']:
            os.remove(file_name)

    def update(self, cleanup=True):
        self.write_data()
        os.system('pdflatex -output-directory={dir} {tex_file}'.format(
            tex_file=self.paths['standalone'],
            dir=self.paths['dir']
        ))
        if cleanup:
            self.cleanup()

    def build(self, include=False):
        self.write_standalone()
        self.update()
        if include:
            self.write_include()
