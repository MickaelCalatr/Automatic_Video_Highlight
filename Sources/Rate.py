from Positions import get_position_penalty_area
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
        self.points = get_position_penalty_area(self.width, self.height, camera)
        self.bbPath = mplPath.Path(self.points)
        self.action = ""
        self.max_keep = 10
