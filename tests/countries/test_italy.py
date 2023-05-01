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

from holidays import Italy, IT, ITA
from tests.common import TestCase


class TestItaly(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Italy)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_country_aliases(self):
        self.assertCountryAliases(Italy, IT, ITA)

    def test_2017(self):
        # https://www.giorni-festivi.it/
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 6), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 4, 25), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 6, 2), self.holidays)
        self.assertIn(date(2017, 8, 15), self.holidays)
        self.assertIn(date(2017, 11, 1), self.holidays)
        self.assertIn(date(2017, 12, 8), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_new_years(self):
        for year in range(1974, 2100):
            self.assertIn(date(year, 1, 1), self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 16), self.holidays)

    def test_easter_monday(self):
        self.assertIn(date(2017, 4, 17), self.holidays)

    def test_republic_day_before_1948(self):
        self.holidays = Italy(years=[1947])
        self.assertNotIn(date(1947, 6, 2), self.holidays)

    def test_republic_day_after_1948(self):
        self.holidays = Italy(years=[1948])
        self.assertIn(date(1948, 6, 2), self.holidays)

    def test_liberation_day_before_1946(self):
        self.holidays = Italy(years=1945)
        self.assertNotIn(date(1945, 4, 25), self.holidays)

    def test_liberation_day_after_1946(self):
        self.holidays = Italy(years=1946)
        self.assertIn(date(1946, 4, 25), self.holidays)

    def test_christmas(self):
        self.holidays = Italy(years=2017)
        self.assertIn(date(2017, 12, 25), self.holidays)

    def test_saint_stephan(self):
        self.holidays = Italy(years=2017)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_province_specific_days(self):
        prov_ag = Italy(subdiv="AG", years=2017)
        prov_al = Italy(subdiv="AL", years=2017)
        prov_an = Italy(subdiv="AN", years=2017)
        prov_ao = Italy(subdiv="AO", years=2017)
        prov_ap = Italy(subdiv="AP", years=2017)
        prov_aq = Italy(subdiv="AQ", years=2017)
        prov_ar = Italy(subdiv="AR", years=2017)
        prov_at = Italy(subdiv="AT", years=2017)
        prov_av = Italy(subdiv="AV", years=2017)
        prov_ba = Italy(subdiv="BA", years=2017)
        prov_bg = Italy(subdiv="BG", years=2017)
        prov_bi = Italy(subdiv="BI", years=2017)
        prov_bl = Italy(subdiv="BL", years=2017)
        prov_bn = Italy(subdiv="BN", years=2017)
        prov_bo = Italy(subdiv="BO", years=2017)
        prov_br = Italy(subdiv="BR", years=2017)
        prov_bs = Italy(subdiv="BS", years=2017)
        prov_bt = Italy(subdiv="BT", years=2017)
        prov_barletta = Italy(subdiv="Barletta", years=2017)
        prov_andria = Italy(subdiv="Andria", years=2017)
        prov_trani = Italy(subdiv="Trani", years=2017)
        prov_bz = Italy(subdiv="BZ", years=2017)
        prov_ca = Italy(subdiv="CA", years=2017)
        prov_cb = Italy(subdiv="CB", years=2017)
        prov_ce = Italy(subdiv="CE", years=2017)
        prov_ch = Italy(subdiv="CH", years=2017)
        prov_cl = Italy(subdiv="CL", years=2017)
        prov_cn = Italy(subdiv="CN", years=2017)
        prov_co = Italy(subdiv="CO", years=2017)
        prov_cr = Italy(subdiv="CR", years=2017)
        prov_cs = Italy(subdiv="CS", years=2017)
        prov_ct = Italy(subdiv="CT", years=2017)
        prov_cz = Italy(subdiv="CZ", years=2017)
        prov_en = Italy(subdiv="EN", years=2017)
        prov_fc = Italy(subdiv="FC", years=2017)
        prov_forli = Italy(subdiv="Forlì", years=2017)
        prov_cesena = Italy(subdiv="Cesena", years=2017)
        prov_fe = Italy(subdiv="FE", years=2017)
        prov_fg = Italy(subdiv="FG", years=2017)
        prov_fi = Italy(subdiv="FI", years=2017)
        prov_fm = Italy(subdiv="FM", years=2017)
        prov_fr = Italy(subdiv="FR", years=2017)
        prov_ge = Italy(subdiv="GE", years=2017)
        prov_go = Italy(subdiv="GO", years=2017)
        prov_gr = Italy(subdiv="GR", years=2017)
        prov_im = Italy(subdiv="IM", years=2017)
        prov_is = Italy(subdiv="IS", years=2017)
        prov_kr = Italy(subdiv="KR", years=2017)
        prov_lc = Italy(subdiv="LC", years=2017)
        prov_le = Italy(subdiv="LE", years=2017)
        prov_li = Italy(subdiv="LI", years=2017)
        prov_lo = Italy(subdiv="LO", years=2017)
        prov_lt = Italy(subdiv="LT", years=2017)
        prov_lu = Italy(subdiv="LU", years=2017)
        prov_mb = Italy(subdiv="MB", years=2017)
        prov_mc = Italy(subdiv="MC", years=2017)
        prov_me = Italy(subdiv="ME", years=2017)
        prov_mi = Italy(subdiv="MI", years=2017)
        prov_mn = Italy(subdiv="MN", years=2017)
        prov_mo = Italy(subdiv="MO", years=2017)
        prov_ms = Italy(subdiv="MS", years=2017)
        prov_mt = Italy(subdiv="MT", years=2017)
        prov_na = Italy(subdiv="NA", years=2017)
        prov_no = Italy(subdiv="NO", years=2017)
        prov_nu = Italy(subdiv="NU", years=2017)
        prov_or = Italy(subdiv="OR", years=2017)
        prov_pa = Italy(subdiv="PA", years=2017)
        prov_pc = Italy(subdiv="PC", years=2017)
        prov_pd = Italy(subdiv="PD", years=2017)
        prov_pe = Italy(subdiv="PE", years=2017)
        prov_pg = Italy(subdiv="PG", years=2017)
        prov_pi = Italy(subdiv="PI", years=2017)
        prov_pn = Italy(subdiv="PN", years=2017)
        prov_po = Italy(subdiv="PO", years=2017)
        prov_pr = Italy(subdiv="PR", years=2017)
        prov_pt = Italy(subdiv="PT", years=2017)
        prov_pu = Italy(subdiv="PU", years=2017)
        prov_pesaro = Italy(subdiv="Pesaro", years=2017)
        prov_urbino = Italy(subdiv="Urbino", years=2017)
        prov_pv = Italy(subdiv="PV", years=2017)
        prov_pz = Italy(subdiv="PZ", years=2017)
        prov_ra = Italy(subdiv="RA", years=2017)
        prov_rc = Italy(subdiv="RC", years=2017)
        prov_re = Italy(subdiv="RE", years=2017)
        prov_rg = Italy(subdiv="RG", years=2017)
        prov_ri = Italy(subdiv="RI", years=2017)
        prov_rm = Italy(subdiv="RM", years=2017)
        prov_rn = Italy(subdiv="RN", years=2017)
        prov_ro = Italy(subdiv="RO", years=2017)
        prov_sa = Italy(subdiv="SA", years=2017)
        prov_si = Italy(subdiv="SI", years=2017)
        prov_so = Italy(subdiv="SO", years=2017)
        prov_sp = Italy(subdiv="SP", years=2017)
        prov_sr = Italy(subdiv="SR", years=2017)
        prov_ss = Italy(subdiv="SS", years=2017)
        prov_su = Italy(subdiv="SU", years=2017)
        prov_sv = Italy(subdiv="SV", years=2017)
        prov_ta = Italy(subdiv="TA", years=2017)
        prov_te = Italy(subdiv="TE", years=2017)
        prov_tn = Italy(subdiv="TN", years=2017)
        prov_to = Italy(subdiv="TO", years=2017)
        prov_tp = Italy(subdiv="TP", years=2017)
        prov_tr = Italy(subdiv="TR", years=2017)
        prov_ts = Italy(subdiv="TS", years=2017)
        prov_tv = Italy(subdiv="TV", years=2017)
        prov_ud = Italy(subdiv="UD", years=2017)
        prov_va = Italy(subdiv="VA", years=2017)
        prov_vb = Italy(subdiv="VB", years=2017)
        prov_vc = Italy(subdiv="VC", years=2017)
        prov_ve = Italy(subdiv="VE", years=2017)
        prov_vi = Italy(subdiv="VI", years=2017)
        prov_vr = Italy(subdiv="VR", years=2017)
        prov_vt = Italy(subdiv="VT", years=2017)
        prov_vv = Italy(subdiv="VV", years=2017)

        self.assertIn("2017-02-25", prov_ag)
        self.assertIn("2017-11-10", prov_al)
        self.assertIn("2017-05-04", prov_an)
        self.assertIn("2017-09-07", prov_ao)
        self.assertIn("2017-08-05", prov_ap)
        self.assertIn("2017-06-10", prov_aq)
        self.assertIn("2017-08-07", prov_ar)
        self.assertIn("2017-05-02", prov_at)
        self.assertIn("2017-02-14", prov_av)
        self.assertIn("2017-12-06", prov_ba)
        self.assertIn("2017-08-26", prov_bg)
        self.assertIn("2017-12-26", prov_bi)
        self.assertIn("2017-12-26", prov_bl)
        self.assertIn("2017-08-24", prov_bn)
        self.assertIn("2017-10-04", prov_bo)
        self.assertIn("2017-09-03", prov_br)
        self.assertIn("2017-02-15", prov_bs)
        self.assertIn("2017-12-30", prov_bt)
        self.assertIn("2017-09-17", prov_bt)
        self.assertIn("2017-05-03", prov_bt)
        self.assertIn("2017-12-30", prov_barletta)
        self.assertIn("2017-09-17", prov_andria)
        self.assertIn("2017-05-03", prov_trani)
        self.assertIn("2017-08-15", prov_bz)
        self.assertIn("2017-06-05", prov_bz)
        self.assertIn("2017-10-30", prov_ca)
        self.assertIn("2017-04-23", prov_cb)
        self.assertIn("2017-01-20", prov_ce)
        self.assertIn("2017-05-11", prov_ch)
        self.assertIn("2017-09-29", prov_cl)
        self.assertIn("2017-09-29", prov_cn)
        self.assertIn("2017-08-31", prov_co)
        self.assertIn("2017-11-13", prov_cr)
        self.assertIn("2017-02-12", prov_cs)
        self.assertIn("2017-02-05", prov_ct)
        self.assertIn("2017-07-16", prov_cz)
        self.assertIn("2017-07-02", prov_en)
        self.assertIn("2017-06-24", prov_fc)
        self.assertIn("2017-02-04", prov_fc)
        self.assertIn("2017-02-04", prov_forli)
        self.assertIn("2017-06-24", prov_cesena)
        self.assertIn("2017-04-23", prov_fe)
        self.assertIn("2017-03-22", prov_fg)
        self.assertIn("2017-06-24", prov_fi)
        self.assertIn("2017-08-15", prov_fm)
        self.assertIn("2017-08-16", prov_fm)
        self.assertIn("2017-06-20", prov_fr)
        self.assertIn("2017-06-24", prov_ge)
        self.assertIn("2017-03-16", prov_go)
        self.assertIn("2017-08-10", prov_gr)
        self.assertIn("2017-11-26", prov_im)
        self.assertIn("2017-05-19", prov_is)
        self.assertIn("2017-10-09", prov_kr)
        self.assertIn("2017-12-06", prov_lc)
        self.assertIn("2017-08-26", prov_le)
        self.assertIn("2017-05-22", prov_li)
        self.assertIn("2017-01-19", prov_lo)
        self.assertIn("2017-04-25", prov_lt)
        self.assertIn("2017-07-12", prov_lu)
        self.assertIn("2017-06-24", prov_mb)
        self.assertIn("2017-08-31", prov_mc)
        self.assertIn("2017-06-03", prov_me)
        self.assertIn("2017-12-07", prov_mi)
        self.assertIn("2017-03-18", prov_mn)
        self.assertIn("2017-01-31", prov_mo)
        self.assertIn("2017-10-04", prov_ms)
        self.assertIn("2017-07-02", prov_mt)
        self.assertIn("2017-09-19", prov_na)
        self.assertIn("2017-01-22", prov_no)
        self.assertIn("2017-08-05", prov_nu)
        self.assertIn("2017-02-13", prov_or)
        self.assertIn("2017-07-15", prov_pa)
        self.assertIn("2017-07-04", prov_pc)
        self.assertIn("2017-06-13", prov_pd)
        self.assertIn("2017-10-10", prov_pe)
        self.assertIn("2017-01-29", prov_pg)
        self.assertIn("2017-06-17", prov_pi)
        self.assertIn("2017-04-25", prov_pn)
        self.assertIn("2017-09-08", prov_pn)
        self.assertIn("2017-12-26", prov_po)
        self.assertIn("2017-01-13", prov_pr)
        self.assertIn("2017-07-25", prov_pt)
        self.assertIn("2017-09-24", prov_pu)
        self.assertIn("2017-06-01", prov_pu)
        self.assertIn("2017-09-24", prov_pesaro)
        self.assertIn("2017-06-01", prov_urbino)
        self.assertIn("2017-12-09", prov_pv)
        self.assertIn("2017-05-30", prov_pz)
        self.assertIn("2017-07-23", prov_ra)
        self.assertIn("2017-04-23", prov_rc)
        self.assertIn("2017-11-24", prov_re)
        self.assertIn("2017-04-23", prov_rg)
        self.assertIn("2017-12-04", prov_ri)
        self.assertIn("2017-06-29", prov_rm)
        self.assertIn("2017-10-14", prov_rn)
        self.assertIn("2017-11-26", prov_ro)
        self.assertIn("2017-09-21", prov_sa)
        self.assertIn("2017-12-01", prov_si)
        self.assertIn("2017-06-19", prov_so)
        self.assertIn("2017-03-19", prov_sp)
        self.assertIn("2017-12-13", prov_sr)
        self.assertIn("2017-12-06", prov_ss)
        self.assertIn("2017-05-18", prov_su)
        self.assertIn("2017-03-18", prov_sv)
        self.assertIn("2017-05-10", prov_ta)
        self.assertIn("2017-12-19", prov_te)
        self.assertIn("2017-06-26", prov_tn)
        self.assertIn("2017-06-24", prov_to)
        self.assertIn("2017-08-07", prov_tp)
        self.assertIn("2017-02-14", prov_tr)
        self.assertIn("2017-11-03", prov_ts)
        self.assertIn("2017-04-27", prov_tv)
        self.assertIn("2017-07-12", prov_ud)
        self.assertIn("2017-05-08", prov_va)
        self.assertIn("2017-05-08", prov_vb)
        self.assertIn("2017-08-01", prov_vc)
        self.assertIn("2017-04-25", prov_ve)
        self.assertIn("2017-04-25", prov_vi)
        self.assertIn("2017-05-21", prov_vr)
        self.assertIn("2017-09-04", prov_vt)
        self.assertIn("2017-03-01", prov_vv)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions(
            "This subdivision is deprecated and will be removed "
            "after Dec, 1st 2023.",
        )
