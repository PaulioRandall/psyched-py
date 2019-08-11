#!/usr/bin/env python

"""
This code is copyrighted work by Paul Williams.
Distributed under the BSD-3-Clause license available:
    https://opensource.org/licenses/BSD-3-Clause
"""


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import randint


class WaterMarkerTypeError(TypeError):
    """
    Raised to signal an invalid argument type to a function or method.
    """


class WaterMarkerValueError(ValueError):
    """
    Raised to signal an argument with an invalid argument value.
    """


class Corner:
    """
    Represents the corners of a rectangle.
    """

    _top_left = (0, 0)
    _bottom_left = (0, 1)
    _top_right = (1, 0)
    _bottom_right = (1, 1)

    """
    Gets the top left corner representation.
     
    Returns:
        Top left corner representation.
    """
    @staticmethod
    def top_left():
        return Corner._top_left

    """
    Gets the top right corner representation.

    Returns:
        Top right corner representation.
    """
    @staticmethod
    def top_right():
        return Corner._top_right

    """
    Gets the bottom left corner representation.

    Returns:
        Bottom left corner representation.
    """
    @staticmethod
    def bottom_left():
        return Corner._bottom_left

    """
    Gets the bottom right corner representation.

    Returns:
        Bottom right corner representation.
    """
    @staticmethod
    def bottom_right():
        return Corner._bottom_right

    """
    Validates a corner argument.
    
    Args:
        corner: The corner value to validate.

    Raises:
        WaterMarkerTypeError: If the corner parameter has not been
        provided or is not a corner value from the Corner class.
    """
    @staticmethod
    def validate(corner):
        if corner is None:
            raise WaterMarkerTypeError(
                "A corner value must be provided")

        if not isinstance(corner, tuple):
            raise WaterMarkerTypeError(
                "Only corner values from the Corner class are"
                " valid")

        if corner is not Corner._top_left\
            and corner is not Corner._top_right\
            and corner is not Corner._bottom_left\
                and corner is not Corner._bottom_right:

            raise WaterMarkerTypeError(
                "Only corner values from the Corner class are"
                " valid")


class Edge:
    """
    Represents the edges of a rectangle.
    """

    _left = (0, 0.5)
    _right = (1, 0.5)
    _top = (0.5, 0)
    _bottom = (0.5, 1)

    """
    Gets the left edge representation.

    Returns:
        Left edge representation.
    """
    @staticmethod
    def left():
        return Edge._left

    """
    Gets the right edge representation.

    Returns:
        Right edge representation.
    """
    @staticmethod
    def right():
        return Edge._right

    """
    Gets the top edge representation.

    Returns:
        Top edge representation.
    """
    @staticmethod
    def top():
        return Edge._top

    """
    Gets the bottom edge representation.

    Returns:
        Bottom edge representation.
    """
    @staticmethod
    def bottom():
        return Edge._bottom

    """
    Validates an edge argument.

    Args:
        edge: The edge value to validate.

    Raises:
        WaterMarkerTypeError: If the edge parameter has not been
        provided or is not an edge value from the Edge class.
    """
    @staticmethod
    def validate(edge):
        if edge is None:
            raise WaterMarkerTypeError(
                "An edge value must be provided")

        if not isinstance(edge, tuple):
            raise WaterMarkerTypeError(
                "Only edge values from the Edge class are"
                " valid")

        if edge is not Edge._left\
                and edge is not Edge._right\
                and edge is not Edge._top\
                and edge is not Edge._bottom:
            raise WaterMarkerTypeError(
                "Only edge values from the Edge class are"
                " valid")


