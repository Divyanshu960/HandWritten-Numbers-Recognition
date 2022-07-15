import pygame
from  process_image import get_output_image

# pre defined colors, pen radius and font color
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
draw_on = False
last_pos = (0, 0)
color = (255, 128, 0)
radius = 7
font_size = 500

#image size
width,height = 640,640


# initializing screen
screen = pygame.display.set_mode((width*2, height))
screen.fill(white)
pygame.font.init()



def show_output_image(img):
    surf = pygame.pixelcopy.make_surface(img)
    surf = pygame.transform.rotate(surf, -270)
    surf = pygame.transform.flip(surf, 0, 1)
    screen.blit(surf, (width+2, 0))


def crope(orginal):
    cropped = pygame.Surface((width-5, height-5))
    cropped.blit(orginal, (0, 0), (0, 0, width-5, height-5))
    return cropped


def roundline(srf, color, start, end, radius=1):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(srf, color, (x, y), radius)


def draw_partition_line():
    pygame.draw.line(screen, black, [width, 0], [width,height ], 8)


try:
    while True:
        pygame.display.set_caption('YAIPS')
        Icon = pygame.image.load('gehu.png')
        pygame.display.set_icon(Icon)
        e = pygame.event.wait()# e to get all events
        draw_partition_line()

    
        if(e.type == pygame.MOUSEBUTTONDOWN and e.button == 3):# clear screen
            screen.fill(white)

       
        if e.type == pygame.QUIT: # quit
            raise StopIteration

        
        if(e.type == pygame.MOUSEBUTTONDOWN and e.button != 3):# start drawing
            color = black
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True

        
        if e.type == pygame.MOUSEBUTTONUP and e.button != 3:# stop drawing
            draw_on = False
            fname = "last_image.png"

            img = crope(screen)
            pygame.image.save(img, fname)

            output_img = get_output_image(fname)
            show_output_image(output_img)

        
        if e.type == pygame.MOUSEMOTION: #start drawing line
            if draw_on:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos

        pygame.display.flip()

except StopIteration:
    pass

pygame.quit()
