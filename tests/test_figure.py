import pytest
from pytikz import Figure
import os


def test_figure():
    f = Figure("a")
    assert f.name == "a"
    assert f.path_target_directory == os.getcwd()
    assert f.path_target_file("test.tex") == os.path.join(
        f.path_target_directory, "a_test.tex"
    )
    assert f.path_data == f.path_target_file("data.tex")
    assert f.path_include == f.path_target_file("include.tex")
    assert f.path_standalone == f.path_target_file("standalone.tex")
    f.append_string("a")
    assert f._string == "a"
    f.append_string("b")
    assert f._string == "ab"
    f.append_string("c\n")
    assert f._string == "abc\n"
    assert f.contents_data == f._string
    assert (
        f.contents_include
        == f"""\\begin{{tikzpicture}}
\\input{{{f.path_data}}}
\\end{{tikzpicture}}
"""
    )
    assert f.contents_standalone == (
        "\\documentclass[preview,11pt,dvipsnames]{standalone}\n"
        "\\usepackage{tikz}\n"
        "\\begin{document}\n"
        "\\begin{tikzpicture}\n"
        f"\\input{{{f.path_data}}}\n"
        "\\end{tikzpicture}\n"
        "\\end{document}\n"
    )
    assert f.write_data is not None
    assert f.write_include is not None
    assert f.write_standalone is not None

    print(f.path_target_directory)
