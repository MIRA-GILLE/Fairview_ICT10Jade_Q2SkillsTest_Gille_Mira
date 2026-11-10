from pyscript import document, display

def check_element(e):
    element = {
        "H": "Hydrogen",
        "He": "Helium",
        "Li": "Lithium",
        "Be": "Beryllium",
        "fr": "France",
    }

    document.getElementById("output1").innerHTML = ""
    
    element_symbol = document.getElementById("elements").value

    #add an element
    element["B"] = "Boron"

  
    display(element.get(element_symbol, "Element symbol not found."), target="output1")

def show_element(e):
    document.getElementById("output1").innerHTML = "" 
element = {
        "H": "Hydrogen", "Atomic Number": 1,
        "He": "Helium", "Atomic Number": 2,
        "Li": "Lithium", "Atomic Number": 3,
        "Be": "Beryllium", "Atomic Number": 4,
        "B": "Boron", "Atomic Number": 5,
        "C": "Carbon", "Atomic Number": 6,
        "N": "Nitrogen", "Atomic Number": 7,
        "O": "Oxygen", "Atomic Number": 8,
        "F": "Fluorine", "Atomic Number": 9,
        "Ne": "Neon", "Atomic Number": 10
    }

element_symbol = document.getElementById("elements").value

show_element = element_symbol in element
list_element = list(element.keys()) #the element symbols
#list_element = list(element.values()) (for the actual values)

display("The number of elements is", len(element), target="output1")
display("Is it in the dictionary?", show_element, target = "output1")
display("What are the elements in the list?", list_element, target= "output1")
