import time
from joystick import Joystick
from character import Character
from obstacle import Obstacle
from PIL import Image, ImageDraw, ImageFont


def create_stage(stage_number, joystick_width, joystick_height):
    cell_size = joystick_width // 10
    
    if stage_number == 1:
        maze_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        obstacles = [  ]
        start_position = [0 * cell_size, 5 * cell_size]
        goal_position = [9 * cell_size, 5 * cell_size]
    
    elif stage_number == 2:
        maze_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        obstacles = [
            Obstacle([3 * cell_size, 4 * cell_size], [6 * cell_size, 4 * cell_size], cell_size - 8, speed=1),
            Obstacle([5 * cell_size, 6 * cell_size], [8 * cell_size, 6 * cell_size], cell_size - 8, speed=1),
            Obstacle([0 * cell_size, 2 * cell_size], [3 * cell_size, 2 * cell_size], cell_size - 8, speed=1),
        ]
        start_position = [2 * cell_size, 8 * cell_size]
        goal_position = [8 * cell_size, 1 * cell_size]
        
        

    elif stage_number == 3:
        maze_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        obstacles = [
            Obstacle([2 * cell_size, 2 * cell_size], [4 * cell_size, 2 * cell_size], cell_size - 8, speed=2),
            Obstacle([6 * cell_size, 3 * cell_size], [6 * cell_size, 5 * cell_size], cell_size - 8, speed=2),
            Obstacle([2 * cell_size, 6 * cell_size], [2 * cell_size, 8 * cell_size], cell_size - 8, speed=2),
        ]
        start_position = [1 * cell_size, 7 * cell_size]
        goal_position = [7 * cell_size, 1 * cell_size]
        
    elif stage_number == 4:
        maze_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        obstacles = [
            Obstacle([1 * cell_size, 2 * cell_size], [1 * cell_size, 7 * cell_size], cell_size - 8, speed=4),
            Obstacle([3 * cell_size, 2 * cell_size], [3 * cell_size, 7 * cell_size], cell_size - 8, speed=4),
            Obstacle([5 * cell_size, 2 * cell_size], [5 * cell_size, 7 * cell_size], cell_size - 8, speed=4),
            Obstacle([7 * cell_size, 2 * cell_size], [7 * cell_size, 7 * cell_size], cell_size - 8, speed=4),
        ]
        start_position = [0 * cell_size, 5 * cell_size]
        goal_position = [9 * cell_size, 5 * cell_size]
        

    elif stage_number == 5:
        maze_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        obstacles = [
            Obstacle([3 * cell_size, 2 * cell_size], [5 * cell_size, 2 * cell_size], cell_size - 8, speed=2),
            Obstacle([6 * cell_size, 4 * cell_size], [6 * cell_size, 7 * cell_size], cell_size - 8, speed=2),
            Obstacle([6 * cell_size, 6 * cell_size], [6 * cell_size, 7 * cell_size], cell_size - 8, speed=2),
            Obstacle([7 * cell_size, 3 * cell_size], [8 * cell_size, 3 * cell_size], cell_size - 8, speed=2),
        ]
        start_position = [1 * cell_size, 8 * cell_size]
        goal_position = [8 * cell_size, 1 * cell_size]


    return maze_map, obstacles, start_position, goal_position


def show_game_over_message(joystick):
    # 게임 종료 메시지 배경 설정
    width, height = joystick.width, joystick.height
    message_background = Image.new("RGB", (width, height), (0, 0, 0))  # 검은색 배경
    draw = ImageDraw.Draw(message_background)

    # 폰트 설정
    try:
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        font = ImageFont.truetype(font_path, 24)  # 글씨 크기 24
    except IOError:
        print("Font not found. Exiting...")
        exit(1)

    # 표시할 메시지
    message = "Congratulation!\nGame Clear!"
    text_color = (255, 255, 255)  # 흰색

    # 메시지 줄 나누기 및 텍스트 크기 계산
    lines = message.split("\n")
    total_text_height = 0
    line_dimensions = []

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)  # 텍스트 크기를 Bounding Box로 계산
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        total_text_height += text_height + 10  # 줄 간격 포함
        line_dimensions.append((text_width, text_height))

    # 텍스트를 화면 중앙에 정렬
    current_y = (height - total_text_height) // 2
    for line, (text_width, text_height) in zip(lines, line_dimensions):
        x = (width - text_width) // 2
        draw.text((x, current_y), line, font=font, fill=text_color)
        current_y += text_height + 10

    # 메시지 표시
    joystick.disp.image(message_background)
    time.sleep(3) 


def main():
    joystick = Joystick()
    character = Character(joystick.width, joystick.height)

    for stage in range(1, 6):
        maze_map, obstacles, start_position, goal_position = create_stage(
            stage, joystick.width, joystick.height
        )
        character.set_position(start_position)

        background = Image.new("RGB", (joystick.width, joystick.height), (255, 255, 255))
        background_draw = ImageDraw.Draw(background)
        cell_size = joystick.width // len(maze_map[0])

        for y, row in enumerate(maze_map):
            for x, cell in enumerate(row):
                if cell == 1:
                    x0 = x * cell_size
                    y0 = y * cell_size
                    background_draw.rectangle(
                        [x0, y0, x0 + cell_size, y0 + cell_size], fill=(0, 0, 0)
                    )

        # 목표 지점을 녹색 사각형으로 표시
        goal_size = cell_size - 3
        goal_x, goal_y = goal_position[0], goal_position[1]
        background_draw.rectangle(
            [goal_x, goal_y, goal_x + goal_size, goal_y + goal_size], fill=(0, 255, 0)
        )

        joystick.disp.image(background)

        stage_cleared = False

        while not stage_cleared:
            command = None
            if not joystick.button_U.value:
                command = "up"
            elif not joystick.button_D.value:
                command = "down"
            elif not joystick.button_L.value:
                command = "left"
            elif not joystick.button_R.value:
                command = "right"

            character.move(command)

            collision = False
            for y, row in enumerate(maze_map):
                for x, cell in enumerate(row):
                    if cell == 1:
                        wall_box = [
                            x * cell_size,
                            y * cell_size,
                            (x + 1) * cell_size,
                            (y + 1) * cell_size,
                        ]
                        if character.collides_with(wall_box):
                            collision = True
                            break
                if collision:
                    break

            for obstacle in obstacles:
                obstacle.update_position()
                if obstacle.collides_with(character.position):
                    collision = True
                    break

            if collision:
                character.set_position(start_position)


            
            # 목표 도달 여부 확인 (goal_size 추가 전달)
            if character.is_at_goal(goal_position, goal_size):
                 stage_cleared = True
                 break

            frame = background.copy()
            frame_draw = ImageDraw.Draw(frame)

            character.draw(frame_draw)
            for obstacle in obstacles:
                obstacle.draw(frame_draw)

            joystick.disp.image(frame)
            time.sleep(0.01)

    show_game_over_message(joystick)


if __name__ == "__main__":
    main()
