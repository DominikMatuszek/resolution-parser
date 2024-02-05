import pdfplumber
import re


def parse_resolution(pdf_path):
    parsed = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text(x_tolerance=1)

            if text:
                parsed.append(text)

    return "\n".join(parsed)


def normalize_whitespace(s):
    return " ".join(s.split())


def normalize_interpunction(s):
    return s.replace("„", "\"").replace("”", "\"")


def remove_non_standard_characters(s):
    # Creating a regex that will remove anything that is not a number, interpunction or a polish/latin letter
    polish_alphabet_regex = r"AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż"
    numbers = r"0-9"
    interpunction = r"\.\,\(\)\""

    # I didn't want to combine f-strings with regexes, as chaos would ensue 
    total_regex = r"[^" + polish_alphabet_regex + numbers + interpunction + r"]"

    return re.sub(total_regex, " ", s)


def misc_cleanup(s):
    # PDF reading artifacts will sometimes insert spaces in the middle of words
    s = re.sub(r"J\s*a\s*g\s*i\s*e\s*l\s*l\s*o\s*ń\s*s\s*k\s*i\s*e\s*g\s*o", "Jagiellońskiego", s)
    s = re.sub(r"J\s*a\s*g\s*i\s*e\s*l\s*l\s*o\s*ń\s*s\s*k\s*i\s*m", "Jagiellońskim", s)

    # Uniwersytetu
    s = re.sub(r"U\s*n\s*i\s*w\s*e\s*r\s*s\s*y\s*t\s*e\s*t\s*u", "Uniwersytetu", s)

    # dotację 
    s = re.sub(r"d\s*o\s*t\s*a\s*c\s*j\s*ę", "dotację", s)

    # biotechnologii 
    s = re.sub(r"B\s*i\s*o\s*t\s*e\s*c\s*h\s*n\s*o\s*l\s*o\s*g\s*i\s*i", "Biotechnologii", s)

    # Społecznej
    s = re.sub(r"S\s*p\s*o\s*ł\s*e\s*c\s*z\s*n\s*e\s*j", "Społecznej", s)

    # Informatyki 
    s = re.sub(r"I\s*n\s*f\s*o\s*r\s*m\s*a\s*t\s*y\s*k\s*i", "Informatyki", s)

    # Międzynarodowych
    s = re.sub(r"M\s*i\s*ę\s*d\s*z\s*y\s*n\s*a\s*r\s*o\s*d\s*o\s*w\s*y\s*c\s*h", "Międzynarodowych", s)

    # Politycznych
    s = re.sub(r"P\s*o\s*l\s*i\s*t\s*y\s*c\s*z\s*n\s*y\s*c\s*h", "Politycznych", s)

    # Humanistycznych
    s = re.sub(r"H\s*u\s*m\s*a\s*n\s*i\s*s\s*t\s*y\s*c\s*z\s*n\s*y\s*c\s*h", "Humanistycznych", s)

    # Studentów 
    s = re.sub(r"S\s*t\s*u\s*d\s*e\s*n\s*t\s*ó\s*w", "Studentów", s)

    # misspellings
    s = s.replace("Wydzialu", "Wydziału")
    s = s.replace("Indywidulanych", "Indywidualnych")

    return s


def get_normalised_resolution(pdf_path):
    resolution = parse_resolution(pdf_path)
    resolution = normalize_whitespace(resolution)
    resolution = normalize_interpunction(resolution)
    resolution = remove_non_standard_characters(resolution)
    resolution = normalize_whitespace(resolution)
    resolution = misc_cleanup(resolution)

    return resolution
