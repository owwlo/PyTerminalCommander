import unittest

from PyTerminalCommander import super_move

class Tests(unittest.TestCase):
    def test_basic(self):
        back_no_del_cases = [
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 1),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 7),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 8),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 11),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 16),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 17),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 18),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 19),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 20),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 19),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 33),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 28),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 37),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 36),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 100),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 45),
            ],
        ]
        for case in back_no_del_cases:
            print("case back_forward=1,del_char=0:")
            print("case: {}".format(case[0]))
            print("exp:  {}".format(case[1]))
            print("out:  {}".format(super_move(case[0][0], case[0][1], True, False)))
            assert case[1] == super_move(case[0][0], case[0][1], True, False)

        back_del_cases = [
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 1),
                ("efhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 7),
                ("_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 8),
                ("fwoijwfo___wifowef  wef -_- qeojefioj", 0),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 11),
                ("wefhwof_ijwfo___wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 16),
                ("wefhwof____wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 17),
                ("wefhwof___wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 18),
                ("wefhwof__wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 19),
                ("wefhwof_wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 20),
                ("wefhwof_fwoijwfo___ifowef  wef -_- qeojefioj", 19),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 33),
                ("wefhwof_fwoijwfo___wifowef  _- qeojefioj", 28),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 37),
                ("wefhwof_fwoijwfo___wifowef  wef -_- eojefioj", 36),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 100),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 45),
            ],

        ]
        for case in back_del_cases:
            print("case back_forward=1,del_char=1:")
            print("case: {}".format(case[0]))
            print("exp:  {}".format(case[1]))
            print("out:  {}".format(super_move(case[0][0], case[0][1], True, True)))
            assert case[1] == super_move(case[0][0], case[0][1], True, True)

        forward_no_del_cases = [
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 7),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 1),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 7),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 7),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 16),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 8),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 16),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 11),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 16),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 16),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 26),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 17),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 26),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 18),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 26),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 19),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 26),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 20),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 26),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 30),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 31),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 33),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 45),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 37),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 45),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 100),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 45),
            ],
        ]
        for case in forward_no_del_cases:
            print("case back_forward=0,del_char=0:")
            print("case: {}".format(case[0]))
            print("exp:  {}".format(case[1]))
            print("out:  {}".format(super_move(case[0][0], case[0][1], False, False)))
            assert case[1] == super_move(case[0][0], case[0][1], False, False)

        forward_del_cases = [
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
                ("_fwoijwfo___wifowef  wef -_- qeojefioj", 0),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 1),
                ("w_fwoijwfo___wifowef  wef -_- qeojefioj", 1),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 7),
                ("wefhwof___wifowef  wef -_- qeojefioj", 7),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 8),
                ("wefhwof____wifowef  wef -_- qeojefioj", 8),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 11),
                ("wefhwof_fwo___wifowef  wef -_- qeojefioj", 11),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 16),
                ("wefhwof_fwoijwfo  wef -_- qeojefioj", 16),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 17),
                ("wefhwof_fwoijwfo_  wef -_- qeojefioj", 17),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 18),
                ("wefhwof_fwoijwfo__  wef -_- qeojefioj", 18),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 19),
                ("wefhwof_fwoijwfo___  wef -_- qeojefioj", 19),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 20),
                ("wefhwof_fwoijwfo___w  wef -_- qeojefioj", 20),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 30),
                ("wefhwof_fwoijwfo___wifowef  we -_- qeojefioj", 30),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 33),
                ("wefhwof_fwoijwfo___wifowef  wef -", 33),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 37),
                ("wefhwof_fwoijwfo___wifowef  wef -_- q", 37),
            ],
            [
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 100),
                ("wefhwof_fwoijwfo___wifowef  wef -_- qeojefioj", 45),
            ],

        ]
        for case in forward_del_cases:
            print("case back_forward=0,del_char=1:")
            print("case: {}".format(case[0]))
            print("exp:  {}".format(case[1]))
            print("out:  {}".format(super_move(case[0][0], case[0][1], False, True)))
            assert case[1] == super_move(case[0][0], case[0][1], False, True)
