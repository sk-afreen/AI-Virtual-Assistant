import text_to_speech
import speech_to_txt
import datetime
import webbrowser
import weather


def action(data):
    user_data=data

    if "what is your full name" in user_data:
        text_to_speech.text_to_speech("my name is virtual ai")
        return "my name is virtual ai"
    elif "hello" in user_data or "hy" in user_data:
        text_to_speech.text_to_speech("hy , sir how i can help u")
        return "hy , sir how i can help u"
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir"
    elif "good afternoon" in user_data:
        text_to_speech.text_to_speech("good afternoon sir")
        return "good afternoon sir"
    elif "good evening" in user_data:
        text_to_speech.text_to_speech("good evening sir")
        return "good evening sir"
    elif "good night" in user_data:
        text_to_speech.text_to_speech("good night sir")
        return "good night sir"
    
    elif "what are you doing" in user_data:
        text_to_speech.text_to_speech("talking with you")
        return "talking with you"
    
    elif " what is thetime now" in user_data:
        current_time=datetime.datetime.now()
        Time=f"current time is {current_time.hour} hour and {current_time.minute} minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"

    elif "open gaana.com" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is opened for u ")
        return "gaana.com is opened for u"

    elif "open related to education" in user_data:
        webbrowser.open("https://www.geeksforgeeks.org/")
        text_to_speech.text_to_speech("the most famous geeks for geeks website platform is opened for u here u can learn anything u want")
        return "the most fanous geeks for geeks website platform is opened for u here u can learn anything u want"


    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is opened for u ")
        return "youtube.com is opened for u"
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is opened for u ")
        return "google.com is opened for u"
    elif "open linkedin" in user_data:
        webbrowser.open("https://linkedin.com/")
        text_to_speech.text_to_speech("linkedin.com is openedfor u ")
        return "linkedin.com is opened for u"
    elif "open zomato" in user_data:
        webbrowser.open("https://zomato.com/")
        text_to_speech.text_to_speech("zomato.com is opened for u")
        return "zomato.com is opened for u"
    elif "open meesho" in user_data:
        webbrowser.open("https://meesho.com/")
        text_to_speech.text_to_speech("meesho is opened for u")
        return "meesho is opened for u "
    elif "how are you" in user_data:
        text_to_speech.text_to_speech("iam good sir ")
        return "iam good sir "
    elif "open weather" in user_data:
        ans=weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        response = "I am not able to understand."
    print("Assistant --->", response)
    text_to_speech.text_to_speech(response)
    return response

