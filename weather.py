#https://www.google.com/search?q=weather+patna
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
#<div class="wob_loc q8U8x" id="wob_loc">Weather</div>
#<span class="wob_t q8U8x" id="wob_tm" style="display:inline">14</span>#<div jscontroller="e0Sh5" class="vk_bk wob-unit" jsaction="rcuQ6b:npT2md"><span class="wob_t" style="" aria-label="°Celsius" aria-disabled="true" role="button">°C</span><a class="wob_t" href="#" style="text-decoration: none; display: none;" data-lams="" data-metric="true" data-url="/setprefs?fheit=0&amp;sig=0_2SNuSGvjd0iM-C3R4H3j9JlAQDo=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bpatna%2Bcity%26rlz%3D1C1RXQR_enIN1095IN1095%26oq%3D%26gs_lcrp%3D%26sourceid%3Dchrome%26ie%3DUTF-8" role="button" jsaction="ytDzMd" data-ved="2ahUKEwjsjoGw4v-KAxUfdfUHHWtMMDUQ-lt6BAgWEAE"><span aria-label="°Celsius">°C</span></a><span class="Az4ne"></span><a class="wob_t" href="#" style="text-decoration: none; margin-left: -1px;" data-lams="" data-metric="false" data-url="/setprefs?fheit=1&amp;sig=0_2SNuSGvjd0iM-C3R4H3j9JlAQDo=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bpatna%2Bcity%26rlz%3D1C1RXQR_enIN1095IN1095%26oq%3D%26gs_lcrp%3D%26sourceid%3Dchrome%26ie%3DUTF-8" role="button" jsaction="ytDzMd" data-ved="2ahUKEwjsjoGw4v-KAxUfdfUHHWtMMDUQ-1t6BAgWEAI"><span aria-label="°Fahrenheit">°F</span></a>    <span class="wob_t" style="margin-left: -1px; display: none;" aria-label="°Fahrenheit" aria-disabled="true" role="button">°F</span></div>
#<div jscontroller="e0Sh5" class="vk_bk wob-unit" jsaction="rcuQ6b:npT2md"><span class="wob_t" style="" aria-label="°Celsius" aria-disabled="true" role="button">°C</span><a class="wob_t" href="#" style="text-decoration: none; display: none;" data-lams="" data-metric="true" data-url="/setprefs?fheit=0&amp;sig=0_2SNuSGvjd0iM-C3R4H3j9JlAQDo=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bpatna%2Bcity%26rlz%3D1C1RXQR_enIN1095IN1095%26oq%3D%26gs_lcrp%3D%26sourceid%3Dchrome%26ie%3DUTF-8" role="button" jsaction="ytDzMd" data-ved="2ahUKEwjsjoGw4v-KAxUfdfUHHWtMMDUQ-lt6BAgWEAE"><span aria-label="°Celsius">°C</span></a><span class="Az4ne"></span><a class="wob_t" href="#" style="text-decoration: none; margin-left: -1px;" data-lams="" data-metric="false" data-url="/setprefs?fheit=1&amp;sig=0_2SNuSGvjd0iM-C3R4H3j9JlAQDo=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bpatna%2Bcity%26rlz%3D1C1RXQR_enIN1095IN1095%26oq%3D%26gs_lcrp%3D%26sourceid%3Dchrome%26ie%3DUTF-8" role="button" jsaction="ytDzMd" data-ved="2ahUKEwjsjoGw4v-KAxUfdfUHHWtMMDUQ-1t6BAgWEAI"><span aria-label="°Fahrenheit">°F</span></a>    <span class="wob_t" style="margin-left: -1px; display: none;" aria-label="°Fahrenheit" aria-disabled="true" role="button">°F</span></div>
#<span id="wob_dc">Clear</span>
#d700b9877f348ae78df5f3f45dad9cf5



import requests  # Importing the requests library to make HTTP requests

def weather():
    # Define the API URL and parameters
    api_key = "d700b9877f348ae78df5f3f45dad9cf5"  # Replace with your OpenWeatherMap API key
    city="patna,IN"
     # The city for which you want the weather information
    # Constructing the full API URL with the necessary parameters (city name, API key, and units in Celsius)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Making a GET request to the OpenWeatherMap API to fetch weather data
    response = requests.get(url)
    
    # Check if the request was successful (status code 200 means success)
    if response.status_code != 200:
        print("Error fetching the weather data.")
        return "Error fetching the data "  # If the request failed, stop the function
    
    # If successful, parse the JSON response
    data = response.json()  # Convert the response to a Python dictionary
    
    # Extract the temperature (from the 'main' section of the response)
    temp = data["main"]["temp"]  # Temperature is found under the 'main' key
    unit = "°C"  # We specify the unit for temperature (Celsius)
    
    # Extract the weather description (from the 'weather' section of the response)
    desc = data["weather"][0]["description"]  # Description of the weather (like 'clear sky')
    
    # Return the temperature and description in a readable format
    return f"the weather in {city} is {temp}{unit} with {desc}"

# Example usage
#print(action()  # Call the function and print the weather data

























































































