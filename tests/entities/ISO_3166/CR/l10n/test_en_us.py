#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.entities.ISO_3166.CR import CrHolidays
from tests.common import CommonCountryTests


class TestCrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CrHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-04-11", "Juan Santamaría Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "International Labor Day"),
            ("2022-07-25", "Annexation of the Party of Nicoya to Costa Rica"),
            ("2022-08-02", "Feast of Our Lady of the Angels"),
            ("2022-08-15", "Mother's Day"),
            ("2022-09-04", "Day of the Black Person and Afro-Costa Rican Culture (observed)"),
            ("2022-09-19", "Independence Day (observed)"),
            ("2022-12-05", "Army Abolition Day (observed)"),
            ("2022-12-25", "Christmas Day"),
        )