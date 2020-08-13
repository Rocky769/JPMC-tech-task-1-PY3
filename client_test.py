import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote),(quote['stock'],float(quote['top_bid']['price']),float(quote['top_ask']['price']),(float(quote['top_bid']['price'])+float(quote['top_ask']['price']))/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote),(quote['stock'],float(quote['top_bid']['price']),float(quote['top_ask']['price']),(float(quote['top_bid']['price'])+float(quote['top_ask']['price']))/2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_price_b_equal_to_zero(self):
      self.assertIsNone(getRatio(2,0))

  def test_getRatio_greaterThanOne(self):
      self.assertGreater(getRatio(87.97,85.93),1)

  def test_getRatio_lessThanOne(self):
      self.assertLess(getRatio(85.93,87.97),1)

  def test_getRatio_equalToOne(self):
      self.assertEqual(getRatio(85.93,85.93),1)


if __name__ == '__main__':
    unittest.main()
