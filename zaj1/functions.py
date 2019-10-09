def decrase_sellin(item):
    if item.sell_in >= 0:
        item.sell_in -= 1

def decrase_quality(item):
    if item.quality > 0:
        item.quality -= 1

def incrace_quality(item):
   if item.quality < 50:
        item.quality += 1


def incrase_quality(item):
    if item.quality < 50:
        item.quality += 1