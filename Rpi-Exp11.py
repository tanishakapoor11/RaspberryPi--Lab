from bottle import route, run, request
temp = input("Enter the temperature: ")
humi = input("Enter the humidity: ")
wind = input("Enter the wind speed: ")
rain = input("Enter the rain probability: ")
@route("/")
def sensor():
 sensor_log = [
 {'sensor': 'temperature', 'value': temp},
 {'sensor': 'humidity', 'value': humi},
 {'sensor': 'wind_speed', 'value': wind},
 {'sensor': 'rain', 'value': rain},
 ]
 return dict(data=sensor_log)
run(host='localhost', port=7777, debug=True)
