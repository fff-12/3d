from direct.showbase.ShowBase import ShowBase

class Hero():
    def __init__(self, pos, land):
        self.land = land

        self.mode = True

        self.hero = loader.loadModel("Cube.obj")
        self.hero.setColor(1, 0.5, 0, 1)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.hero.setScale(0.03)

        self.cameraBind()

        self.accept_events()

    def cheak_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return 0, -1
        
        elif angle >= 20 and angle <= 65:
            return 1, -1
        
        elif angle >= 65 and angle <= 110:
            return 1, 0
        
        elif angle >= 110 and angle <= 155:
            return 1, 1
        
        elif angle >= 155 and angle <= 200:
            return 0, 1
        
        elif angle >= 200 and angle <= 245:
            return -1, 1
        
        elif angle >= 245 and angle <= 290:
            return -1, 0
        
        elif angle >= 290 and angle <= 335:
            return -1, -1
        
        elif angle >= 335 and angle <= 0:
            return 0, -1
        
    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.cheak_dir(angle)

        return from_x + dx, from_y + dy, from_z

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(self.hero.getPos())

        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()

        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()

        self.cameraOn = False

    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('n'+'-repeat', self.turn_left)

        base.accept('w'+'-repeat', self.forward)
        base.accept('s'+'-repeat', self.back)
        base.accept('a'+'-repeat', self.left)
        base.accept('d'+'-repeat', self.right)

        base.accept('e'+'-repeat', self.up)
        base.accept('q'+'-repeat', self.down)

        base.accept('z', self.changeMode)

    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True

    def up(self):
        self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        self.hero.setZ(self.hero.getZ() - 1)

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()

        else:
            self.cameraBind()

    def try_move(self, angle):
        position = self.look_at(angle)

        if self.land.isEmpty(position):
            position = self.land.findHighestEmpty(position)
            self.hero.setPos(position)

        else:
            pos = pos[0], pos[1], pos[2] + 1

            if self.isEmpty(position):
                self.hero.setPos(position)

    def just_move(self, angle):
        position = self.look_at(angle)
        self.hero.setPos(position)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.just_move(angle)

    def forward(self):
        angle = (self.hero.getH() + 0) % 360
        self.move_to(angle)
        
    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)
        
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)
        
    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)
        
