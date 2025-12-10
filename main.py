import warnings
warnings.filterwarnings("ignore")

import pygame, sys
from collections import deque

pygame.init()

# Constants
W,H = 400,400
ROWS,COLS = 7,7
T = W//COLS
FPS = 8

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PATH_COLORS = [(255,100,100),(100,255,100)]  # BFS, Greedy paths

# Maze
MAP = [
[1,1,1,1,1,1,1],
[1,0,0,0,0,0,1],
[1,0,1,0,1,0,1],
[1,0,0,0,0,0,1],
[1,0,1,0,1,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1],
]

dots = [(c,r) for r in range(ROWS) for c in range(COLS) if MAP[r][c]==0]

# Player
px,py = 1,1
score=0

# Ghosts
ghosts = [(5,5),(5,1)]
ghost_counters = [0,0]
ghost_speed = 12
ghost_paths = [[],[]]

# Analysis
bfs_steps = 0
greedy_steps = 0
bfs_distance = 0
greedy_distance = 0
start_time = pygame.time.get_ticks()

# Window
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Pac-Man Mini")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,25)

# Load Images
pacman_img = pygame.image.load("pacman.png")
pacman_img = pygame.transform.scale(pacman_img, (T, T))

ghost_imgs = [
    pygame.transform.scale(pygame.image.load("ghost1.png"), (T, T)),
    pygame.transform.scale(pygame.image.load("ghost2.png"), (T, T))
]

# BFS + Greedy Functions
def bfs(start,end):
    queue = deque([start])
    visited = {start:None}
    while queue:
        node = queue.popleft()
        if node==end: break
        x,y = node
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<COLS and 0<=ny<ROWS and MAP[ny][nx]==0 and (nx,ny) not in visited:
                visited[(nx,ny)] = node
                queue.append((nx,ny))
    if end not in visited: return []
    path=[]
    node=end
    while node and node in visited:
        path.append(node)
        node=visited[node]
    path.reverse()
    return path[1:]

def greedy_step(pos,end):
    x,y = pos
    ex,ey = end
    moves = []
    for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=nx<COLS and 0<=ny<ROWS and MAP[ny][nx]==0:
            dist = abs(nx-ex)+abs(ny-ey)
            moves.append((dist,(nx,ny)))
    if not moves: return pos
    moves.sort()
    return moves[0][1]

# GAME LOOP
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Player move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and px>0 and MAP[py][px-1]==0: px-=1
    if keys[pygame.K_RIGHT] and px<COLS-1 and MAP[py][px+1]==0: px+=1
    if keys[pygame.K_UP] and py>0 and MAP[py-1][px]==0: py-=1
    if keys[pygame.K_DOWN] and py<ROWS-1 and MAP[py+1][px]==0: py+=1

    # Collect dots
    if (px,py) in dots:
        dots.remove((px,py))
        score+=10

    # Ghost movement
    for i,(gx,gy) in enumerate(ghosts):
        ghost_counters[i]+=1
        if ghost_counters[i]>=ghost_speed:
            if i==0:  # BFS ghost
                path = bfs((gx,gy),(px,py))
                if path: ghosts[i]=path[0]; bfs_steps+=1
                ghost_paths[i]=path
                bfs_distance=len(path)
            else:     # Greedy ghost
                next_step = greedy_step((gx,gy),(px,py))
                ghosts[i]=next_step
                greedy_steps+=1

                path=[]
                visited=set()
                pos=next_step
                while pos!=(px,py):
                    if pos in visited: break
                    visited.add(pos)
                    pos=greedy_step(pos,(px,py))
                    path.append(pos)
                    if len(path)>50: break
                ghost_paths[i]=path
                greedy_distance=len(path)
            ghost_counters[i]=0

    # Collision or Win
    game_over = any((gx,gy)==(px,py) for gx,gy in ghosts)
    win = not dots

    if game_over or win:
        end_time = pygame.time.get_ticks()
        total_time = end_time - start_time
        # Efficiency
        bfs_eff = bfs_distance / bfs_steps if bfs_steps>0 else 0
        greedy_eff = greedy_distance / greedy_steps if greedy_steps>0 else 0

        # Display results 
        screen.fill(BLACK)
        left_margin = 20
        top = H//2 - 60
        screen.blit(font.render("GAME OVER!" if game_over else "YOU WIN!", True, RED if game_over else YELLOW), (left_margin, top))
        screen.blit(font.render(f"Score: {score}", True, WHITE), (left_margin, top+30))
        screen.blit(font.render(f"BFS Steps: {bfs_steps}       BFS Distance: {bfs_distance}", True, RED), (left_margin, top+60))
        screen.blit(font.render(f"Greedy Steps: {greedy_steps}    Greedy Distance: {greedy_distance}", True, YELLOW), (left_margin, top+90))
        screen.blit(font.render(f"BFS Efficiency: {bfs_eff:.2f}    Greedy Efficiency: {greedy_eff:.2f}", True, WHITE), (left_margin, top+120))
        screen.blit(font.render(f"Total Time (ms): {total_time}", True, WHITE), (left_margin, top+150))
        pygame.display.flip()
        pygame.time.wait(15000)
        pygame.quit()
        sys.exit()

    # Draw
    screen.fill(BLACK)
    for r in range(ROWS):
        for c in range(COLS):
            if MAP[r][c]==1:
                pygame.draw.rect(screen,BLUE,(c*T,r*T,T,T))
    for d in dots:
        pygame.draw.circle(screen,WHITE,(d[0]*T+T//2,d[1]*T+T//2),T//6)

    screen.blit(pacman_img,(px*T,py*T))
    for i,(gx,gy) in enumerate(ghosts):
        screen.blit(ghost_imgs[i],(gx*T,gy*T))
    for i,color in enumerate(PATH_COLORS):
        for pos in ghost_paths[i]:
            pygame.draw.rect(screen,color,(pos[0]*T,pos[1]*T,T,T),2)

    # Display Score & Steps during play
    screen.blit(font.render(f"Score: {score}", True, WHITE), (5,5))
    screen.blit(font.render(f"BFS Steps: {bfs_steps}       BFS Distance: {bfs_distance}", True, RED), (5,25))
    screen.blit(font.render(f"Greedy Steps: {greedy_steps}    Greedy Distance: {greedy_distance}", True, YELLOW), (5,45))

    pygame.display.flip()