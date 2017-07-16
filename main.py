from Config import conf
from GetData import GetData
from Detect import Detect
import os

if __name__ == '__main__':
    try:
        print("Initialize...")
        conf.initialize()
        print("Initialize : Done!\n")

        for i in range(len(conf.video_source)):
            if (i == 0 or i == 2):
                conf.camera = i
                print("Loading data from :", conf.video_source[i], "...")
                data = GetData()
                data.get_video(conf.video_source[i])
                print("Loading data : Done!\n")

                print("Processing...\n")
                detection = Detect(conf, data)
                detection.run()
                print("Processing : Done!\n")

        print("Video creating...")
        #os.system("ffmpeg -r 29 -f image2 -s 1920x1080 -i tmp/pic%07d.png  " + conf.video_name_dest)
        print("Video creating : Done!")

    except KeyboardInterrupt:
        print("\n\nEXIT: interrupt received, stoppin...")
    except FileNotFoundError:
        print("ERROR: Video  [", conf.video_source,"]  doesn't exist.")
    print("Finish.")
