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


def periodic_element(e):

#refresh for not_applicable
    element = document.getElementById("periodic_table").value.strip().title()
    not_applicable = elements.get(element, ("Element not found", "-", "-"))

    document.getElementById("div_name").innerHTML = f"""
        Symbol: {element}
        <br>
        Element: {not_applicable[0]}
        <br>
        Atomic Number: {not_applicable[1]}
        <br>
        Atomic Mass: {not_applicable[2]}
    """
    element_symbol = document.getElementById("periodic_table").value.strip().title()
