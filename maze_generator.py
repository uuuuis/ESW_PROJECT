import random

def generate_maze(width, height):
    """랜덤한 미로를 생성합니다. width와 height는 미로의 가로 세로 크기입니다."""
    # 미로 배열 초기화 (벽: 1, 길: 0)
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # 시작 위치 초기화 (무작위 좌표 선택 가능)
    start_x, start_y = random.choice(range(1, width, 2)), random.choice(range(1, height, 2))
    maze[start_y][start_x] = 0  # 시작 지점은 길로 설정

    # DFS를 사용해 미로 생성
    stack = [(start_x, start_y)]
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]  # 상하좌우 이동 (두 칸씩)

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)  # 무작위로 방향 선택
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 다음 위치가 유효한 범위 내에 있고, 벽이면 길로 만든다
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == 1:
                maze[ny][nx] = 0  # 이동한 위치를 길로 설정
                maze[y + dy // 2][x + dx // 2] = 0  # 이동 경로의 중간을 길로 설정
                stack.append((nx, ny))
                break
        else:
            stack.pop()  # 더 이상 이동할 곳이 없으면 스택에서 제거

    # 외곽에 벽 추가 (미로 경계 설정)
    for i in range(width):
        maze[0][i] = maze[height - 1][i] = 1
    for j in range(height):
        maze[j][0] = maze[j][width - 1] = 1

    return maze
