# 이것은 각 상태들을 객체로 구현한 것임.
from random import randint

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, load_font
from state_machine import *
from ball import Ball
import game_world
import game_framework

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    def __init__(self):
        self.font =load_font('ENCR10B.TTF', 16)
        self.x, self.y = randint(0, 800), randint(90, 600)
        self.face_dir = 1
        self.frame = 0
        self.action = 0
        self.image = load_image('bird_animation.png')

    def update(self):
        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1600 or self.x < 0:
            self.face_dir = -self.face_dir
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * 180, (3 - self.action) * 160, 180, 160, self.x, self.y, 50, 50)
            if int(self.frame) == 4 or (int(self.frame) == 3 and self.action == 2):
                self.frame = 0
                self.action = (self.action+1) % 3
        elif self.face_dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 180, (3 - self.action) * 160, 180, 160,0, 'h', self.x, self.y, 50, 50)
            if int(self.frame) == 4 or (int(self.frame) == 3 and self.action == 2):
                self.frame = 0
                self.action = (self.action +1) % 3

# 새의 크기 가로 크기 90, 세로 크기 80 픽셀
#속도 초당
#스프라이트 크기//????