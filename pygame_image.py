import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_fliped = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    tmr = 0
    bg_img_x_coordinate = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        bg_img_x_coordinate = -(tmr % 3200)
        screen.blit(bg_img, [bg_img_x_coordinate, 0])
        screen.blit(bg_img_fliped, [bg_img_x_coordinate + 1600, 0])
        screen.blit(bg_img, [bg_img_x_coordinate + 3200, 0])
        screen.blit(bg_img_fliped, [bg_img_x_coordinate + 4800, 0])

        screen.blit(kk_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()