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
from datetime import timedelta as td
from gettext import gettext as tr

from holidays.calendars.gregorian import (
    GREGORIAN_CALENDAR,
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Ukraine(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Current holidays list:
    https://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454

    Substituted holidays:
    2001 - https://zakon.rada.gov.ua/laws/show/138-2001-%D1%80
    2002,
    2003 - https://zakon.rada.gov.ua/laws/show/202-2002-%D1%80,
           https://zakon.rada.gov.ua/laws/show/705-2002-%D1%80
    2004 - https://zakon.rada.gov.ua/laws/show/773-2003-%D1%80
    2005 - https://zakon.rada.gov.ua/laws/show/936-2004-%D1%80,
           https://zakon.rada.gov.ua/laws/show/133-2005-%D1%80
    2006 - https://zakon.rada.gov.ua/laws/show/490-2005-%D1%80,
           https://zakon.rada.gov.ua/laws/show/562-2005-%D1%80
    2007 - https://zakon.rada.gov.ua/laws/show/612-2006-%D1%80
    2008 - https://zakon.rada.gov.ua/laws/show/1059-2007-%D1%80,
           https://zakon.rada.gov.ua/laws/show/538-2008-%D1%80
    2009 - https://zakon.rada.gov.ua/laws/show/1458-2008-%D1%80
    2010 - https://zakon.rada.gov.ua/laws/show/1412-2009-%D1%80
    2011 - https://zakon.rada.gov.ua/laws/show/2130-2010-%D1%80
    2012 - https://zakon.rada.gov.ua/laws/show/1210-2011-%D1%80
    2013 - https://zakon.rada.gov.ua/laws/show/1043-2012-%D1%80
    2014 - https://zakon.rada.gov.ua/laws/show/920-2013-%D1%80
    2015 - https://zakon.rada.gov.ua/laws/show/1084-2014-%D1%80
    2016 - https://zakon.rada.gov.ua/laws/show/1155-2015-%D1%80
    2017 - https://zakon.rada.gov.ua/laws/show/850-2016-%D1%80
    2018 - https://zakon.rada.gov.ua/laws/show/1-2018-%D1%80
    2019 - https://zakon.rada.gov.ua/laws/show/7-2019-%D1%80
    2020 - https://zakon.rada.gov.ua/laws/show/995-2019-%D1%80
    2021 - https://zakon.rada.gov.ua/laws/show/1191-2020-%D1%80
    2022 - https://zakon.rada.gov.ua/laws/show/1004-2021-%D1%80
    """

    country = "UA"
    default_language = "uk"
    supported_languages = ("ar", "en_US", "uk")
    # Date format (see strftime() Format Codes)
    substituted_date_format = tr("%d.%m.%Y")
    # Day off (substituted from %s).
    substituted_label = tr("Вихідний день (перенесено з %s)")
    substituted_holidays = {
        2001: (
            (APR, 28, APR, 30),
            (MAY, 5, MAY, 10),
            (MAY, 6, MAY, 11),
            (JUN, 23, JUN, 29),
            (2001, DEC, 29, DEC, 31),
        ),
        2002: (
            (MAY, 11, MAY, 3),
            (DEC, 28, DEC, 30),
            (DEC, 29, DEC, 31),
        ),
        2003: ((JAN, 4, JAN, 6),),
        2004: (
            (JAN, 10, JAN, 2),
            (JAN, 17, JAN, 5),
            (JAN, 31, JAN, 6),
            (AUG, 21, AUG, 23),
        ),
        2005: (
            (MAR, 5, MAR, 7),
            (MAY, 14, MAY, 10),
            (JUN, 25, JUN, 27),
        ),
        2006: (
            (JAN, 21, JAN, 3),
            (FEB, 4, JAN, 4),
            (FEB, 18, JAN, 5),
            (MAR, 11, JAN, 6),
            (MAY, 6, MAY, 8),
            (SEP, 9, AUG, 25),
        ),
        2007: (
            (JAN, 20, JAN, 2),
            (JAN, 27, JAN, 3),
            (FEB, 10, JAN, 4),
            (FEB, 24, JAN, 5),
            (MAR, 3, MAR, 9),
            (APR, 28, APR, 30),
            (JUN, 16, JUN, 29),
            (DEC, 29, DEC, 31),
        ),
        2008: (
            (JAN, 12, JAN, 2),
            (JAN, 26, JAN, 3),
            (FEB, 9, JAN, 4),
            (MAY, 17, APR, 29),
            (MAY, 31, APR, 30),
        ),
        2009: (
            (JAN, 10, JAN, 2),
            (JAN, 24, JAN, 5),
            (FEB, 7, JAN, 6),
        ),
        2010: (
            (JAN, 30, JAN, 4),
            (FEB, 13, JAN, 5),
            (FEB, 27, JAN, 6),
            (MAR, 13, JAN, 8),
            (AUG, 21, AUG, 23),
        ),
        2011: (
            (MAR, 12, MAR, 7),
            (JUN, 25, JUN, 27),
        ),
        2012: (
            (MAR, 3, MAR, 9),
            (APR, 28, APR, 20),
            (JUL, 7, JUN, 29),
            (DEC, 29, DEC, 31),
        ),
        2013: (
            (MAY, 18, MAY, 3),
            (JUN, 1, MAY, 10),
        ),
        2014: (
            (JAN, 11, JAN, 2),
            (JAN, 25, JAN, 3),
            (FEB, 8, JAN, 6),
        ),
        2015: (
            (JAN, 17, JAN, 2),
            (JAN, 31, JAN, 8),
            (FEB, 14, JAN, 9),
        ),
        2016: (
            (JAN, 16, JAN, 8),
            (MAR, 12, MAR, 7),
            (JUL, 2, JUN, 27),
        ),
        2017: (
            (MAY, 13, MAY, 8),
            (AUG, 19, AUG, 25),
        ),
        2018: (
            (MAR, 3, MAR, 9),
            (MAY, 5, APR, 30),
            (JUN, 23, JUN, 29),
            (DEC, 22, DEC, 24),
            (DEC, 29, DEC, 31),
        ),
        2019: (
            (MAY, 11, APR, 30),
            (DEC, 21, DEC, 30),
            (DEC, 28, DEC, 31),
        ),
        2020: (JAN, 11, JAN, 6),
        2021: (
            (JAN, 16, JAN, 8),
            (AUG, 28, AUG, 23),
            (OCT, 23, OCT, 15),
        ),
        2022: (MAR, 12, MAR, 7),
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        # The current set of holidays came into force in 1991
        if year <= 1990:
            return None

        # There is no holidays in Ukraine during the period of martial law
        # https://zakon.rada.gov.ua/laws/show/2136-20#n26
        # law is in force from March 15, 2022
        if year >= 2023:
            return None

        super()._populate(year)
        observed_dates = set()

        # New Year's Day.
        observed_dates.add(self._add_new_years_day(tr("Новий рік")))

        observed_dates.add(
            self._add_christmas_day(
                # Christmas (Julian calendar).
                tr("Різдво Христове (за юліанським календарем)")
            )
        )

        # International Women's Day.
        observed_dates.add(self._add_womens_day(tr("Міжнародний жіночий день")))

        # There is no holidays from March 15, 2022
        # https://zakon.rada.gov.ua/laws/show/2136-20#n26
        if year <= 2021:
            # Easter Sunday (Pascha).
            observed_dates.add(self._add_easter_sunday(tr("Великдень (Пасха)")))

            # Holy Trinity Day.
            observed_dates.add(self._add_whit_sunday(tr("Трійця")))

            name = (
                # Labour Day.
                tr("День праці")
                if year >= 2018
                # International Workers' Solidarity Day.
                else tr("День міжнародної солідарності трудящих")
            )
            may_1 = self._add_labor_day(name)
            observed_dates.add(may_1)
            if year <= 2017:
                observed_dates.add(self._add_holiday(name, may_1 + td(days=+1)))

            name = (
                # Day of Victory over Nazism in World War II (Victory Day).
                tr("День перемоги над нацизмом у Другій світовій війні (День перемоги)")
                if year >= 2016
                # Victory Day.
                else tr("День перемоги")
            )
            observed_dates.add(self._add_world_war_two_victory_day(name))

            if year >= 1997:
                observed_dates.add(
                    # Day of the Constitution of Ukraine.
                    self._add_holiday(tr("День Конституції України"), JUN, 28)
                )

            # Independence Day.
            name = tr("День незалежності України")
            if year >= 1992:
                observed_dates.add(self._add_holiday(name, AUG, 24))
            else:
                self._add_holiday(name, JUL, 16)

            if year >= 2015:
                name = (
                    # Day of defenders of Ukraine.
                    tr("День захисників і захисниць України")
                    if year >= 2021
                    # Defender of Ukraine Day.
                    else tr("День захисника України")
                )
                observed_dates.add(self._add_holiday(name, OCT, 14))

            if year <= 1999:
                # Anniversary of the Great October Socialist Revolution.
                name = tr("Річниця Великої Жовтневої соціалістичної революції")
                observed_dates.add(self._add_holiday(name, NOV, 7))
                observed_dates.add(self._add_holiday(name, NOV, 8))

            if year >= 2017:
                observed_dates.add(
                    self._add_christmas_day(
                        # Christmas (Gregorian calendar).
                        tr("Різдво Христове (за григоріанським календарем)"),
                        GREGORIAN_CALENDAR,
                    )
                )

        # 27.01.1995: holiday on weekend move to next workday
        # https://zakon.rada.gov.ua/laws/show/35/95-вр
        # 10.01.1998: cancelled
        # https://zakon.rada.gov.ua/laws/show/785/97-вр
        # 23.04.1999: holiday on weekend move to next workday
        # https://zakon.rada.gov.ua/laws/show/576-14
        if self.observed:
            for dt in sorted(observed_dates):
                if self._is_weekend(dt) and (
                    date(1995, JAN, 27) <= dt <= date(1998, JAN, 9) or dt >= date(1999, APR, 23)
                ):
                    obs_date = dt + td(days=+2 if self._is_saturday(dt) else +1)
                    while obs_date in self:
                        obs_date += td(days=+1)
                    hol_name = self.tr("%s (вихідний)") % self[dt]
                    self._add_holiday(hol_name, obs_date)


class UA(Ukraine):
    pass


class UKR(Ukraine):
    pass
