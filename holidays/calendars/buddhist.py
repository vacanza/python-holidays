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
from holidays.constants import MAY, JUN

VESAK = "VESAK"
VESAK_MAY = "VESAK_MAY"


class _BuddhistLunisolar:
    VESAK_DATES = {
        1901: (JUN, 1),
        1902: (MAY, 22),
        1903: (MAY, 11),
        1904: (MAY, 29),
        1905: (MAY, 18),
        1906: (MAY, 8),
        1907: (MAY, 26),
        1908: (MAY, 14),
        1909: (JUN, 2),
        1910: (MAY, 23),
        1911: (MAY, 13),
        1912: (MAY, 31),
        1913: (MAY, 20),
        1914: (MAY, 9),
        1915: (MAY, 28),
        1916: (MAY, 16),
        1917: (JUN, 4),
        1918: (MAY, 24),
        1919: (MAY, 14),
        1920: (JUN, 1),
        1921: (MAY, 22),
        1922: (MAY, 11),
        1923: (MAY, 30),
        1924: (MAY, 18),
        1925: (MAY, 7),
        1926: (MAY, 26),
        1927: (MAY, 15),
        1928: (JUN, 2),
        1929: (MAY, 23),
        1930: (MAY, 13),
        1931: (MAY, 31),
        1932: (MAY, 20),
        1933: (MAY, 9),
        1934: (MAY, 27),
        1935: (MAY, 17),
        1936: (JUN, 4),
        1937: (MAY, 24),
        1938: (MAY, 14),
        1939: (JUN, 2),
        1940: (MAY, 21),
        1941: (MAY, 10),
        1942: (MAY, 29),
        1943: (MAY, 18),
        1944: (MAY, 7),
        1945: (MAY, 26),
        1946: (MAY, 15),
        1947: (JUN, 3),
        1948: (MAY, 23),
        1949: (MAY, 12),
        1950: (MAY, 31),
        1951: (MAY, 20),
        1952: (MAY, 8),
        1953: (MAY, 27),
        1954: (MAY, 17),
        1955: (JUN, 5),
        1956: (MAY, 24),
        1957: (MAY, 14),
        1958: (JUN, 2),
        1959: (MAY, 22),
        1960: (MAY, 10),
        1961: (MAY, 29),
        1962: (MAY, 18),
        1963: (MAY, 8),
        1964: (MAY, 26),
        1965: (MAY, 15),
        1966: (JUN, 3),
        1967: (MAY, 23),
        1968: (MAY, 11),
        1969: (MAY, 30),
        1970: (MAY, 19),
        1971: (MAY, 9),
        1972: (MAY, 27),
        1973: (MAY, 17),
        1974: (MAY, 6),
        1975: (MAY, 25),
        1976: (MAY, 13),
        1977: (JUN, 1),
        1978: (MAY, 21),
        1979: (MAY, 10),
        1980: (MAY, 28),
        1981: (MAY, 18),
        1982: (MAY, 8),
        1983: (MAY, 27),
        1984: (MAY, 15),
        1985: (JUN, 3),
        1986: (MAY, 23),
        1987: (MAY, 12),
        1988: (MAY, 30),
        1989: (MAY, 19),
        1990: (MAY, 9),
        1991: (MAY, 28),
        1992: (MAY, 17),
        1993: (JUN, 4),
        1994: (MAY, 25),
        1995: (MAY, 14),
        1996: (MAY, 31),
        1997: (MAY, 21),
        1998: (MAY, 10),
        1999: (MAY, 29),
        2000: (MAY, 18),
        2001: (MAY, 7),
        2002: (MAY, 26),
        2003: (MAY, 15),
        2004: (JUN, 2),
        2005: (MAY, 22),
        2006: (MAY, 12),
        2007: (MAY, 31),
        2008: (MAY, 19),
        2009: (MAY, 9),
        2010: (MAY, 28),
        2011: (MAY, 17),
        2012: (MAY, 5),
        2013: (MAY, 24),
        2014: (MAY, 13),
        2015: (JUN, 1),
        2016: (MAY, 21),
        2017: (MAY, 10),
        2018: (MAY, 29),
        2019: (MAY, 19),
        2020: (MAY, 7),
        2021: (MAY, 26),
        2022: (MAY, 15),
        2023: (JUN, 2),
        2024: (MAY, 22),
        2025: (MAY, 11),
        2026: (MAY, 31),
        2027: (MAY, 20),
        2028: (MAY, 9),
        2029: (MAY, 27),
        2030: (MAY, 16),
        2031: (JUN, 4),
        2032: (MAY, 23),
        2033: (MAY, 13),
        2034: (JUN, 1),
        2035: (MAY, 22),
        2036: (MAY, 10),
        2037: (MAY, 29),
        2038: (MAY, 18),
        2039: (MAY, 7),
        2040: (MAY, 25),
        2041: (MAY, 14),
        2042: (JUN, 2),
        2043: (MAY, 23),
        2044: (MAY, 12),
        2045: (MAY, 31),
        2046: (MAY, 20),
        2047: (MAY, 9),
        2048: (MAY, 27),
        2049: (MAY, 16),
        2050: (JUN, 4),
        2051: (MAY, 24),
        2052: (MAY, 13),
        2053: (JUN, 1),
        2054: (MAY, 22),
        2055: (MAY, 11),
        2056: (MAY, 29),
        2057: (MAY, 18),
        2058: (MAY, 7),
        2059: (MAY, 26),
        2060: (MAY, 14),
        2061: (JUN, 2),
        2062: (MAY, 23),
        2063: (MAY, 12),
        2064: (MAY, 30),
        2065: (MAY, 19),
        2066: (MAY, 8),
        2067: (MAY, 27),
        2068: (MAY, 16),
        2069: (MAY, 5),
        2070: (MAY, 24),
        2071: (MAY, 14),
        2072: (JUN, 1),
        2073: (MAY, 21),
        2074: (MAY, 10),
        2075: (MAY, 29),
        2076: (MAY, 17),
        2077: (MAY, 7),
        2078: (MAY, 26),
        2079: (MAY, 15),
        2080: (JUN, 2),
        2081: (MAY, 23),
        2082: (MAY, 12),
        2083: (MAY, 31),
        2084: (MAY, 19),
        2085: (MAY, 8),
        2086: (MAY, 27),
        2087: (MAY, 17),
        2088: (MAY, 5),
        2089: (MAY, 24),
        2090: (MAY, 14),
        2091: (JUN, 1),
        2092: (MAY, 20),
        2093: (MAY, 10),
        2094: (MAY, 28),
        2095: (MAY, 18),
        2096: (MAY, 7),
        2097: (MAY, 26),
        2098: (MAY, 15),
        2099: (JUN, 3),
    }

    VESAK_MAY_DATES = {
        1901: (MAY, 3),
        1902: (MAY, 22),
        1903: (MAY, 11),
        1904: (MAY, 29),
        1905: (MAY, 18),
        1906: (MAY, 8),
        1907: (MAY, 26),
        1908: (MAY, 14),
        1909: (MAY, 4),
        1910: (MAY, 23),
        1911: (MAY, 13),
        1912: (MAY, 1),
        1913: (MAY, 20),
        1914: (MAY, 9),
        1915: (MAY, 28),
        1916: (MAY, 16),
        1917: (MAY, 5),
        1918: (MAY, 24),
        1919: (MAY, 14),
        1920: (MAY, 3),
        1921: (MAY, 22),
        1922: (MAY, 11),
        1923: (MAY, 30),
        1924: (MAY, 18),
        1925: (MAY, 7),
        1926: (MAY, 26),
        1927: (MAY, 15),
        1928: (MAY, 4),
        1929: (MAY, 23),
        1930: (MAY, 13),
        1931: (MAY, 2),
        1932: (MAY, 20),
        1933: (MAY, 9),
        1934: (MAY, 27),
        1935: (MAY, 17),
        1936: (MAY, 5),
        1937: (MAY, 24),
        1938: (MAY, 14),
        1939: (MAY, 4),
        1940: (MAY, 21),
        1941: (MAY, 10),
        1942: (MAY, 29),
        1943: (MAY, 18),
        1944: (MAY, 7),
        1945: (MAY, 26),
        1946: (MAY, 15),
        1947: (MAY, 5),
        1948: (MAY, 23),
        1949: (MAY, 12),
        1950: (MAY, 1),
        1951: (MAY, 20),
        1952: (MAY, 8),
        1953: (MAY, 27),
        1954: (MAY, 17),
        1955: (MAY, 6),
        1956: (MAY, 24),
        1957: (MAY, 14),
        1958: (MAY, 3),
        1959: (MAY, 22),
        1960: (MAY, 10),
        1961: (MAY, 29),
        1962: (MAY, 18),
        1963: (MAY, 8),
        1964: (MAY, 26),
        1965: (MAY, 15),
        1966: (MAY, 5),
        1967: (MAY, 23),
        1968: (MAY, 11),
        1969: (MAY, 1),
        1970: (MAY, 19),
        1971: (MAY, 9),
        1972: (MAY, 27),
        1973: (MAY, 17),
        1974: (MAY, 6),
        1975: (MAY, 25),
        1976: (MAY, 13),
        1977: (MAY, 2),
        1978: (MAY, 21),
        1979: (MAY, 10),
        1980: (MAY, 28),
        1981: (MAY, 18),
        1982: (MAY, 8),
        1983: (MAY, 27),
        1984: (MAY, 15),
        1985: (MAY, 4),
        1986: (MAY, 23),
        1987: (MAY, 12),
        1988: (MAY, 30),
        1989: (MAY, 19),
        1990: (MAY, 9),
        1991: (MAY, 28),
        1992: (MAY, 17),
        1993: (MAY, 6),
        1994: (MAY, 25),
        1995: (MAY, 14),
        1996: (MAY, 2),
        1997: (MAY, 21),
        1998: (MAY, 10),
        1999: (MAY, 29),
        2000: (MAY, 18),
        2001: (MAY, 7),
        2002: (MAY, 26),
        2003: (MAY, 15),
        2004: (MAY, 3),
        2005: (MAY, 22),
        2006: (MAY, 12),
        2007: (MAY, 1),
        2008: (MAY, 19),
        2009: (MAY, 9),
        2010: (MAY, 28),
        2011: (MAY, 17),
        2012: (MAY, 5),
        2013: (MAY, 24),
        2014: (MAY, 13),
        2015: (MAY, 3),
        2016: (MAY, 21),
        2017: (MAY, 10),
        2018: (MAY, 29),
        2019: (MAY, 19),
        2020: (MAY, 7),
        2021: (MAY, 26),
        2022: (MAY, 15),
        2023: (MAY, 4),
        2024: (MAY, 22),
        2025: (MAY, 11),
        2026: (MAY, 1),
        2027: (MAY, 20),
        2028: (MAY, 9),
        2029: (MAY, 27),
        2030: (MAY, 16),
        2031: (MAY, 6),
        2032: (MAY, 23),
        2033: (MAY, 13),
        2034: (MAY, 3),
        2035: (MAY, 22),
        2036: (MAY, 10),
        2037: (MAY, 29),
        2038: (MAY, 18),
        2039: (MAY, 7),
        2040: (MAY, 25),
        2041: (MAY, 14),
        2042: (MAY, 4),
        2043: (MAY, 23),
        2044: (MAY, 12),
        2045: (MAY, 1),
        2046: (MAY, 20),
        2047: (MAY, 9),
        2048: (MAY, 27),
        2049: (MAY, 16),
        2050: (MAY, 5),
        2051: (MAY, 24),
        2052: (MAY, 13),
        2053: (MAY, 3),
        2054: (MAY, 22),
        2055: (MAY, 11),
        2056: (MAY, 29),
        2057: (MAY, 18),
        2058: (MAY, 7),
        2059: (MAY, 26),
        2060: (MAY, 14),
        2061: (MAY, 4),
        2062: (MAY, 23),
        2063: (MAY, 12),
        2064: (MAY, 1),
        2065: (MAY, 19),
        2066: (MAY, 8),
        2067: (MAY, 27),
        2068: (MAY, 16),
        2069: (MAY, 5),
        2070: (MAY, 24),
        2071: (MAY, 14),
        2072: (MAY, 2),
        2073: (MAY, 21),
        2074: (MAY, 10),
        2075: (MAY, 29),
        2076: (MAY, 17),
        2077: (MAY, 7),
        2078: (MAY, 26),
        2079: (MAY, 15),
        2080: (MAY, 4),
        2081: (MAY, 23),
        2082: (MAY, 12),
        2083: (MAY, 1),
        2084: (MAY, 19),
        2085: (MAY, 8),
        2086: (MAY, 27),
        2087: (MAY, 17),
        2088: (MAY, 5),
        2089: (MAY, 24),
        2090: (MAY, 14),
        2091: (MAY, 3),
        2092: (MAY, 20),
        2093: (MAY, 10),
        2094: (MAY, 28),
        2095: (MAY, 18),
        2096: (MAY, 7),
        2097: (MAY, 26),
        2098: (MAY, 15),
        2099: (MAY, 4),
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

    def vesak_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(VESAK, year)

    def vesak_may_date(self, year: int) -> Tuple[Optional[date], bool]:
        return self._get_holiday(VESAK_MAY, year)
