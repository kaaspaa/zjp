"""This file is my try on refactoring "Gilded Rose Kata" """


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_item()
