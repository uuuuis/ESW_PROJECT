import numpy as np

class Character:
    def __init__(self, width, height):
        self.position = np.array([0, 0, 12, 12])
        self.width = width
        self.height = height
        self.outline = "#FF0000"
        self.speed = 3

    def move(self, command):
        if command == 'up' and self.position[1] > 0:
            self.position[1] -= self.speed
            self.position[3] -= self.speed
        elif command == 'down' and self.position[3] < self.height:
            self.position[1] += self.speed
            self.position[3] += self.speed
        elif command == 'left' and self.position[0] > 0:
            self.position[0] -= self.speed
            self.position[2] -= self.speed
        elif command == 'right' and self.position[2] < self.width:
            self.position[0] += self.speed
            self.position[2] += self.speed

    def draw(self, draw_obj):
        draw_obj.ellipse(self.position.tolist(), outline=self.outline, fill=(0, 0, 0))

    def set_position(self, start_position):
        self.position = np.array([start_position[0], start_position[1], start_position[0] + 12, start_position[1] + 12])

    def collides_with(self, wall_box):
        return (
            self.position[2] > wall_box[0] and self.position[0] < wall_box[2] and
            self.position[3] > wall_box[1] and self.position[1] < wall_box[3]
        )

    def is_at_goal(self, goal_position, goal_size):
        goal_x0, goal_y0 = goal_position
        goal_x1, goal_y1 = goal_x0 + goal_size, goal_y0 + goal_size

        char_x0, char_y0, char_x1, char_y1 = self.position

        return not (
            char_x1 < goal_x0 or char_x0 > goal_x1 or char_y1 < goal_y0 or char_y0 > goal_y1
        )
