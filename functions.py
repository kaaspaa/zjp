"""These are functions used in "gilded_rose.py" file"""


def decrease_sell_in(item):
    """This function decreases "sell in" value in item"""
    if item.sell_in >= 0:
        item.sell_in -= 1


def decrease_quality(item):
    """This function decreases "quality" value in item"""
    if item.quality > 0:
        item.quality -= 1
    if "Conjured" in item.name and item.quality > 0:
        item.quality -= 1


def increase_quality(item):
    """This function increases "quality" value in item"""
    if item.quality < 50:
        item.quality += 1


def increase_quality_in_concert_passes(item):
    """This function updates values for backstage passes to a "TAFKAL80ETC" concert"""
    increase_quality(item)
    if item.sell_in <= 10:  # 10 dni przed
        increase_quality(item)
        if item.sell_in <= 5:  # 5 dni przed
            increase_quality(item)
