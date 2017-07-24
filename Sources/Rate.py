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

    def width_compute(self, x):
        return int((self.width / x) * self.width / 1280)

    def height_compute(self, y):
        return int((self.height / y) * self.height / 720)

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
            up = [self.width_compute(1.7), self.height_compute(1.9)]
            down = [self.width_compute(2), self.height_compute(1.1)]
            left = [int(-150 * self.width / 1280), self.height_compute(1.3)]
            right = [int(self.width + 20), self.height_compute(1.7)]
        else:
            up = [self.width_compute(9), self.height_compute(2.8)]
            down = [self.width_compute(2.4), self.height_compute(1.8)]
            left = [int(-150 * self.width / 1280), self.height_compute(2.3)]
            right = [self.width_compute(1.4), self.height_compute(2.3)]
        self.points = np.array([up, left, down, right])
        self.bbPath = mplPath.Path(self.points)
        self.action = ""
        self.max_keep = 10
