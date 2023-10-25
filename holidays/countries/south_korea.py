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

import warnings
from datetime import date
from datetime import timedelta as td
from gettext import gettext as tr

from holidays.calendars import _CustomChineseHolidays
from holidays.calendars.gregorian import (
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
    SAT,
    SUN,
)
from holidays.constants import BANK, PUBLIC
from holidays.groups import (
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class SouthKorea(
    HolidayBase,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    StaticHolidays,
):
    """
    References:
    1. https://en.wikipedia.org/wiki/Public_holidays_in_South_Korea
    2. https://www.law.go.kr/법령/관공서의%20공휴일에%20관한%20규정
    3. https://elaw.klri.re.kr/eng_service/lawView.do?lang=ENG&hseq=34678
    4. https://elaw.klri.re.kr/eng_service/%20lawView.do?hseq=38405&lang=ENG
    5. https://namu.wiki/w/대통령%20선거일

    Checked With:
    1. https://publicholidays.co.kr/ko/2020-dates/

    According to (3), the alt holidays in Korea are as follows:
    - The alt holiday means next first non holiday after the holiday.
    - Independence Movement Day, Liberation Day, National Foundation Day,
      Hangul Day, Children's Day, Birthday of the Buddha, Christmas Day have
      alt holiday if they fell on Saturday or Sunday.
    - Korean New Year's Day, Korean Mid Autumn Day have alt holiday if they
      fell on Sunday.

    """

    country = "KR"
    supported_categories = {BANK, PUBLIC}

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self, cls=SouthKoreaLunisolarHolidays)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=SouthKoreaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _add_alt_holiday(
        self, dt: date, name: str = "", since: int = 2014, include_sat: bool = True
    ) -> None:
        """Add alternative holiday on first day from the date provided
        that's not already a another holiday nor a weekend.

        :param dt:
           The date of the holiday.

        :param name:
           The name of the holiday.

        :param since:
           Year starting from which alt holiday should be added

        :param include_sat:
           Whether Saturday is to be considered a weekend in addition to
           Sunday.
        """
        if not self.observed:
            return None

        target_weekday = {SUN}
        if include_sat:
            target_weekday.add(SAT)
        if (dt.weekday() in target_weekday or len(self.get_list(dt)) > 1) and dt.year >= since:
            obs_date = dt + td(days=+1)
            while obs_date.weekday() in target_weekday or obs_date in self:
                obs_date += td(days=+1)
            for name in (name,) if name else self.get_list(dt):
                if "Alternative holiday" not in name:
                    # Alternative holiday for %s.
                    self._add_holiday(tr("%s 대체 휴일") % name, obs_date)

    def _add_three_day_holiday(self, name: str, dt: date) -> None:
        for dt_alt in (
            # The day preceding %s.
            self._add_holiday(tr("%s 전날") % name, dt + td(days=-1)),
            dt,
            # The second day of %s.
            self._add_holiday(tr("%s 다음날") % name, dt + td(days=+1)),
        ):
            self._add_alt_holiday(dt_alt, name=name, include_sat=False)  # type: ignore[arg-type]

    def _populate_public_holidays(self):
        if self._year <= 1947:
            return None

        # Fixed Date Holidays.

        # New Year's Day.
        name = tr("신정")
        self._add_new_years_day(name)
        if self._year <= 1998:
            self._add_new_years_day_two(name)

        # Lunar New Year.
        name = tr("설날")
        self._add_three_day_holiday(name, self._add_chinese_new_years_day(name))

        # Independence Movement Day.
        mar_1 = self._add_holiday_mar_1(tr("3ㆍ1절"))
        self._add_alt_holiday(mar_1, since=2022)

        if 1949 <= self._year <= 2005 and self._year != 1960:
            # Tree Planting Day.
            self._add_holiday_apr_5(tr("식목일"))

        # Buddha's Birthday.
        self._add_alt_holiday(self._add_chinese_birthday_of_buddha(tr("부처님오신날")), since=2023)

        if self._year >= 1975:
            # Children's Day.
            self._add_alt_holiday(self._add_holiday_may_5(tr("어린이날")), since=2015)

        # Memorial Day.
        jun_6 = self._add_holiday_jun_6(tr("현충일"))

        if self._year <= 2007:
            # Constitution Day.
            self._add_holiday_jul_17(tr("제헌절"))

        # Liberation Day.
        self._add_alt_holiday(self._add_holiday_aug_15(tr("광복절")), since=2021)

        # National Foundation Day.
        self._add_alt_holiday(self._add_holiday_oct_3(tr("개천절")), since=2021)

        if self._year <= 1990 or self._year >= 2013:
            # Hangul Day.
            self._add_alt_holiday(self._add_holiday_oct_9(tr("한글날")), since=2021)

        # Chuseok.
        name = tr("추석")
        self._add_three_day_holiday(name, self._add_mid_autumn_festival(name))

        # Christmas Day.
        self._add_alt_holiday(self._add_christmas_day(tr("기독탄신일")), since=2023)

        # Election Days since Sep 2006; excluding the 2017 Special Presidential Election Day.

        # Based on Article 34 of the Public Official Election Act.
        # (1) The election day for each election to be held at the expiration of the term shall
        #     be as follows: <Amended by Act No. 5508, Feb. 6, 1998; Act No. 7189, Mar. 12, 2004>
        #       1. The presidential election shall be held on the first Wednesday from the 70th
        #          day before the expiration of the term of office;
        #       2. The election of National Assembly members shall be held on the first Wednesday
        #          from the 50th day before the expiration of the term of office;
        #       3. The election of local council members and the head of each local government
        #          shall be held on the first Wednesday from the 30th day before the expiration
        #          of the term of office.
        # (2) Where the election day as provided in paragraph (1) falls on a folk festival day or
        #     legal holiday closely related with the lives of the people or the day preceding or
        #     following the election day is a legal holiday, the election shall be held on the
        #     Wednesday of the following week. <Amended by Act No. 7189, Mar. 12, 2004>

        # National Assembly Election Day.
        name = tr("국회의원 선거일")

        if self._year == 2020:
            self._add_holiday_apr_15(name)
        elif self._year >= 2007 and (self._year - 2008) % 4 == 0:
            self._add_holiday_2nd_wed_of_apr(name)

        # Presidential Election Day.
        name = tr("대통령 선거일")

        if self._year >= 2007 and (self._year - 2007) % 5 == 0:
            if self._year <= 2012:
                self._add_holiday_3rd_wed_of_dec(name)
            elif self._year >= 2022:
                if (
                    self._is_tuesday(mar_1)
                    or self._is_wednesday(mar_1)
                    or self._is_thursday(mar_1)
                ):
                    # Moved as per Paragraph 2 of Article 34 due to conflict with
                    # Independence Movement Day (MAR, 1).
                    self._add_holiday_2nd_wed_of_mar(name)
                else:
                    self._add_holiday_1st_wed_of_mar(name)

        # Local Election Day.
        name = tr("지방선거일")

        if self._year >= 2007 and (self._year - 2010) % 4 == 0:
            if self._is_tuesday(jun_6) or self._is_wednesday(jun_6) or self._is_thursday(jun_6):
                # Moved as per Paragraph 2 of Article 34 due to conflict with
                # Memorial Day (JUN, 6).
                self._add_holiday_2nd_wed_of_jun(name)
            else:
                self._add_holiday_1st_wed_of_jun(name)

    def _populate_bank_holidays(self):
        if self._year <= 1947:
            return None

        # Workers' Day.
        name = tr("근로자의날")
        if self._year >= 1994:
            self._add_labor_day(name)
        else:
            self._add_holiday_mar_10(name)


