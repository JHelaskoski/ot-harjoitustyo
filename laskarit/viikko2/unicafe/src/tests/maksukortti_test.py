import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(300)
        self.assertEqual(self.maksukortti.saldo_euroina(), 13.00)
        
    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.00)
    
    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        
    def test_true_rahat_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)
        
    def test_false_jos_rahaa_ei_riita(self):    
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)
        
    def test_saldon_tulostus_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")