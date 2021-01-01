import pygame
import math
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

def get_intersections(position1, radius1, position2, radius2):
    distance_vector = position2-position1
    distance = distance_vector.length()
    # distance = a + b
    a = (radius1**2 - radius2**2 + distance**2)/(2*distance)
    # Calculate height
    height = math.sqrt(radius1**2 - a**2)
    height_vector = Vector2D(-height*distance_vector.sin(), height*distance_vector.cos())

    # Calculate intersection points' coordinates
    point = position1 + distance_vector.normalized()
    intersection1 = point + height_vector
    intersection2 = point - height_vector

    return (intersection1, intersection2)

def find_side():
    pass

def resolve_ik():
    pass

def draw_vectors_chain(window, position, chain):
    pass


'''#Main loop
fps = 60
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_vectors_chain(window, Vector2D(window_width/2, window_height/2), vectors)
    delta_time = clock.tick(fps)/1000'''