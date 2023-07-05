from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, JUL, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import IslamicHolidays, InternationalHolidays


class Algeria(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Algeria
    """

    country = "DZ"
    default_language = "ar"
    estimated_label = tr("(تقدير*) *%s")
    supported_languages = ("ar", "en_US")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day(tr("رأس السنة الميلادية"))

        # Amazigh New Year / Yennayer
        # In January 2018, Algeria declared Yennayer a national holiday
        if year >= 2018:
            self._add_holiday(tr("رأس السنة الأمازيغية"), JAN, 12)

        # Labour Day
        self._add_labor_day(tr("عيد العمال"))

        # Independence Day
        if year >= 1962:
            self._add_holiday(tr("عيد الإستقلال"), JUL, 5)

        # Revolution Day
        if year >= 1963:
            self._add_holiday(tr("عيد الثورة"), NOV, 1)

        # Islamic New Year
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        # Ashura
        self._add_ashura_day(tr("عاشورة"))

        # Mawlid / Prophet's Birthday
        self._add_mawlid_day(tr("عيد المولد النبوي"))

        # As of April 30, 2023. Algeria has 3 days of Eid holidays
        # (https://www.horizons.dz/english/archives/amp/12021)
        # Eid al-Fitr - Feast Festive
        self._add_eid_al_fitr_day(tr("عيد الفطر"))
        self._add_eid_al_fitr_day_two(tr("عطلة عيد الفطر"))
        if year >= 2024:
            self._add_eid_al_fitr_day_three(tr("عطلة عيد الفطر"))

        # Eid al-Adha - Scarfice Festive
        self._add_eid_al_adha_day(tr("عيد الأضحى"))
        self._add_eid_al_adha_day_two(tr("عطلة عيد الأضحى"))
        if year >= 2023:
            self._add_eid_al_adha_day_three(tr("عطلة عيد الأضحى"))


class DZ(Algeria):
    pass


class DZA(Algeria):
    pass
