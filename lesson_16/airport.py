import csv
import argparse
from re import search


class CheckDataAirport:
    def __init__(self):
        self.ident_code = args.ident
        self.country = args.country
        self.name = args.name

    def check_ident_code(self):
        with open("airport-codes_csv.csv", "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            ident_code = {}
            for line in csv_reader:
                if line["ident"] == self.ident_code:
                    try:
                        ident_code.update(line)
                    except AirportNotFoundError:
                        print(AirportNotFoundError(self.ident_code, message="Airport not found"))
            return ident_code

    def check_country(self):
        with open("airport-codes_csv.csv", "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            dict_of_airports = {}
            for line in csv_reader:
                if line['iso_country'] == self.country:
                    try:
                        dict_of_airports.update(line)
                    except Exception:
                        raise CountryNotFoundError(self.country, message="Country not found")
            return dict_of_airports

    def check_name_of_airport(self):
        with open("airport-codes_csv.csv", "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            list_of_names = []
            for line in csv_reader:
                if search(self.name, line['name']):
                    try:
                        list_of_names.append(line['name'])
                    except Exception:
                        raise AirportNotFoundError(self.name, message="Airport not found")
            return list_of_names

    def check_validation_ident_code(self):
        valid_code = self.ident_code.upper()
        if valid_code == self.ident_code:
            print("Valid code")
        else:
            raise IATACodeError

    def check_amount_of_params(self):
        if len(vars(first_try)) < 0:
            raise NoOptionsFoundError(message="Parameters not found")
        elif len(vars(first_try)) > 1:
            raise MultipleOptionsError(message="Just one parameter is necessary")
        else:
            print("Your amount of params is corrected")


class AirportNotFoundError(Exception):
    """Exception raised for errors in the input ident_code or name error."""

    def __init__(self, ident_code: str, message="Airport not found"):
        self.ident_code = ident_code
        self.message = message
        super().__init__(self.message)


class CountryNotFoundError(Exception):

    """Exception raised for errors for airport location (country)"""
    def __init__(self, country, message="Country not found"):
        self.country = country
        self.message = message
        super().__init__(self.message)


class MultipleOptionsError(Exception):
    def __init__(self, numbers_of_params, message="Just one parameter is necessary"):
        self.numbers_of_params = numbers_of_params
        self.message = message
        super().__init__(self.message)


class NoOptionsFoundError(Exception):
    def __init__(self, numbers_of_params, message="Parameters not found"):
        self.numbers_of_params = numbers_of_params
        self.message = message
        super().__init__(self.message)


class IATACodeError(Exception):
    def __init__(self, ident_code, message="Not valid value"):
        self.ident_code = ident_code
        self.message = message
        super().__init__(self.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checking data from airport")
    # parser.add_argument("--iata_data", help="Three capital letter") это поле пустое в документе
    parser.add_argument("--ident", default="00AA", help="Ident code in airport doc")
    parser.add_argument("--country", default="US", help="Name of a country")
    parser.add_argument("--name", default="liman", help="Name of airport")
    args = parser.parse_args()


first_try = CheckDataAirport()
print(first_try.check_ident_code())
# print(first_try.check_country())
# print(first_try.check_name_of_airport())
# first_try.check_validation_ident_code()
# first_try.check_amount_of_params()







