import pygame
import math
import numpy
from vector import Vector2D

#Init window
window_width = 320*3
window_height = 180*3
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Inverse kinematics")

# Init variables
chain = [61, 56, 40]
vectors = []
end_effector = Vector2D(0, 0)
pole = Vector2D(0, 0)
maximal_distance = sum(chain)
# Fill array of vectors
for i in range(0, chain.__len__()):
    vectors.append(Vector2D(chain[i], 0))

screen_middle_position = Vector2D(window_width/2, window_height/2)
pole_global = Vector2D(0, 0)
end_effector_global = Vector2D(0, 0)

def check_triangle_validity(a, b, c): 
    return a+b>=c or a+c>=b or b+c>= a or math.isclose(a + b, c) or math.isclose(a + c, b) or math.isclose(b + c, a)

def get_intersections(position1, radius1, position2, radius2):
    # Calculate distance
    distance_vector = position2-position1
    distance = distance_vector.length()

    # Distance = a + b
    a = max((radius1**2 - radius2**2 + distance**2)/(2*distance), 0)

    # Calculate height
    height = math.sqrt(max(radius1**2 - a**2, 0))
    height_vector = Vector2D(-height * distance_vector.sin(), height * distance_vector.cos())

    # Calculate intersections' position
    point = position1 + distance_vector.normalized()*a
    intersection1 = point + height_vector
    intersection2 = point - height_vector

    '''position1_global = Vector2D(position1.x, -position1.y) + screen_middle_position
    position2_global = Vector2D(position2.x, -position2.y) + screen_middle_position
    pygame.draw.circle(window, (255, 255, 255), (int(position1_global.x), int(position1_global.y)), int(radius1), 1)
    pygame.draw.circle(window, (255, 255, 255), (int(position2_global.x), int(position2_global.y)), int(radius2), 1)'''

    return intersection1, intersection2

def find_side(minimal_length, maximal_length, side1, side2):
    for side in numpy.arange(maximal_length, minimal_length, -0.5):
        # print(side, side1, side2, check_triangle_validity(side, side1, side2))
        if check_triangle_validity(side, side1, side2):
            return side
    return 0

def resolve_ik(chain, vectors, end_effector, maximal_distance, pole):
    # Init variables
    new_vectors = []
    # Calculate current side
    if end_effector.length() > maximal_distance:
        end_effector = end_effector.normalized() * maximal_distance
    current_side_vector = end_effector

    for i in range(chain.__len__()-1, 0, -1):
        current_side = current_side_vector.length()
        # Find possible side
        new_side = find_side(0, sum(chain[:i]), chain[i], current_side)
        # Find intersection nearest to the pole
        intersections = []
        if i != 1:
            intersections = get_intersections(current_side_vector, chain[i], Vector2D(0, 0), new_side)
        else:
            intersections = get_intersections(current_side_vector, chain[i], Vector2D(0, 0), chain[0])

        intersection = Vector2D(0, 0)
        if intersections[0]-pole < intersections[1]-pole:
            intersection = intersections[0]
        else:
            intersection = intersections[1]
        # Change vector
        new_vectors.insert(0, current_side_vector - intersection)

        # print(new_vectors.__len__())
        current_side_vector = intersection

    new_vectors.insert(0, current_side_vector)

    return new_vectors

def draw_vectors_chain(window, position, chain, color, width=1, draw_circles=False, radius=1, circle_color=(255, 255, 255)):
        for vector in chain:
            new_vector = Vector2D(vector.x + position.x, -vector.y + position.y)
            pygame.draw.line(window, color, (position.x, position.y), (new_vector.x, new_vector.y), width)  
            if draw_circles:
                pygame.draw.circle(window, circle_color, (position.x, position.y), radius)
                pygame.draw.circle(window, circle_color, (new_vector.x, new_vector.y), radius)

            position = new_vector

# Main loop
fps = 60
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((226, 95, 91))

    if pygame.mouse.get_pressed()[0]:
        end_effector_global = Vector2D(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        end_effector = end_effector_global - screen_middle_position
        end_effector.y *= -1
        vectors = resolve_ik(chain, vectors, end_effector, maximal_distance, pole)
        
    if pygame.mouse.get_pressed()[2]:
        pole_global = Vector2D(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        pole = pole_global - screen_middle_position
        pole.y *= -1

    # draw_vectors_chain(window, screen_middle_position, [end_effector.normalized() * maximal_distance], (15, 153, 113))

    # Draw pole and end effector
    pygame.draw.circle(window, (0, 242, 255), (int(pole_global.x), int(pole_global.y)), 5)
    pygame.draw.circle(window, (15, 153, 113), (int(end_effector_global.x), int(end_effector_global.y)), 5)

    draw_vectors_chain(window, screen_middle_position, vectors, (255, 255, 255), width=7, draw_circles=True, circle_color=(55, 59, 68), radius=7)

    delta_time = clock.tick(fps)

    pygame.display.update()