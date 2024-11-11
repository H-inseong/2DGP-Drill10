from pico2d import *
import game_framework

import game_world
from bird import Bird
from grass import Grass
from boy import Boy

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    global grass
    global birds

    grass = Grass()
    game_world.add_object(grass, 0)

    birds = [Bird() for i in range(10)]
    for i in range(10):
        game_world.add_object(birds[i], 0)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

