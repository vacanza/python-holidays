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

from datetime import timedelta as td
from gettext import gettext as tr

from dateutil.easter import easter

from holidays.constants import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.constants import NOV, DEC
from holidays.holiday_base import HolidayBase


class Portugal(HolidayBase):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays
    in Portugal.


    References:

    - Based on:
        https://en.wikipedia.org/wiki/Public_holidays_in_Portugal

    National Level:
    - [Labour Day]
        https://www.e-konomista.pt/dia-do-trabalhador/
    - [Portugal Day]
        Decreto 17.171
    - [Restoration of Independence Day]
        Gazeta de Lisboa, 8 de Dezembro de 1823 (n.º 290), pp. 1789 e 1790

    Regional Level:
    - [Azores]
        https://files.dre.pt/1s/1980/08/19200/23052305.pdf
    - [Madeira]
        https://files.dre.pt/1s/1979/11/25900/28782878.pdf
        https://files.dre.pt/1s/1989/02/02800/04360436.pdf
        https://files.dre.pt/1s/2002/11/258a00/71837183.pdf

    """

    country = "PT"
    default_language = "pt_PT"

    # https://en.wikipedia.org/wiki/ISO_3166-2:PT
    # `Ext` represents the national holidays most people have off
    subdivisions = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "20",
        "30",
        "Ext",
    ]

    def _populate(self, year):
        super()._populate(year)

        self._add_holiday(tr("Ano Novo"), JAN, 1)

        easter_date = easter(year)

        # carnival is no longer a holiday, but some companies let workers off.
        # @todo recollect the years in which it was a public holiday
        # self[e + td(days=-47)] = "Carnaval"

        self._add_holiday(tr("Sexta-feira Santa"), easter_date + td(days=-2))
        self._add_holiday(tr("Páscoa"), easter_date)

        # Revoked holidays in 2013–2015

        if year <= 2012 or year >= 2016:
            self._add_holiday(tr("Corpo de Deus"), easter_date + td(days=+60))
            if year >= 1910:
                self._add_holiday(tr("Implantação da República"), OCT, 5)
            self._add_holiday(tr("Dia de Todos os Santos"), NOV, 1)
            if year >= 1823:
                self._add_holiday(tr("Restauração da Independência"), DEC, 1)

        if year >= 1974:
            self._add_holiday(tr("Dia da Liberdade"), APR, 25)
            self._add_holiday(tr("Dia do Trabalhador"), MAY, 1)
        if year >= 1911:
            if 1933 <= year <= 1973:
                self._add_holiday(
                    tr("Dia de Camões, de Portugal e da Raça"), JUN, 10
                )
            elif year >= 1978:
                self._add_holiday(
                    tr(
                        "Dia de Portugal, de Camões e das Comunidades "
                        "Portuguesas"
                    ),
                    JUN,
                    10,
                )
            else:
                self._add_holiday(tr("Dia de Portugal"), JUN, 10)
        self._add_holiday(tr("Assunção de Nossa Senhora"), AUG, 15)
        self._add_holiday(tr("Imaculada Conceição"), DEC, 8)
        self._add_holiday(tr("Dia de Natal"), DEC, 25)

        if self.subdiv == "Ext":
            """
            Adds extended days that most people have as a bonus from their
            companies:

            - Carnival
            - the day before and after xmas
            - the day before the new year
            - Lisbon's city holiday
            """

            self._add_holiday(tr("Carnaval"), easter_date + td(days=-47))
            self._add_holiday(tr("Véspera de Natal"), DEC, 24)
            self._add_holiday(tr("26 de Dezembro"), DEC, 26)
            self._add_holiday(tr("Véspera de Ano Novo"), DEC, 31)
            self._add_holiday(tr("Dia de Santo António"), JUN, 13)

            # TODO add bridging days
            # - get Holidays that occur on Tuesday  and add Monday (-1 day)
            # - get Holidays that occur on Thursday and add Friday (+1 day)

        # District holidays: starts in 12 October 1910 via decree

        if year >= 1911:
            if self.subdiv == "01":
                self._add_holiday(tr("Dia de Santa Joana"), MAY, 12)
            if self.subdiv == "02":
                self._add_holiday(
                    tr("Quinta-feira da Ascensão"), easter_date + td(days=+39)
                )
            if self.subdiv in {"03", "13"}:
                self._add_holiday(tr("Dia de São João"), JUN, 24)
            if self.subdiv == "04":
                self._add_holiday(
                    tr("Dia de Nossa Senhora das Graças"), AUG, 22
                )
            if self.subdiv == "05":
                self._add_holiday(
                    tr("Dia de Nossa Senhora de Mércoles"),
                    easter_date + td(days=+16),
                )
            if self.subdiv == "06":
                self._add_holiday(tr("Dia de Santa Isabel"), JUL, 4)
            if self.subdiv == "07":
                self._add_holiday(tr("Dia de São Pedro"), JUN, 29)
            if self.subdiv == "08":
                self._add_holiday(tr("Dia do Município de Faro"), SEP, 7)
            if self.subdiv == "09":
                self._add_holiday(tr("Dia do Município da Guarda"), NOV, 27)
            if self.subdiv == "10":
                self._add_holiday(tr("Dia do Município de Leiria"), MAY, 22)
            if self.subdiv in {"11", "17"}:
                self._add_holiday(tr("Dia de Santo António"), JUN, 13)
            if self.subdiv == "12":
                self._add_holiday(
                    tr("Dia do Município de Portalegre"), MAY, 23
                )
            if self.subdiv == "14":
                self._add_holiday(tr("Dia de São José"), MAR, 19)
            if self.subdiv == "15":
                self._add_holiday(tr("Dia de Bocage"), SEP, 15)
            if self.subdiv == "16":
                self._add_holiday(
                    tr("Dia de Nossa Senhora da Agonia"), AUG, 20
                )
            if self.subdiv == "18":
                self._add_holiday(tr("Dia de São Mateus"), SEP, 21)
            if self.subdiv == "20" and year >= 1981:
                self._add_holiday(
                    tr("Dia da Região Autónoma dos Açores"),
                    easter_date + td(days=+50),
                )
            if self.subdiv == "30":
                if 1979 <= year <= 1988:
                    self._add_holiday(
                        tr("Dia da Região Autónoma da Madeira"), JUL, 1
                    )
                elif year >= 1989:
                    self._add_holiday(
                        tr(
                            "Dia da Região Autónoma da Madeira e "
                            "das Comunidades Madeirenses"
                        ),
                        JUL,
                        1,
                    )
                if year >= 2002:
                    self._add_holiday(tr("Primeira Oitava"), DEC, 26)


class PT(Portugal):
    pass


class PRT(Portugal):
    pass
