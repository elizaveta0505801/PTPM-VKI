import unittest

from main import triangle_info


class TestTriangleInfo(unittest.TestCase):

    def test_equilateral_triangle(self):
        triangle_type, _ = triangle_info("5", "5", "5")
        self.assertEqual(triangle_type, "равносторонний")

    def test_isosceles_triangle_with_equal_a_and_b(self):
        triangle_type, _ = triangle_info("5", "5", "6")
        self.assertEqual(triangle_type, "равнобедренный")

    def test_isosceles_triangle_with_equal_a_and_c(self):
        triangle_type, _ = triangle_info("5", "6", "5")
        self.assertEqual(triangle_type, "равнобедренный")

    def test_isosceles_triangle_with_equal_b_and_c(self):
        triangle_type, _ = triangle_info("6", "5", "5")
        self.assertEqual(triangle_type, "равнобедренный")

    def test_scalene_triangle(self):
        triangle_type, _ = triangle_info("4", "5", "6")
        self.assertEqual(triangle_type, "разносторонний")

    def test_invalid_when_a_plus_b_equals_c(self):
        result = triangle_info("1", "2", "3")
        self.assertEqual(result[0], "не треугольник")

    def test_invalid_when_a_plus_c_equals_b(self):
        result = triangle_info("1", "3", "2")
        self.assertEqual(result[0], "не треугольник")

    def test_invalid_when_b_plus_c_equals_a(self):
        result = triangle_info("3", "1", "2")
        self.assertEqual(result[0], "не треугольник")

    def test_non_numeric_input_returns_empty_type(self):
        triangle_type, _ = triangle_info("abc", "5", "6")
        self.assertEqual(triangle_type, "")

    def test_non_numeric_input_returns_minus_two_coordinates(self):
        _, coordinates = triangle_info("abc", "5", "6")
        self.assertEqual(coordinates, [(-2, -2)] * 3)

    def test_zero_side_is_rejected(self):
        triangle_type, coordinates = triangle_info("0", "5", "6")
        self.assertEqual(triangle_type, "не треугольник")
        self.assertEqual(coordinates, [(-1, -1)] * 3)

    def test_negative_side_is_rejected(self):
        triangle_type, coordinates = triangle_info("-1", "5", "6")
        self.assertEqual(triangle_type, "не треугольник")
        self.assertEqual(coordinates, [(-1, -1)] * 3)

    def test_nan_side_is_rejected(self):
        triangle_type, coordinates = triangle_info("nan", "5", "6")
        self.assertEqual(triangle_type, "не треугольник")
        self.assertEqual(coordinates, [(-1, -1)] * 3)

    def test_positive_infinity_is_rejected(self):
        triangle_type, coordinates = triangle_info("inf", "5", "6")
        self.assertEqual(triangle_type, "не треугольник")
        self.assertEqual(coordinates, [(-1, -1)] * 3)

    def test_negative_infinity_is_rejected(self):
        triangle_type, coordinates = triangle_info("-inf", "5", "6")
        self.assertEqual(triangle_type, "не треугольник")
        self.assertEqual(coordinates, [(-1, -1)] * 3)

    def test_decimal_sides_are_accepted(self):
        triangle_type, _ = triangle_info("3.5", "4.5", "5.5")
        self.assertEqual(triangle_type, "разносторонний")

    def test_valid_triangle_has_three_coordinates(self):
        _, coordinates = triangle_info("3", "4", "5")
        self.assertEqual(len(coordinates), 3)

    def test_each_coordinate_contains_two_values(self):
        _, coordinates = triangle_info("3", "4", "5")
        for point in coordinates:
        self.assertEqual(len(point), 2)

    def test_coordinates_are_integers(self):
        _, coordinates = triangle_info("3", "4", "5")
        for point in coordinates:
        for value in point:
        self.assertIsInstance(value, int)

    def test_coordinates_fit_inside_drawing_area(self):
        _, coordinates = triangle_info("3", "4", "5")
        for x, y in coordinates:
            self.assertGreaterEqual(x, 5)
            self.assertLessEqual(x, 95)
            self.assertGreaterEqual(y, 5)
            self.assertLessEqual(y, 95)


if __name__ == "__main__":
    unittest.main()
