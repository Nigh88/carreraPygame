import pygame
import sys

class Game():
    
    corredores = []
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
        
        self.runner = pygame.image.load("images/smalball.png")
       
    def competir(self):
        
        x = 0
        gameOver = False
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()
            
            x += 3
            if x >= 250:
                gameOver = True
                
        pygame.quit()
        sys.exit()
       
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()