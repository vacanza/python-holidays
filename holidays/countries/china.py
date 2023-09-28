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

from holidays.calendars.gregorian import JAN, MAY, SEP, OCT, DEC
from holidays.constants import HALF_DAY, PUBLIC
from holidays.groups import ChineseCalendarHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class China(HolidayBase, ChineseCalendarHolidays, InternationalHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_China
    - https://zh.wikipedia.org/wiki/中华人民共和国节日与公众假期
    - https://www.gov.cn/gongbao/content/2023/content_5736714.htm # 2023
    - https://www.gov.cn/gongbao/content/2021/content_5651728.htm # 2022
    - https://www.gov.cn/gongbao/content/2020/content_5567750.htm # 2021
    - https://www.gov.cn/gongbao/content/2019/content_5459138.htm # 2020
    - https://www.gov.cn/gongbao/content/2018/content_5350046.htm # 2019
    - https://www.gov.cn/gongbao/content/2017/content_5248221.htm # 2018
    - https://www.gov.cn/gongbao/content/2016/content_5148793.htm # 2017
    - https://www.gov.cn/gongbao/content/2016/content_2979719.htm # 2016
    - https://www.gov.cn/gongbao/content/2015/content_2799019.htm # 2015
    - https://www.gov.cn/gongbao/content/2014/content_2561299.htm # 2014
    - https://www.gov.cn/gongbao/content/2012/content_2292057.htm # 2013
    - https://www.gov.cn/gongbao/content/2011/content_2020918.htm # 2012
    - https://www.gov.cn/gongbao/content/2010/content_1765282.htm # 2011
    - https://www.gov.cn/gongbao/content/2009/content_1487011.htm # 2010
    - https://www.gov.cn/gongbao/content/2008/content_1175823.htm # 2009
    - https://www.gov.cn/gongbao/content/2008/content_859870.htm # 2008
    - https://www.gov.cn/gongbao/content/2007/content_503397.htm # 2007
    - https://zh.wikisource.org/wiki/国务院办公厅关于2006年部分节假日安排的通知 # 2006
    - https://zh.wikisource.org/wiki/国务院办公厅关于2005年部分节假日安排的通知 # 2005
    - https://zh.wikisource.org/wiki/国务院办公厅关于2004年部分节假日安排的通知 # 2004
    - https://zh.wikisource.org/wiki/国务院办公厅关于2003年部分节假日休息安排的通知 # 2003
    - https://zh.wikisource.org/wiki/国务院办公厅关于2002年部分节假日休息安排的通知 # 2002
    - https://zh.wikisource.org/wiki/国务院办公厅关于2001年春节、“五一”、“十一”放假安排的通知 # 2001

    Checked With:
    - https://www.officeholidays.com/countries/china/2023
    - https://www.china-briefing.com/news/china-public-holiday-2023-schedule/
    - https://www.timeanddate.com/calendar/?year=2023&country=41
    - https://m.wannianli.tianqi.com/fangjiaanpai/2001.html # 2001-2010

    Limitations:

    - Only checked with the official General Office of the State Council Notice from 2001 onwards.

    - Due to its complexity, need yearly checks 3-weeks before year's end each year.
    """

    country = "CN"
    supported_categories = {PUBLIC, HALF_DAY}
    default_language = "zh_CN"
    supported_languages = ("en_US", "th", "zh_CN", "zh_TW")

    # Special Cases.

    # New Year's Day.
    new_years_day_overflow = tr("元旦")

    # National Day.
    national_day_2008_gdw = tr("国庆节")

    # Mid-Autumn Festival.
    mid_autumn_fest_2010_special = tr("中秋节")

    special_public_holidays = {
        2007: (
            # 2007: Overflow from 2008 Notice.
            (DEC, 30, new_years_day_overflow),
            (DEC, 31, new_years_day_overflow),
        ),
        2008: (
            # 2008: weird National Day Golden Week pattern.
            (SEP, 29, national_day_2008_gdw),
            (SEP, 30, national_day_2008_gdw),
            (OCT, 4, national_day_2008_gdw),
            (OCT, 5, national_day_2008_gdw),
        ),
        2010: (
            # 2010: doesn't fit with existing observed pattern.
            (SEP, 23, mid_autumn_fest_2010_special),
            (SEP, 24, mid_autumn_fest_2010_special),
        ),
        2013: (
            # 2013: doesn't fit with existing observed pattern.
            (JAN, 2, new_years_day_overflow),
            (JAN, 3, new_years_day_overflow),
        ),
        2018: (
            # 2018: Overflow from 2019 Notice.
            (DEC, 30, new_years_day_overflow),
            (DEC, 31, new_years_day_overflow),
        ),
        2022: (
            # 2022: Overflow from 2023 Notice.
            (DEC, 31, new_years_day_overflow),
        ),
        2023: (
            # 2023: Overflow from 2023 Notice.
            (JAN, 2, new_years_day_overflow),
        ),
    }

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _one_off_observed_pattern(self, dt: date):
        # Based on 2002-2023 data, calculates observance for one-off
        # holidays (New Year's Day, Tomb-Sweeping Day, ...)
        # - Monday -> Tue-Wed (????-2007), [Sat]-[Sun] (2008-???)
        # - Tuesday -> Wed-Thu (????-2007), [Sun]-[Mon] (2008-????)
        # - Wednesday -> None (????-2007), [Mon]-[Tue] (2008-????)
        # - Thursday -> None (????-2007), Fri-Sat (2008-????)
        # - Friday -> Sat-Sun (????-????)
        # - Saturday -> [Fri]-Sun (2012-2019), Sun-Mon (????-2011, 2020-????)
        # - Sunday -> Mon-Tue (????-2007, 2012-2019), [Sat]-Mon (2008-2011, 2020-????)

        if self._is_monday(dt):
            if self._year <= 2007:
                # TUE-WED
                self._add_holiday(self[dt], dt + td(days=1))
                self._add_holiday(self[dt], dt + td(days=2))
            elif self._year >= 2008:
                # [SAT]-[SUN]
                self._add_holiday(self[dt], dt - td(days=2))
                self._add_holiday(self[dt], dt - td(days=1))
                if dt == date(self._year, MAY, 1) and self._year >= 2020:
                    # 2 Extra Days for May Day >= 2020:
                    self._add_holiday(self[dt], dt + td(days=1))
                    self._add_holiday(self[dt], dt + td(days=2))
        elif self._is_tuesday(dt):
            if self._year <= 2007:
                # WED-THU
                self._add_holiday(self[dt], dt + td(days=1))
                self._add_holiday(self[dt], dt + td(days=2))
            elif self._year >= 2008:
                # [SUN]-[MON]
                self._add_holiday(self[dt], dt - td(days=2))
                self._add_holiday(self[dt], dt - td(days=1))
                if dt == date(self._year, MAY, 1) and self._year >= 2020:
                    # 2 Extra Days for May Day >= 2020:
                    self._add_holiday(self[dt], dt + td(days=1))
                    self._add_holiday(self[dt], dt + td(days=2))
        elif self._is_wednesday(dt) and self._year >= 2008:
            # [MON]-[TUE]
            self._add_holiday(self[dt], dt - td(days=2))
            self._add_holiday(self[dt], dt - td(days=1))
            if dt == date(self._year, MAY, 1) and self._year >= 2020:
                # 2 Extra Days for May Day >= 2020:
                self._add_holiday(self[dt], dt + td(days=1))
                self._add_holiday(self[dt], dt + td(days=2))
        elif self._is_thursday(dt) and self._year >= 2008:
            # [FRI]-[SAT]
            self._add_holiday(self[dt], dt + td(days=1))
            self._add_holiday(self[dt], dt + td(days=2))
            if dt == date(self._year, MAY, 1) and self._year >= 2020:
                # 2 Extra Days for May Day >= 2020:
                self._add_holiday(self[dt], dt + td(days=3))
                self._add_holiday(self[dt], dt + td(days=4))
        elif self._is_friday(dt):
            # [SAT]-[SUN]
            self._add_holiday(self[dt], dt + td(days=1))
            self._add_holiday(self[dt], dt + td(days=2))
            if dt == date(self._year, MAY, 1) and self._year >= 2020:
                # 2 Extra Days for May Day >= 2020:
                self._add_holiday(self[dt], dt + td(days=3))
                self._add_holiday(self[dt], dt + td(days=4))
        elif self._is_saturday(dt):
            if self._year <= 2011 or self._year >= 2020:
                # SUN-MON
                self._add_holiday(self[dt], dt + td(days=1))
                self._add_holiday(self[dt], dt + td(days=2))
                if dt == date(self._year, MAY, 1) and self._year >= 2020:
                    # 2 Extra Days for May Day >= 2020:
                    self._add_holiday(self[dt], dt + td(days=3))
                    self._add_holiday(self[dt], dt + td(days=4))
            elif 2012 <= self._year <= 2019:
                # [FRI]-[SUN]
                self._add_holiday(self[dt], dt - td(days=1))
                self._add_holiday(self[dt], dt + td(days=1))
        elif self._is_sunday(dt):
            if self._year <= 2007 or 2012 <= self._year <= 2019:
                # MON-TUE
                self._add_holiday(self[dt], dt + td(days=1))
                self._add_holiday(self[dt], dt + td(days=2))
            elif 2008 <= self._year <= 2011 or self._year >= 2020:
                # [SAT]-MON
                self._add_holiday(self[dt], dt - td(days=1))
                self._add_holiday(self[dt], dt + td(days=1))
                if dt == date(self._year, MAY, 1) and self._year >= 2020:
                    # 2 Extra Days for May Day >= 2020:
                    self._add_holiday(self[dt], dt + td(days=2))
                    self._add_holiday(self[dt], dt + td(days=3))

    def _populate_public_holidays(self):
        # Proclamation of the People's Republic of China on Oct 1, 1949.
        if self._year <= 1949:
            return None

        # 元旦 (simp.) / 新年 (trad.)
        # Status: In-Use (Statutory).
        # Jan 1 in 1949, 1999, 2007, and 2013 revision.
        # Consecutive Holidays are available from 2002, except in 2014/2016/2017/2018.

        # New Year's Day.
        jan_1 = self._add_new_years_day(tr("元旦"))

        if (
            self.observed
            and (2002 <= self._year <= 2015 or self._year >= 2020)
            and self._year
            not in {
                2008,
                2013,
                2014,
                2023,
            }
        ):
            self._one_off_observed_pattern(jan_1)

        # 春节
        # Status: In-Use (Statutory).
        # Day 1-3 of Chinese New Year in 1949, 1999, 2007, and 2013 revision.

        # Spring Festival Golden Weekend
        # Checked with Official Notice from 2001-2023.
        # Consecutive Holidays are available from 2000 (1999 rev.).

        # Chinese New Year (Spring Festival).
        chinese_new_year = tr("春节")
        self._add_chinese_new_years_day(chinese_new_year)
        self._add_chinese_new_years_day_two(chinese_new_year)
        self._add_chinese_new_years_day_three(chinese_new_year)
        if self.observed and self._year >= 2000:
            # Non-Statutory.
            self._add_chinese_new_years_day_four(chinese_new_year)
            self._add_chinese_new_years_day_five(chinese_new_year)
            self._add_chinese_new_years_day_six(chinese_new_year)
            if 2008 <= self._year <= 2013 or self._year >= 2015:
                self._add_chinese_new_years_eve(chinese_new_year)
            else:
                self._add_chinese_new_years_day_seven(chinese_new_year)

        # 劳动节
        # Status: In-Use (Statutory).
        # May 1 in 1949, 1999, 2007, and 2013 revision.
        # Additional Holidays (May 2-3) are available from 2000 (1999 rev.) - 2007 (2007 rev.).

        # Labour Day Golden Weekend
        # Checked with Official Notice from 2001-2023.
        # Consecutive Holidays are available from 2002, with exception of ????-????.

        # Labour Day.
        labour_day = tr("劳动节")
        may_1 = self._add_labor_day(labour_day)
        if 2000 <= self._year <= 2007:
            self._add_labor_day_two(labour_day)
            self._add_labor_day_three(labour_day)
            if self.observed:
                # Non-Statutory.
                self._add_holiday_may_4(labour_day)
                self._add_holiday_may_5(labour_day)
                self._add_holiday_may_6(labour_day)
                self._add_holiday_may_7(labour_day)
        elif self.observed and (
            2008 <= self._year <= 2014 or self._year == 2018 or self._year >= 2020
        ):
            self._one_off_observed_pattern(may_1)

        # 国庆节
        # Status: In-Use (Statutory).
        # Oct 1-2 in 1949, 1999, 2007, and 2013 revision
        # Additional Holiday (Oct 3) is available from Sep 1999 (1999 rev.).

        # National Day Golden Weekend
        # Checked with Official Notice from 2001-2023.

        # National Day.
        national_day = tr("国庆节")
        self._add_holiday_oct_1(national_day)
        self._add_holiday_oct_2(national_day)
        if self._year >= 1999:
            self._add_holiday_oct_3(national_day)
        if self.observed and 2000 <= self._year != 2008:
            # Non-Statutory.
            self._add_holiday_oct_4(national_day)
            self._add_holiday_oct_5(national_day)
            self._add_holiday_oct_6(national_day)
            if self._year != 2023:
                self._add_holiday_oct_7(national_day)

        if self._year >= 2008:
            # 清明节
            # Status: In-Use (Statutory).
            # Tomb-Sweeping Day in 2007, and 2013 revision.
            # Consecutive Holidays are available from 2008, except in 2014/2015/2016/2019.

            # Tomb-Sweeping Day.
            qingming_fest = self._add_qingming_festival(tr("清明节"))

            if self.observed and self._year not in {2014, 2015, 2016, 2019, 2023}:
                # Non-Statutory.
                self._one_off_observed_pattern(qingming_fest)

            # 端午节
            # Status: In-Use (Statutory).
            # Dragon Boat Festival in 2007, and 2013 revision.
            # Consecutive Holidays are available from 2008, except in 2014/2015/2018/2019/2023.

            # Dragon Boat Festival.
            dragon_boat_fest = self._add_dragon_boat_festival(tr("端午节"))

            if self.observed and self._year not in {2014, 2015, 2018, 2019}:
                # Non-Statutory.
                self._one_off_observed_pattern(dragon_boat_fest)

            # 中秋节
            # Status: In-Use (Statutory).
            # Mid-Autumn Festival in 2007, and 2013 revision.
            # Consecutive Holidays are available from 2008, except in 2010/2014/2015/2018/2019.
            # Extra Day (Oct 8) is instead aded to the National Day Week if overlaps.

            # Mid-Autumn Festival.
            mid_autumn_fest = self._add_mid_autumn_festival(tr("中秋节"))

            if self.observed:
                # Non-Statutory.
                if (
                    mid_autumn_fest == date(self._year, OCT, 1)
                    or mid_autumn_fest == date(self._year, OCT, 2)
                    or mid_autumn_fest == date(self._year, OCT, 3)
                    or mid_autumn_fest == date(self._year, OCT, 4)
                    or mid_autumn_fest == date(self._year, OCT, 5)
                    or mid_autumn_fest == date(self._year, OCT, 6)
                    or mid_autumn_fest == date(self._year, OCT, 7)
                ):
                    self._add_holiday_oct_8(national_day)
                elif mid_autumn_fest == date(self._year, SEP, 30):
                    # No Additional Consecutive Holidays got added.
                    pass
                elif mid_autumn_fest == date(self._year, SEP, 29):
                    self._add_holiday_sep_30(self[mid_autumn_fest])
                elif self._year not in {2010, 2014, 2015, 2018, 2019}:
                    self._one_off_observed_pattern(mid_autumn_fest)

    def _populate_half_day_holidays(self):
        # No in-lieus are given for this category.
        # Proclamation of the People's Republic of China on Oct 1, 1949.
        if self._year <= 1949:
            return None

        # International Women's Day.
        self._add_womens_day(tr("国际妇女节"))

        # Youth Day.
        self._add_holiday_may_4(tr("五四青年节"))

        # Children's Day.
        self._add_childrens_day(tr("六一儿童节"))

        # Army Day.
        self._add_holiday_aug_1(tr("建军节"))


class CN(China):
    pass


class CHN(China):
    pass
