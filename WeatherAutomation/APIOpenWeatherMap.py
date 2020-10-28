import requests

class APIWeather:
    def get_temperature_api(self,APIDataDict):
        API_Dict={"City": ["PrimaryTemperature", "WeatherType"]}
        for i in APIDataDict["City"]:
            InURL = f"http://api.openweathermap.org/data/2.5/weather?q={i}&appid={APIDataDict['appid']}"
            r = requests.get(InURL)
            temp = r.json()
            PrimaryTemperature = round(((temp["main"])["temp"] - 273.15),2)
            API_Dict[i] = [PrimaryTemperature, (temp["weather"])[0]["main"]]
        return API_Dict


