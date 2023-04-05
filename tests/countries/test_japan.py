#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from unittest import mock

from holidays.countries.japan import Japan, JP, JPN
from tests.common import TestCase


class TestJapan(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Japan, years=range(1949, 2051))

    def test_country_aliases(self):
        self.assertCountryAliases(Japan, JP, JPN)

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            Japan(years=1945)
        with self.assertRaises(NotImplementedError):
            Japan(years=2100)

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1949, 2051))

    def test_coming_of_age(self):
        self.assertHoliday(f"{year}-01-15" for year in range(1949, 2000))

        self.assertHoliday(
            "2000-01-10",
            "2001-01-08",
            "2002-01-14",
            "2003-01-13",
            "2004-01-12",
            "2005-01-10",
            "2006-01-09",
            "2007-01-08",
            "2008-01-14",
            "2009-01-12",
            "2010-01-11",
            "2011-01-10",
            "2012-01-09",
            "2013-01-14",
            "2014-01-13",
            "2015-01-12",
            "2016-01-11",
            "2017-01-09",
            "2018-01-08",
            "2019-01-14",
            "2020-01-13",
            "2021-01-11",
            "2022-01-10",
            "2023-01-09",
            "2024-01-08",
            "2025-01-13",
            "2026-01-12",
            "2027-01-11",
            "2028-01-10",
            "2029-01-08",
            "2030-01-14",
            "2031-01-13",
            "2032-01-12",
            "2033-01-10",
            "2034-01-09",
            "2035-01-08",
            "2036-01-14",
            "2037-01-12",
            "2038-01-11",
            "2039-01-10",
            "2040-01-09",
            "2041-01-14",
            "2042-01-13",
            "2043-01-12",
            "2044-01-11",
            "2045-01-09",
            "2046-01-08",
            "2047-01-14",
            "2048-01-13",
            "2049-01-11",
            "2050-01-10",
        )

        self.assertNoHoliday("2000-01-15", "2017-01-15", "2030-01-15")

    def test_foundation_day(self):
        self.assertHoliday(f"{year}-02-11" for year in range(1967, 2051))
        self.assertNoHoliday("1966-02-11")
        self.assertNoHolidayNameInYears("建国記念の日", 1966)

    def test_vernal_equinox_day(self):
        self.assertHolidaysName(
            "春分の日",
            "1949-03-21",
            "1950-03-21",
            "1951-03-21",
            "1952-03-21",
            "1953-03-21",
            "1954-03-21",
            "1955-03-21",
            "1956-03-21",
            "1957-03-21",
            "1958-03-21",
            "1959-03-21",
            "1960-03-20",
            "1961-03-21",
            "1962-03-21",
            "1963-03-21",
            "1964-03-20",
            "1965-03-21",
            "1966-03-21",
            "1967-03-21",
            "1968-03-20",
            "1969-03-21",
            "1970-03-21",
            "1971-03-21",
            "1972-03-20",
            "1973-03-21",
            "1974-03-21",
            "1975-03-21",
            "1976-03-20",
            "1977-03-21",
            "1978-03-21",
            "1979-03-21",
            "1980-03-20",
            "1981-03-21",
            "1982-03-21",
            "1983-03-21",
            "1984-03-20",
            "1985-03-21",
            "1986-03-21",
            "1987-03-21",
            "1988-03-20",
            "1989-03-21",
            "1990-03-21",
            "1991-03-21",
            "1992-03-20",
            "1993-03-20",
            "1994-03-21",
            "1995-03-21",
            "1996-03-20",
            "1997-03-20",
            "1998-03-21",
            "1999-03-21",
            "2000-03-20",
            "2001-03-20",
            "2002-03-21",
            "2003-03-21",
            "2004-03-20",
            "2005-03-20",
            "2006-03-21",
            "2007-03-21",
            "2008-03-20",
            "2009-03-20",
            "2010-03-21",
            "2011-03-21",
            "2012-03-20",
            "2013-03-20",
            "2014-03-21",
            "2015-03-21",
            "2016-03-20",
            "2017-03-20",
            "2018-03-21",
            "2019-03-21",
            "2020-03-20",
            "2021-03-20",
            "2022-03-21",
            "2023-03-21",
            "2024-03-20",
            "2025-03-20",
            "2026-03-20",
            "2027-03-21",
            "2028-03-20",
            "2029-03-20",
            "2030-03-20",
            "2031-03-21",
            "2032-03-20",
            "2033-03-20",
            "2034-03-20",
            "2035-03-21",
            "2036-03-20",
            "2037-03-20",
            "2038-03-20",
            "2039-03-21",
            "2040-03-20",
            "2041-03-20",
            "2042-03-20",
            "2043-03-21",
            "2044-03-20",
            "2045-03-20",
            "2046-03-20",
            "2047-03-21",
            "2048-03-20",
            "2049-03-20",
            "2050-03-20",
        )

    def test_showa_day(self):
        name = "昭和の日"
        self.assertHolidaysName(
            name, (f"{year}-04-29" for year in range(2007, 2051))
        )
        self.assertNoHolidayNameInYears(name, 2006)

    def test_constitution_memorial_day(self):
        self.assertHolidaysName(
            "憲法記念日", (f"{year}-05-03" for year in range(1949, 2051))
        )

    def test_greenery_day(self):
        name = "みどりの日"
        self.assertHolidaysName(
            name, (f"{year}-04-29" for year in range(1989, 2007))
        )
        self.assertHolidaysName(
            name, (f"{year}-05-04" for year in range(2007, 2051))
        )
        self.assertNoHolidayNameInYears(name, 1988)

    def test_national_holiday(self):
        name = "国民の休日"
        for year in (
            1988,
            1989,
            1990,
            1991,
            1993,
            1994,
            1995,
            1996,
            1999,
            2000,
            2001,
            2002,
            2004,
            2005,
            2006,
        ):
            self.assertHolidaysName(name, f"{year}-05-04")
            self.assertNoNonObservedHoliday(f"{year}-05-04")

        for dt in (
            "2009-09-22",
            "2015-09-22",
            "2019-04-30",
            "2019-05-02",
            "2026-09-22",
            "2032-09-21",
            "2037-09-22",
            "2043-09-22",
            "2049-09-21",
        ):
            self.assertHolidaysName(name, dt)
            self.assertNoNonObservedHoliday(dt)

    def test_childrens_day(self):
        self.assertHolidaysName(
            "こどもの日", (f"{year}-05-05" for year in range(1949, 2051))
        )

    def test_marine_day(self):
        self.assertHolidaysName(
            "海の日",
            "1996-07-20",
            "1997-07-20",
            "1998-07-20",
            "1999-07-20",
            "2000-07-20",
            "2001-07-20",
            "2002-07-20",
            "2003-07-21",
            "2004-07-19",
            "2005-07-18",
            "2006-07-17",
            "2007-07-16",
            "2008-07-21",
            "2009-07-20",
            "2010-07-19",
            "2011-07-18",
            "2012-07-16",
            "2013-07-15",
            "2014-07-21",
            "2015-07-20",
            "2016-07-18",
            "2017-07-17",
            "2018-07-16",
            "2019-07-15",
            "2020-07-23",
            "2021-07-22",
            "2022-07-18",
            "2023-07-17",
            "2024-07-15",
            "2025-07-21",
            "2026-07-20",
            "2027-07-19",
            "2028-07-17",
            "2029-07-16",
            "2030-07-15",
            "2031-07-21",
            "2032-07-19",
            "2033-07-18",
            "2034-07-17",
            "2035-07-16",
            "2036-07-21",
            "2037-07-20",
            "2038-07-19",
            "2039-07-18",
            "2040-07-16",
            "2041-07-15",
            "2042-07-21",
            "2043-07-20",
            "2044-07-18",
            "2045-07-17",
            "2046-07-16",
            "2047-07-15",
            "2048-07-20",
            "2049-07-19",
            "2050-07-18",
        )

        self.assertNoHoliday("1950-07-20")

    def test_mountain_day(self):
        years = set(range(2016, 2051)).difference({2020, 2021})
        name = "山の日"
        self.assertHolidaysName(name, (f"{year}-08-11" for year in years))
        self.assertHolidaysName(name, "2020-08-10", "2021-08-08")
        self.assertNoHoliday("2015-08-11")
        self.assertNoHolidayNameInYears(name, 2015)

    def test_respect_for_the_aged_day(self):
        name = "敬老の日"
        self.assertHolidaysName(
            name, (f"{year}-09-15" for year in range(1966, 2003))
        )
        self.assertNoHoliday("1965-09-15")
        self.assertNoHolidayNameInYears(name, 1965)

        self.assertHolidaysName(
            name,
            "2003-09-15",
            "2004-09-20",
            "2005-09-19",
            "2006-09-18",
            "2007-09-17",
            "2008-09-15",
            "2009-09-21",
            "2010-09-20",
            "2011-09-19",
            "2012-09-17",
            "2013-09-16",
            "2014-09-15",
            "2015-09-21",
            "2016-09-19",
            "2017-09-18",
            "2018-09-17",
            "2019-09-16",
            "2020-09-21",
            "2021-09-20",
            "2022-09-19",
            "2023-09-18",
            "2024-09-16",
            "2025-09-15",
            "2026-09-21",
            "2027-09-20",
            "2028-09-18",
            "2029-09-17",
            "2030-09-16",
            "2031-09-15",
            "2032-09-20",
            "2033-09-19",
            "2034-09-18",
            "2035-09-17",
            "2036-09-15",
            "2037-09-21",
            "2038-09-20",
            "2039-09-19",
            "2040-09-17",
            "2041-09-16",
            "2042-09-15",
            "2043-09-21",
            "2044-09-19",
            "2045-09-18",
            "2046-09-17",
            "2047-09-16",
            "2048-09-21",
            "2049-09-20",
            "2050-09-19",
        )

    def test_autumnal_equinox_day(self):
        self.assertHolidaysName(
            "秋分の日",
            "1949-09-23",
            "1950-09-23",
            "1951-09-24",
            "1952-09-23",
            "1953-09-23",
            "1954-09-23",
            "1955-09-24",
            "1956-09-23",
            "1957-09-23",
            "1958-09-23",
            "1959-09-24",
            "1960-09-23",
            "1961-09-23",
            "1962-09-23",
            "1963-09-24",
            "1964-09-23",
            "1965-09-23",
            "1966-09-23",
            "1967-09-24",
            "1968-09-23",
            "1969-09-23",
            "1970-09-23",
            "1971-09-24",
            "1972-09-23",
            "1973-09-23",
            "1974-09-23",
            "1975-09-24",
            "1976-09-23",
            "1977-09-23",
            "1978-09-23",
            "1979-09-24",
            "1980-09-23",
            "1981-09-23",
            "1982-09-23",
            "1983-09-23",
            "1984-09-23",
            "1985-09-23",
            "1986-09-23",
            "1987-09-23",
            "1988-09-23",
            "1989-09-23",
            "1990-09-23",
            "1991-09-23",
            "1992-09-23",
            "1993-09-23",
            "1994-09-23",
            "1995-09-23",
            "1996-09-23",
            "1997-09-23",
            "1998-09-23",
            "1999-09-23",
            "2000-09-23",
            "2001-09-23",
            "2002-09-23",
            "2003-09-23",
            "2004-09-23",
            "2005-09-23",
            "2006-09-23",
            "2007-09-23",
            "2008-09-23",
            "2009-09-23",
            "2010-09-23",
            "2011-09-23",
            "2012-09-22",
            "2013-09-23",
            "2014-09-23",
            "2015-09-23",
            "2016-09-22",
            "2017-09-23",
            "2018-09-23",
            "2019-09-23",
            "2020-09-22",
            "2021-09-23",
            "2022-09-23",
            "2023-09-23",
            "2024-09-22",
            "2025-09-23",
            "2026-09-23",
            "2027-09-23",
            "2028-09-22",
            "2029-09-23",
            "2030-09-23",
            "2031-09-23",
            "2032-09-22",
            "2033-09-23",
            "2034-09-23",
            "2035-09-23",
            "2036-09-22",
            "2037-09-23",
            "2038-09-23",
            "2039-09-23",
            "2040-09-22",
            "2041-09-23",
            "2042-09-23",
            "2043-09-23",
            "2044-09-22",
            "2045-09-22",
            "2046-09-23",
            "2047-09-23",
            "2048-09-22",
            "2049-09-22",
            "2050-09-23",
        )

    def test_health_and_sports_day(self):
        name = "体育の日"
        self.assertHolidaysName(
            name, (f"{year}-10-10" for year in range(1966, 2000))
        )
        self.assertNoHoliday("1965-10-10", "2000-10-10")
        self.assertNoHolidayNameInYears(name, 1965, 2020)

        self.assertHolidaysName(
            name,
            "2000-10-09",
            "2001-10-08",
            "2002-10-14",
            "2003-10-13",
            "2004-10-11",
            "2005-10-10",
            "2006-10-09",
            "2007-10-08",
            "2008-10-13",
            "2009-10-12",
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-09",
            "2018-10-08",
            "2019-10-14",
        )

        name = "スポーツの日"
        self.assertHolidaysName(
            name,
            "2020-07-24",
            "2021-07-23",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
            "2026-10-12",
            "2027-10-11",
            "2028-10-09",
            "2029-10-08",
            "2030-10-14",
            "2031-10-13",
            "2032-10-11",
            "2033-10-10",
            "2034-10-09",
            "2035-10-08",
            "2036-10-13",
            "2037-10-12",
            "2038-10-11",
            "2039-10-10",
            "2040-10-08",
            "2041-10-14",
            "2042-10-13",
            "2043-10-12",
            "2044-10-10",
            "2045-10-09",
            "2046-10-08",
            "2047-10-14",
            "2048-10-12",
            "2049-10-11",
            "2050-10-10",
        )
        self.assertNoHolidayNameInYears(name, 2019)

    def test_culture_day(self):
        self.assertHolidaysName(
            "文化の日", (f"{year}-11-03" for year in range(1949, 2051))
        )

    def test_labour_thanks_giving_day(self):
        self.assertHolidaysName(
            "勤労感謝の日", (f"{year}-11-23" for year in range(1949, 2051))
        )

    def test_emperors_birthday(self):
        name = "天皇誕生日"
        self.assertHolidaysName(
            name, (f"{year}-04-29" for year in range(1949, 1989))
        )
        self.assertHolidaysName(
            name, (f"{year}-12-23" for year in range(1989, 2019))
        )
        self.assertHolidaysName(
            name, (f"{year}-02-23" for year in range(2020, 2051))
        )
        self.assertNoHoliday("2019-12-23")

    def test_showa_emperor_holidays(self):
        self.assertHoliday("1989-02-24")

    def test_heisei_emperor_holidays(self):
        self.assertHoliday("1959-04-10", "1990-11-12")

    def test_reiwa_emperor_holidays(self):
        self.assertHoliday(
            "1993-06-09",
            "2019-05-01",
            "2019-10-22",
        )

    def test_observed_holidays(self):
        name = "振替休日"
        dt = (
            "1973-04-30",
            "1973-09-24",
            "1974-05-06",
            "1974-09-16",
            "1974-11-04",
            "1975-11-24",
            "1976-10-11",
            "1978-01-02",
            "1978-01-16",
            "1979-02-12",
            "1979-04-30",
            "1980-11-24",
            "1981-05-04",
            "1982-03-22",
            "1982-10-11",
            "1984-01-02",
            "1984-01-16",
            "1984-04-30",
            "1984-09-24",
            "1985-05-06",
            "1985-09-16",
            "1985-11-04",
            "1986-11-24",
            "1987-05-04",
            "1988-03-21",
            "1989-01-02",
            "1989-01-16",
            "1990-02-12",
            "1990-04-30",
            "1990-09-24",
            "1990-12-24",
            "1991-05-06",
            "1991-09-16",
            "1991-11-04",
            "1992-05-04",
            "1993-10-11",
            "1995-01-02",
            "1995-01-16",
            "1996-02-12",
            "1996-05-06",
            "1996-09-16",
            "1996-11-04",
            "1997-07-21",
            "1997-11-24",
            "1998-05-04",
            "1999-03-22",
            "1999-10-11",
            "2001-02-12",
            "2001-04-30",
            "2001-09-24",
            "2001-12-24",
            "2002-05-06",
            "2002-09-16",
            "2002-11-04",
            "2003-11-24",
            "2005-03-21",
            "2006-01-02",
            "2007-02-12",
            "2007-04-30",
            "2007-09-24",
            "2007-12-24",
            "2008-05-06",
            "2008-11-24",
            "2009-05-06",
            "2010-03-22",
            "2012-01-02",
            "2012-04-30",
            "2012-12-24",
            "2013-05-06",
            "2013-11-04",
            "2014-05-06",
            "2014-11-24",
            "2015-05-06",
            "2016-03-21",
            "2017-01-02",
            "2018-02-12",
            "2018-04-30",
            "2018-09-24",
            "2018-12-24",
            "2019-05-06",
            "2019-08-12",
            "2019-11-04",
            "2020-02-24",
            "2020-05-06",
            "2023-01-02",
            "2024-02-12",
            "2024-05-06",
            "2024-08-12",
            "2024-09-23",
            "2024-11-04",
            "2025-02-24",
            "2025-05-06",
            "2025-11-24",
            "2026-05-06",
            "2027-03-22",
            "2029-02-12",
            "2029-04-30",
            "2029-09-24",
            "2030-05-06",
            "2030-08-12",
            "2030-11-04",
            "2031-02-24",
            "2031-05-06",
            "2031-11-24",
            "2033-03-21",
            "2034-01-02",
            "2035-02-12",
            "2035-04-30",
            "2035-09-24",
            "2036-05-06",
            "2036-11-24",
            "2037-05-06",
            "2040-01-02",
            "2040-04-30",
            "2041-05-06",
            "2041-08-12",
            "2041-11-04",
            "2042-02-24",
            "2042-05-06",
            "2042-11-24",
            "2043-05-06",
            "2044-03-21",
            "2045-01-02",
            "2046-02-12",
            "2046-04-30",
            "2046-09-24",
            "2047-05-06",
            "2047-08-12",
            "2047-11-04",
            "2048-02-24",
            "2048-05-06",
            "2050-03-21",
        )
        self.assertHolidaysName(name, dt)
        self.assertNoNonObservedHoliday(dt)

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                jp = Japan(language=language)
                self.assertEqual(jp["2022-01-01"], "元日")
                self.assertEqual(jp["2022-11-23"], "勤労感謝の日")

        run_tests((Japan.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Japan.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        jp = Japan(language=en_us)
        self.assertEqual(jp["2022-01-01"], "New Year's Day")
        self.assertEqual(jp["2022-11-23"], "Labor Thanksgiving Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            jp = Japan(language=language)
            self.assertEqual(jp["2022-01-01"], "New Year's Day")
            self.assertEqual(jp["2022-11-23"], "Labor Thanksgiving Day")

    @mock.patch("importlib.util.find_spec", return_value=None)
    def test_dependency_pymeeus(self, find_spec):
        self.assertRaises(ImportError, lambda: Japan())
