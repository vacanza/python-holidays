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

"""
References:
    - https://www.feriados.cl
    - `Excellent history of Chile holidays <http://www.feriadoschilenos.cl>`_
    - https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Chile
    - Law 2.977 (established official Chile holidays in its current form)
    - Law 20.983 (Day after New Year's Day, if it's a Sunday)
    - Law 19.668 (floating Monday holiday)
    - Law 19.668 (Corpus Christi)
    - Law 2.200, (Labour Day)
    - Law 18.018 (Labour Day renamed)
    - Law 16.840, Law 18.432 (Saint Peter and Saint Paul)
    - Law 20.148 (Day of Virgin of Carmen)
    - Law 18.026 (Day of National Liberation)
    - Law 19.588, Law 19.793 (Day of National Unity)
    - Law 20.983 (National Holiday Friday preceding Independence Day)
    - Law 20.215 (National Holiday Monday preceding Independence Day)
    - Law 20.215 (National Holiday Friday following Army Day)
    - Decree-law 636, Law 8.223
    - Law 3.810 (Columbus Day)
    - Law 20.299 (National Day of the Evangelical and Protestant Churches)
    - Law 20.663 (Región de Arica y Parinacota)
    - Law 20.678 (Región de Ñuble)
    - `Law 19.656 (Dec 31, 1999 holiday) <https://www.bcn.cl/leychile/navegar?idNorma=149328&idVersion=1999-12-15>`_
    - `Law 12.051 (bank holidays Jun 30 and Dec 31) <https://www.bcn.cl/leychile/navegar?idNorma=27013&idVersion=1956-07-12>`_
    - `Decree-law 1.171 (eliminate Jun 30) <https://www.bcn.cl/leychile/navegar?idNorma=6507&idVersion=1975-09-05>`_
    - `Law 19.528 (eliminate Dec 31) <https://www.bcn.cl/leychile/navegar?idNorma=76630&idVersion=1997-11-04>`_
    - `Law 19.559 (restore Dec 31) <https://www.bcn.cl/leychile/navegar?idNorma=97758&idVersion=1998-04-16>`_
"""

from gettext import gettext as tr
from typing import Tuple

from holidays.calendars.gregorian import JUN, SEP, DEC
from holidays.constants import BANK, PUBLIC
from holidays.entities.ISO_3166 import Iso3166Entity
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    MON_ONLY,
    MON_FRI_ONLY,
    TUE_TO_PREV_FRI,
    WED_TO_NEXT_FRI,
    FRI_ONLY,
    WORKDAY_TO_NEAREST_MON,
)


