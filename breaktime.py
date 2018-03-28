import time
import webbrowser

count = 0
print("This program started on "+time.ctime())
while (count<3):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=5-sfG8BV8wU")
    count = count + 1
