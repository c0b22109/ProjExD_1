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
    kk_img_rect = kk_img.get_rect()
    kk_img_rect.center = (300, 200)
    tmr = 0
    bg_img_x_coordinate = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        kk_move_val = [-1, 0]

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_move_val[1] -= 1
        if key_lst[pg.K_DOWN]:
            kk_move_val[1] += 1
        if key_lst[pg.K_RIGHT]:
            kk_move_val[0] += 2
        if key_lst[pg.K_LEFT]:
            kk_move_val[0] -= 1

        kk_img_rect.move_ip(kk_move_val)

        bg_img_x_coordinate = -(tmr % 3200)
        screen.blit(bg_img, [bg_img_x_coordinate, 0])
        screen.blit(bg_img_fliped, [bg_img_x_coordinate + 1600, 0])
        screen.blit(bg_img, [bg_img_x_coordinate + 3200, 0])

        screen.blit(kk_img, kk_img_rect)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()