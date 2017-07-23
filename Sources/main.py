from Config import conf
from GetData import GetData
from Detect import Detect

from SaveData import concatenate
import Folder
import os

if __name__ == '__main__':
    try:
        print("Initialize...")
        conf.initialize()
        print("Initialize : Done!\n")

        for i in range(len(conf.video_source)):
            if (i == 0 or i == 2):
                name = conf.video_source[i].split("/")
                conf.camera = int(name[-1].split('.')[0])
                print("Loading data from :", conf.video_source[i], "...")
                data = GetData()
                data.get_video(conf.video_source[i])
                print("Loading data : Done!\n")

                print("Processing...\n")
                detection = Detect(data)
                detection.run()
                print("Processing : Done!\n")

        print("Video creating...")
        concatenate()
        print("Video creating : Done!")

        print("Cleaning...")
        Folder.remove(conf.result_file)
        Folder.delete("tmp")
        print("Cleaning : Done!")

    except KeyboardInterrupt:
        print("\n\nEXIT: interrupt received, stoppin...")
    except FileNotFoundError:
        print("ERROR: Video  [", conf.video_source,"]  doesn't exist.")
    print("Finish.")
