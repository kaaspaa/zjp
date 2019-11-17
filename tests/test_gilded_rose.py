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

    def test_Aged_Brie(self):
        items = [Item("Aged Brie", sell_in=5, quality=5),
                 Item("Aged Brie", sell_in=2, quality=5)]
        gilded_rose = GildedRose(items)
        for day in range(6):
            gilded_rose.update_quality()
        self.assertEqual(12, gilded_rose.items[0].quality)
        self.assertEqual(15, gilded_rose.items[1].quality)

    def test_Backstage_pass_before_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=10),
                 Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=2),
                 Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        for day in range(5):
            gilded_rose.update_quality()
        self.assertEqual(15, gilded_rose.items[0].quality)
        self.assertEqual(17, gilded_rose.items[1].quality)
        self.assertEqual(30,gilded_rose.items[2].quality)

    def test_Backstage_pass_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)
        for day in range(20):
            gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(-1, gilded_rose.items[0].sell_in)

    def test_normal_item(self):
        items = [Item("+5 Dexterity Vest", sell_in=10, quality=20),
                 Item("+9 Dexterity Vest", sell_in=3, quality=40)]
        gilded_rose = GildedRose(items)
        for day in range(6):
            gilded_rose.update_quality()
        self.assertEqual(14, gilded_rose.items[0].quality)
        self.assertEqual(31, gilded_rose.items[1].quality)

    def test_Conjured_item(self):
        items = [Item("Conjured Mana Cake", sell_in=5, quality=14), Item("Conjured Mana Cheese", sell_in=2, quality=20)]
        gilded_rose = GildedRose(items)
        for day in range(5):
            gilded_rose.update_quality()
        self.assertEqual(4, gilded_rose.items[0].quality)
        self.assertEqual(4, gilded_rose.items[1].quality)