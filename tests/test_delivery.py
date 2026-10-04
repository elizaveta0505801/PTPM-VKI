import datetime
import unittest

from Delivery import calculate_delivery_cost


class TestCalculateDeliveryCost(unittest.TestCase):

    def test_calculates_basic_delivery_cost(self):
        cost, _ = calculate_delivery_cost(1, 100, "обычный")
        self.assertEqual(cost, 700)

    def test_adds_fee_for_fragile_package(self):
        cost, _ = calculate_delivery_cost(1, 100, "хрупкий")
        self.assertEqual(cost, 1000)

    def test_adds_fee_for_dangerous_package(self):
        cost, _ = calculate_delivery_cost(1, 100, "опасный")
        self.assertEqual(cost, 1700)

    def test_applies_weight_rate_above_five_kg(self):
        cost, _ = calculate_delivery_cost(6, 100, "обычный")
        self.assertEqual(cost, 840)

    def test_applies_weight_rate_at_twenty_kg(self):
        cost, _ = calculate_delivery_cost(20, 100, "обычный")
        self.assertEqual(cost, 1050)

    def test_does_not_apply_weight_rate_at_five_kg(self):
        cost, _ = calculate_delivery_cost(5, 100, "обычный")
        self.assertEqual(cost, 700)

    def test_accepts_minimum_weight(self):
        cost, delivery_date = calculate_delivery_cost(0.1, 100, "обычный")
        self.assertEqual(cost, 700)
        self.assertNotEqual(delivery_date, "0000-00-00")

    def test_rejects_weight_below_minimum(self):
        result = calculate_delivery_cost(0.09, 100, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_accepts_maximum_weight(self):
        cost, delivery_date = calculate_delivery_cost(50, 100, "обычный")
        self.assertEqual(cost, 1050)
        self.assertNotEqual(delivery_date, "0000-00-00")

    def test_rejects_weight_above_maximum(self):
        result = calculate_delivery_cost(50.1, 100, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_accepts_minimum_distance(self):
        result = calculate_delivery_cost(1, 1, "обычный")
        self.assertNotEqual(result, (-1, "0000-00-00"))

    def test_rejects_distance_below_minimum(self):
        result = calculate_delivery_cost(1, 0, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_accepts_maximum_distance(self):
        result = calculate_delivery_cost(1, 5000, "обычный")
        self.assertNotEqual(result, (-1, "0000-00-00"))

    def test_rejects_distance_above_maximum(self):
        result = calculate_delivery_cost(1, 5001, "обычный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_rejects_unknown_package_type(self):
        result = calculate_delivery_cost(1, 100, "неизвестный")
        self.assertEqual(result, (-1, "0000-00-00"))

    def test_delivery_date_is_calculated_from_today(self):
        _, delivery_date = calculate_delivery_cost(1, 100, "обычный")
        expected_date = datetime.date.today() + datetime.timedelta(days=1)
        self.assertEqual(delivery_date, expected_date.strftime("%Y-%m-%d"))

    def test_distance_above_five_hundred_km_needs_two_days(self):
        _, delivery_date = calculate_delivery_cost(1, 501, "обычный")
        expected_date = datetime.date.today() + datetime.timedelta(days=2)
        self.assertEqual(delivery_date, expected_date.strftime("%Y-%m-%d"))

    def test_express_delivery_costs_more_than_regular_delivery(self):
        regular_cost, _ = calculate_delivery_cost(1, 100, "обычный")
        express_cost, _ = calculate_delivery_cost(
        1, 100, "обычный", is_express=True
        )
        self.assertEqual(express_cost, int(regular_cost * 1.5))

    def test_express_delivery_takes_at_least_one_day(self):
        _, delivery_date = calculate_delivery_cost(
        1, 100, "обычный", is_express=True
        )
        expected_date = datetime.date.today() + datetime.timedelta(days=1)
        self.assertEqual(delivery_date, expected_date.strftime("%Y-%m-%d"))

    def test_calculates_cost_at_maximum_distance(self):
        cost, _ = calculate_delivery_cost(1, 5000, "обычный")

        self.assertEqual(cost, 25200)


if __name__ == "__main__":
    unittest.main()
