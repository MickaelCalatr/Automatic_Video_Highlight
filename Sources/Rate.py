import matplotlib.path as mplPath
import numpy as np

class Player:
    def __init__(self, x, w, y, h):
        self.x = int(x + (w / 2))
        self.y = int(y + h)

class RateImage:
    def is_in_box(self, player):
        return self.bbPath.contains_point((player.x, player.y))

    def rate_player(self, player, l, r, u, d):
        if (player.x < r and player.x > l) and (player.y < d and player.y > u):
            return 1
        return 0

    def rate_img(self):
        for player in self.players:
            if self.is_in_box(player):
                self.rate += 1
        if self.rate >= self.max_keep:
            return True
        return False

    def add_player(self, x, y, h, w):
        player = Player(x, w, y, h)
        player.x = int((player.x * self.width) / 1280)
        player.y = int((player.y * self.height) / 720)
        self.players.append(player)

    def __init__(self, shape, camera):
        self.players = []
        (self.height, self.width, _) = shape
        self.rate = 0
        self.camera = camera
        # self.up = int((int(self.height / 10) * self.height) / 720)
        # self.down = int((int((3 * self.height) / 5.5) * self.height) / 720)
        # if camera == 0:
        #     self.right = int((int((2 * self.width) / 3.1) * self.width) / 1280)
        #     self.left = int((int(self.width / 6) * self.width) / 1280)
        # else:
        #     self.right = int((int((2 * self.width) / 2.7) * self.width) / 1280)
        #     self.left = int((int(self.width / 3) * self.width) / 1280)


        if camera == 0:
            self.right = int((int((2 * self.width) / 3.1) * self.width) / 1280)
            self.left = int((int(self.width / 6) * self.width) / 1280)
        else:
            up_x = int((int(self.width / 9) * self.width) / 1280)
            up_y = int((int(self.height / 2.8) * self.height) / 720)
            down_x = int((int(self.width / 2.4) * self.width) / 1280)
            down_y = int((int(self.height / 1.8) * self.height) / 720)
            left_x = int((-150 * self.width) / 1280)
            left_y = int((int(self.height / 2.3) * self.height) / 720)
            right_x = int((int(self.width) / 1.4 * self.width) / 1280)
            right_y = int((int(self.height / 2.3) * self.height) / 720)
        self.points = np.array([[up_x, up_y], [left_x, left_y], [down_x, down_y], [right_x, right_y]])
        self.bbPath = mplPath.Path(self.points)
        self.action = ""
        self.max_keep = 10
