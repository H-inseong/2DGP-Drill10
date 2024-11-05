import pico2d
import game_framework
import logo_mode
import play_mode

pico2d.open_canvas()

#game_framework.run(logo_mode)
game_framework.run(play_mode)

pico2d.close_canvas()
