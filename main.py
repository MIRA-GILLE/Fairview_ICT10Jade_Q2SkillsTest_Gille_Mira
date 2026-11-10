from pyscript import document, display

elements = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Boron",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Ne": "Neon",
    "Fr": "Francium",
}


def check_element(e):
    document.getElementById("output1").innerHTML = ""

    element_symbol = document.getElementById("elements").value

    display(elements.get(element_symbol, "Element symbol not found."), target="output1")

def show_element(e):
    document.getElementById("output1").innerHTML = ""
    element_symbol = document.getElementById("elements").value

    is_in_dictionary = element_symbol in elements
    element_symbols = list(elements)

    display("The number of elements is", len(elements), target="output1")
    display("Is it in the dictionary?", is_in_dictionary, target="output1")
    display("What are the elements in the list?", element_symbols, target="output1")
