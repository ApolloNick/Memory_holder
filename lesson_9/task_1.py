import argparse
import csv


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is program for checking car number and all info"
                                                 "which car can consist")
    parser.add_argument("o")
    parser.add_argument("--brand")
    parser.add_argument("--color")
    parser.add_argument("--year")
    parser.add_argument("--fuel")
    parser.add_argument("--reg_num")
    args = parser.parse_args()


def reading_csv_data():
    whole_data = [["D_REG", "BRAND", "MODEL", "COLOR", "MAKE_YEAR", "FUEL", "N_REG_NEW"]]
    with open("tz_opendata_z01012021_po01072021.csv", "r", encoding="utf-8") as csv_file:
        reading_csv = csv.DictReader(csv_file, delimiter=";")
        for row in reading_csv:
            prepared_list = []
            if row["BRAND"] == args.brand:
                if row["COLOR"] == args.color:
                    if row["MAKE_YEAR"] == args.year:
                        prepared_list.append(row["D_REG"])
                        prepared_list.append(row["BRAND"])
                        prepared_list.append(row["MODEL"])
                        prepared_list.append(row["COLOR"])
                        prepared_list.append(row["MAKE_YEAR"])
                        prepared_list.append(row["FUEL"])
                        prepared_list.append(row["N_REG_NEW"])
                        whole_data.append(prepared_list)
    return whole_data


def corrected_name():
    prepared_string = []
    if args.brand != "None":
        prepared_string.append(args.brand)
        if args.color != "None":
            prepared_string.append(args.color)
            if args.year != "None":
                prepared_string.append(args.year)
                if args.fuel != "None":
                    prepared_string.append(args.fuel)
                    if args.reg_num != "None":
                        prepared_string.append(args.reg_num)
                    else:
                        print(None)
    verified_name = "-".join(prepared_string)
    return verified_name


def writing_csv(name_file):
    list_of_data = reading_csv_data()
    with open(f"{name_file}.csv", "w", encoding="utf-8") as file:
        writing_csv = csv.writer(file)
        writing_csv.writerows(list_of_data)


writing_csv(corrected_name())




