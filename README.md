# resolution-parser
To repozytorium zawiera skrypt w języku Python, mający na celu dokonać analizy uchwał dotyczących wydawania pieniędzy przez Zarząd Samorządu Studenckiego Uniwersytetu Jagiellońskiego w Krakowie. 

Wyniki użycia skryptu na wszystkich uchwałach w BIPie SSUJ ([link](https://samorzad.uj.edu.pl/) -- należy kliknąć w zakładkę "BIP") do 2024-01-22 włącznie znajdują się w pliku `parsed.csv`.

Plik `parsed.csv` w obrębie wiersza reprezentującego uchwałę zawiera:
- Numer uchwały
- Beneficjenta uchwały
- Kwotę przyznaną w ramach uchwały
- Nazwę projektu, na który przyznano pieniądze
- Datę podjęcia uchwały

Plik ten może być od razu zaimportowany do arkusza kalkulacyjnego, celem przeprowadzenia dalszej analizy. Nazwy beneficjentów zostały znormalizowane (więcej informacji w dalszej części README), by ułatwić analizę danych podczas tworzenia tabeli przestawnej. 

## Użycie skryptu

**Uwaga** : skrypt wykonuje parsing uchwał z BIPu korzystając z wyrażeń regularnych. Uchwały te nie są w pełni zestandaryzowane, a więc możliwe są błędy w parsowaniu. Warto zweryfikować wyniki działania skrpytu korzystając z zapewnionych przez niego informacji o numerze uchwały i dacie podjęcia (które to liczby umożliwiają jej jednoznaczną identyfikację na stronie BIPu). Ponadto, w przyszłości format uchwał może ulec zmianie. Może to wymagać aktualizacji wyrażeń regularnych używanych przez skrypt. 

Po pobraniu repozytorium na komputer (np. za pomocą polecenia terminala `git clone`) należy utworzyć wewnątrz katalogu repozytorium folder `resolutions`, a w nim umieścić pliki z uchwałami zarządu w formacie `.pdf`. 

Następnie należy zainstalować dependencje skryptu, korzystając z polecenia `pip install -r requirements.txt`.

Skrypt uruchamia się za pomocą polecenia `python main.py`. Zacznie przetwarzać pliki w folderze `resolutions` i zapisze wyniki w pliku `parsed.csv`.

## Weryfikacja poprawności

Część uchwał nie zostanie potraktowana przez skrypt jako mówiąca o przyznaniu pieniędzy; uchwały takie zostają pominięte przy generowaniu pliku `parsed.csv`. O tym, czy uchwała zostaje pominięta czy nie, decyduje funkcja `money_was_given` w pliku `extract_data.py`. Celem weryfikacji jak wyglądają uchwały które zostały pominięte istnieje plik `sanity_check.py` który wypisze na standardowe wyjście uchwały które zostały pominięte przez skrypt, a nie są odmowami przyznania pieniędzy i zawierają jakąkolwiek wzmiankę o pieniądzach (tj. jako spójny podciąg pojawia się fraza `zł` albo `z ł`). Wynik działania tego skryptu został zapisany w pliku `sanity_check.txt`. 

## Struktura plików

Skrypt korzysta z następujących plików:

- `parse.py`, który zawiera funkcje do wstępnego przetworzenia tekstu uchwały, w tym:
    - `parse_resolution`, która wczytuje określony plik `.pdf`
    - funkcje usuwające znaki utrudniające parsowanie
    - funkcję `misc_cleanup`, która usuwa spacje wewnątrz słów (które to spacje są artefaktem parsowania PDFów) oraz poprawia literówki w nazwach beneficjentów
    - funkcję `get_normalised_resolution`, która przyjmuje ścieżkę do pliku `.pdf` i tekst uchwały poddany normalizacji
- `extract_data.py`, który zawiera funkcje do wydobycia z uchwały informacji o numerze uchwały, beneficjencie, kwocie, nazwie projektu i dacie podjęcia uchwały. Sprawdzane jest również (w bardzo prosty sposób), czy uchwała dotyczy wydania pieniędzy. Plik ten może w przyszłości wymagać modyfikacji gdyby format uchwał uległ zmianie.
- `beneficiaries.py`, który zawiera funkcję `standardize_beneficiaries` do znormalizowania nazw jednostek, którym przyznano pieniądze. Konieczność powstania tego pliku wynika z faktu, że w uchwałach jedna jednostka może być nazwana na kilka różnych sposobów. Znacząco utrudnia to analizę danych. Plik ten również może wymagać modyfikacji w przyszłości, gdyby w przyszłych uchwałach pojawiły się nowe nazwy tych samych jednostek.
- `main.py`, który zawiera funkcję `main`, uruchamiającą skrypt. Sam skrypt najpierw wywołuje funkcję `get_normalised_resolution` z pliku `parse.py`, a następnie funkcje z pliku `extract_data.py` i `beneficiaries.py` w celu wydobycia informacji o uchwałach i znormalizowania nazw beneficjentów. Wyniki zapisywane są do pliku `parsed.csv`.

