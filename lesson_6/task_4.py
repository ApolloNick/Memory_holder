import json
import datetime


def convert_seconds_to_time(x):
    converted_time = datetime.timedelta(seconds=x)
    return converted_time


with open("acdc.json", "r") as file:
    file_dict = json.load(file)
    overall_data_for_count_duration = file_dict["album"]["tracks"]["track"]



def parse_time_duration(value):
    list_of_duration = []
    for item in overall_data_for_count_duration:
        for x in item:
            list_of_duration.append(int(item.get("duration")))
            break

    overall_time_of_songs = sum(list_of_duration)
    return overall_time_of_songs


print("Total amount is " + str(parse_time_duration(overall_data_for_count_duration)) + " seconds")
print(f"Duration of album is {convert_seconds_to_time(parse_time_duration(overall_data_for_count_duration))}")


