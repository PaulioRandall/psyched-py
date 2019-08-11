#!/usr/bin/env python

import unittest
from PIL import Image
from project.textual_water_marker import TextualWaterMarker
from project.textual_water_marker import WaterMarkerTypeError
from project.textual_water_marker import WaterMarkerValueError
from project.textual_water_marker import Corner
from project.textual_water_marker import Edge


class WM_Tester(unittest.TestCase):
    """
    Tests the TextualWaterMarker class.
    """

    @staticmethod
    def _create_wm():
        img = Image.new('RGB', (512, 512))
        return TextualWaterMarker(img)

    '''
    __init__
    '''
    def test__init__img_is_image__raises_no_exception(self):
        img = Image.new('RGB', (8, 8))
        TextualWaterMarker(img)
        self.assertTrue(True)

    def test__init__img_is_none__raises_wm_type_error(self):
        img = None
        self.assertRaises(WaterMarkerTypeError, TextualWaterMarker, img)

    def test__init__img_not_image__raises_wm_type_error(self):
        img = "String is a bad type!"
        self.assertRaises(WaterMarkerTypeError, TextualWaterMarker, img)

    '''
    font_file
    '''
    def test__font_file__font_file_is_valid__returns_self(self):
        expected = self._create_wm()
        actual = expected.font("Arial.ttf")
        self.assertIs(expected, actual)

    def test__font_file__font_file_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.font, None)

    def test__font_file__font_file_not_str__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.font, 2017)

    def test__font_file__font_file_is_empty__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.font, " ")

    '''
    font_size
    '''
    def test__font_size__size_pt_is_valid__returns_self(self):
        expected = self._create_wm()
        actual = expected.size(12)
        self.assertIs(expected, actual)

    def test__font_size__size_pt_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.size, None)

    def test__font_size__size_pt_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.size, "bad_typ")

    def test__font_size__size_pt_too_small__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.size, 0)

    '''
    font_colour
    '''
    def test__colour__rgb_colour_is_valid__returns_self(self):
        expected = self._create_wm()
        actual = expected.colour((128, 128, 128))
        self.assertIs(expected, actual)

    def test__colour__rgb_colour_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.colour, None)

    def test__colour__rgb_colour_not_a_tuple__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.colour, "bad_typ")

    def test__colour__rgb_colour_tuple_value_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.colour, (255, "Not int", 255))

    def test__colour__rgb_colour_tuple_len_2__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.colour, (255, 255))

    def test__colour__rgb_colour_tuple_len_4__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.colour,
                          (255, 255, 255, 255))

    def test__colour__rgb_colour_red_lt_zero__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.colour,
                          (-1, 255, 255))

    def test__colour__rgb_colour_green_lt_zero__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.colour,
                          (255, -1, 255))

    def test__colour__rgb_colour_blue_lt_zero__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.colour,
                          (255, 255, -1))

    def test__colour__rgb_colour_red_gt_255__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.colour, (256, 0, 0))

    def test__colour__rgb_colour_green_gt_255__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.colour, (0, 256, 0))

    def test__colour__rgb_colour_blue_gt_255__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.colour, (0, 0, 256))

    '''
    rotate
    '''
    def test__rotation__degrees_is_valid__returns_self(self):
        expected = self._create_wm()
        actual = expected.rotation(225)
        self.assertIs(expected, actual)

    def test__rotation__degrees_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.rotation, None)

    def test__rotation__degrees_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.rotation, "bad_typ")

    def test__rotation__degrees_lt_0__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.rotation, -1)

    def test__rotation__degrees_gt_360__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.rotation, 361)

    '''
    reverse
    '''
    def test__reverse__reverse_is_valid__returns_self(self):
        expected = self._create_wm()
        actual = expected.reverse(True)
        self.assertIs(expected, actual)

    def test__reverse__reverse_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.reverse, None)

    def test__reverse__reverse_not_bool__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.reverse, 2017)

    '''
    margin
    '''
    def test__margin__margin_is_valid__returns_self(self):
        expected = self._create_wm()
        actual = expected.margin(10)
        self.assertIs(expected, actual)

    def test__margin__margin_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.margin, None)

    def test__margin__margin_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.margin, "NOT INT")

    '''
    apply_centre
    '''
    def test__apply_centre__text_is_valid__returns_image(self):
        wm = self._create_wm()
        actual = wm.apply_centre("WATERMARK")
        self.assertIsInstance(actual, Image.Image)

    def test__apply_centre__text_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_centre, None)

    def test__apply_centre__text_is_wrong_type__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_centre, 2017)

    def test__apply_centre__text_is_empty__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_centre, " ")

    '''
    apply_corner
    '''
    def test__apply_corner__valid_params__returns_image(self):
        wm = self._create_wm()
        actual = wm.apply_corner("WATERMARK", Corner.top_left())
        self.assertIsInstance(actual, Image.Image)

    def test__apply_corner__text_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_corner,
                          None, Corner.top_left())

    def test__apply_corner__text_is_wrong_type__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_corner,
                          2017, Corner.top_left())

    def test__apply_corner__text_is_empty__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_corner, " ",
                          Corner.top_left())

    def test__apply_corner__corner_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_corner,
                          "WATERMARK", None)

    def test__apply_corner__corner_is_wrong_type__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_corner,
                          "WATERMARK", 2017)

    def test__apply_corner__corner_not_from_Corner__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_corner,
                          "WATERMARK", (0, 1))

    '''
    apply_edge
    '''
    def test__apply_edge__valid_params__returns_image(self):
        wm = self._create_wm()
        actual = wm.apply_edge("WATERMARK", Edge.left())
        self.assertIsInstance(actual, Image.Image)

    def test__apply_edge__text_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_edge,
                          None, Edge.left())

    def test__apply_edge__text_is_wrong_type__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_edge,
                          2017, Edge.left())

    def test__apply_edge__text_is_empty__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_edge, " ",
                          Edge.left())

    def test__apply_edge__edge_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_edge,
                          "WATERMARK", None)

    def test__apply_edge__edge_is_wrong_type__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_edge,
                          "WATERMARK", 2017)

    def test__apply_edge__edge_not_from_Edge__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_edge,
                          "WATERMARK", (0, 0.5))

    '''
    apply_absolute
    '''
    def test__apply_absolute__valid_params__returns_image(self):
        wm = self._create_wm()
        actual = wm.apply_absolute("WATERMARK", 20, 20)
        self.assertIsInstance(actual, Image.Image)

    def test__apply_absolute__text_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_absolute, None,
                          20, 20)

    def test__apply_absolute__text_is_wrong_type__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_absolute, 2017,
                          20, 20)

    def test__apply_absolute__text_is_empty__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_absolute, " ",
                          20, 20)

    def test__apply_absolute__x_pos_px_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_absolute,
                          "WATERMARK", None, 20)

    def test__apply_absolute__y_pos_px_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_absolute,
                          "WATERMARK", 20, None)

    def test__apply_absolute__x_pos_px_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_absolute,
                          "WATERMARK", "NOT INT", 20)

    def test__apply_absolute__y_pos_px_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_absolute,
                          "WATERMARK", 20, "NOT INT")

    '''
    apply_percent
    '''
    def test__apply_percent__valid_params__returns_image(self):
        wm = self._create_wm()
        actual = wm.apply_percent("WATERMARK", 20, 20)
        self.assertIsInstance(actual, Image.Image)

    def test__apply_percent__text_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_percent, None,
                          20, 20)

    def test__apply_percent__text_is_wrong_type__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_percent, 2017,
                          20, 20)

    def test__apply_percent__text_is_empty__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_percent, " ",
                          20, 20)

    def test__apply_percent__left_indent_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_percent,
                          "WATERMARK", None, 20)

    def test__apply_percent__top_indent_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_percent,
                          "WATERMARK", 20, None)

    def test__apply_percent__left_indent_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_percent,
                          "WATERMARK", "NOT INT", 20)

    def test__apply_percent__top_indent_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_percent,
                          "WATERMARK", 20, "NOT INT")

    '''
    apply_random
    '''
    def test__apply_random__valid_text__returns_image(self):
        wm = self._create_wm()
        actual = wm.apply_random("WATERMARK")
        self.assertIsInstance(actual, Image.Image)

    def test__apply_random__valid_text_and_quantity__returns_image(self):
        wm = self._create_wm()
        actual = wm.apply_random("WATERMARK", quantity=5)
        self.assertIsInstance(actual, Image.Image)

    def test__apply_random__text_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_random,
                          None)

    def test__apply_random__text_is_empty__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_random, " ")

    def test__apply_random__quantity_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_random,
                          "WATERMARK", None)

    def test__apply_random__quantity_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_random,
                          "WATERMARK", "NOT INT")

    def test__apply_random__quantity_is_lt_1__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_random,
                          "WATERMARK", 0)

    '''
    apply_lattice
    '''
    def test__apply_lattice__valid_params__returns_image(self):
        wm = self._create_wm()
        actual = wm.apply_lattice("WATERMARK", 100, 100, 50, 50)
        self.assertIsInstance(actual, Image.Image)

    def test__apply_lattice__text_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_lattice,
                          None, 100, 100)

    def test__apply_lattice__text_is_empty__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_lattice, " ",
                          100, 100)

    def test__apply_lattice__horizontal_margin_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_lattice,
                          "WATERMARK",
                          horizontal_margin=None,
                          vertical_margin=100)

    def test__apply_lattice__vertical_margin_is_none__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_lattice,
                          "WATERMARK",
                          horizontal_margin=100,
                          vertical_margin=None)

    def test__apply_lattice__horizontal_margin_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_lattice,
                          "WATERMARK",
                          horizontal_margin="NOT INT",
                          vertical_margin=100)

    def test__apply_lattice__vertical_margin_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_lattice,
                          "WATERMARK",
                          horizontal_margin=100,
                          vertical_margin="NOT INT")

    def test__apply_lattice__horizontal_margin_is_lt_1__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_lattice,
                          "WATERMARK",
                          horizontal_margin=0,
                          vertical_margin=100)

    def test__apply_lattice__vertical_margin_is_lt_1__raises_wm_value_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerValueError, wm.apply_lattice,
                          "WATERMARK",
                          horizontal_margin=100,
                          vertical_margin=0)

    def test__apply_lattice__horizontal_start_margin_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_lattice,
                          "WATERMARK",
                          100, 100,
                          horizontal_start_margin="NOT INT")

    def test__apply_lattice__vertical_start_margin_is_not_int__raises_wm_type_error(self):
        wm = self._create_wm()
        self.assertRaises(WaterMarkerTypeError, wm.apply_lattice,
                          "WATERMARK",
                          100, 100,
                          vertical_start_margin="NOT INT")

if __name__ == '__main__':
    unittest.main()