class TextualWaterMarker(object):
    """
    Applies textual watermarks to an image using a functional style
    interface.

    TODO:
        Implement apply_lattice
        Implement reversed text
    """

    _img = None
    _font_file = "Arial_Bold.ttf"
    _size_pt = 20
    _rgb_colour = (0, 0, 0)
    _degrees = 0
    _reverse = False
    _margin = 0

    """
    Initialiser.
    
    Args:
        img: Pillow Image to watermark.
        
    Raises:
        WaterMarkerTypeError: If the image parameter has not been
        provided or is not of the correct type.
    """
    def __init__(self, img):
        if img is None:
            raise WaterMarkerTypeError(
                "An image must be provided")

        if not isinstance(img, Image.Image):
            raise WaterMarkerTypeError(
                "The image parameter must be a Pillow Image")

        self._img = img

    """
    Gets the image with any applied watermarks.

    Returns:
        The image.
    """
    def collect(self):
        return self._img

    """
    Sets the font file name containing the font typeface to use.
    
    Args:
        font_file: Font file name.
        
    Returns:
        Self; instance that received the invocation.
        
    Raises:
        WaterMarkerTypeError: If the font file parameter has not been
        provided or is not of the correct type.
        WaterMarkerValueError: If the font file parameter is empty. 
    """
    def font(self, font_file):
        if font_file is None:
            raise WaterMarkerTypeError(
                "A font file must be provided")

        if not isinstance(font_file, str):
            raise WaterMarkerTypeError(
                "The image parameter must be a Pillow Image")

        if font_file.strip() == "":
            raise WaterMarkerValueError(
                "The font file cannot be empty")

        self._font_file = font_file
        return self

    """
    Sets the font size.

    Args:
        size_pt: Font size in points (pt).

    Returns:
        Self; instance that received the invocation.
        
    Raises:
        WaterMarkerTypeError: If the font size parameter has not been
        provided or is not of the correct type.
        WaterMarkerValueError: If the font size parameter is less than
        1pt.
    """
    def size(self, size_pt):
        if size_pt is None:
            raise WaterMarkerTypeError(
                "A font size must be provided")

        if not isinstance(size_pt, int):
            raise WaterMarkerTypeError(
                "The font size parameter must be an integer")

        if size_pt <= 0:
            raise WaterMarkerValueError(
                "The font size must be greater than 0 (Zero)")

        self._size_pt = size_pt
        return self

    """
    Sets the font colour.

    Args:
        rgb_colour: Font colour as a (red, green, blue) tuple.

    Returns:
        Self; instance that received the invocation.
        
    Raises:
        WaterMarkerTypeError: If the colour tuple has not been
        provided or is not of the correct type.
        WaterMarkerValueError: If the colour tuple has the wrong
        number of values, a tuple value is less than 0 or a tuple value
        is greater than 255.
    """
    def colour(self, rgb_colour):
        if rgb_colour is None:
            raise WaterMarkerTypeError(
                "A colour tuple must be provided")

        if not isinstance(rgb_colour, tuple):
            raise WaterMarkerTypeError(
                "The colour parameter must be a tuple")

        if len(rgb_colour) != 3:
            raise WaterMarkerValueError(
                "The colour tuple must have a length of 3")

        for colour in rgb_colour:
            if not isinstance(colour, int):
                raise WaterMarkerTypeError(
                    "Each tuple value must be an integer")
            elif colour < 0 or colour > 255:
                raise WaterMarkerValueError(
                    "Each tuple value must be between 0 (inclusive) and"
                    " 255 (inclusive)")

        self._rgb_colour = rgb_colour
        return self

    """
    Sets the rotation anticlockwise of the text relative to it's natural
    alignment; in this case the texts natural alignment is horizontal.

    Args:
        degrees: Degrees in which to rotate the text anticlockwise.

    Returns:
        Self; instance that received the invocation.
        
    Raises:
        WaterMarkerTypeError: If the rotation has not been provided or
        is not of the correct type.
        WaterMarkerValueError: If the rotation is negative or greater
        than 360.
    """
    def rotation(self, degrees):
        if degrees is None:
            raise WaterMarkerTypeError(
                "A rotation in degrees must be provided")

        if not isinstance(degrees, int):
            raise WaterMarkerTypeError(
                "The rotation must be in degrees as an integer")

        if degrees < 0:
            raise WaterMarkerValueError(
                "The rotation must be 0 (Zero) or greater")

        if degrees > 360:
            raise WaterMarkerValueError(
                "The rotation must be 360 or less")

        if degrees == 360:
            degrees = 0

        self._degrees = degrees
        return self

    """
    Sets the direction of the text. True if the text that reads left to
    right should be reversed so that it reads right to left (assuming no
    rotation).

    Args:
        reverse: True if the text should be reversed.

    Returns:
        Self; instance that received the invocation.
        
    Raises:
        WaterMarkerTypeError: If the reverse parameter has not been
        provided or is not of the correct type.
    """
    def reverse(self, reverse):
        if reverse is None:
            raise WaterMarkerTypeError(
                "A True/False reverse state must be provided")

        if not isinstance(reverse, bool):
            raise WaterMarkerTypeError(
                "The reverse must be a boolean")

        self._reverse = reverse
        return self

    """
    Sets the text margin to apply for applicable application methods.

    Args:
        margin: Margin to apply.

    Returns:
        Self; instance that received the invocation.

    Raises:
        WaterMarkerTypeError: If the margin parameter is none or is not
        of the correct type.
    """
    def margin(self, margin):
        if margin is None:
            raise WaterMarkerTypeError(
                "Margin value must not be none")

        if not isinstance(margin, int):
            raise WaterMarkerTypeError(
                "The margin must be an integer")

        self._margin = margin
        return self

    """
    Applies the watermark at the centre of the image.

    Args:
        text: Text to apply as the watermark.

    Returns:
        Watermarked image.
        
    Raises:
        WaterMarkerTypeError: If the text is none or is not a
        string.
        WaterMarkerValueError: If the text is empty or only contains
        white space.
    """
    def apply_centre(self, text):
        self._validate_text(text)
        text = text.strip()

        text_img = self._prepare_text_img(text)

        img_width, img_height = self._img.size
        text_img_width, text_img_height = text_img.size

        pos_x = (img_width / 2) - (text_img_width / 2)
        pos_y = (img_height / 2) - (text_img_height / 2)

        self._img.paste(text_img, (int(pos_x), int(pos_y)), text_img)
        return self._img

    """
    Applies the watermark at a corner of the image. The whole watermark
    will be printed inside the image providing the image is larger than
    the watermark.

    Args:
        text: Text to apply as the watermark.
        corner: Corner to apply the watermark too.

    Returns:
        Watermarked image.
        
    Raises:
        WaterMarkerTypeError: If the text is none, the text is not a
        string, the corner has not been provided or the corner is not a
        corner attribute from the Corner class.
        WaterMarkerValueError: If the text is empty or only contains
        white space.
    """
    def apply_corner(self, text, corner):
        self._validate_text(text)
        Corner.validate(corner)
        text = text.strip()

        text_img = self._prepare_text_img(text)

        img_width, img_height = self._img.size
        text_img_width, text_img_height = text_img.size
        x_fraction, y_fraction = corner

        pos_x = (img_width * x_fraction)
        pos_y = (img_height * y_fraction)

        if pos_x > 0:
            pos_x -= text_img_width + self._margin
        else:
            pos_x = self._margin

        if pos_y > 0:
            pos_y -= text_img_height + self._margin
        else:
            pos_y = self._margin

        self._img.paste(text_img, (int(pos_x), int(pos_y)), text_img)
        return self._img

    """
    Applies the watermark at the edge of the image. The whole watermark
    will be printed inside the image providing the image is larger than
    the watermark.

    Args:
        text: Text to apply as the watermark.
        edge: Edge to apply the watermark too.

    Returns:
        Watermarked image.
        
    Raises:
        WaterMarkerTypeError: If the text is none, the text is not a
        string, the edge has not been provided or the edge is not an
        edge attribute from the Edge class.
        WaterMarkerValueError: If the text is empty or only contains
        white space.
    """
    def apply_edge(self, text, edge):
        self._validate_text(text)
        Edge.validate(edge)
        text = text.strip()

        text_img = self._prepare_text_img(text)

        img_width, img_height = self._img.size
        text_img_width, text_img_height = text_img.size
        x_fraction, y_fraction = edge

        pos_x = (img_width * x_fraction)
        pos_y = (img_height * y_fraction)

        if x_fraction not in (0, 1):
            pos_x -= (text_img_width / 2)
        elif x_fraction == 1:
            pos_x -= text_img_width + self._margin
        else:
            pos_x += self._margin

        if y_fraction not in (0, 1):
            pos_y -= (text_img_height / 2)
        elif y_fraction == 1:
            pos_y -= text_img_height + self._margin
        else:
            pos_y += self._margin

        self._img.paste(text_img, (int(pos_x), int(pos_y)), text_img)
        return self._img

    """
    Applies the watermark at a point relative to the top left of the
    image.

    Args:
        text: Text to apply as the watermark.
        x_pos_px: X position in pixels relative to the left edge of the
        image.
        y_pos_px: Y position in pixels relative to the top edge of the
        image.

    Returns:
        Watermarked image.
        
    Raises:
        WaterMarkerTypeError: If the text is none, the text is not a
        string, the X position is none, the Y position is none, the X
        position is not an integer, the Y position is not an integer.
        WaterMarkerValueError: If the text is empty or only contains
        white space.
    """
    def apply_absolute(self, text, x_pos_px, y_pos_px):
        self._validate_text(text)
        text = text.strip()

        if x_pos_px is None:
            raise WaterMarkerTypeError(
                "An X position in pixels must be provided")

        if y_pos_px is None:
            raise WaterMarkerTypeError(
                "A Y position in pixels must be provided")

        if not isinstance(x_pos_px, int):
            raise WaterMarkerTypeError(
                "The X position must be an integer")

        if not isinstance(y_pos_px, int):
            raise WaterMarkerTypeError(
                "The Y position must be an integer")

        text_img = self._prepare_text_img(text)

        self._img.paste(text_img, (int(x_pos_px), int(y_pos_px)),
                        text_img)
        return self._img

    """
    Applies the watermark at a point relative to the top left of the
    image.

    Args:
        text: Text to apply as the watermark.
        x_from_left: X position as a percentage relative to the left
        edge of the image.
        y_from_top: Y position as a percentage relative to the top
        edge of the image.

    Returns:
        Watermarked image.
        
    Raises:
        WaterMarkerTypeError: If the text is none, the text is not a
        string, X from left is none, Y from top is none, X from left is 
        not an integer, Y from top is not an integer.
        WaterMarkerValueError: If the text is empty or only contains
        white space.
    """
    def apply_percent(self, text, x_from_left, y_from_top):
        self._validate_text(text)
        text = text.strip()

        if x_from_left is None:
            raise WaterMarkerTypeError(
                "A left indent amount as a percentage must be provided")

        if y_from_top is None:
            raise WaterMarkerTypeError(
                "A top indent amount as a percentage must be provided")

        if not isinstance(x_from_left, int):
            raise WaterMarkerTypeError(
                "The left indent must be an integer")

        if not isinstance(y_from_top, int):
            raise WaterMarkerTypeError(
                "The top indent must be an integer")

        text_img = self._prepare_text_img(text)

        img_width, img_height = self._img.size

        pos_x = (img_width / 100.0) * x_from_left
        pos_y = (img_height / 100.0) * y_from_top

        self._img.paste(text_img, (int(pos_x), int(pos_y)), text_img)
        return self._img

    """
    Applies the watermark at a random point on the image without
    overflowing any edges.

    Args:
        text: Text to apply as the watermark.
        quantity: Number of times to apply the watermark. Defaults to 1.

    Returns:
        Watermarked image.
        
    Raises:
        WaterMarkerTypeError: If the text is none, the text is not a
        string, the quantity is none or the quantity is not an integer.
        WaterMarkerValueError: If the text is empty, only contains
        white space or the quantity is less than 1.
    """
    def apply_random(self, text, quantity=1):
        self._validate_text(text)
        text = text.strip()

        if quantity is None:
            raise WaterMarkerTypeError("The quantity must not be none")

        if not isinstance(quantity, int):
            raise WaterMarkerTypeError("The quantity must be an "
                                       "integer")

        if quantity < 1:
            raise WaterMarkerValueError("The quantity must be 1 or "
                                        "greater")

        text_img = self._prepare_text_img(text)

        img_width, img_height = self._img.size
        text_img_width, text_img_height = text_img.size

        max_x = (img_width - text_img_width) - self._margin
        max_y = (img_height - text_img_height) - self._margin

        for count in range(quantity):
            pos_x = randint(self._margin, int(max_x))
            pos_y = randint(self._margin, int(max_y))

            self._img.paste(text_img, (int(pos_x), int(pos_y)),
                            text_img)

        return self._img

    """
    Applies the watermark, multiple times both horizontally and
    vertically, across the image as a lattice or grid.

    Args:
        text: Text to apply as the watermark.
        horizontal_margin: Space between watermarks horizontally.
        vertical_margin: Space between watermarks vertically.
        horizontal_start_margin: Space between left edge and first
        watermark. Set as the horizontal margin by default.
        vertical_start_margin: Space between top edge and first
        watermark. Set as the vertical margin by default.

    Returns:
        Watermarked image.
        
    Raises:
        WaterMarkerTypeError: If the text is none, the text is not a
        string, any non-start margin is none, any margin is not an
        integer.
        WaterMarkerValueError: If the text is empty, only contains
        white space, the horizontal margin is less than one or the
        vertical margin is less than one.
    """
    def apply_lattice(self, text,
                      horizontal_margin,
                      vertical_margin,
                      horizontal_start_margin=None,
                      vertical_start_margin=None):

        self._validate_text(text)
        text = text.strip()

        if horizontal_margin is None:
            raise WaterMarkerTypeError("Horizontal margin must not be "
                                       "none")

        if vertical_margin is None:
            raise WaterMarkerTypeError("Vertical margin must not be "
                                       "none")

        if not isinstance(horizontal_margin, int):
            raise WaterMarkerTypeError("Horizontal margin must be an "
                                       "integer")

        if not isinstance(vertical_margin, int):
            raise WaterMarkerTypeError("Vertical margin must be an "
                                       "integer")

        if horizontal_margin < 1:
            raise WaterMarkerValueError("Horizontal margin must be"
                                        " greater than 0 (zero)")

        if vertical_margin < 1:
            raise WaterMarkerValueError("Vertical margin must be"
                                        " greater than 0 (zero)")

        if horizontal_start_margin is None:
            horizontal_start_margin = horizontal_margin

        if vertical_start_margin is None:
            vertical_start_margin = vertical_margin

        if not isinstance(horizontal_start_margin, int):
            raise WaterMarkerTypeError("Horizontal start margin must be"
                                       " an integer")

        if not isinstance(vertical_start_margin, int):
            raise WaterMarkerTypeError("Vertical start margin must be"
                                       " an integer")

        text_img = self._prepare_text_img(text)

        img_width, img_height = self._img.size
        text_img_width, text_img_height = text_img.size

        y = vertical_start_margin
        while y < img_height:

            x = horizontal_start_margin
            while x < img_width:
                self._img.paste(text_img, (int(x), int(y)), text_img)
                x += text_img_width + horizontal_margin

            y += text_img_height + vertical_margin

        return self._img

    '''
    Prepares the text image that will overlay the user image.

    Args:
        text: Text to apply as the watermark.

    Returns:
        Text as an image. 
    '''
    def _prepare_text_img(self, text):
        font = ImageFont.truetype(self._font_file, self._size_pt)
        text_width, text_height = font.getsize(text)

        transparent = (0, 0, 0, 0)
        text_as_img = Image.new('RGBA',
                                (text_width, text_height), transparent)

        img_editor = ImageDraw.Draw(text_as_img)
        img_editor.text((0, 0), text, self._rgb_colour, font=font)

        if self._reverse:
            text_as_img = text_as_img.transpose(Image.FLIP_LEFT_RIGHT)

        if self._degrees is not 0:
            text_as_img = text_as_img.rotate(self._degrees, expand=1)

        return text_as_img

    '''
    Validates the watermark text.
    
    Args:
        text: Watermark text to validate.
    
    Raises:
        WaterMarkerTypeError: If the text is none or is not a
        string.
        WaterMarkerValueError: If the text is empty or only contains
        white space.
    '''
    @staticmethod
    def _validate_text(text):
        if text is None:
            raise WaterMarkerTypeError(
                "Some watermark text must be provided")

        if not isinstance(text, str):
            raise WaterMarkerTypeError(
                "The text parameter must be a string")

        if text.strip() == "":
            raise WaterMarkerValueError(
                "The watermark text cannot be empty")

