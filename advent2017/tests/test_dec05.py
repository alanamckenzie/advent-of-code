from advent2017.code import dec05


def test_instruction_jumps():
    assert dec05.InstructionJumps().get_num_exit_moves([0, 3, 0, 1, -3]) == 5


def test_instruction_jumps_modified():
    assert dec05.InstructionJumpsModified().get_num_exit_moves([0, 3, 0, 1, -3]) == 10
