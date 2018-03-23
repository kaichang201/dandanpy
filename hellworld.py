'''
Created on Jan 29, 2017

@author: kai
'''

import requests

myKey = '68d80040a0370286'
wunderGround = 'http://api.wunderground.com/api/'
foreCastURI = '/forecast/q'
hourlyURI = '/hourly/q'
hoboken = '/NJ/Hoboken'
jsonRequest = '.json'




if __name__ == '__main__':
    myForecastTxtDict = dict()
    myForecastTempDict = dict()
    myHourlyDict = dict()
    
    resp = requests.get(wunderGround+myKey+foreCastURI+hoboken+jsonRequest)
    myForecast = resp.json()
    resp = requests.get(wunderGround+myKey+hourlyURI+hoboken+jsonRequest)
    myHourly = resp.json()
    

    timeStamp = myForecast['forecast']['txt_forecast']['date']
    
    print (timeStamp + ' ' + hoboken)

    # parsing    
    for forecastText in myForecast['forecast']['txt_forecast']['forecastday']:
        myForecastTxtDict[forecastText['title']] = forecastText['fcttext']
        
    for forecastText in myForecast['forecast']['simpleforecast']['forecastday']:
        myForecastTempDict[forecastText['date']['weekday']] = forecastText['low']['fahrenheit'] + '-' + forecastText['high']['fahrenheit']
        
    for forecastText in myHourly['hourly_forecast']:
        myHourlyDict[forecastText['FCTTIME']['civil']] = forecastText['condition'] + ' ' + forecastText['temp']['english'] + ' Feels ' + forecastText['feelslike']['english']

    # printing       
    
    print ("\n12 Hour Forecast")
    for key in myHourlyDict:
        print (key + ": " + myHourlyDict[key])
    

    print ('\nDaily')
    for key in myForecastTempDict:
        print (key + ": " + myForecastTempDict[key])

    print ('\nDetails')
        
    for key in myForecastTxtDict:
        print (key + " : " + myForecastTxtDict[key])
        
