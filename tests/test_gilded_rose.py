# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose
from item import Item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", gilded_rose.items[0].name)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        gilded_rose = GildedRose(items)
        for day in range(150):
            gilded_rose.update_quality()
        self.assertEqual(-1, gilded_rose.items[0].sell_in)
        self.assertEqual(80, gilded_rose.items[0].quality)

