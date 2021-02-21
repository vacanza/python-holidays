# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import os
import sys
import unittest
import warnings
from glob import glob
from itertools import product

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, MO
from flake8.api import legacy as flake8

import holidays


class TestIreland(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.Ireland()

    def test_2020(self):
        self.assertIn('2020-01-01', self.holidays)  # New Year's Day
        self.assertIn('2020-03-17', self.holidays)  # St. Patrick's Day
        self.assertIn('2020-04-13', self.holidays)  # Easter Monday
        self.assertIn('2020-05-04', self.holidays)  # May Day in IE
        self.assertNotIn('2020-05-08', self.holidays)  # May Day in UK not IE
        self.assertIn('2020-06-01', self.holidays)  # June Bank Holiday
        self.assertIn('2020-08-03', self.holidays)  # Summer Bank Holiday
        self.assertIn('2020-10-26', self.holidays)  # October Bank Holiday
        self.assertIn('2020-12-25', self.holidays)  # Christmas Day
        self.assertIn('2020-12-26', self.holidays)  # Boxing Day
        self.assertIn('2020-12-28', self.holidays)  # Boxing Day (Observed)

    def test_may_day(self):
        # Specific Ireland "May Day"
        for dt in [date(1978, 5, 1), date(1979, 5, 7), date(1980, 5, 5),
                   date(1995, 5, 8), date(1999, 5, 3), date(2000, 5, 1),
                   date(2010, 5, 3), date(2018, 5, 7), date(2019, 5, 6),
                   date(2020, 5, 4)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_st_stephens_day(self):
        # St. Stephen's Day
        self.holidays.observed = False

        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2009, 12, 28), self.holidays)
        self.assertNotIn(date(2010, 12, 27), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2004, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 28), self.holidays)
        for year, day in enumerate([26, 26, 26, 28, 26,
                                    26, 26, 26, 28, 28,
                                    26, 26, 26, 26, 26,
                                    26, 26, 26, 26, 26, 28],
                                   2001):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertIn(
                self.holidays[dt],
                ["St. Stephen's Day", "St. Stephen's Day (Observed)"]
            )


class TestIE(unittest.TestCase):

    def setUp(self):
        self.irish_holidays = holidays.IE()

    def test_new_year_day(self):
        self.assertIn('2017-01-02', self.irish_holidays)
        self.assertIn('2018-01-01', self.irish_holidays)

    def test_st_patricks_day(self):
        self.assertIn('2017-03-17', self.irish_holidays)
        self.assertIn('2018-03-17', self.irish_holidays)

    def test_easter_monday(self):
        self.assertIn('2017-04-17', self.irish_holidays)
        self.assertIn('2018-04-02', self.irish_holidays)

    def test_may_bank_holiday(self):
        self.assertIn('2017-05-01', self.irish_holidays)
        self.assertIn('2018-05-07', self.irish_holidays)

    def test_june_bank_holiday(self):
        self.assertIn('2017-06-05', self.irish_holidays)
        self.assertIn('2018-06-04', self.irish_holidays)

    def test_august_bank_holiday(self):
        self.assertIn('2017-08-07', self.irish_holidays)
        self.assertIn('2018-08-06', self.irish_holidays)

    def test_october_bank_holiday(self):
        self.assertIn('2017-10-30', self.irish_holidays)
        self.assertIn('2018-10-29', self.irish_holidays)

    def test_christmas_period(self):
        self.assertIn('2015-12-25', self.irish_holidays)
        self.assertIn('2015-12-28', self.irish_holidays)
        self.assertIn('2016-12-26', self.irish_holidays)
        self.assertIn('2016-12-27', self.irish_holidays)
        self.assertIn('2017-12-25', self.irish_holidays)
        self.assertIn('2017-12-26', self.irish_holidays)
        self.assertIn('2018-12-25', self.irish_holidays)
        self.assertIn('2018-12-26', self.irish_holidays)