class Korea(SouthKorea):
    def __init__(self, *args, **kwargs) -> None:
        warnings.warn("Korea is deprecated, use SouthKorea instead.", DeprecationWarning)

        super().__init__(*args, **kwargs)


class KR(SouthKorea):
    pass


class KOR(SouthKorea):
    pass


class SouthKoreaLunisolarHolidays(_CustomChineseHolidays):
    BUDDHA_BIRTHDAY_DATES = {
        1931: (MAY, 25),
        1968: (MAY, 5),
        2001: (MAY, 1),
        2012: (MAY, 28),
        2023: (MAY, 27),
        2025: (MAY, 5),
    }

    LUNAR_NEW_YEAR_DATES = {
        1916: (FEB, 4),
        1944: (JAN, 26),
        1954: (FEB, 4),
        1958: (FEB, 19),
        1966: (JAN, 22),
        1988: (FEB, 18),
        1997: (FEB, 8),
        2027: (FEB, 7),
        2028: (JAN, 27),
    }

    MID_AUTUMN_DATES = {
        1942: (SEP, 25),
        2040: (SEP, 21),
    }


class SouthKoreaStaticHolidays:
    """
    References:
      - https://namu.wiki/w/임시공휴일

    * Election Dates featured here are the ones prior to the proper recodification to
      Article 34 of the Public Official Election Act(September 2006)
    """

    # Common Special Holiday Types.

    # National Assembly Election Day.
    national_assembly_election_day = tr("국회의원 선거일")

    # Presidential Election Day.
    presidential_election_day = tr("대통령 선거일")

    # Local Election Day.
    local_election_day = tr("지방선거일")

    # Temporary Public Holiday.
    temporary_public_holiday = tr("임시공휴일")

    # Presidential Inauguration Day.
    presidential_inauguration_day = tr("대통령 취임식")

    # National Conference for Unification Election Day.
    national_conference_for_unification_election_day = tr("통일주체국민회의 선거일")

    # Yushin Constitution Referendum Day.
    yushin_constitution_referendum_day = tr("유신헌법 국민투표일")

    # May 16 Military Coup d'État Anniversary.
    may_16_coup_anniversary = tr("5.16 군사혁명 기념일")

    # April 19 Revolution Anniversary.
    apr_19_revolution_anniversary = tr("4.19 혁명 기념일")

    # President Syngman Rhee’s Birthday.
    syngman_rhee_birthday = tr("이승만 대통령 탄신일")

    special_public_holidays = {
        1948: (
            # 1st National Assembly Election.
            (MAY, 10, national_assembly_election_day),
            # 1st Presidential Election.
            (JUL, 20, presidential_election_day),
            # Republic of Korea's United Nations Recognation Celebrations.
            (DEC, 15, tr("국제연합의 대한민국 정부 승인 경축 국민대회")),
        ),
        1949: (
            # Anniversary of the 1st National Assembly Election.
            (MAY, 10, tr("5.10 제헌의회선거 1주년 기념일")),
            # Baekbeom Kim Ku's Funeral Ceremony.
            (JUL, 5, tr("백범 김구 선생 국민장 영결식")),
        ),
        1950: (
            # 2nd National Assembly Election.
            (MAY, 30, national_assembly_election_day),
            # Joint Memorial Service for Fallen Soldiers.
            (JUN, 21, tr("부통령 선거일")),
        ),
        1951: (
            # Vice Presidential Election.
            (MAY, 16, tr("부통령 선거일")),
        ),
        1952: (
            # City/Town/Township-level Local Elections.
            (APR, 25, local_election_day),
            # Provincial-level Local Elections.
            (MAY, 10, local_election_day),
            # 2nd Presidential Election/3rd Vice President Election.
            (AUG, 5, presidential_election_day),
        ),
        1954: (
            # 3rd National Assembly Election.
            (MAY, 20, national_assembly_election_day),
        ),
        1956: (
            # 3rd Presidential Election/4th Vice President Election.
            (MAY, 15, presidential_election_day),
            # City/Town/Township-level Local Elections.
            (AUG, 8, local_election_day),
            # Provincial-level Local Elections.
            (AUG, 13, local_election_day),
        ),
        # President Syngman Rhee’s Birthday.
        1957: (MAR, 26, syngman_rhee_birthday),
        1958: (
            # 4th National Assembly Election.
            (MAY, 2, national_assembly_election_day),
            # President Syngman Rhee’s Birthday.
            (MAR, 26, syngman_rhee_birthday),
        ),
        # President Syngman Rhee’s Birthday.
        1959: (MAR, 26, syngman_rhee_birthday),
        1960: (
            # President Syngman Rhee’s Birthday.
            (MAR, 26, syngman_rhee_birthday),
            # 4th Presidential Election/5th Vice President Election.
            (MAR, 15, presidential_election_day),
            # 5th National Assembly Election.
            (JUL, 29, national_assembly_election_day),
            # 4th Presidential Election.
            (AUG, 12, presidential_election_day),
            # New Government Celebration Day.
            (OCT, 1, tr("신정부 경축의 날")),
            # Special City/Provincial-level Councillors Local Elections.
            (DEC, 12, local_election_day),
            # City/Town/Township-level Councillors Local Elections.
            (DEC, 19, local_election_day),
            # Special City/Provincial-level Mayors Local Elections.
            (DEC, 26, local_election_day),
            # City/Town/Township-level Governors Local Elections.
            (DEC, 29, local_election_day),
        ),
        # April 19 Revolution Anniversary.
        1961: (APR, 19, apr_19_revolution_anniversary),
        1962: (
            # April 19 Revolution Anniversary.
            (APR, 19, apr_19_revolution_anniversary),
            # May 16 Military Coup d'État Anniversary.
            (MAY, 16, may_16_coup_anniversary),
        ),
        1963: (
            # April 19 Revolution Anniversary.
            (APR, 19, apr_19_revolution_anniversary),
            # May 16 Military Coup d'État Anniversary.
            (MAY, 16, may_16_coup_anniversary),
            # 5th Presidential Election.
            (OCT, 15, presidential_election_day),
            # 6th National Assembly Election.
            (NOV, 26, national_assembly_election_day),
            # President Park Chung Hee's Inauguration Day.
            (DEC, 17, presidential_inauguration_day),
        ),
        # Armed Forces Day.
        1966: (OCT, 1, tr("국군의 날")),
        1967: (
            # In-lieu observance for New Year's Day.
            (JAN, 4, temporary_public_holiday),
            # 6th Presidential Election.
            (MAY, 3, presidential_election_day),
            # 7th National Assembly Election.
            (JUN, 8, national_assembly_election_day),
            # President Park Chung Hee's Inauguration Day.
            (JUL, 1, presidential_inauguration_day),
        ),
        1969: (
            # Commemoration of the Apollo 11 Moon Landing.
            (JUL, 21, tr("아폴로 11호 달 착륙 기념")),
            # Third-term Constitutional Referendum Day.
            (OCT, 17, tr("삼선 헌법 개정 국민투표일")),
        ),
        1971: (
            # 7th Presidential Election.
            (APR, 27, presidential_election_day),
            # 8th National Assembly Election.
            (MAY, 25, national_assembly_election_day),
            # President Park Chung Hee's Inauguration Day.
            (JUL, 1, presidential_inauguration_day),
        ),
        1972: (
            # Yushin Constitution Referendum Day.
            (NOV, 21, yushin_constitution_referendum_day),
            # 1st National Conference for Unification Election Day.
            (DEC, 15, national_conference_for_unification_election_day),
            # 8th Presidential Election.
            (DEC, 23, presidential_election_day),
            # President Park Chung Hee's Inauguration Day.
            (DEC, 27, presidential_inauguration_day),
        ),
        # 9th National Assembly Election.
        1973: (FEB, 27, national_assembly_election_day),
        # First Lady Yuk Young-soo's Funeral Ceremony.
        1974: (AUG, 19, tr("대통령 영부인 육영수 여사 국민장 영결식")),
        # Yushin Constitution Referendum Day.
        1975: (FEB, 12, yushin_constitution_referendum_day),
        1978: (
            # 2nd National Conference for Unification Election Day.
            (MAY, 18, national_conference_for_unification_election_day),
            # 9th Presidential Election.
            (JUL, 6, presidential_election_day),
            # 10th National Assembly Election.
            (DEC, 12, national_assembly_election_day),
            # President Park Chung Hee's Inauguration Day.
            (DEC, 27, presidential_inauguration_day),
        ),
        1979: (
            # President Park Chung Hee's Funeral Ceremony.
            (NOV, 3, tr("박정희 대통령 국장 영결식")),
            # 10th Presidential Election.
            (DEC, 6, presidential_election_day),
            # President Choi Kyu-hah's Inauguration Day.
            (DEC, 21, presidential_inauguration_day),
        ),
        1980: (
            # 11th Presidential Election.
            (AUG, 27, presidential_election_day),
            # President Chun Doo-hwan's Inauguration Day.
            (SEP, 1, presidential_inauguration_day),
            # 5th Republic Constitutional Referendum Day.
            (OCT, 22, tr("제5공화국 헌법 개정 국민투표일")),
        ),
        1981: (
            # Electoral College Election Day.
            (FEB, 11, tr("선거를 위한 선거인단 선일")),
            # 12th Presidential Election.
            (FEB, 25, presidential_election_day),
            # President Chun Doo-hwan's Inauguration Day.
            (MAR, 3, presidential_inauguration_day),
            # 11th National Assembly Election.
            (MAR, 25, national_assembly_election_day),
        ),
        # Added due to overlaps between Chuseok and Armed Forces Day.
        1982: (OCT, 2, temporary_public_holiday),
        # 12th National Assembly Election.
        1985: (FEB, 12, national_assembly_election_day),
        1987: (
            # 13th Presidential Election.
            (DEC, 16, presidential_election_day),
            # 6th Republic Constitutional Referendum Day.
            (OCT, 27, tr("제6공화국 헌법 개정 국민투표일")),
        ),
        1988: (
            # President Roh Tae-woo's Inauguration Day.
            (FEB, 25, presidential_inauguration_day),
            # 13th National Assembly Election.
            (APR, 26, national_assembly_election_day),
            # 1988 Seoul Olympics Opening Ceremony.
            (SEP, 17, tr("1988 서울 올림픽 개막식")),
        ),
        1991: (
            # District/City/County-level Local Elections.
            (MAR, 26, local_election_day),
            # Metropolitan/Provincial-level Local Elections.
            (JUN, 20, local_election_day),
        ),
        1992: (
            # 14th National Assembly Election.
            (MAR, 24, national_assembly_election_day),
            # 14th Presidential Election.
            (DEC, 18, presidential_election_day),
        ),
        # 1st Nationwide Local Election.
        1995: (JUN, 27, local_election_day),
        # 15th National Assembly Election.
        1996: (APR, 11, national_assembly_election_day),
        # 15th Presidential Election.
        1997: (DEC, 18, presidential_election_day),
        # 2nd Nationwide Local Election.
        1998: (JUN, 4, local_election_day),
        # 16th National Assembly Election.
        2000: (APR, 13, national_assembly_election_day),
        2002: (
            # 3rd Nationwide Local Election.
            (JUN, 13, local_election_day),
            # 2002 FIFA World Cup National Team Semi-Finals Celebrations.
            (JUL, 1, tr("2002년 한일 월드컵 대표팀 4강 진출")),
            # 16th Presidential Election.
            (DEC, 19, presidential_election_day),
        ),
        # 17th National Assembly Election.
        2004: (APR, 15, national_assembly_election_day),
        # 4th Nationwide Local Election.
        2006: (MAY, 31, local_election_day),
        # Added to help cope with MERS Pandemic fatigue.
        2015: (AUG, 14, temporary_public_holiday),
        # Added to fill in holiday gaps between Children's Day and Saturday.
        2016: (MAY, 6, temporary_public_holiday),
        2017: (
            # Special Presidential Election due to Park Geun-hye's impeachment.
            (MAY, 9, presidential_election_day),
            # Added to create a 10-day long holiday period.
            (OCT, 2, temporary_public_holiday),
        ),
        # Added to help cope with Covid-19 Pandemic fatigue.
        2020: (AUG, 17, temporary_public_holiday),
        # Added to create a 6-day long holiday period.
        2023: (OCT, 2, temporary_public_holiday),
    }
