from Config import conf
from GetData import GetData
from Detect import Detect
from ColorsFinder import find_colors
from SaveData import concatenate
import Folder
import os

if __name__ == '__main__':
    try:
        print("Initialize...")
        conf.initialize()
        print("Initialize : Done!\n")

        for i in range(len(conf.video_source)):
            name = conf.video_source[i].split("/")
            conf.camera = int(name[-1].split('.')[0])
            if (conf.camera == 0 or conf.camera == 2):
                print("Loading data from :", conf.video_source[i], "...")
                data = GetData()
                data.get_video(conf.video_source[i])
                print("Loading data : Done!\n")

                if len(conf.teams) == 0:
                    print("Finding teams's colors ...")
                    find_colors(data)
                print("Finding colors :Done!", conf.teams, "\n")

                print("Processing...\n\n\n")
                detection = Detect(data)
                detection.run()
                print("Processing : Done!\n")

        print("Video creating...")
        concatenate()
        print("Video creating : Done!")

    except KeyboardInterrupt:
        print("\n\nEXIT: interrupt received, stoppin...")
    except FileNotFoundError:
        print("ERROR: Video  [", conf.video_source,"]  doesn't exist.")
    print("Cleaning...")
    Folder.remove(conf.result_file)
    Folder.delete("tmp")
    print("Cleaning : Done!")
    print("Finish.")