"""
Simple example of usage.
"""
if __name__ == "__main__":

    image_path = raw_input("Image file to watermark: ")
    #image_path = "../../_temp/ae2.jpg"

    try:
        image = Image.open(image_path)
    except IOError:
        error_text = "File '{}' does not exist, is not an image or" \
                     " does not have a supported media type"
        raise Exception(error_text.format(image_path))

    water_marker = TextualWaterMarker(image)
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (175, 175, 175)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    water_marker.font("Comic_Sans_MS_Bold.ttf").margin(0)

    water_marker.colour(red).size(14)
    water_marker.apply_lattice("LATTICE", 64, 64, 16, 32)

    water_marker.colour(grey).size(16)
    water_marker.apply_random("RANDOM", 5)

    water_marker.colour(white).size(20)
    water_marker.apply_centre("CENTRE")

    water_marker.reverse(True).rotation(90).colour(blue)
    water_marker.apply_edge("RIGHT-EDGE-REVERSED", Edge.right())
    water_marker.reverse(False).rotation(0).colour(white)

    water_marker.apply_absolute("(X: 300, Y: 60)", 300, 60)
    water_marker.apply_percent("(X: 20%, Y: 80%)", 20, 80)

    water_marker.rotation(45)
    water_marker.apply_corner("TOP-LEFT-CORNER", Corner.top_left())
    water_marker.apply_corner("BOTTOM-RIGHT-CORNER",
                              Corner.bottom_right())

    water_marker.rotation(325)
    water_marker.apply_corner("BOTTOM-LEFT-CORNER",
                              Corner.bottom_left())
    water_marker.apply_corner("TOP-RIGHT-CORNER",
                              Corner.top_right())

    image.show()
