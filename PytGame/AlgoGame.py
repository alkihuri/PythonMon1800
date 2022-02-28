from pygame import*
window=display.set_mode((700,500))

background=image.load("fantasyforest.png")
background=transform.scale(background,(100,100))


gameison=True
while gameison:

    window.blit(background,(0,0))



    for i in event.get():
        if i.type==KEYDOWN:
            if i.key==K_x:
                gameison=False