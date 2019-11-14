"""This file is my try on refactoring "Gilded Rose Kata" """
# -*- coding: utf-8 -*-
from functions import *


class GildedRose(object):
    """Gilded Rose is containing Items and method to update quality of these items"""
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """This method updates quality of Items"""
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":  #zmieniono ifa z Sulfurasem na sam poczatek
                if item.name == "Aged Brie":
                    increase_quality(item)
                    if item.sell_in <= 0:
                        increase_quality(item)
                    decrease_sell_in(item)  #zmniejszenie sell_in
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in <= 0:  # po koncercie
                        item.quality = 0
                    else:
                        increase_quality_in_concert_passes(item)
                    decrease_sell_in(item)
                else:
                    if item.sell_in <= 0:  #jak sellin jest juz ponizej 0ra
                        decrease_quality(item)
                    decrease_quality(item)
                    decrease_sell_in(item)


class Item:
    """This class has values needed to run database from "Gilded Rose Kata" """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
