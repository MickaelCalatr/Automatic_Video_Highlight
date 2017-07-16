
class Player:
    def __init__(self, x, w, y, h):
        self.x = int(x + (w / 2))
        self.y = int(y + (h / 2))

class RateImage:
    def rate_player(self, player, l, r, u, d):
        if (player.x < r and player.x > l) and (player.y < d and player.y > u):
            return 1
        return 0
        
    def rate_img(self):
        for i in self.players:
            self.rate += self.rate_player(i, self.left, self.right, self.up, self.down)
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
        self.up = int((int(self.height / 10) * self.height) / 720)
        self.down = int((int((3 * self.height) / 5.5) * self.height) / 720)
        if camera == 0:
            self.right = int((int((2 * self.width) / 3.1) * self.width) / 1280)
            self.left = int((int(self.width / 6) * self.width) / 1280)
        else:
            self.right = int((int((2 * self.width) / 2.7) * self.width) / 1280)
            self.left = int((int(self.width / 3) * self.width) / 1280)
        self.action = ""
        self.max_keep = 10
        

        
