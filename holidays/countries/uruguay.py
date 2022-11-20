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
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import TH, FR

from holidays.constants import JAN, APR, MAY, JUN, JUL, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Uruguay(HolidayBase):
    # https://www.ute.com.uy/clientes/tramites-y-servicios/potencia-contratada

    country = "UY"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if not self.observed and self._is_weekend(year, JAN, 1):
            pass
        else:
            self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"

        # Carnival days
        # revisar este día para futuros casos
        name = "Día de Carnaval [Carnival's Day]"
        self[easter(year) - rd(days=48)] = name
        self[easter(year) - rd(days=47)] = name

        # Día de Reyes - Feriado en el cual se conmemora la llegada de
        # los reyes magos a Jesus
        if not self.observed and self._is_weekend(year, JAN, 6):
            pass
        else:
            self[date(year, JAN, 6)] = "Día de Reyes"

        # Holy Week
        name_thu = "Semana Santa (Jueves Santo)  [Holy day (Holy Thursday)]"
        name_fri = "Semana Santa (Viernes Santo)  [Holy day (Holy Friday)]"
        name_easter = "Día de Pascuas [Easter Day]"

        self[easter(year) + rd(weekday=TH(-1))] = name_thu
        self[easter(year) + rd(weekday=FR(-1))] = name_fri

        if not self.observed and self._is_weekend(easter(year)):
            pass
        else:
            self[easter(year)] = name_easter

        # Desembarco de los 33 Orientales en la playa de la Agraciada
        if not self.observed and self._is_weekend(year, APR, 19):
            pass
        else:
            self[date(year, APR, 19)] = (
                "Desembarco de los 33 Orientales "
                "Landing of the 33 Orientals"
                " Aterrissagem dos 33 Orientais"
                " Sbarco dei 33 orientali"
            )

        # Día de los Trabajadores
        name = "Día del Trabajo [Labour Day]"
        if not self.observed and self._is_weekend(year, MAY, 1):
            pass
        else:
            self[date(year, MAY, 1)] = name

        # Batalla de las piedras
        name = "Batalla de las Piedras [Battle of the stones]"
        if not self.observed and self._is_weekend(year, MAY, 17):
            pass
        else:
            self[date(year, MAY, 17)] = name

        # Natalicio de José Gervacio Artigas
        name = "Natalicio de José Gervacio Artigas "
        if not self.observed and self._is_weekend(year, JUN, 19):
            pass
        else:
            self[date(year, JUN, 19)] = name

        # Jura de la Constitución
        name = "Jura de la constitución "
        if not self.observed and self._is_weekend(year, JUL, 18):
            pass
        else:
            self[date(year, JUL, 18)] = name

        # Declaratoria de la Independencia
        name = "Día de la Independencia [Independence Day]"
        if not self.observed and self._is_weekend(year, AUG, 25):
            pass
        else:
            self[date(year, AUG, 25)] = name

        # Respect for Cultural Diversity Day or Columbus day
        if not self.observed and self._is_weekend(year, OCT, 11):
            pass
        elif year < 2010:
            self[date(year, OCT, 11)] = "Día de la Raza [Columbus day]"
        else:
            self[date(year, OCT, 11)] = (
                "Día del Respeto a la Diversidad"
                " Cultural [Respect for"
                " Cultural Diversity Day]"
            )
        # Día de los difuntos
        name = "Día de los difuntos"
        if not self.observed and self._is_weekend(year, NOV, 2):
            pass
        else:
            self[date(year, NOV, 2)] = name

        # Christmas
        self[date(year, DEC, 25)] = "Navidad [Christmas]"


class UY(Uruguay):
    pass


class URY(Uruguay):
    pass
