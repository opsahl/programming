import stacker

class TestInterpreter:
    def __init__(self):
        self.inter = stacker.Interpreter()

    def test_add(self):
        self.inter.execute(["2", "3", "ADD"])
        assert self.inter.stack == ["5"]

    def test_subtract(self):
        self.inter.execute(["1", "2", "SUBTRACT"])
        assert self.inter.stack == ["-1"]

    def test_multiply(self):
        self.inter.execute(["10", "3", "MULTIPLY"])
        assert self.inter.stack == ["30"]

    def test_divide(self):
        self.inter.execute(["6", "2", "DIVIDE"])
        assert self.inter.stack == ["3"]

    def test_mod(self):
        self.inter.execute(["4", "3", "MOD", "15", "3", "MOD"])
        assert self.inter.stack == (["1", "0"])

    def test_lt(self):
        self.inter.execute(["3", "10", "<", "5", "4", "<"])
        assert self.inter.stack == ([True, False])

    def test_gt(self):
        self.inter.execute(["3", "10", ">", "5", "4", ">"])
        assert self.inter.stack == ([False, True])

    def test_equal(self):
        self.inter.execute(["1", "1", "=", "1", "2", "="])
        assert self.inter.stack == ([True, False])

    def test_if(self):
        self.inter.execute([True, "IF", "1", "2", "ADD", "ELSE",
            "6", "THEN", "2", "5", "MULTIPLY"])
        assert self.inter.stack == ["3", "10"]
