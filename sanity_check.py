from extract_data import money_was_given
from parse import get_normalised_resolution

import os


def print_resolution_if_interesting(resolution):
    about_money = money_was_given(resolution)
    is_rejection = "Odmawia się" in resolution
    money_present = "zł" in resolution or "z ł" in resolution

    if not about_money and not is_rejection and money_present:
        print(resolution)


def check_resolutions(resolutions_folder):
    for file in os.listdir(resolutions_folder):
        if file.endswith(".pdf"):
            resolution = get_normalised_resolution(os.path.join(resolutions_folder, file))
            print_resolution_if_interesting(resolution)

        else:
            print(f"File {file} is not a PDF file, skipping it")


def main():
    check_resolutions("resolutions")

if __name__ == "__main__":
    main()
