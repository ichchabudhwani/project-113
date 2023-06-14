import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/ichchabudhwani/Downloads"              # Add the path of you "Downloads" folder.
to_dir = "C:/Users/ichchabudhwani/Desktop/Downloaded_Files" #Create "Document_Files" folder in your Desktop and update the path accordingly.


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created(self,event):
        print(f"Hey,{event.src_path}has been created!")

    #2_on_deleted
    def on_deleted(self,event):
        print(f"oops SomeOneDeleted{event.src_path}!")
    #3_on_modified
    def on_modified(self,event):
        print(f"Hey,{event.src_path}has been modified!")
    #4_on_moved
    def on_moved(self,event):
        print(f"Someone moved{event.src_path}to{event.dest_path}")
    def on_created(self, event):


        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Downloaded " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt

while True:
    time.sleep(2)
    print("running...")







