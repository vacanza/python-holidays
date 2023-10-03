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

from holidays.constants import HALF_DAY, PUBLIC
from holidays.countries.china import China, CN, CHN
from tests.common import TestCase


class TestChina(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(China, years=range(1950, 2051))

    def test_country_aliases(self):
        self.assertCountryAliases(China, CN, CHN)

    def test_no_holidays(self):
        self.assertNoHolidays(China(years=1949))
        self.assertNoHolidays(China(years=1949, categories=(HALF_DAY,)))

    def test_national_day(self):
        name = "国庆节"
        for year in range(1950, 1999):
            self.assertHolidayName(name, (f"{year}-10-01", f"{year}-10-02"))
        for year in range(1999, 2051):
            self.assertHolidayName(name, (f"{year}-10-01", f"{year}-10-02", f"{year}-10-03"))

        self.assertNoNonObservedHoliday(
            "2022-10-04",
            "2022-10-05",
            "2022-10-06",
            "2022-10-07",
            "2023-09-30",
            "2023-10-04",
            "2023-10-05",
            "2023-10-06",
        )

    def test_1950_public_holiday(self):
        self.assertHolidays(
            China(categories=(PUBLIC,), years=1950),
            ("1950-01-01", "元旦"),
            ("1950-02-17", "春节"),
            ("1950-02-18", "春节"),
            ("1950-02-19", "春节"),
            ("1950-05-01", "劳动节"),
            ("1950-10-01", "国庆节"),
            ("1950-10-02", "国庆节"),
        )

    def test_1999_public_holiday(self):
        self.assertHolidays(
            China(categories=(PUBLIC,), years=1999),
            ("1999-01-01", "元旦"),
            ("1999-02-16", "春节"),
            ("1999-02-17", "春节"),
            ("1999-02-18", "春节"),
            ("1999-05-01", "劳动节"),
            ("1999-10-01", "国庆节"),
            ("1999-10-02", "国庆节"),
            ("1999-10-03", "国庆节"),
        )

    def test_2001_public_holiday(self):
        # https://zh.wikisource.org/wiki/国务院办公厅关于2001年春节、“五一”、“十一”放假安排的通知
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2001),
            # New Year is not listed, but should be there according to 1999 revision.
            ("2001-01-01", "元旦"),
            ("2001-01-24", "春节"),
            ("2001-01-25", "春节"),
            ("2001-01-26", "春节"),
            ("2001-01-27", "春节"),
            ("2001-01-28", "春节"),
            ("2001-01-29", "春节"),
            ("2001-01-30", "春节"),
            ("2001-05-01", "劳动节"),
            ("2001-05-02", "劳动节"),
            ("2001-05-03", "劳动节"),
            ("2001-05-04", "劳动节"),
            ("2001-05-05", "劳动节"),
            ("2001-05-06", "劳动节"),
            ("2001-05-07", "劳动节"),
            ("2001-10-01", "国庆节"),
            ("2001-10-02", "国庆节"),
            ("2001-10-03", "国庆节"),
            ("2001-10-04", "国庆节"),
            ("2001-10-05", "国庆节"),
            ("2001-10-06", "国庆节"),
            ("2001-10-07", "国庆节"),
        )

    def test_2002_public_holiday(self):
        # https://zh.wikisource.org/wiki/国务院办公厅关于2002年部分节假日休息安排的通知
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2002),
            ("2002-01-01", "元旦"),
            ("2002-01-02", "元旦"),
            ("2002-01-03", "元旦"),
            ("2002-02-12", "春节"),
            ("2002-02-13", "春节"),
            ("2002-02-14", "春节"),
            ("2002-02-15", "春节"),
            ("2002-02-16", "春节"),
            ("2002-02-17", "春节"),
            ("2002-02-18", "春节"),
            ("2002-05-01", "劳动节"),
            ("2002-05-02", "劳动节"),
            ("2002-05-03", "劳动节"),
            ("2002-05-04", "劳动节"),
            ("2002-05-05", "劳动节"),
            ("2002-05-06", "劳动节"),
            ("2002-05-07", "劳动节"),
            ("2002-10-01", "国庆节"),
            ("2002-10-02", "国庆节"),
            ("2002-10-03", "国庆节"),
            ("2002-10-04", "国庆节"),
            ("2002-10-05", "国庆节"),
            ("2002-10-06", "国庆节"),
            ("2002-10-07", "国庆节"),
        )

    def test_2003_public_holiday(self):
        # https://zh.wikisource.org/wiki/国务院办公厅关于2003年部分节假日休息安排的通知
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2003),
            ("2003-01-01", "元旦"),
            ("2003-02-01", "春节"),
            ("2003-02-02", "春节"),
            ("2003-02-03", "春节"),
            ("2003-02-04", "春节"),
            ("2003-02-05", "春节"),
            ("2003-02-06", "春节"),
            ("2003-02-07", "春节"),
            ("2003-05-01", "劳动节"),
            ("2003-05-02", "劳动节"),
            ("2003-05-03", "劳动节"),
            ("2003-05-04", "劳动节"),
            ("2003-05-05", "劳动节"),
            ("2003-05-06", "劳动节"),
            ("2003-05-07", "劳动节"),
            ("2003-10-01", "国庆节"),
            ("2003-10-02", "国庆节"),
            ("2003-10-03", "国庆节"),
            ("2003-10-04", "国庆节"),
            ("2003-10-05", "国庆节"),
            ("2003-10-06", "国庆节"),
            ("2003-10-07", "国庆节"),
        )

    def test_2004_public_holiday(self):
        # https://zh.wikisource.org/wiki/国务院办公厅关于2004年部分节假日安排的通知
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2004),
            ("2004-01-01", "元旦"),
            ("2004-01-22", "春节"),
            ("2004-01-23", "春节"),
            ("2004-01-24", "春节"),
            ("2004-01-25", "春节"),
            ("2004-01-26", "春节"),
            ("2004-01-27", "春节"),
            ("2004-01-28", "春节"),
            ("2004-05-01", "劳动节"),
            ("2004-05-02", "劳动节"),
            ("2004-05-03", "劳动节"),
            ("2004-05-04", "劳动节"),
            ("2004-05-05", "劳动节"),
            ("2004-05-06", "劳动节"),
            ("2004-05-07", "劳动节"),
            ("2004-10-01", "国庆节"),
            ("2004-10-02", "国庆节"),
            ("2004-10-03", "国庆节"),
            ("2004-10-04", "国庆节"),
            ("2004-10-05", "国庆节"),
            ("2004-10-06", "国庆节"),
            ("2004-10-07", "国庆节"),
        )

    def test_2005_public_holiday(self):
        # https://zh.wikisource.org/wiki/国务院办公厅关于2005年部分节假日安排的通知
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2005),
            ("2005-01-01", "元旦"),
            ("2005-01-02", "元旦"),
            ("2005-01-03", "元旦"),
            ("2005-02-09", "春节"),
            ("2005-02-10", "春节"),
            ("2005-02-11", "春节"),
            ("2005-02-12", "春节"),
            ("2005-02-13", "春节"),
            ("2005-02-14", "春节"),
            ("2005-02-15", "春节"),
            ("2005-05-01", "劳动节"),
            ("2005-05-02", "劳动节"),
            ("2005-05-03", "劳动节"),
            ("2005-05-04", "劳动节"),
            ("2005-05-05", "劳动节"),
            ("2005-05-06", "劳动节"),
            ("2005-05-07", "劳动节"),
            ("2005-10-01", "国庆节"),
            ("2005-10-02", "国庆节"),
            ("2005-10-03", "国庆节"),
            ("2005-10-04", "国庆节"),
            ("2005-10-05", "国庆节"),
            ("2005-10-06", "国庆节"),
            ("2005-10-07", "国庆节"),
        )

    def test_2006_public_holiday(self):
        # https://zh.wikisource.org/wiki/国务院办公厅关于2006年部分节假日安排的通知
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2006),
            ("2006-01-01", "元旦"),
            ("2006-01-02", "元旦"),
            ("2006-01-03", "元旦"),
            ("2006-01-29", "春节"),
            ("2006-01-30", "春节"),
            ("2006-01-31", "春节"),
            ("2006-02-01", "春节"),
            ("2006-02-02", "春节"),
            ("2006-02-03", "春节"),
            ("2006-02-04", "春节"),
            ("2006-05-01", "劳动节"),
            ("2006-05-02", "劳动节"),
            ("2006-05-03", "劳动节"),
            ("2006-05-04", "劳动节"),
            ("2006-05-05", "劳动节"),
            ("2006-05-06", "劳动节"),
            ("2006-05-07", "劳动节"),
            ("2006-10-01", "国庆节"),
            ("2006-10-02", "国庆节"),
            ("2006-10-03", "国庆节"),
            ("2006-10-04", "国庆节"),
            ("2006-10-05", "国庆节"),
            ("2006-10-06", "国庆节"),
            ("2006-10-07", "国庆节"),
        )

    def test_2007_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2007/content_503397.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2007),
            ("2007-01-01", "元旦"),
            ("2007-01-02", "元旦"),
            ("2007-01-03", "元旦"),
            ("2007-02-18", "春节"),
            ("2007-02-19", "春节"),
            ("2007-02-20", "春节"),
            ("2007-02-21", "春节"),
            ("2007-02-22", "春节"),
            ("2007-02-23", "春节"),
            ("2007-02-24", "春节"),
            ("2007-05-01", "劳动节"),
            ("2007-05-02", "劳动节"),
            ("2007-05-03", "劳动节"),
            ("2007-05-04", "劳动节"),
            ("2007-05-05", "劳动节"),
            ("2007-05-06", "劳动节"),
            ("2007-05-07", "劳动节"),
            ("2007-10-01", "国庆节"),
            ("2007-10-02", "国庆节"),
            ("2007-10-03", "国庆节"),
            ("2007-10-04", "国庆节"),
            ("2007-10-05", "国庆节"),
            ("2007-10-06", "国庆节"),
            ("2007-10-07", "国庆节"),
            # From 2008 Notice.
            ("2007-12-30", "元旦"),
            ("2007-12-31", "元旦"),
        )

    def test_2008_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2008/content_859870.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2008),
            ("2008-01-01", "元旦"),
            ("2008-02-06", "春节"),
            ("2008-02-07", "春节"),
            ("2008-02-08", "春节"),
            ("2008-02-09", "春节"),
            ("2008-02-10", "春节"),
            ("2008-02-11", "春节"),
            ("2008-02-12", "春节"),
            ("2008-04-04", "清明节"),
            ("2008-04-05", "清明节"),
            ("2008-04-06", "清明节"),
            ("2008-05-01", "劳动节"),
            ("2008-05-02", "劳动节"),
            ("2008-05-03", "劳动节"),
            ("2008-06-07", "端午节"),
            ("2008-06-08", "端午节"),
            ("2008-06-09", "端午节"),
            ("2008-09-13", "中秋节"),
            ("2008-09-14", "中秋节"),
            ("2008-09-15", "中秋节"),
            ("2008-09-29", "国庆节"),
            ("2008-09-30", "国庆节"),
            ("2008-10-01", "国庆节"),
            ("2008-10-02", "国庆节"),
            ("2008-10-03", "国庆节"),
            ("2008-10-04", "国庆节"),
            ("2008-10-05", "国庆节"),
        )

    def test_2009_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2008/content_1175823.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2009),
            ("2009-01-01", "元旦"),
            ("2009-01-02", "元旦"),
            ("2009-01-03", "元旦"),
            ("2009-01-25", "春节"),
            ("2009-01-26", "春节"),
            ("2009-01-27", "春节"),
            ("2009-01-28", "春节"),
            ("2009-01-29", "春节"),
            ("2009-01-30", "春节"),
            ("2009-01-31", "春节"),
            ("2009-04-04", "清明节"),
            ("2009-04-05", "清明节"),
            ("2009-04-06", "清明节"),
            ("2009-05-01", "劳动节"),
            ("2009-05-02", "劳动节"),
            ("2009-05-03", "劳动节"),
            ("2009-05-28", "端午节"),
            ("2009-05-29", "端午节"),
            ("2009-05-30", "端午节"),
            ("2009-10-01", "国庆节"),
            ("2009-10-02", "国庆节"),
            ("2009-10-03", "中秋节; 国庆节"),
            ("2009-10-04", "国庆节"),
            ("2009-10-05", "国庆节"),
            ("2009-10-06", "国庆节"),
            ("2009-10-07", "国庆节"),
            ("2009-10-08", "国庆节"),
        )

    def test_2010_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2009/content_1487011.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2010),
            ("2010-01-01", "元旦"),
            ("2010-01-02", "元旦"),
            ("2010-01-03", "元旦"),
            ("2010-02-13", "春节"),
            ("2010-02-14", "春节"),
            ("2010-02-15", "春节"),
            ("2010-02-16", "春节"),
            ("2010-02-17", "春节"),
            ("2010-02-18", "春节"),
            ("2010-02-19", "春节"),
            ("2010-04-03", "清明节"),
            ("2010-04-04", "清明节"),
            ("2010-04-05", "清明节"),
            ("2010-05-01", "劳动节"),
            ("2010-05-02", "劳动节"),
            ("2010-05-03", "劳动节"),
            ("2010-06-14", "端午节"),
            ("2010-06-15", "端午节"),
            ("2010-06-16", "端午节"),
            ("2010-09-22", "中秋节"),
            ("2010-09-23", "中秋节"),
            ("2010-09-24", "中秋节"),
            ("2010-10-01", "国庆节"),
            ("2010-10-02", "国庆节"),
            ("2010-10-03", "国庆节"),
            ("2010-10-04", "国庆节"),
            ("2010-10-05", "国庆节"),
            ("2010-10-06", "国庆节"),
            ("2010-10-07", "国庆节"),
        )

    def test_2011_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2010/content_1765282.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2011),
            ("2011-01-01", "元旦"),
            ("2011-01-02", "元旦"),
            ("2011-01-03", "元旦"),
            ("2011-02-02", "春节"),
            ("2011-02-03", "春节"),
            ("2011-02-04", "春节"),
            ("2011-02-05", "春节"),
            ("2011-02-06", "春节"),
            ("2011-02-07", "春节"),
            ("2011-02-08", "春节"),
            ("2011-04-03", "清明节"),
            ("2011-04-04", "清明节"),
            ("2011-04-05", "清明节"),
            ("2011-04-30", "劳动节"),
            ("2011-05-01", "劳动节"),
            ("2011-05-02", "劳动节"),
            ("2011-06-04", "端午节"),
            ("2011-06-05", "端午节"),
            ("2011-06-06", "端午节"),
            ("2011-09-10", "中秋节"),
            ("2011-09-11", "中秋节"),
            ("2011-09-12", "中秋节"),
            ("2011-10-01", "国庆节"),
            ("2011-10-02", "国庆节"),
            ("2011-10-03", "国庆节"),
            ("2011-10-04", "国庆节"),
            ("2011-10-05", "国庆节"),
            ("2011-10-06", "国庆节"),
            ("2011-10-07", "国庆节"),
        )

    def test_2012_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2011/content_2020918.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2012),
            ("2012-01-01", "元旦"),
            ("2012-01-02", "元旦"),
            ("2012-01-03", "元旦"),
            ("2012-01-22", "春节"),
            ("2012-01-23", "春节"),
            ("2012-01-24", "春节"),
            ("2012-01-25", "春节"),
            ("2012-01-26", "春节"),
            ("2012-01-27", "春节"),
            ("2012-01-28", "春节"),
            ("2012-04-02", "清明节"),
            ("2012-04-03", "清明节"),
            ("2012-04-04", "清明节"),
            ("2012-04-29", "劳动节"),
            ("2012-04-30", "劳动节"),
            ("2012-05-01", "劳动节"),
            ("2012-06-22", "端午节"),
            ("2012-06-23", "端午节"),
            ("2012-06-24", "端午节"),
            ("2012-09-30", "中秋节"),
            ("2012-10-01", "国庆节"),
            ("2012-10-02", "国庆节"),
            ("2012-10-03", "国庆节"),
            ("2012-10-04", "国庆节"),
            ("2012-10-05", "国庆节"),
            ("2012-10-06", "国庆节"),
            ("2012-10-07", "国庆节"),
        )

    def test_2013_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2012/content_2292057.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2013),
            ("2013-01-01", "元旦"),
            ("2013-01-02", "元旦"),
            ("2013-01-03", "元旦"),
            ("2013-02-09", "春节"),
            ("2013-02-10", "春节"),
            ("2013-02-11", "春节"),
            ("2013-02-12", "春节"),
            ("2013-02-13", "春节"),
            ("2013-02-14", "春节"),
            ("2013-02-15", "春节"),
            ("2013-04-04", "清明节"),
            ("2013-04-05", "清明节"),
            ("2013-04-06", "清明节"),
            ("2013-04-29", "劳动节"),
            ("2013-04-30", "劳动节"),
            ("2013-05-01", "劳动节"),
            ("2013-06-10", "端午节"),
            ("2013-06-11", "端午节"),
            ("2013-06-12", "端午节"),
            ("2013-09-19", "中秋节"),
            ("2013-09-20", "中秋节"),
            ("2013-09-21", "中秋节"),
            ("2013-10-01", "国庆节"),
            ("2013-10-02", "国庆节"),
            ("2013-10-03", "国庆节"),
            ("2013-10-04", "国庆节"),
            ("2013-10-05", "国庆节"),
            ("2013-10-06", "国庆节"),
            ("2013-10-07", "国庆节"),
        )

    def test_2014_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2014/content_2561299.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2014),
            ("2014-01-01", "元旦"),
            ("2014-01-31", "春节"),
            ("2014-02-01", "春节"),
            ("2014-02-02", "春节"),
            ("2014-02-03", "春节"),
            ("2014-02-04", "春节"),
            ("2014-02-05", "春节"),
            ("2014-02-06", "春节"),
            ("2014-04-05", "清明节"),
            ("2014-05-01", "劳动节"),
            ("2014-05-02", "劳动节"),
            ("2014-05-03", "劳动节"),
            ("2014-06-02", "端午节"),
            ("2014-09-08", "中秋节"),
            ("2014-10-01", "国庆节"),
            ("2014-10-02", "国庆节"),
            ("2014-10-03", "国庆节"),
            ("2014-10-04", "国庆节"),
            ("2014-10-05", "国庆节"),
            ("2014-10-06", "国庆节"),
            ("2014-10-07", "国庆节"),
        )

    def test_2015_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2015/content_2799019.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2015),
            ("2015-01-01", "元旦"),
            ("2015-01-02", "元旦"),
            ("2015-01-03", "元旦"),
            ("2015-02-18", "春节"),
            ("2015-02-19", "春节"),
            ("2015-02-20", "春节"),
            ("2015-02-21", "春节"),
            ("2015-02-22", "春节"),
            ("2015-02-23", "春节"),
            ("2015-02-24", "春节"),
            ("2015-04-05", "清明节"),
            ("2015-05-01", "劳动节"),
            ("2015-06-20", "端午节"),
            ("2015-09-27", "中秋节"),
            ("2015-10-01", "国庆节"),
            ("2015-10-02", "国庆节"),
            ("2015-10-03", "国庆节"),
            ("2015-10-04", "国庆节"),
            ("2015-10-05", "国庆节"),
            ("2015-10-06", "国庆节"),
            ("2015-10-07", "国庆节"),
        )

    def test_2016_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2016/content_2979719.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2016),
            ("2016-01-01", "元旦"),
            ("2016-02-07", "春节"),
            ("2016-02-08", "春节"),
            ("2016-02-09", "春节"),
            ("2016-02-10", "春节"),
            ("2016-02-11", "春节"),
            ("2016-02-12", "春节"),
            ("2016-02-13", "春节"),
            ("2016-04-04", "清明节"),
            ("2016-05-01", "劳动节"),
            ("2016-06-09", "端午节"),
            ("2016-06-10", "端午节"),
            ("2016-06-11", "端午节"),
            ("2016-09-15", "中秋节"),
            ("2016-09-16", "中秋节"),
            ("2016-09-17", "中秋节"),
            ("2016-10-01", "国庆节"),
            ("2016-10-02", "国庆节"),
            ("2016-10-03", "国庆节"),
            ("2016-10-04", "国庆节"),
            ("2016-10-05", "国庆节"),
            ("2016-10-06", "国庆节"),
            ("2016-10-07", "国庆节"),
        )

    def test_2017_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2016/content_5148793.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2017),
            ("2017-01-01", "元旦"),
            ("2017-01-27", "春节"),
            ("2017-01-28", "春节"),
            ("2017-01-29", "春节"),
            ("2017-01-30", "春节"),
            ("2017-01-31", "春节"),
            ("2017-02-01", "春节"),
            ("2017-02-02", "春节"),
            ("2017-04-02", "清明节"),
            ("2017-04-03", "清明节"),
            ("2017-04-04", "清明节"),
            ("2017-05-01", "劳动节"),
            ("2017-05-28", "端午节"),
            ("2017-05-29", "端午节"),
            ("2017-05-30", "端午节"),
            ("2017-10-01", "国庆节"),
            ("2017-10-02", "国庆节"),
            ("2017-10-03", "国庆节"),
            ("2017-10-04", "中秋节; 国庆节"),
            ("2017-10-05", "国庆节"),
            ("2017-10-06", "国庆节"),
            ("2017-10-07", "国庆节"),
            ("2017-10-08", "国庆节"),
        )

    def test_2018_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2017/content_5248221.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2018),
            ("2018-01-01", "元旦"),
            ("2018-02-15", "春节"),
            ("2018-02-16", "春节"),
            ("2018-02-17", "春节"),
            ("2018-02-18", "春节"),
            ("2018-02-19", "春节"),
            ("2018-02-20", "春节"),
            ("2018-02-21", "春节"),
            ("2018-04-05", "清明节"),
            ("2018-04-06", "清明节"),
            ("2018-04-07", "清明节"),
            ("2018-04-29", "劳动节"),
            ("2018-04-30", "劳动节"),
            ("2018-05-01", "劳动节"),
            ("2018-06-18", "端午节"),
            ("2018-09-24", "中秋节"),
            ("2018-10-01", "国庆节"),
            ("2018-10-02", "国庆节"),
            ("2018-10-03", "国庆节"),
            ("2018-10-04", "国庆节"),
            ("2018-10-05", "国庆节"),
            ("2018-10-06", "国庆节"),
            ("2018-10-07", "国庆节"),
            # From 2019 Notice.
            ("2018-12-30", "元旦"),
            ("2018-12-31", "元旦"),
        )

    def test_2019_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2018/content_5350046.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2019),
            ("2019-01-01", "元旦"),
            ("2019-02-04", "春节"),
            ("2019-02-05", "春节"),
            ("2019-02-06", "春节"),
            ("2019-02-07", "春节"),
            ("2019-02-08", "春节"),
            ("2019-02-09", "春节"),
            ("2019-02-10", "春节"),
            ("2019-04-05", "清明节"),
            ("2019-05-01", "劳动节"),
            ("2019-06-07", "端午节"),
            ("2019-09-13", "中秋节"),
            ("2019-10-01", "国庆节"),
            ("2019-10-02", "国庆节"),
            ("2019-10-03", "国庆节"),
            ("2019-10-04", "国庆节"),
            ("2019-10-05", "国庆节"),
            ("2019-10-06", "国庆节"),
            ("2019-10-07", "国庆节"),
        )

    def test_2020_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2019/content_5459138.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2020),
            ("2020-01-01", "元旦"),
            ("2020-01-24", "春节"),
            ("2020-01-25", "春节"),
            ("2020-01-26", "春节"),
            ("2020-01-27", "春节"),
            ("2020-01-28", "春节"),
            ("2020-01-29", "春节"),
            ("2020-01-30", "春节"),
            ("2020-04-04", "清明节"),
            ("2020-04-05", "清明节"),
            ("2020-04-06", "清明节"),
            ("2020-05-01", "劳动节"),
            ("2020-05-02", "劳动节"),
            ("2020-05-03", "劳动节"),
            ("2020-05-04", "劳动节"),
            ("2020-05-05", "劳动节"),
            ("2020-06-25", "端午节"),
            ("2020-06-26", "端午节"),
            ("2020-06-27", "端午节"),
            ("2020-10-01", "中秋节; 国庆节"),
            ("2020-10-02", "国庆节"),
            ("2020-10-03", "国庆节"),
            ("2020-10-04", "国庆节"),
            ("2020-10-05", "国庆节"),
            ("2020-10-06", "国庆节"),
            ("2020-10-07", "国庆节"),
            ("2020-10-08", "国庆节"),
        )

    def test_2021_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2020/content_5567750.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2021),
            ("2021-01-01", "元旦"),
            ("2021-01-02", "元旦"),
            ("2021-01-03", "元旦"),
            ("2021-02-11", "春节"),
            ("2021-02-12", "春节"),
            ("2021-02-13", "春节"),
            ("2021-02-14", "春节"),
            ("2021-02-15", "春节"),
            ("2021-02-16", "春节"),
            ("2021-02-17", "春节"),
            ("2021-04-03", "清明节"),
            ("2021-04-04", "清明节"),
            ("2021-04-05", "清明节"),
            ("2021-05-01", "劳动节"),
            ("2021-05-02", "劳动节"),
            ("2021-05-03", "劳动节"),
            ("2021-05-04", "劳动节"),
            ("2021-05-05", "劳动节"),
            ("2021-06-12", "端午节"),
            ("2021-06-13", "端午节"),
            ("2021-06-14", "端午节"),
            ("2021-09-19", "中秋节"),
            ("2021-09-20", "中秋节"),
            ("2021-09-21", "中秋节"),
            ("2021-10-01", "国庆节"),
            ("2021-10-02", "国庆节"),
            ("2021-10-03", "国庆节"),
            ("2021-10-04", "国庆节"),
            ("2021-10-05", "国庆节"),
            ("2021-10-06", "国庆节"),
            ("2021-10-07", "国庆节"),
        )

    def test_2022_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2021/content_5651728.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2022),
            ("2022-01-01", "元旦"),
            ("2022-01-02", "元旦"),
            ("2022-01-03", "元旦"),
            ("2022-01-31", "春节"),
            ("2022-02-01", "春节"),
            ("2022-02-02", "春节"),
            ("2022-02-03", "春节"),
            ("2022-02-04", "春节"),
            ("2022-02-05", "春节"),
            ("2022-02-06", "春节"),
            ("2022-04-03", "清明节"),
            ("2022-04-04", "清明节"),
            ("2022-04-05", "清明节"),
            ("2022-04-30", "劳动节"),
            ("2022-05-01", "劳动节"),
            ("2022-05-02", "劳动节"),
            ("2022-05-03", "劳动节"),
            ("2022-05-04", "劳动节"),
            ("2022-06-03", "端午节"),
            ("2022-06-04", "端午节"),
            ("2022-06-05", "端午节"),
            ("2022-09-10", "中秋节"),
            ("2022-09-11", "中秋节"),
            ("2022-09-12", "中秋节"),
            ("2022-10-01", "国庆节"),
            ("2022-10-02", "国庆节"),
            ("2022-10-03", "国庆节"),
            ("2022-10-04", "国庆节"),
            ("2022-10-05", "国庆节"),
            ("2022-10-06", "国庆节"),
            ("2022-10-07", "国庆节"),
            # From 2023 Notice.
            ("2022-12-31", "元旦"),
        )

    def test_2023_public_holiday(self):
        # https://www.gov.cn/gongbao/content/2023/content_5736714.htm
        self.assertHolidays(
            China(categories=(PUBLIC,), years=2023),
            ("2023-01-01", "元旦"),
            ("2023-01-02", "元旦"),
            ("2023-01-21", "春节"),
            ("2023-01-22", "春节"),
            ("2023-01-23", "春节"),
            ("2023-01-24", "春节"),
            ("2023-01-25", "春节"),
            ("2023-01-26", "春节"),
            ("2023-01-27", "春节"),
            ("2023-04-05", "清明节"),
            ("2023-04-29", "劳动节"),
            ("2023-04-30", "劳动节"),
            ("2023-05-01", "劳动节"),
            ("2023-05-02", "劳动节"),
            ("2023-05-03", "劳动节"),
            ("2023-06-22", "端午节"),
            ("2023-06-23", "端午节"),
            ("2023-06-24", "端午节"),
            ("2023-09-29", "中秋节"),
            ("2023-09-30", "中秋节"),
            ("2023-10-01", "国庆节"),
            ("2023-10-02", "国庆节"),
            ("2023-10-03", "国庆节"),
            ("2023-10-04", "国庆节"),
            ("2023-10-05", "国庆节"),
            ("2023-10-06", "国庆节"),
        )

    def test_2022_half_day_holiday(self):
        self.assertHolidays(
            China(categories=(HALF_DAY,), years=2022),
            ("2022-03-08", "国际妇女节"),
            ("2022-05-04", "五四青年节"),
            ("2022-06-01", "六一儿童节"),
            ("2022-08-01", "建军节"),
        )

    def test_2023_half_day_holiday(self):
        self.assertHolidays(
            China(categories=(HALF_DAY,), years=2023),
            ("2023-03-08", "国际妇女节"),
            ("2023-05-04", "五四青年节"),
            ("2023-06-01", "六一儿童节"),
            ("2023-08-01", "建军节"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "元旦"),
            ("2022-01-02", "元旦"),
            ("2022-01-03", "元旦"),
            ("2022-01-31", "春节"),
            ("2022-02-01", "春节"),
            ("2022-02-02", "春节"),
            ("2022-02-03", "春节"),
            ("2022-02-04", "春节"),
            ("2022-02-05", "春节"),
            ("2022-02-06", "春节"),
            ("2022-03-08", "国际妇女节"),
            ("2022-04-03", "清明节"),
            ("2022-04-04", "清明节"),
            ("2022-04-05", "清明节"),
            ("2022-04-30", "劳动节"),
            ("2022-05-01", "劳动节"),
            ("2022-05-02", "劳动节"),
            ("2022-05-03", "劳动节"),
            ("2022-05-04", "五四青年节; 劳动节"),
            ("2022-06-01", "六一儿童节"),
            ("2022-06-03", "端午节"),
            ("2022-06-04", "端午节"),
            ("2022-06-05", "端午节"),
            ("2022-08-01", "建军节"),
            ("2022-09-10", "中秋节"),
            ("2022-09-11", "中秋节"),
            ("2022-09-12", "中秋节"),
            ("2022-10-01", "国庆节"),
            ("2022-10-02", "国庆节"),
            ("2022-10-03", "国庆节"),
            ("2022-10-04", "国庆节"),
            ("2022-10-05", "国庆节"),
            ("2022-10-06", "国庆节"),
            ("2022-10-07", "国庆节"),
            ("2022-12-31", "元旦"),
        )

    def test_l10n_en_US(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-03", "New Year's Day"),
            ("2022-01-31", "Chinese New Year (Spring Festival)"),
            ("2022-02-01", "Chinese New Year (Spring Festival)"),
            ("2022-02-02", "Chinese New Year (Spring Festival)"),
            ("2022-02-03", "Chinese New Year (Spring Festival)"),
            ("2022-02-04", "Chinese New Year (Spring Festival)"),
            ("2022-02-05", "Chinese New Year (Spring Festival)"),
            ("2022-02-06", "Chinese New Year (Spring Festival)"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-03", "Tomb-Sweeping Day"),
            ("2022-04-04", "Tomb-Sweeping Day"),
            ("2022-04-05", "Tomb-Sweeping Day"),
            ("2022-04-30", "Labour Day"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day"),
            ("2022-05-03", "Labour Day"),
            ("2022-05-04", "Labour Day; Youth Day"),
            ("2022-06-01", "Children's Day"),
            ("2022-06-03", "Dragon Boat Festival"),
            ("2022-06-04", "Dragon Boat Festival"),
            ("2022-06-05", "Dragon Boat Festival"),
            ("2022-08-01", "Army Day"),
            ("2022-09-10", "Mid-Autumn Festival"),
            ("2022-09-11", "Mid-Autumn Festival"),
            ("2022-09-12", "Mid-Autumn Festival"),
            ("2022-10-01", "National Day"),
            ("2022-10-02", "National Day"),
            ("2022-10-03", "National Day"),
            ("2022-10-04", "National Day"),
            ("2022-10-05", "National Day"),
            ("2022-10-06", "National Day"),
            ("2022-10-07", "National Day"),
            ("2022-12-31", "New Year's Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันปีใหม่สากล"),
            ("2022-01-02", "วันปีใหม่สากล"),
            ("2022-01-03", "วันปีใหม่สากล"),
            ("2022-01-31", "วันตรุษจีน"),
            ("2022-02-01", "วันตรุษจีน"),
            ("2022-02-02", "วันตรุษจีน"),
            ("2022-02-03", "วันตรุษจีน"),
            ("2022-02-04", "วันตรุษจีน"),
            ("2022-02-05", "วันตรุษจีน"),
            ("2022-02-06", "วันตรุษจีน"),
            ("2022-03-08", "วันสตรีสากล"),
            ("2022-04-03", "วันเช็งเม้ง"),
            ("2022-04-04", "วันเช็งเม้ง"),
            ("2022-04-05", "วันเช็งเม้ง"),
            ("2022-04-30", "วันแรงงาน"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-02", "วันแรงงาน"),
            ("2022-05-03", "วันแรงงาน"),
            ("2022-05-04", "วันเยาวชนห่งชาติจีน; วันแรงงาน"),
            ("2022-06-01", "วันเด็กสากล"),
            ("2022-06-03", "วันไหว้บ๊ะจ่าง"),
            ("2022-06-04", "วันไหว้บ๊ะจ่าง"),
            ("2022-06-05", "วันไหว้บ๊ะจ่าง"),
            ("2022-08-01", "วันสถาปนากองทัพปลดปล่อยประชาชนจีน"),
            ("2022-09-10", "วันไหว้พระจันทร์"),
            ("2022-09-11", "วันไหว้พระจันทร์"),
            ("2022-09-12", "วันไหว้พระจันทร์"),
            ("2022-10-01", "วันชาติจีน"),
            ("2022-10-02", "วันชาติจีน"),
            ("2022-10-03", "วันชาติจีน"),
            ("2022-10-04", "วันชาติจีน"),
            ("2022-10-05", "วันชาติจีน"),
            ("2022-10-06", "วันชาติจีน"),
            ("2022-10-07", "วันชาติจีน"),
            ("2022-12-31", "วันปีใหม่สากล"),
        )

    def test_l10n_zh_TW(self):
        self.assertLocalizedHolidays(
            "zh_TW",
            ("2022-01-01", "元旦"),
            ("2022-01-02", "元旦"),
            ("2022-01-03", "元旦"),
            ("2022-01-31", "春節"),
            ("2022-02-01", "春節"),
            ("2022-02-02", "春節"),
            ("2022-02-03", "春節"),
            ("2022-02-04", "春節"),
            ("2022-02-05", "春節"),
            ("2022-02-06", "春節"),
            ("2022-03-08", "國際婦女節"),
            ("2022-04-03", "清明節"),
            ("2022-04-04", "清明節"),
            ("2022-04-05", "清明節"),
            ("2022-04-30", "勞動節"),
            ("2022-05-01", "勞動節"),
            ("2022-05-02", "勞動節"),
            ("2022-05-03", "勞動節"),
            ("2022-05-04", "五四青年節; 勞動節"),
            ("2022-06-01", "六一兒童節"),
            ("2022-06-03", "端午節"),
            ("2022-06-04", "端午節"),
            ("2022-06-05", "端午節"),
            ("2022-08-01", "建軍節"),
            ("2022-09-10", "中秋節"),
            ("2022-09-11", "中秋節"),
            ("2022-09-12", "中秋節"),
            ("2022-10-01", "國慶日"),
            ("2022-10-02", "國慶日"),
            ("2022-10-03", "國慶日"),
            ("2022-10-04", "國慶日"),
            ("2022-10-05", "國慶日"),
            ("2022-10-06", "國慶日"),
            ("2022-10-07", "國慶日"),
            ("2022-12-31", "元旦"),
        )
