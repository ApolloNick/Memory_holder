import requests
import datetime

city = input("Enter name of your city: ")
amount_of_days = int(input("Enter the number of days for forecast: "))


def get_data():
    received_data = requests.get("https://api.openweathermap.org/data/2.5/forecast/daily?"
                                 f"q=Odesa&cnt=5&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8",
                                 params={"amount_of_days": amount_of_days, "city": city})
    return received_data.json()


def extracted_data() -> list:
    info_json = get_data()
    list_of_data = []
    for key in info_json["list"]:
        data_for_insert = []
        if len(str(key["dt"])) > 9:
            full_date = datetime.datetime.fromtimestamp(key["dt"])
            date = full_date.strftime("%d-%m-%Y")
            data_for_insert.append(date)
        data_for_insert.append(str(key["temp"]["day"]))
        data_for_insert.append(str(key["feels_like"]["day"]))
        data_for_insert.append(str(key["temp"]["night"]))
        list_of_data.append(data_for_insert)
    return list_of_data


def verified_name_for_file(data):
    insert_in_name = get_data()
    transform_date = datetime.datetime.fromtimestamp(insert_in_name['list'][0]["dt"])
    date = transform_date.strftime("%d-%m-%Y")
    verified_name = "".join(str(date) + "-" + str(insert_in_name["city"]["name"]) + "-" + str(insert_in_name["cnt"]))
    return verified_name


def save_to_file(filename):
    with open(f"{filename}-days-weather-forecast.txt", "w") as file:
        formatting_data = extracted_data()
        for day_data in formatting_data:
            file.write("         ".join(day_data) + "\n")


def main():
    data = get_data()
    file_name = verified_name_for_file(data)
    save_to_file(file_name)


main()






















# dictionary = {"city":{"id":698740,"name":"Odesa","coord":{"lon":30.7326,"lat":46.4775},"country":"UA",
# "population":1001558,"timezone":10800},"cod":"200","message":0.0622214,"cnt":1,
#
# "list":
# [{"dt":1625652000,"sunrise":1625623927,"sunset":1625680288,"temp":{"day":23.35,"min":20.36,
# "max":25.87,"night":21.96,"eve":24.46,"morn":20.72},"feels_like":{"day":23.62,"night":22.38,
# "eve":24.71,"morn":21.07},"pressure":1014,"humidity":72,"weather":[{"id":804,"main":"Clouds",
# "description":"overcast clouds","icon":"04d"}],"speed":8.22,"deg":15,"gust":12.72,"clouds":100,"pop":0.12}]}

# list":[{"dt":1625652000,"sunrise":1625623927,"sunset":1625680288,"temp":{"day":23.35,"min":20.36,"max":25.87,"night":22.78,"eve":24.24,"morn":20.72},
# "feels_like":{"day":23.62,"night":23.12,"eve":24.52,"morn":21.07},"pressure":1014,"humidity":72,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds",
# "icon":"04d"}],"speed":8.22,"deg":15,"gust":12.72,"clouds":100,"pop":0.12},
# {"dt":1625738400,"sunrise":1625710373,"sunset":1625766660,"temp":{"day":26.41,"min":20.34,"max":27.84,"night":24.42,"eve":27.02,"morn":21.08},"feels_like":{"day":26.41,"night":24.67,"eve":27.82,"morn":21.31},"pressure":1021,"humidity":60,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"speed":5.89,"deg":56,"gust":9.07,"clouds":3,"pop":0.37,"rain":0.5},{"dt":1625824800,"sunrise":1625796821,"sunset":1625853029,"temp":{"day":26.18,"min":21.87,"max":27.27,"night":25.44,"eve":27.27,"morn":22.18},"feels_like":{"day":26.18,"night":25.42,"eve":27.29,"morn":22.18},"pressure":1021,"humidity":49,"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"speed":5.5,"deg":56,"gust":8.66,"clouds":0,"pop":0},





