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

    def look_at(self):
        pass

    def cheak_dear(self):
        pass

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

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()

        else:
            self.cameraBind()