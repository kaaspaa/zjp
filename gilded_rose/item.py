from functions import *


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_item(self):
        if not self.name.contains("Sulfuras"):  # zmieniono ifa z Sulfurasem na sam poczatek
            if self.name == "Aged Brie":
                increase_quality(self)
                if self.sell_in <= 0:
                    increase_quality(self)
                decrease_sell_in(self)
            elif self.name.contains("Backstage passes"):
                if self.sell_in <= 0:
                    self.quality = 0
                else:
                    increase_quality_in_concert_passes(self)
                decrease_sell_in(self)  # zmniejszenie sell_in
            else:
                if self.sell_in <= 0:
                    decrease_quality(self)
                decrease_quality(self)
                decrease_sell_in(self)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
