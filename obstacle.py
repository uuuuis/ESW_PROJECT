class Obstacle:
    def __init__(self, start_pos, end_pos, cell_size, speed=1):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.current_pos = list(start_pos) 
        self.cell_size = cell_size
        self.speed = speed

        self.direction = [
            1 if end > start else -1 if end < start else 0
            for start, end in zip(self.start_pos, self.end_pos)
        ]


    def update_position(self):
        if self.start_pos == self.end_pos:
            return 

        for i in range(2): 
            if self.start_pos[i] != self.end_pos[i]:

                self.current_pos[i] += self.direction[i] * self.speed

                if self.direction[i] == 1 and self.current_pos[i] >= self.end_pos[i]:
                    self.current_pos[i] = self.end_pos[i]
                    self.direction[i] = -1 

                elif self.direction[i] == -1 and self.current_pos[i] <= self.start_pos[i]:
                    self.current_pos[i] = self.start_pos[i]
                    self.direction[i] = 1 

                self.current_pos[i] = max(self.start_pos[i], min(self.current_pos[i], self.end_pos[i]))

    

    def draw(self, draw_obj):
        x, y = self.current_pos
        draw_obj.rectangle(
            [x, y, x + self.cell_size, y + self.cell_size], fill=(255, 0, 0)
        )

    def collides_with(self, char_box):
        x0, y0, x1, y1 = char_box
        ox0, oy0 = self.current_pos
        ox1, oy1 = ox0 + self.cell_size, oy0 + self.cell_size
        return not (x1 <= ox0 or x0 >= ox1 or y1 <= oy0 or y0 >= oy1)

