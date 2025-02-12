import os
import time
from playsound3 import playsound as ps
          
def runnningLoop(frames:list, song_file:str=None, framerate:float=.5, total_runs:int=10):
     if song_file != None:
          ps(song_file, block=False)
          time.sleep(1)
     
     runs = 0
     while runs != total_runs:
          for frame in frames:
               os.system("cls")
               print(frame)
               time.sleep(framerate)
          runs += 1
              
         
def flossing():
     frames = [
     """
         /\_/\\
        |0) 0)|
        |\_\ \_\\
        |_| |_| 
     """,
     """  
         /\_/\\
        |0) 0)|
       /_/ /_/|
        |_| |_| 
     """
     ]
    
     runnningLoop(frames, "./floss.mp3", framerate=.25)
         
def beegee():
     frames = [
     """  
         /\_/\\
        |(0 (0|_
       /_/ _  //
        |_| |_| 
     """,
     """  
         /\_/\\
        |0) 0)|
       /_//_/ |
        |_| |_| 
     """
     ]
    
     runnningLoop(frames, "./beegee.mp3")
     
def ymca():
     frames = [
     """  
         /\_/\\
       _| 0  0|_
       \\\  _  //
        |_| |_| 
     """,
     """  
         /\_/\\
        | 0  0|
       /_/ _ \_\\
        |_| |_| 
     """,
     """  
         /\_/\\
        |_0  0|_
        // _  //
        |_| |_| 
     """,
     """  
         /\_/\\
        |_0  0|
        // _ \\\\
        |_| |_| 
     """,
     ]
     
     runnningLoop(frames)
 
def main():
     dances = ["Floss","BeeGee", "ymca"]
     
     os.system("cls")
     print("Welcome to Dancing!!!")
     print()
     
     for i,e in enumerate(dances):
          print(f"{i+1}: {e}")
     print()
          
     selection = input("What dancing would you like to see? ")
          
     match selection:
          case '1':
               flossing()
          case '2':
               beegee()
          case '3':
               ymca()
     
if __name__ == "__main__":
     main()