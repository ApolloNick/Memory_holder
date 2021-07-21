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
print(whole_data)


with open(f"brand-{args.brand}-year-{args.year}.csv", "w", encoding="utf-8") as file:
    writing_csv = csv.writer(file)
    writing_csv.writerows(whole_data)




