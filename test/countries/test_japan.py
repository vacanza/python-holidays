#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

import holidays


class TestJapan(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Japan(observed=False)

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            holidays.Japan(years=[1945])
        with self.assertRaises(NotImplementedError):
            holidays.Japan(years=[2100])

    def test_new_years_day(self):
        self.assertIn(date(1949, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2050, 1, 1), self.holidays)

    def test_coming_of_age(self):
        self.assertIn(date(1999, 1, 15), self.holidays)
        self.assertIn(date(2000, 1, 10), self.holidays)
        self.assertIn(date(2017, 1, 9), self.holidays)
        self.assertIn(date(2030, 1, 14), self.holidays)
        self.assertIn(date(2050, 1, 10), self.holidays)

        self.assertNotIn(date(2000, 1, 15), self.holidays)
        self.assertNotIn(date(2017, 1, 15), self.holidays)
        self.assertNotIn(date(2030, 1, 15), self.holidays)

    def test_foundation_day(self):
        self.assertNotIn(date(1949, 2, 11), self.holidays)
        self.assertNotIn(date(1966, 2, 11), self.holidays)
        self.assertIn(date(1967, 2, 11), self.holidays)
        self.assertIn(date(2017, 2, 11), self.holidays)
        self.assertIn(date(2050, 2, 11), self.holidays)

    def test_vernal_equinox_day(self):
        self.assertIn(date(1956, 3, 21), self.holidays)
        self.assertIn(date(1960, 3, 20), self.holidays)
        self.assertIn(date(1970, 3, 21), self.holidays)
        self.assertIn(date(1980, 3, 20), self.holidays)
        self.assertIn(date(1990, 3, 21), self.holidays)
        self.assertIn(date(2000, 3, 20), self.holidays)
        self.assertIn(date(2010, 3, 21), self.holidays)
        self.assertIn(date(2017, 3, 20), self.holidays)
        self.assertIn(date(2020, 3, 20), self.holidays)
        self.assertIn(date(2030, 3, 20), self.holidays)
        self.assertIn(date(2040, 3, 20), self.holidays)
        self.assertIn(date(2092, 3, 19), self.holidays)

    def test_showa_day(self):
        self.assertIn(date(1950, 4, 29), self.holidays)
        self.assertIn(date(1990, 4, 29), self.holidays)
        self.assertIn(date(2010, 4, 29), self.holidays)

    def test_constitution_memorial_day(self):
        self.assertIn(date(1950, 5, 3), self.holidays)
        self.assertIn(date(2000, 5, 3), self.holidays)
        self.assertIn(date(2050, 5, 3), self.holidays)

    def test_greenery_day(self):
        self.assertNotIn(date(1950, 5, 4), self.holidays)
        self.assertIn(date(2007, 5, 4), self.holidays)
        self.assertIn(date(2050, 5, 4), self.holidays)

    def test_childrens_day(self):
        self.assertIn(date(1950, 5, 5), self.holidays)
        self.assertIn(date(2000, 5, 5), self.holidays)
        self.assertIn(date(2050, 5, 5), self.holidays)

    def test_marine_day(self):
        self.assertNotIn(date(1950, 7, 20), self.holidays)
        self.assertIn(date(2000, 7, 20), self.holidays)
        self.assertIn(date(2003, 7, 21), self.holidays)
        self.assertIn(date(2017, 7, 17), self.holidays)
        self.assertIn(date(2020, 7, 23), self.holidays)
        self.assertIn(date(2021, 7, 22), self.holidays)
        self.assertIn(date(2050, 7, 18), self.holidays)

    def test_mountain_day(self):
        self.assertNotIn(date(1950, 8, 11), self.holidays)
        self.assertNotIn(date(2015, 8, 11), self.holidays)
        self.assertIn(date(2016, 8, 11), self.holidays)
        self.assertIn(date(2017, 8, 11), self.holidays)
        self.assertIn(date(2020, 8, 10), self.holidays)
        self.assertIn(date(2021, 8, 8), self.holidays)
        self.assertIn(date(2050, 8, 11), self.holidays)

    def test_respect_for_the_aged_day(self):
        self.assertNotIn(date(1965, 9, 15), self.holidays)
        self.assertIn(date(1966, 9, 15), self.holidays)
        self.assertIn(date(2002, 9, 15), self.holidays)
        self.assertIn(date(2003, 9, 15), self.holidays)
        self.assertNotIn(date(2004, 9, 15), self.holidays)
        self.assertIn(date(2004, 9, 20), self.holidays)
        self.assertIn(date(2017, 9, 18), self.holidays)
        self.assertIn(date(2050, 9, 19), self.holidays)

    def test_autumnal_equinox_day(self):
        self.assertIn(date(2000, 9, 23), self.holidays)
        self.assertIn(date(2010, 9, 23), self.holidays)
        self.assertIn(date(2017, 9, 23), self.holidays)
        self.assertIn(date(2020, 9, 22), self.holidays)
        self.assertIn(date(2030, 9, 23), self.holidays)
        self.assertIn(date(1979, 9, 24), self.holidays)
        self.assertIn(date(2032, 9, 21), self.holidays)

    def test_health_and_sports_day(self):
        self.assertNotIn(date(1965, 10, 10), self.holidays)
        self.assertIn(date(1966, 10, 10), self.holidays)
        self.assertIn(date(1999, 10, 10), self.holidays)
        self.assertNotIn(date(2000, 10, 10), self.holidays)
        self.assertIn(date(2000, 10, 9), self.holidays)
        self.assertIn(date(2017, 10, 9), self.holidays)
        self.assertIn(date(2020, 7, 24), self.holidays)
        self.assertIn(date(2021, 7, 23), self.holidays)
        self.assertIn(date(2050, 10, 10), self.holidays)

    def test_culture_day(self):
        self.assertIn(date(1950, 11, 3), self.holidays)
        self.assertIn(date(2000, 11, 3), self.holidays)
        self.assertIn(date(2050, 11, 3), self.holidays)

    def test_labour_thanks_giving_day(self):
        self.assertIn(date(1950, 11, 23), self.holidays)
        self.assertIn(date(2000, 11, 23), self.holidays)
        self.assertIn(date(2050, 11, 23), self.holidays)

    def test_emperors_birthday(self):
        self.assertIn(date(1989, 12, 23), self.holidays)
        self.assertIn(date(2017, 12, 23), self.holidays)
        self.assertNotIn(date(2019, 12, 23), self.holidays)
        self.assertIn(date(2020, 2, 23), self.holidays)

    def test_showa_emperor_holidays(self):
        self.assertIn(date(1989, 2, 24), self.holidays)

    def test_heisei_emperor_holidays(self):
        self.assertIn(date(1959, 4, 10), self.holidays)
        self.assertIn(date(1990, 11, 12), self.holidays)

    def test_reiwa_emperor_holidays(self):
        self.assertIn(date(1993, 6, 9), self.holidays)
        self.assertIn(date(2019, 4, 30), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 2), self.holidays)
        self.assertIn(date(2019, 10, 22), self.holidays)

    def test_invalid_years(self):
        self.assertRaises(
            NotImplementedError, lambda: date(1948, 1, 1) in self.holidays
        )
        self.assertRaises(
            NotImplementedError, lambda: date(2100, 1, 1) in self.holidays
        )

    def test_substitute_holidays(self):
        for dt in (
            (1973, 4, 30),
            (1973, 9, 24),
            (1974, 5, 6),
            (1974, 9, 16),
            (1974, 11, 4),
            (1975, 11, 24),
            (1976, 10, 11),
            (1978, 1, 2),
            (1978, 1, 16),
            (1979, 2, 12),
            (1979, 4, 30),
            (1980, 11, 24),
            (1981, 5, 4),
            (1982, 3, 22),
            (1982, 10, 11),
            (1984, 1, 2),
            (1984, 1, 16),
            (1984, 4, 30),
            (1984, 9, 24),
            (1985, 5, 6),
            (1985, 9, 16),
            (1985, 11, 4),
            (1986, 11, 24),
            (1987, 5, 4),
            (1988, 3, 21),
            (1989, 1, 2),
            (1989, 1, 16),
            (1990, 2, 12),
            (1990, 4, 30),
            (1990, 9, 24),
            (1990, 12, 24),
            (1991, 5, 6),
            (1991, 9, 16),
            (1991, 11, 4),
            (1992, 5, 4),
            (1993, 10, 11),
            (1995, 1, 2),
            (1995, 1, 16),
            (1996, 2, 12),
            (1996, 5, 6),
            (1996, 9, 16),
            (1996, 11, 4),
            (1997, 7, 21),
            (1997, 11, 24),
            (1998, 5, 4),
            (1999, 3, 22),
            (1999, 10, 11),
            (2001, 2, 12),
            (2001, 4, 30),
            (2001, 9, 24),
            (2001, 12, 24),
            (2002, 5, 6),
            (2002, 9, 16),
            (2002, 11, 4),
            (2003, 11, 24),
            (2005, 3, 21),
            (2006, 1, 2),
            (2007, 2, 12),
            (2007, 4, 30),
            (2007, 9, 24),
            (2007, 12, 24),
            (2008, 5, 6),
            (2008, 11, 24),
            (2009, 5, 6),
            (2010, 3, 22),
            (2012, 1, 2),
            (2012, 4, 30),
            (2012, 12, 24),
            (2013, 5, 6),
            (2013, 11, 4),
            (2014, 5, 6),
            (2014, 11, 24),
            (2015, 5, 6),
            (2016, 3, 21),
            (2017, 1, 2),
            (2018, 2, 12),
            (2018, 4, 30),
            (2018, 9, 24),
            (2018, 12, 24),
            (2019, 5, 6),
            (2019, 8, 12),
            (2019, 11, 4),
            (2020, 2, 24),
            (2020, 5, 6),
            (2023, 1, 2),
            (2024, 2, 12),
            (2024, 5, 6),
            (2024, 8, 12),
            (2024, 9, 23),
            (2024, 11, 4),
            (2025, 2, 24),
            (2025, 5, 6),
            (2025, 11, 24),
            (2026, 5, 6),
            (2027, 3, 22),
            (2029, 2, 12),
            (2029, 4, 30),
            (2029, 9, 24),
            (2030, 5, 6),
            (2030, 8, 12),
            (2030, 11, 4),
            (2031, 2, 24),
            (2031, 5, 6),
            (2031, 11, 24),
            (2033, 3, 21),
            (2034, 1, 2),
            (2035, 2, 12),
            (2035, 4, 30),
            (2035, 9, 24),
            (2036, 5, 6),
            (2036, 11, 24),
            (2037, 5, 6),
            (2040, 1, 2),
            (2040, 4, 30),
            (2041, 5, 6),
            (2041, 8, 12),
            (2041, 11, 4),
            (2042, 2, 24),
            (2042, 5, 6),
            (2042, 11, 24),
            (2043, 5, 6),
            (2044, 3, 21),
            (2045, 1, 2),
            (2046, 2, 12),
            (2046, 4, 30),
            (2046, 9, 24),
            (2047, 5, 6),
            (2047, 8, 12),
            (2047, 11, 4),
            (2048, 2, 24),
            (2048, 5, 6),
            (2050, 3, 21),
        ):
            self.assertIn(date(*dt), self.holidays)
