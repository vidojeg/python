import webbrowser
import time

total_break = 3
break_count = 0

while break_count < total_break:
    time.sleep(10)
    webbrowser.open("https://youtube.com")
    break_count = break_count + 1
