# -*- coding: utf-8 -*-
from functions import *

class GildedRose(object):
    
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":#zmieniono ifa z Sulfurasem na sam poczatek
                if item.name == "Aged Brie":
                    incrase_quality(item)
                    if item.sell_in <= 0:
                        incrase_quality(item)
                    decrase_sellin(item)#zmniejszenie sell_in

                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in <= 0: #po koncercie
                        item.quality = 0
                    else:
                        incrase_quality(item)
                        if item.sell_in <= 10:#10 dni przed
                            incrase_quality(item)
                            if item.sell_in <= 5:#5 dni przed
                                incrace_quality(item)
                    decrase_sellin(item)#zmniejszenie sell_in
                else:
                    if item.sell_in <= 0:#jak sellin jest juz ponizej 0ra
                        decrase_quality(item)
                        if "Conjured" in item.name:
                            decrase_quality(item)
                    decrase_quality(item)
                    if "Conjured" in item.name:
                        decrase_quality(item)
                    decrase_sellin(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
