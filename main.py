import pygame, sys
import random

class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'octopus')
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 3)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
    
    def avanzar(self):
        self.position[0] += random.randint(1, 4)


class Game():
    runners = []
    __posY = (100, 145, 215, 275)
    __names = ("Speedy", "Fishyy", "Rehis", "MocoCoco")
    __startLine = -5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True
                
            self.__screen.blit(self.background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
       
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()