import argparse

VERSION = "1.6.3.2"

class Config:
    def initialize(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-d", "--debug", help = "Debug mode (1 to activate)")
        ap.add_argument("-n", "--name", help = "Video result name", type=str, default="Result.mp4")
        ap.add_argument("-m", "--msec", help = "time record before the action (in msec).", type=int, default=90)
        ap.add_argument("-th", "--thread", help = "Number of thread in same time (1 to desactivate).", type=int, default=15)
        ap.add_argument('--version', action='version', version='%(prog)s V' + str(VERSION))
        ap.add_argument("-i", "--input", help = "Video", required=True, nargs='+')
        ap.add_argument("-tc1", "--team1", help = "Color of team one (blue, red, yellow, green)?", required=True)
        ap.add_argument("-tc2", "--team2", help = "Color of team two (blue, red, yellow, green)?", required=True)

        args = vars(ap.parse_args())
        if args["debug"] != None and args["debug"] == "1":
            self.debug = True
        self.video_name_dest = args["name"]
        self.max_thread = args["thread"]
        self.video_source = args["input"]
        self.msec = args["msec"]
        self.teams.append(args["team1"])
        self.teams.append(args["team2"])

    def __init__(self):
        self.folder_out = "./output/"
        self.video_source = []
        self.video_name_dest = ""
        self.msec = 90
        self.max_thread = 15
        self.teams = []
        self.camera = 0
        self.result_file = "videos_list.txt"
        # Debug variables
        self.debug = False

        # Colours
        self.contrast = 1.3
        self.color = 1
        self.boundaries = {
            'blue': ([86, 31, 4], [220, 88, 50]),
            'red': ([0, 0, 170], [140, 125, 255]),
            'yellow': ([140, 140, 0], [255, 255, 70]),
            'white': ([245, 245, 245], [255, 255, 255])
        }
        self.point_color = [
            (255, 0, 0),
            (0, 255, 0)
        ]


conf = Config()