class ClHolidays(
    ObservedHolidayBase, Iso3166Entity, ChristianHolidays, InternationalHolidays, StaticHolidays
):
    """A class to represent holidays for Chile."""

    code = "CL"
    name = "Chile"
    default_language = "es"
    subdivisions = (
        "AI",
        "AN",
        "AP",
        "AR",
        "AT",
        "BI",
        "CO",
        "LI",
        "LL",
        "LR",
        "MA",
        "ML",
        "NB",
        "RM",
        "TA",
        "VS",
    )
    supported_categories = (BANK, PUBLIC)
    supported_languages = ("en_US", "es", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, ClStaticHolidays)
        kwargs.setdefault("observed_rule", WORKDAY_TO_NEAREST_MON)
        kwargs.setdefault("observed_since", 2000)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1914:
            return None

        # New Year's Day.
        self._add_new_years_day(tr("Año Nuevo"))
        if self._year >= 2017:
            self._add_observed(self._add_new_years_day_two(tr("Feriado nacional")), rule=MON_ONLY)

        # Good Friday.
        self._add_good_friday(tr("Viernes Santo"))

        # Holy Saturday.
        self._add_holy_saturday(tr("Sábado Santo"))

        if self._year <= 1967:
            # Ascension Day.
            self._add_ascension_thursday(tr("Ascensión del Señor"))

        if self._year <= 1967 or 1987 <= self._year <= 2006:
            # Corpus Christi.
            name = tr("Corpus Christi")
            if self._year <= 1999:
                self._add_corpus_christi_day(name)
            else:
                self._add_holiday_57_days_past_easter(name)

        if self._year >= 1932:
            # Labor Day.
            self._add_labor_day(tr("Día Nacional del Trabajo"))

        # Naval Glories Day.
        self._add_holiday_may_21(tr("Día de las Glorias Navales"))

        if self._year >= 2021:
            # National Day of Indigenous Peoples.
            name = tr("Día Nacional de los Pueblos Indígenas")
            if self._year == 2021:
                self._add_holiday_jun_21(name)
            else:
                self._add_holiday(name, self._summer_solstice_date)

        if self._year <= 1967 or self._year >= 1986:
            # Saint Peter and Saint Paul.
            self._move_holiday(self._add_saints_peter_and_paul_day(tr("San Pedro y San Pablo")))

        if self._year >= 2007:
            # Day of Virgin of Carmen.
            self._add_holiday_jul_16(tr("Virgen del Carmen"))

        # Assumption Day.
        self._add_assumption_of_mary_day(tr("Asunción de la Virgen"))

        if 1981 <= self._year <= 1998:
            # Day of National Liberation.
            self._add_holiday_sep_11(tr("Día de la Liberación Nacional"))
        elif 1999 <= self._year <= 2001:
            self._add_holiday_1st_mon_of_sep(
                # Day of National Unity.
                tr("Día de la Unidad Nacional")
            )

        if self._year >= 2007:
            self._add_observed(
                # National Holiday.
                self._add_holiday_sep_17(tr("Fiestas Patrias")),
                rule=MON_FRI_ONLY if self._year >= 2017 else MON_ONLY,
            )

        # Independence Day.
        self._add_holiday_sep_18(tr("Día de la Independencia"))

        # Army Day.
        self._add_holiday_sep_19(tr("Día de las Glorias del Ejército"))

        if self._year >= 2008:
            self._add_observed(self._add_holiday_sep_20(tr("Fiestas Patrias")), rule=FRI_ONLY)

        if 1932 <= self._year <= 1944:
            self._add_holiday_sep_20(tr("Fiestas Patrias"))

        if self._year >= 1922 and self._year != 1973:
            name = (
                # Meeting of Two Worlds' Day.
                tr("Día del Encuentro de dos Mundos")
                if self._year >= 2000
                # Columbus Day.
                else tr("Día de la Raza")
            )
            self._move_holiday(self._add_columbus_day(name))

        if self._year >= 2008:
            # This holiday is moved to the preceding Friday if it falls on a Tuesday,
            # or to the following Friday if it falls on a Wednesday.
            self._move_holiday(
                self._add_holiday_oct_31(
                    # National Day of the Evangelical and Protestant Churches.
                    tr("Día Nacional de las Iglesias Evangélicas y Protestantes")
                ),
                rule=TUE_TO_PREV_FRI + WED_TO_NEXT_FRI,
            )

        # All Saints' Day.
        self._add_all_saints_day(tr("Día de Todos los Santos"))

        # Immaculate Conception.
        self._add_immaculate_conception_day(tr("La Inmaculada Concepción"))

        if 1944 <= self._year <= 1988:
            # Christmas Eve.
            self._add_christmas_eve(tr("Víspera de Navidad"))

        # Christmas Day.
        self._add_christmas_day(tr("Navidad"))

    def _populate_subdiv_ap_public_holidays(self):
        if self._year >= 2013:
            # Assault and Capture of Cape Arica.
            self._add_holiday_jun_7(tr("Asalto y Toma del Morro de Arica"))

    def _populate_subdiv_nb_public_holidays(self):
        if self._year >= 2014:
            self._add_holiday_aug_20(
                # Nativity of Bernardo O'Higgins (Chillán and Chillán Viejo communes)
                tr("Nacimiento del Prócer de la Independencia (Chillán y Chillán Viejo)")
            )

    def _populate_bank_holidays(self):
        # Bank Holiday.
        name = tr("Feriado bancario")
        if 1957 <= self._year <= 1975:
            self._add_holiday_jun_30(name)

        if self._year >= 1956 and self._year != 1997:
            self._add_holiday_dec_31(name)

    @property
    def _summer_solstice_date(self) -> Tuple[int, int]:
        day = 20
        if (self._year % 4 > 1 and self._year <= 2046) or (
            self._year % 4 > 2 and self._year <= 2075
        ):
            day = 21
        return JUN, day


class ClStaticHolidays:
    # National Holiday.
    national_holiday = tr("Feriado nacional")

    special_public_holidays = {
        1999: (DEC, 31, national_holiday),
        2022: (SEP, 16, national_holiday),
    }
