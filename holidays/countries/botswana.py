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

from dateutil.easter import easter
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAY, JUL, SEP, DEC, SAT, SUN
from holidays.holiday_base import HolidayBase


class Botswana(HolidayBase):
    """
    https://www.gov.bw/public-holidays
    https://publicholidays.africa/botswana/2021-dates/
    https://www.timeanddate.com/holidays/botswana/
    http://www.ilo.org/dyn/travail/docs/1766/Public%20Holidays%20Act.pdf
    """

    country = "BW"
    special_holidays = {2019: ((JUL, 2, "Public Holiday"),)}

    def _populate(self, year: int):
        def _add_with_observed(
            hol_date: date, hol_name1: str, hol_name2: str = None
        ) -> None:
            self[hol_date] = hol_name1
            if hol_name2:
                self[hol_date + td(days=+1)] = hol_name2

            if self.observed and year >= 1995:
                if hol_date.weekday() == SAT and hol_name2:
                    self[hol_date + td(days=+2)] = f"{hol_name2} (Observed)"
                elif hol_date.weekday() == SUN:
                    self[
                        hol_date + td(days=+2 if hol_name2 else +1)
                    ] = f"{hol_name1} (Observed)"

        if year <= 1965:
            return None

        super()._populate(year)

        _add_with_observed(
            date(year, JAN, 1), "New Year's Day", "New Year's Day Holiday"
        )

        # Easter and easter related calculations
        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date + td(days=-1)] = "Holy Saturday"
        self[easter_date + td(days=+1)] = "Easter Monday"
        self[easter_date + td(days=+39)] = "Ascension Day"

        _add_with_observed(date(year, MAY, 1), "Labour Day")
        if (
            self.observed
            and year >= 2016
            and date(year, MAY, 1).weekday() == SAT
        ):
            self[date(year, MAY, 1) + td(days=+2)] = "Labour Day Holiday"

        _add_with_observed(date(year, JUL, 1), "Sir Seretse Khama Day")

        # 3rd Monday of July = "President's Day"
        dt = date(year, JUL, 1) + rd(weekday=MO(+3))
        self[dt] = "President's Day"
        self[dt + td(days=+1)] = "President's Day Holiday"

        _add_with_observed(
            date(year, SEP, 30), "Botswana Day", "Botswana Day Holiday"
        )

        _add_with_observed(date(year, DEC, 25), "Christmas Day", "Boxing Day")

        if (
            self.observed
            and year >= 2016
            and date(year, DEC, 26).weekday() == SAT
        ):
            self[date(year, DEC, 26) + td(days=+2)] = "Boxing Day Holiday"


class BW(Botswana):
    pass


class BWA(Botswana):
    pass
