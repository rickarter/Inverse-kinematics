import pygame
from vector import Vector2D

#Init window
window_width = 320*2
window_height = 180*2
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Inverse kinematics")

# Init variables
chain = [10, 10, 10, 10]
vectors = []
# Fill array of vectors
for i in range(0, chain.__len__()):
    vectors.append(Vector2D(chain[i], 0))

def check_triangle_validity(a, b, c):  
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True  

'''#Main loop
fps = 60
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    delta_time = clock.tick(fps)/1000'''