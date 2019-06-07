import uuid

import PIL

from arcade.arcade_types import Color
from arcade.draw_commands import Texture


class Canvas:
    """Allows user to draw to a canvas and use it as a arcade.Texture."""
    def __init__(self, width: int=0, height: int=0, bg_color: Color=(0, 0, 0, 0)):
        self.width = width
        self.height = height
        self._img = PIL.Image.new("RGBA", (width, height), bg_color)
        self._draw = PIL.ImageDraw.Draw(self._img)

    def draw_circle_filled(self, center_x: float, center_y: float, radius: float,
                           color: Color, num_segments: int = 128):
        x1 = center_x - radius
        y1 = self.height - center_y - radius
        x2 = center_x + radius
        y2 = self.height - center_y + radius

        self._draw.ellipse((x1, y1, x2, y2), fill=color)

    def draw_xywh_rectangle_filled(self, bottom_left_x: float, bottom_left_y: float,
                                   width: float, height: float, color: Color):
        self._draw.rectangle((bottom_left_x,
                              self.height-bottom_left_y,
                              bottom_left_x + width,
                              self.height-bottom_left_y - height), color)

    @property
    def texture(self):
        name = f"{uuid.uuid4().hex}"
        return Texture(name, self._img)
