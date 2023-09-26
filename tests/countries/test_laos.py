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

from holidays.constants import BANK, PUBLIC, SCHOOL, WORKDAY
from holidays.countries.laos import Laos, LA, LAO
from tests.common import TestCase


class TestLaos(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Laos, years=range(1976, 2058), years_non_observed=range(2018, 2058))

    def test_country_aliases(self):
        self.assertCountryAliases(Laos, LA, LAO)

    def test_no_holidays(self):
        self.assertNoHolidays(Laos(years=1975))

    def test_2022_public_holiday(self):
        self.assertHolidays(
            Laos(categories=(PUBLIC,), years=2022),
            ("2022-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2022-01-03", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2022-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2022-04-14", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2022-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2022-05-02", "ພັກຊົດເຊີຍວັນກຳມະກອນສາກົນ"),
            ("2022-12-02", "ວັນຊາດ"),
        )

    def test_2023_public_holiday(self):
        self.assertHolidays(
            Laos(categories=(PUBLIC,), years=2023),
            ("2023-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2023-01-02", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2023-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2023-04-14", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-17", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2023-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2023-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2023-12-02", "ວັນຊາດ"),
            ("2023-12-04", "ພັກຊົດເຊີຍວັນຊາດ"),
        )

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1976, 2058))

        self.assertNoNonObservedHoliday(
            "2022-01-03",
            "2023-01-02",
        )

    def test_international_women_rights_day(self):
        self.assertHoliday(f"{year}-03-08" for year in range(1976, 2058))

        self.assertNoNonObservedHoliday(
            "2020-03-09",
        )

    def test_laos_new_year_day(self):
        for year in range(1976, 2058):
            self.assertHoliday(f"{year}-04-14", f"{year}-04-15", f"{year}-04-16")

        self.assertNoNonObservedHoliday(
            "2018-04-17",
            "2018-04-18",
            "2019-04-17",
            "2022-04-18",
            "2023-04-17",
            "2023-04-18",
        )

    def test_labor_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1976, 2058))

        self.assertNoNonObservedHoliday(
            "2021-05-03",
            "2022-05-02",
        )

    def test_international_children_day_public(self):
        self.assertHoliday(f"{year}-06-01" for year in range(1990, 2018))

    def test_lao_national_day(self):
        self.assertHoliday(f"{year}-12-02" for year in range(1976, 2058))

        self.assertNoNonObservedHoliday(
            "2018-12-03",
            "2023-12-04",
        )

    def test_2022_bank_holiday(self):
        self.assertHolidays(
            Laos(categories=(BANK,), years=2022),
            ("2022-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2022-12-28", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2022-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2022-12-30", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_2023_bank_holiday(self):
        self.assertHolidays(
            Laos(categories=(BANK,), years=2023),
            ("2023-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2023-10-09", "ພັກຊົດເຊີຍວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2023-12-27", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2023-12-28", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2023-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_1993_school_holiday(self):
        # Prior to Adoption of National Teacher Day
        # All dates need to be checked again
        self.assertHolidays(
            Laos(categories=(SCHOOL,), years=1993),
            ("1993-02-16", "ວັນບຸນມາຂະບູຊາ"),
            ("1993-05-15", "ວັນບຸນວິສາຂະບູຊາ"),
            ("1993-07-13", "ວັນບຸນເຂົ້າພັນສາ"),
            ("1993-08-26", "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"),
            ("1993-09-10", "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"),
            ("1993-10-10", "ວັນບຸນອອກພັນສາ"),
            ("1993-10-11", "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"),
            ("1993-11-08", "ວັນບຸນທາດຫລວງ"),
        )

    def test_2022_school_holiday(self):
        self.assertHolidays(
            Laos(categories=(SCHOOL,), years=2022),
            ("2022-02-16", "ວັນບຸນມາຂະບູຊາ"),
            ("2022-05-15", "ວັນບຸນວິສາຂະບູຊາ"),
            ("2022-07-13", "ວັນບຸນເຂົ້າພັນສາ"),
            ("2022-08-26", "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"),
            ("2022-09-10", "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"),
            ("2022-10-07", "ວັນຄູແຫ່ງຊາດ"),
            ("2022-10-10", "ວັນບຸນອອກພັນສາ"),
            ("2022-10-11", "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"),
            ("2022-11-08", "ວັນບຸນທາດຫລວງ"),
        )

    def test_2023_school_holiday(self):
        self.assertHolidays(
            Laos(categories=(SCHOOL,), years=2023),
            ("2023-02-05", "ວັນບຸນມາຂະບູຊາ"),
            ("2023-05-04", "ວັນບຸນວິສາຂະບູຊາ"),
            ("2023-08-01", "ວັນບຸນເຂົ້າພັນສາ"),
            ("2023-09-14", "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"),
            ("2023-09-29", "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"),
            ("2023-10-07", "ວັນຄູແຫ່ງຊາດ"),
            ("2023-10-29", "ວັນບຸນອອກພັນສາ"),
            ("2023-10-30", "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"),
            ("2023-11-27", "ວັນບຸນທາດຫລວງ"),
        )

    def test_1990_workday(self):
        # Prior to Kaysone Phomvihane's Presidency and 1991 Constitution Adoption.
        self.assertHolidays(
            Laos(categories=(WORKDAY,), years=1990),
            ("1990-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("1990-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("1990-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("1990-04-14", "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("1990-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ"),
            (
                "1990-07-13",
                (
                    "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ; "
                    "ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ"
                ),
            ),
            ("1990-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("1990-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("1990-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("1990-10-12", "ວັນປະກາດເອກະລາດ"),
        )

    def test_2017_workday(self):
        # Prior to 2018 International Children's Day is in `PUBLIC` category
        self.assertHolidays(
            Laos(categories=(WORKDAY,), years=2017),
            ("2017-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("2017-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("2017-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("2017-04-14", "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("2017-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ"),
            (
                "2017-07-13",
                (
                    "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ; "
                    "ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ"
                ),
            ),
            ("2017-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("2017-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("2017-08-15", "ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"),
            ("2017-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("2017-10-12", "ວັນປະກາດເອກະລາດ"),
            ("2017-12-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"),
        )

    def test_2022_workday(self):
        self.assertHolidays(
            Laos(categories=(WORKDAY,), years=2022),
            ("2022-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("2022-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("2022-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("2022-04-14", "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("2022-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ; ວັນເດັກສາກົນ"),
            (
                "2022-07-13",
                (
                    "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ; "
                    "ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ"
                ),
            ),
            ("2022-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("2022-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("2022-08-15", "ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"),
            ("2022-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("2022-10-12", "ວັນປະກາດເອກະລາດ"),
            ("2022-12-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2022-01-03", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2022-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2022-04-14", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2022-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2022-05-02", "ພັກຊົດເຊີຍວັນກຳມະກອນສາກົນ"),
            ("2022-12-02", "ວັນຊາດ"),
        )

    def test_l10n_en_US(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (in lieu)"),
            ("2022-03-08", "International Women's Rights Day"),
            ("2022-04-14", "Lao New Year's Day"),
            ("2022-04-15", "Lao New Year's Day"),
            ("2022-04-16", "Lao New Year's Day"),
            ("2022-04-18", "Lao New Year's Day (in lieu)"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (in lieu)"),
            ("2022-12-02", "Lao National Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "วันปีใหม่สากล"),
            ("2022-01-03", "ชดเชยวันปีใหม่สากล"),
            ("2022-03-08", "วันสตรีสากล"),
            ("2022-04-14", "วันปีใหม่ลาว"),
            ("2022-04-15", "วันปีใหม่ลาว"),
            ("2022-04-16", "วันปีใหม่ลาว"),
            ("2022-04-18", "ชดเชยวันปีใหม่ลาว"),
            ("2022-05-01", "วันแรงงานสากล"),
            ("2022-05-02", "ชดเชยวันแรงงานสากล"),
            ("2022-12-02", "วันชาติ สปป. ลาว"),
        )
