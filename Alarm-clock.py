# Python Alarm Clock
import time
import datetime
import contextlib
import os

with open(os.devnull, 'w') as f, contextlib.redirect_stdout(f):
    import pygame

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    sound_file = "My-music.mp3"
    is_running = True
    
    while is_running:
        
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("Wake Up!🥱")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False
        time.sleep(1)
            

if __name__ == "__main__":
    alarm_time = input("Enter the time for the alarm in (HH:MM:SS): ")
    set_alarm(alarm_time)