"""Building Types"""

from .split import SplitMixin


class BuildingTypeMixin(SplitMixin):
    """Determines if a string represents a known building type"""

    @classmethod
    @property
    def known_building_types(cls):
        """Returns known building types"""
        return (
            "BACK OF", "BLOCK", "BLOCKS", "BUILDING",
            "MAISONETTE", "MAISONETTES", "REAR OF",
            "SHOP", "SHOPS", "STALL", "STALLS",
            "SUITE", "SUITES", "UNIT", "UNITS",
            "FLAT", "FLATS", "PO BOX"
            )

    @classmethod
    @property
    def known_sub_building_types(cls):
        """Returns known sub-building types"""
        return cls.known_building_types

    @classmethod
    @property
    def known_split_building_types(cls):
        """Returns known split building types"""
        return ("UNIT",)

    def is_known_building_type(self, attr='building_name'):
        """Returns if attribute starts with a known type"""
        return self.but_last_word(attr) in self.known_building_types

    def is_known_sub_building_type(self, attr='sub_building_name'):
        """Returns if attribute starts with a known type"""
        return self.but_last_word(attr) in self.known_sub_building_types

    def is_known_split_building_type(self, attr='building_name'):
        """Returns if attribute starts with a known type"""
        return self.but_last_word(attr) in self.known_split_building_types
