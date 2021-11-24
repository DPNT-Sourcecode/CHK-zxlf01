from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout():
    def test_checkout(self):
        assert checkout("FFF") == 20
        assert checkout("AAABC") == 180
        assert checkout("AAAAA") == 200
        assert checkout("DDEF") == 80
        assert checkout("EEB") == 80
        assert checkout("BBB") == 75
        assert checkout("") == 0
        assert checkout("BBGTI") == 120
        assert checkout("LLKKAAAED") == 515
        assert checkout("UUUU") == 120
        assert checkout("STXYZ") == 82
        assert checkout("STXY") == 62


