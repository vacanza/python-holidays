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

from datetime import date
from typing import Optional, Tuple

from holidays.calendars.custom import _CustomCalendarType
from holidays.constants import JAN, FEB, MAR, OCT, NOV

DIWALI = "DIWALI"
THAIPUSAM = "THAIPUSAM"


class _HinduLunisolar:
    DIWALI_DATES = {
        1901: (NOV, 9),
        1902: (OCT, 29),
        1903: (NOV, 17),
        1904: (NOV, 5),
        1905: (OCT, 26),
        1906: (NOV, 14),
        1907: (NOV, 4),
        1908: (OCT, 23),
        1909: (NOV, 11),
        1910: (OCT, 31),
        1911: (NOV, 19),
        1912: (NOV, 7),
        1913: (OCT, 27),
        1914: (NOV, 15),
        1915: (NOV, 5),
        1916: (OCT, 25),
        1917: (NOV, 13),
        1918: (NOV, 2),
        1919: (NOV, 20),
        1920: (NOV, 8),
        1921: (OCT, 29),
        1922: (NOV, 17),
        1923: (NOV, 6),
        1924: (OCT, 26),
        1925: (NOV, 14),
        1926: (NOV, 3),
        1927: (OCT, 23),
        1928: (NOV, 10),
        1929: (OCT, 30),
        1930: (NOV, 18),
        1931: (NOV, 8),
        1932: (OCT, 27),
        1933: (NOV, 16),
        1934: (NOV, 5),
        1935: (OCT, 25),
        1936: (NOV, 12),
        1937: (NOV, 1),
        1938: (NOV, 20),
        1939: (NOV, 9),
        1940: (OCT, 29),
        1941: (NOV, 17),
        1942: (NOV, 6),
        1943: (OCT, 27),
        1944: (NOV, 14),
        1945: (NOV, 3),
        1946: (OCT, 23),
        1947: (NOV, 11),
        1948: (OCT, 30),
        1949: (NOV, 18),
        1950: (NOV, 8),
        1951: (OCT, 28),
        1952: (NOV, 15),
        1953: (NOV, 5),
        1954: (OCT, 25),
        1955: (NOV, 12),
        1956: (NOV, 1),
        1957: (NOV, 20),
        1958: (NOV, 9),
        1959: (OCT, 30),
        1960: (NOV, 17),
        1961: (NOV, 6),
        1962: (OCT, 26),
        1963: (NOV, 14),
        1964: (NOV, 2),
        1965: (OCT, 22),
        1966: (NOV, 10),
        1967: (OCT, 31),
        1968: (NOV, 18),
        1969: (NOV, 8),
        1970: (OCT, 28),
        1971: (NOV, 16),
        1972: (NOV, 4),
        1973: (OCT, 24),
        1974: (NOV, 12),
        1975: (NOV, 1),
        1976: (NOV, 19),
        1977: (NOV, 9),
        1978: (OCT, 30),
        1979: (NOV, 18),
        1980: (NOV, 6),
        1981: (OCT, 26),
        1982: (NOV, 13),
        1983: (NOV, 3),
        1984: (OCT, 22),
        1985: (NOV, 10),
        1986: (OCT, 31),
        1987: (NOV, 19),
        1988: (NOV, 7),
        1989: (OCT, 27),
        1990: (NOV, 15),
        1991: (NOV, 4),
        1992: (OCT, 24),
        1993: (NOV, 12),
        1994: (NOV, 1),
        1995: (NOV, 20),
        1996: (NOV, 9),
        1997: (OCT, 29),
        1998: (NOV, 17),
        1999: (NOV, 6),
        2000: (OCT, 25),
        2001: (NOV, 13),
        2002: (NOV, 3),
        2003: (OCT, 23),
        2004: (NOV, 10),
        2005: (OCT, 31),
        2006: (NOV, 19),
        2007: (NOV, 8),
        2008: (OCT, 27),
        2009: (NOV, 15),
        2010: (NOV, 4),
        2011: (OCT, 25),
        2012: (NOV, 12),
        2013: (NOV, 1),
        2014: (NOV, 20),
        2015: (NOV, 10),
        2016: (OCT, 29),
        2017: (NOV, 16),
        2018: (NOV, 6),
        2019: (OCT, 26),
        2020: (NOV, 13),
        2021: (NOV, 3),
        2022: (OCT, 23),
        2023: (NOV, 11),
        2024: (OCT, 30),
        2025: (NOV, 18),
        2026: (NOV, 7),
        2027: (OCT, 27),
        2028: (NOV, 14),
        2029: (NOV, 4),
        2030: (OCT, 25),
        2031: (NOV, 13),
        2032: (NOV, 1),
        2033: (OCT, 21),
        2034: (NOV, 9),
        2035: (OCT, 29),
        2036: (NOV, 16),
        2037: (NOV, 5),
        2038: (OCT, 26),
        2039: (NOV, 14),
        2040: (NOV, 3),
        2041: (OCT, 23),
        2042: (NOV, 11),
        2043: (OCT, 31),
        2044: (NOV, 17),
        2045: (NOV, 7),
        2046: (OCT, 27),
        2047: (NOV, 15),
        2048: (NOV, 4),
        2049: (OCT, 25),
        2050: (NOV, 12),
        2051: (NOV, 1),
        2052: (NOV, 19),
        2053: (NOV, 8),
        2054: (OCT, 29),
        2055: (NOV, 17),
        2056: (NOV, 5),
        2057: (OCT, 26),
        2058: (NOV, 14),
        2059: (NOV, 3),
        2060: (OCT, 22),
        2061: (NOV, 10),
        2062: (OCT, 30),
        2063: (NOV, 18),
        2064: (NOV, 7),
        2065: (OCT, 27),
        2066: (NOV, 15),
        2067: (NOV, 5),
        2068: (OCT, 24),
        2069: (NOV, 12),
        2070: (NOV, 1),
        2071: (NOV, 20),
        2072: (NOV, 8),
        2073: (OCT, 29),
        2074: (NOV, 17),
        2075: (NOV, 6),
        2076: (OCT, 26),
        2077: (NOV, 14),
        2078: (NOV, 3),
        2079: (OCT, 23),
        2080: (NOV, 9),
        2081: (OCT, 30),
        2082: (NOV, 18),
        2083: (NOV, 8),
        2084: (OCT, 27),
        2085: (NOV, 15),
        2086: (NOV, 4),
        2087: (OCT, 24),
        2088: (NOV, 11),
        2089: (OCT, 31),
        2090: (NOV, 19),
        2091: (NOV, 9),
        2092: (OCT, 29),
        2093: (NOV, 17),
        2094: (NOV, 6),
        2095: (OCT, 26),
        2096: (NOV, 13),
        2097: (NOV, 2),
        2098: (OCT, 22),
        2099: (NOV, 10),
    }

    THAIPUSAM_DATES = {
        1901: (MAR, 5),
        1902: (FEB, 23),
        1903: (JAN, 14),
        1904: (MAR, 2),
        1905: (FEB, 19),
        1906: (JAN, 10),
        1907: (FEB, 27),
        1908: (FEB, 17),
        1909: (JAN, 7),
        1910: (FEB, 24),
        1911: (JAN, 15),
        1912: (MAR, 4),
        1913: (FEB, 21),
        1914: (JAN, 11),
        1915: (MAR, 1),
        1916: (FEB, 18),
        1917: (JAN, 8),
        1918: (FEB, 26),
        1919: (FEB, 15),
        1920: (MAR, 5),
        1921: (FEB, 23),
        1922: (JAN, 13),
        1923: (MAR, 2),
        1924: (FEB, 19),
        1925: (JAN, 9),
        1926: (FEB, 27),
        1927: (FEB, 17),
        1928: (JAN, 8),
        1929: (FEB, 24),
        1930: (JAN, 15),
        1931: (MAR, 4),
        1932: (FEB, 21),
        1933: (JAN, 11),
        1934: (FEB, 28),
        1935: (FEB, 18),
        1936: (JAN, 9),
        1937: (FEB, 26),
        1938: (FEB, 15),
        1939: (MAR, 6),
        1940: (FEB, 23),
        1941: (JAN, 12),
        1942: (MAR, 2),
        1943: (FEB, 19),
        1944: (JAN, 10),
        1945: (FEB, 27),
        1946: (FEB, 17),
        1947: (JAN, 7),
        1948: (FEB, 25),
        1949: (FEB, 13),
        1950: (MAR, 3),
        1951: (FEB, 21),
        1952: (JAN, 12),
        1953: (FEB, 28),
        1954: (FEB, 18),
        1955: (JAN, 9),
        1956: (FEB, 26),
        1957: (FEB, 15),
        1958: (MAR, 5),
        1959: (FEB, 22),
        1960: (JAN, 13),
        1961: (MAR, 2),
        1962: (FEB, 19),
        1963: (JAN, 10),
        1964: (FEB, 28),
        1965: (FEB, 16),
        1966: (JAN, 6),
        1967: (FEB, 24),
        1968: (FEB, 13),
        1969: (MAR, 3),
        1970: (FEB, 21),
        1971: (JAN, 12),
        1972: (FEB, 29),
        1973: (FEB, 18),
        1974: (JAN, 8),
        1975: (FEB, 26),
        1976: (FEB, 15),
        1977: (MAR, 5),
        1978: (FEB, 22),
        1979: (JAN, 13),
        1980: (MAR, 2),
        1981: (FEB, 19),
        1982: (JAN, 10),
        1983: (FEB, 28),
        1984: (FEB, 17),
        1985: (MAR, 6),
        1986: (FEB, 23),
        1987: (JAN, 14),
        1988: (MAR, 3),
        1989: (FEB, 21),
        1990: (JAN, 12),
        1991: (MAR, 1),
        1992: (FEB, 18),
        1993: (JAN, 8),
        1994: (FEB, 25),
        1995: (FEB, 14),
        1996: (MAR, 4),
        1997: (FEB, 22),
        1998: (JAN, 13),
        1999: (MAR, 3),
        2000: (FEB, 20),
        2001: (JAN, 9),
        2002: (FEB, 27),
        2003: (FEB, 16),
        2004: (JAN, 7),
        2005: (FEB, 23),
        2006: (FEB, 13),
        2007: (MAR, 4),
        2008: (FEB, 22),
        2009: (JAN, 11),
        2010: (MAR, 1),
        2011: (FEB, 18),
        2012: (JAN, 8),
        2013: (FEB, 25),
        2014: (FEB, 14),
        2015: (MAR, 5),
        2016: (FEB, 23),
        2017: (JAN, 13),
        2018: (MAR, 2),
        2019: (FEB, 20),
        2020: (JAN, 10),
        2021: (FEB, 26),
        2022: (FEB, 16),
        2023: (JAN, 7),
        2024: (FEB, 24),
        2025: (JAN, 14),
        2026: (MAR, 4),
        2027: (FEB, 21),
        2028: (JAN, 11),
        2029: (FEB, 28),
        2030: (FEB, 17),
        2031: (JAN, 8),
        2032: (FEB, 26),
        2033: (FEB, 14),
        2034: (MAR, 5),
        2035: (FEB, 23),
        2036: (JAN, 13),
        2037: (MAR, 2),
        2038: (FEB, 19),
        2039: (JAN, 9),
        2040: (FEB, 27),
        2041: (FEB, 15),
        2042: (JAN, 7),
        2043: (FEB, 24),
        2044: (FEB, 14),
        2045: (MAR, 4),
        2046: (FEB, 21),
        2047: (JAN, 11),
        2048: (FEB, 28),
        2049: (FEB, 17),
        2050: (JAN, 8),
        2051: (FEB, 26),
        2052: (FEB, 15),
        2053: (MAR, 5),
        2054: (FEB, 22),
        2055: (JAN, 13),
        2056: (MAR, 1),
        2057: (FEB, 18),
        2058: (JAN, 9),
        2059: (FEB, 27),
        2060: (FEB, 17),
        2061: (JAN, 6),
        2062: (FEB, 24),
        2063: (FEB, 13),
        2064: (MAR, 3),
        2065: (FEB, 20),
        2066: (JAN, 11),
        2067: (FEB, 28),
        2068: (FEB, 18),
        2069: (JAN, 8),
        2070: (FEB, 25),
        2071: (FEB, 15),
        2072: (MAR, 5),
        2073: (FEB, 22),
        2074: (JAN, 12),
        2075: (MAR, 2),
        2076: (FEB, 19),
        2077: (JAN, 9),
        2078: (FEB, 27),
        2079: (FEB, 16),
        2080: (JAN, 7),
        2081: (FEB, 23),
        2082: (FEB, 12),
        2083: (MAR, 3),
        2084: (FEB, 21),
        2085: (JAN, 11),
        2086: (FEB, 28),
        2087: (FEB, 18),
        2088: (JAN, 9),
        2089: (FEB, 25),
        2090: (FEB, 14),
        2091: (MAR, 5),
        2092: (FEB, 22),
        2093: (JAN, 12),
        2094: (MAR, 1),
        2095: (FEB, 19),
        2096: (JAN, 10),
        2097: (FEB, 27),
        2098: (FEB, 16),
        2099: (JAN, 6),
    }

    def _get_holiday(
        self, holiday: str, year: int
    ) -> Tuple[Optional[date], bool]:
        estimated_dates = getattr(self, f"{holiday}_DATES", {})
        exact_dates = getattr(
            self,
            f"{holiday}_DATES_{_CustomCalendarType.CUSTOM_ATTR_POSTFIX}",
            {},
        )
        dt = exact_dates.get(year, estimated_dates.get(year, ()))
        return date(year, *dt) if dt else None, year not in exact_dates

    def diwali_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(DIWALI, year)

    def thaipusam_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(THAIPUSAM, year)
