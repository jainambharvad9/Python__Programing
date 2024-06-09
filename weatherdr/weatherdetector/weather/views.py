# from django.shortcuts import render
# import json
# import urllib.request
# # Create your views here.


# def index(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=d504fc9f3ae689a02a0141fe4cdc6767').read()
#         json_data = json.loads(res)
#         data = {
#             "country_code": str(json_data['sys']['country']),
#             "coordinate": str(json_data['coord']['lon'])+ ' ' + 
#             str(json_data['coord']['lat']),
#             "temp": str(json_data['main']['temp']) + 'k',
#             "pressure": str(json_data['main']['pressure']),
#             "humidity": str(json_data['main']['humidity']),
#         }
#     else:
#         data = {
            
#         }
#     print(res)
#     return render(request, 'index.html',data)


# from django.shortcuts import render
# import json
# import urllib.request
# from urllib.error import HTTPError

# # Create your views here.
# def index(request):
#     if request.method == 'POST':
#         city = request.POST['city']
#         api_key = 'd504fc9f3ae689a02a0141fe4cdc6767'  # Your API key
#         api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
#         try:
#             res = urllib.request.urlopen(api_url).read()
#             json_data = json.loads(res)
#             data = {
#                 "country_code": str(json_data['sys']['country']),
#                 "coordinate": f"{json_data['coord']['lon']} {json_data['coord']['lat']}",
#                 "temp": f"{json_data['main']['temp']} K",
#                 "pressure": str(json_data['main']['pressure']),
#                 "humidity": str(json_data['main']['humidity']),
#             }
#         except HTTPError as e:
#             data = {"error": f"HTTP error occurred: {e.reason}"}
#         except Exception as e:
#             data = {"error": str(e)}
#     else:
#         data = {}
#     return render(request, 'index.html', data)

# from django.shortcuts import render 
# # import json to load json data to python dictionary 
# import json 
# # urllib.request to make a request to api 
# import urllib.request 


# def index(request): 
	# if request.method == 'POST': 
	# 	city = request.POST.get('city') 
	# 	''' api key might be expired use your own api_key 
	# 		place api_key in place of appid ="your_api_key_here " '''

	# 	# source contain JSON data from API 

	# 	source = urllib.request.urlopen( 
	# 		'http://api.openweathermap.org/data/2.5/weather?q ='
	# 				+ city + '&appid = d504fc9f3ae689a02a0141fe4cdc6767').read() 

	# 	# converting JSON data to a dictionary 
	# 	list_of_data = json.loads(source) 

	# 	# data for variable list_of_data 
	# 	data = { 
	# 		"country_code": str(list_of_data['sys']['country']), 
	# 		"coordinate": str(list_of_data['coord']['lon']) + ' '
	# 					+ str(list_of_data['coord']['lat']), 
	# 		"temp": str(list_of_data['main']['temp']) + 'k', 
	# 		"pressure": str(list_of_data['main']['pressure']), 
	# 		"humidity": str(list_of_data['main']['humidity']), 
	# 	} 
	# 	print(data) 
	# else: 
	# 	data ={} 
	# return render(request, "index.html", data) 




from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    data = {}  # Initialize data dictionary
    city = ''
    if request.method == 'POST':
        city = request.POST.get('city')  # Use get method to safely fetch 'city' from POST data
        if city:
            try:
                api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=d504fc9f3ae689a02a0141fe4cdc6767'
                response = urllib.request.urlopen(api_url).read()
                json_data = json.loads(response)
                data = {
                    "country_code": str(json_data['sys']['country']),
                    "coordinate": f"{json_data['coord']['lon']} {json_data['coord']['lat']}",
                    "temp": f"{json_data['main']['temp']}K",
                    "pressure": str(json_data['main']['pressure']),
                    "humidity": str(json_data['main']['humidity']),
                }
                print(data)  # Debug print to check data
            except urllib.error.HTTPError as e:
                data = {"error": f"HTTP Error: {e.code} - {e.reason}"}
            except urllib.error.URLError as e:
                data = {"error": f"URL Error: {e.reason}"}
            except Exception as e:
                data = {"error": str(e)}
        else:
            data = {"error": "Please enter a city name."}

    return render(request, 'index.html', {'data': data, 'city': city})
