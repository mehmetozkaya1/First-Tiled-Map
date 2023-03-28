import pygame, sys
from pytmx.util_pygame import load_pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
sprite_group = pygame.sprite.Group()
pygame.display.set_caption("First Map")

tmx_data = load_pygame('TilesetGrass/firstMap.tmx')

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

print(tmx_data.layers)

for layer in tmx_data.visible_layers:
    if hasattr(layer,'data'):
        for x,y,surf in layer.tiles():
            pos = (x * 16, y * 16)
            Tile(pos=pos,surf=surf, groups= sprite_group)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    sprite_group.draw(screen)
    pygame.display.update()