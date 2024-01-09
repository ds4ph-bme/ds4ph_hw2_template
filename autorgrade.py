import nbformat
import re

def read_ipynb(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)

# Replace 'your_notebook.ipynb' with the path to your notebook file
notebook = read_ipynb('hw2.ipynb')

def test_q1():
    defines_sorting_hat = False
    contains_input = False
    contains_return = False
    contains_if = False
    for cell in notebook.cells:
        if cell.source.count("sorting_hat()") > 0 :
            defines_sorting_hat = True
        if cell.source.count("input") > 1 :
            contains_input = True
        if cell.source.count("return") > 0 : 
            contains_return = True
        if cell.source.count("if") > 0:
            contains_if = True
    assert defines_sorting_hat & contains_input & contains_return & contains_if 

def test_q2():
    contains_class = False
    contains_mydata = False
    contains_test_function = False
    contains_selfmean = False
    contains_selfstd = True
    for cell in notebook.cells:
        if cell.source.count("class mydata") > 0:
            contains_class = True
        if cell.source.count("mydata") > 0:
            contains_mydata = True
        if cell.source.count("x = mydata([1, 2, 7, 5])") > 0:
            contains_test_function = True
        if cell.source.count("self.mean"):
            contains_selfmean = True
        if cell.source.count("self.std"):
            contains_sefstd = True
    assert contains_class & contains_mydata & contains_test_function & contains_selfmean & contains_selfstd


def test_q3():
    loads_numpy = False
    uses_nan = False
    uses_indexing = False
    for cell in notebook.cells:
        loads_numpy |= bool(re.search(r'\b(numpy)\b', cell.source)) 
        uses_nan |= bool(re.search(r'\b(nan)\b', cell.source)) 
        uses_indexing |= bool(re.search(r'\[.*?:.*?\]', cell.source)) 
    assert loads_numpy & uses_nan & uses_indexing



def test_q4():
    uses_lambda = False
    name_correct = False
    for cell in notebook.cells:
        if cell.source.count("lambda") > 0:
            uses_lambda  = True
        if cell.source.count("lagGenerator") > 0:
            name_correct = True
    assert uses_lambda and name_correct 

