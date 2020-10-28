from WeatherAutomation import UIWeather, APIOpenWeatherMap
import os
import random
import yaml

# This is the driver script for the project
# Please install the additional python packages for this project to work like pyYaml, selenium, random

# Initiating yaml file loader to read data from config.yaml
yamlFileObj = open('config.yaml')
FullConfig = yaml.load(yamlFileObj, Loader=yaml.FullLoader)
LogConfigDic = FullConfig.get('DataDict')
cityList = LogConfigDic["City"]
GUIDataDict = {"City": LogConfigDic["City"], "Variance":LogConfigDic["Variance"]}
APIDataDict = {"City": LogConfigDic["City"], "appid":LogConfigDic["appid"]}

# Calling submodules to get data from https://weather.com/ and http://api.openweathermap.org
UIObj = UIWeather.UIWeather()
APIObj = APIOpenWeatherMap.APIWeather()
UIDictionary = UIObj.get_temperature_gui(GUIDataDict)
APIDictionary = APIObj.get_temperature_api(APIDataDict)

# Comparing data and generating reports:
try:
    cwd = os.getcwd()
    filename = cwd+"\Results\Result"+str(random.random()).replace(".","")+".html"
    print(filename)
    fileobj = open(filename, "a+")
    instr = "City Name" + ("\t"*2) + "weather.com" + ("\t"*2) + "openweathermap.org" + ("\t"*2) + "PASS" + "\n"
    for i in cityList:
        if abs((UIDictionary[i])[0] - (APIDictionary[i])[0]) <= 3:
            instr = i + ("\t"*2) + str((UIDictionary[i])[0]) + ("\t"*2) + str((APIDictionary[i])[0]) + ("\t"*2) + "PASS" + "\n"
        else:
            instr = i + ("\t"*2) + str((UIDictionary[i])[0]) + ("\t"*2) + str((APIDictionary[i])[0]) + ("\t"*2) + "Difference is more than Variance" + "\n"
        fileobj.write(instr)
        print(instr)
except Exception as e:
    print(e)
finally:
    fileobj.close()

