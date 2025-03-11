# Copyright (C) 2025 <UTN FRA>
#
# Author: Facundo Falcone <f.falcone@sistemas-utnfra.com.ar>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame as pg
from .widget import Widget

class TextBox(Widget):
    
    def __init__(self, x, y, text, screen, font_path: str, font_size = 25, color: tuple = (255,0,0), on_click = None, on_click_param = None):
        super().__init__(x, y, text, screen, font_size)
        self.font = pg.font.Font(font_path, self.font_size)
        self.image = self.font.render(self.text, True, color)
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # self.click_option_sfx = pg.mixer.Sound(SONIDO_SELECT)
        # self.click_option_sfx.set_volume(0.3)
        
        self.on_click = on_click
        self.on_click_param = on_click_param
        
        self.write_on = True
        self.writing = ''
        self.image_writing = self.font.render(self.writing, True, color)
        self.rect_writing = self.image_writing.get_rect()
        self.rect_writing.center = (x, y)
    
    def write_on_box(self, event_list: list):
        for evento in event_list:
            if evento.type == pg.KEYDOWN and self.write_on:
                if evento.key == pg.K_BACKSPACE:
                    self.writing = self.writing[:-1]
                else:
                    self.writing += evento.unicode
                # self.click_option_sfx.play()
    
    def draw(self):
        super().draw()
        self.image.blit(self.screen, (self.rect_writing.x, self.rect_writing.y))
    
    def update(self, event_list: list):
        self.draw()
        self.write_on_box(event_list)