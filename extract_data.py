import re


def extract_cost(resolution):
    cost_regex = re.compile(r"([0-9]|\s|\,|\.)*(?=zł \(sło)")
    cost = cost_regex.search(resolution)

    if cost:
        cost = cost.group()

        # Normalisation of how the cost is written in the resolution
        # It can be written as: 
        # 1.000,00 zł
        # 1 000,00 zł
        # 1000,00 zł
        cost = cost.replace(" ", "").replace(".", "").replace(",", ".")
        cost = float(cost)
        return cost
    else:
        return None


def extract_beneficiary(resolution):
    beneficiary_regex = re.compile(r"(?<=Przyznaje się) .* (?=dotację)")
    beneficiary = beneficiary_regex.search(resolution)

    if beneficiary:
        return beneficiary.group().strip()
    else:
        return None


def extract_name(resolution):
    # The name of the project seems to be always in quotes 
    name_regex = re.compile(r"\".*\"")
    name = name_regex.search(resolution)

    if name:
        return name.group().strip()
    else:
        return None


def extract_date(resolution):
    date_regex = re.compile(
        r"(?<=z dnia) \d* [AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]* \d* (?=r\.)")
    date = date_regex.search(resolution)

    if date:
        return date.group().strip()
    else:
        return None


def extract_resolution_number(resolution):
    # It's the third word in the resolution
    return int(resolution.split()[2])


def money_was_given(resolution):
    regex = re.compile(r"Przyznaje się")
    return regex.search(resolution) is not None
