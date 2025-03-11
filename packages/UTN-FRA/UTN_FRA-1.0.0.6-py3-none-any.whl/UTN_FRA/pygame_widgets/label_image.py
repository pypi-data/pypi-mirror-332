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


class ImageLabel(Widget):
    def __init__(self, x: int, y: int, text: str, screen, image_path: str, width: int, height: int, font_path: str, font_size: int, color: tuple = (255,0,0)):
        super().__init__(x, y, text, screen, font_size)

        self.font = pg.font.Font(font_path, self.font_size)
        self.font_color = color
        self.width = width
        self.height = height
        
        self.__set_background(image_path)
        self.img_original = self.image.copy()

        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.render()

    def __set_background(self, image_path: str) -> None:
        aux_image = None
        if image_path:
            aux_image = pg.image.load(image_path)
            aux_image = pg.transform.scale(aux_image, (self.width, self.height))
        else:
            aux_image = pg.Surface((self.width, self.height), masks=(0,0,0))
            # aux_image.set_alpha(0)#Transparente
        self.image = aux_image
            
    
    def render(self):
        self.image.blit(self.img_original, (0, 0))
        image_text = self.font.render(self.text, True, self.font_color)

        media_texto_horizontal = image_text.get_width() / 2
        media_texto_vertical = image_text.get_height() / 2

        media_horizontal = self.width / 2
        media_vertical = self.height / 2
        diferencia_horizontal = media_horizontal - media_texto_horizontal
        diferencia_vertical = media_vertical - media_texto_vertical

        self.image.blit(
            image_text, (diferencia_horizontal, diferencia_vertical)
        )

    def set_text(self, text):
        self.text = text
        self.render()

    def get_text(self):
        return self.text

    def update(self, lista_eventos):
        self.draw()
