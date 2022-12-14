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

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import TH, SU
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, APR, MAY, JUN, AUG, SEP, NOV, DEC
from holidays.holiday_base import HolidayBase


class Switzerland(HolidayBase):
    country = "CH"
    subdivisions = [
        "AG",
        "AR",
        "AI",
        "BL",
        "BS",
        "BE",
        "FR",
        "GE",
        "GL",
        "GR",
        "JU",
        "LU",
        "NE",
        "NW",
        "OW",
        "SG",
        "SH",
        "SZ",
        "SO",
        "TG",
        "TI",
        "UR",
        "VD",
        "VS",
        "ZG",
        "ZH",
    ]

    def _populate(self, year):
        super()._populate(year)

        # public holidays
        self[date(year, JAN, 1)] = "Neujahrestag"

        if self.subdiv in {
            "AG",
            "BE",
            "FR",
            "GL",
            "GR",
            "JU",
            "LU",
            "NE",
            "OW",
            "SH",
            "SO",
            "TG",
            "VD",
            "ZG",
            "ZH",
        }:
            self[date(year, JAN, 2)] = "Berchtoldstag"

        if self.subdiv in {"SZ", "TI", "UR"}:
            self[date(year, JAN, 6)] = "Heilige Drei Könige"

        if self.subdiv == "NE":
            self[date(year, MAR, 1)] = "Jahrestag der Ausrufung der Republik"

        if self.subdiv in {"NW", "SZ", "TI", "UR", "VS"}:
            self[date(year, MAR, 19)] = "Josefstag"

        easter_date = easter(year)
        # Näfelser Fahrt (first Thursday in April but not in Holy Week)
        if self.subdiv == "GL" and year >= 1835:
            dt = date(year, APR, 1) + rd(weekday=TH)
            if dt == easter_date + rd(days=-3):
                dt += rd(days=+7)
            self[dt] = "Näfelser Fahrt"

        # it's a Holiday on a Sunday
        self[easter_date] = "Ostern"

        # VS don't have easter
        if self.subdiv != "VS":
            self[easter_date + rd(days=-2)] = "Karfreitag"
            self[easter_date + rd(days=+1)] = "Ostermontag"

        if self.subdiv in {
            "BL",
            "BS",
            "JU",
            "NE",
            "SH",
            "SO",
            "TG",
            "TI",
            "ZH",
        }:
            self[date(year, MAY, 1)] = "Tag der Arbeit"

        self[easter_date + rd(days=+39)] = "Auffahrt"

        # it's a Holiday on a Sunday
        self[easter_date + rd(days=+49)] = "Pfingsten"

        self[easter_date + rd(days=+50)] = "Pfingstmontag"

        if self.subdiv in {
            "AI",
            "JU",
            "LU",
            "NW",
            "OW",
            "SZ",
            "TI",
            "UR",
            "VS",
            "ZG",
        }:
            self[easter_date + rd(days=+60)] = "Fronleichnam"

        if self.subdiv == "JU":
            self[date(year, JUN, 23)] = "Fest der Unabhängigkeit"

        if self.subdiv == "TI":
            self[date(year, JUN, 29)] = "Peter und Paul"

        if year >= 1291:
            self[date(year, AUG, 1)] = "Nationalfeiertag"

        if self.subdiv in {
            "AI",
            "JU",
            "LU",
            "NW",
            "OW",
            "SZ",
            "TI",
            "UR",
            "VS",
            "ZG",
        }:
            self[date(year, AUG, 15)] = "Mariä Himmelfahrt"

        if self.subdiv == "VD":
            # Monday after the third Sunday of September
            dt = date(year, SEP, 1) + rd(weekday=SU(+3)) + rd(days=+1)
            self[dt] = "Lundi du Jeûne"

        if self.subdiv == "GE":
            # Thursday after the first Sunday of September
            dt = date(year, SEP, 1) + rd(weekday=SU) + rd(days=+4)
            self[dt] = "Jeûne genevois"

        if self.subdiv == "OW":
            self[date(year, SEP, 25)] = "Bruder Klaus"

        if self.subdiv in {
            "AI",
            "GL",
            "JU",
            "LU",
            "NW",
            "OW",
            "SG",
            "SZ",
            "TI",
            "UR",
            "VS",
            "ZG",
        }:
            self[date(year, NOV, 1)] = "Allerheiligen"

        if self.subdiv in {
            "AI",
            "LU",
            "NW",
            "OW",
            "SZ",
            "TI",
            "UR",
            "VS",
            "ZG",
        }:
            self[date(year, DEC, 8)] = "Mariä Empfängnis"

        self[date(year, DEC, 25)] = "Weihnachten"

        if self.subdiv in {
            "AG",
            "AI",
            "AR",
            "BE",
            "BL",
            "BS",
            "FR",
            "GL",
            "GR",
            "LU",
            "NE",
            "NW",
            "OW",
            "SG",
            "SH",
            "SO",
            "SZ",
            "TG",
            "TI",
            "UR",
            "ZG",
            "ZH",
        }:
            self[date(year, DEC, 26)] = "Stephanstag"

        if self.subdiv == "GE":
            self[date(year, DEC, 31)] = "Wiederherstellung der Republik"


class CH(Switzerland):
    pass


class CHE(Switzerland):
    pass
