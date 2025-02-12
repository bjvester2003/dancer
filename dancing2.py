# <<<<IMPORTS>>>> #
import os
import time
from playsound3 import playsound as ps

from dances import dances

# <<<<PROGRAM CLASS>>>> #
class dancing():
    def init(self):
        self.dance_data = dances
    
    def clearScreen(self):
        os.system("cls")
    
    def danceFloor(self):
        self.clearScreen()
        print("Welcome to Dancing!!!\n")
        
        for i, dance in enumerate(dances):
            print(f"{i+1}: {dance["DanceName"]}")
        print()
        
        userSelection = int(input("What dance would you like to see? "))
        chosenDance = dances[userSelection-1]
        
        return self.runnningLoop(chosenDance["DanceFrames"], chosenDance["SongFile"], chosenDance["FrameRate"])
    
    def runnningLoop(self, frames:list, song_file:str, framerate:float):
        if song_file != None:
            song_file = "./songfiles/"+song_file
            ps(song_file, block=False)
            time.sleep(1)
     
        total_runs = 0
        while total_runs != 25:
            for frame in frames:
                os.system("cls")
                print(frame)
                time.sleep(framerate)
            total_runs += 1
            
        self.danceFloor()
          
# <<<<PROGRAM START>>>>#
if __name__ == "__main__":
    dancer = dancing()
    dancer.danceFloor()