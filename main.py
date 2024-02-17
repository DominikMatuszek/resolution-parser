from extract_data import extract_cost, extract_beneficiary, extract_name, extract_date, money_was_given, \
    extract_resolution_number
from parse import get_normalised_resolution
from beneficiaries import standardize_beneficiaries

import os
import csv


def convert_resolution_to_dict(resolution):
    
    cost, number_of_costs = extract_cost(resolution, sanity_check=True)      
    beneficiary = extract_beneficiary(resolution)
    name = extract_name(resolution)
    date = extract_date(resolution)
    about_money = money_was_given(resolution)
    number = extract_resolution_number(resolution)

    try:
        year = int(date.split()[2])
    except:
        year = "Nie znaleziono roku w uchwale"

    if number_of_costs > 1:
        if about_money:
            raise ValueError(
                "There were multiple costs in the resolution about money. This should not happen. Full resolution: " + resolution)
        else: 
            print("Warning: found multiple costs in a resolution that is not about giving money. It might be a modification of a previous resolution. Full resolution: " + resolution)

    if not cost and about_money:
        raise ValueError(
            "There was no cost in the resolution about money. This should not happen. Full resolution: " + resolution)

    if not beneficiary:
        beneficiary = "Nie znaleziono beneficjenta w uchwale"

    if not name:
        name = "Nie znaleziono nazwy projektu w uchwale"

    if not date:
        date = "Nie znaleziono daty w uchwale"

    return {
        "cost": cost,
        "beneficiary": beneficiary,
        "name": name,
        "date": date,
        "about_money": about_money,
        "year": year,
        "number": number
    }


def load_resolutions(resolutions_folder):
    resolutions = []
    for file in os.listdir(resolutions_folder):
        if file.endswith(".pdf"):
            resolution = get_normalised_resolution(os.path.join(resolutions_folder, file))

            resolution = convert_resolution_to_dict(resolution)

            if resolution["about_money"]:
                resolutions.append(resolution)
        else:
            print(f"File {file} is not a PDF file, skipping it")

    return resolutions


def main():
    resolutions = load_resolutions("resolutions")
    resolutions = standardize_beneficiaries(resolutions)
    resolutions.sort(key=lambda x: (x["year"], x["number"]))

    with open("parsed.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Numer uchwały", "Beneficjent", "Koszt", "Nazwa projektu", "Data uchwały"])
        for resolution in resolutions:
            writer.writerow([resolution["number"], resolution["beneficiary"], resolution["cost"], resolution["name"],
                             resolution["date"]])


if __name__ == "__main__":
    main()
