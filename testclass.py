import unittest


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info


class Shaxstest(unittest.TestCase):

    def test_shaxs(self):
        shaxs1 = Shaxs("Shoxrux", "Xasanov", "afeds2", 2009)
        self.assertIsNotNone(shaxs1.ism)
        self.assertIsNotNone(shaxs1.familiya)
        self.assertIsNotNone(shaxs1.passport)
        self.assertIsNotNone(shaxs1.tyil)


class Talabatest(unittest.TestCase):
    def tests_talaba(self):
        talaba1 = Talaba("Jonibek", "Uralov", "2df4f", 2000, 2202)
        self.assertIsNotNone(talaba1.ism)
        self.assertIsNotNone(talaba1.familiya)
        self.assertIsNotNone(talaba1.passport)
        self.assertIsNotNone(talaba1.tyil)
        self.assertIsNotNone(talaba1.idraqam)

unittest.main()