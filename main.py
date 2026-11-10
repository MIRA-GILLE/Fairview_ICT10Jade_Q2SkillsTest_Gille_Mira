from pyscript import document, display

elements = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
}


def periodic(e):
    element_Name = document.getElementById("elements").value.strip().title()
    var2 = elements.get(element_Name, ("Element not found", "-", "-"))

    document.getElementById("div_name").innerHTML = f"""
        Symbol: {element_Name}<br>
        Element: {var2[0]}<br>
        Atomic Number: {var2[1]}<br>
        Atomic Mass: {var2[2]}
    """

def show_periodic_element(e):
    document.getElementById("div_name").innerHTML = ""
    element_symbol = document.getElementById("elements").value.strip().title()

    is_in_the_periodic_table = element_symbol in elements
    element_symbols = list(elements.keys())

    display("The number of elements is", len(elements), target="div_name")
    display("Is it in the periodic table?", is_in_the_periodic_table, target="div_name")
    display("What are the elements in the list?", element_symbols, target="div_name")
