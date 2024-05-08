import unittest
from unittest.mock import patch
from rock_paper_scissors import get_user_selection, get_computer_selection, determine_winner, Action

class TestRockPaperScissors(unittest.TestCase):
    @patch('builtins.input', return_value='0')
    def test_get_user_selection_rock(self, mock_input):
        self.assertEqual(get_user_selection(), Action.Rock)

    @patch('builtins.input', return_value='1')
    def test_get_user_selection_paper(self, mock_input):
        self.assertEqual(get_user_selection(), Action.Paper)

    @patch('builtins.input', return_value='2')
    def test_get_user_selection_scissors(self, mock_input):
        self.assertEqual(get_user_selection(), Action.Scissors)

    @patch('random.randint', return_value=0)
    def test_get_computer_selection_rock(self, mock_randint):
        self.assertEqual(get_computer_selection(), Action.Rock)

    @patch('random.randint', return_value=1)
    def test_get_computer_selection_paper(self, mock_randint):
        self.assertEqual(get_computer_selection(), Action.Paper)

    @patch('random.randint', return_value=2)
    def test_get_computer_selection_scissors(self, mock_randint):
        self.assertEqual(get_computer_selection(), Action.Scissors)

    @patch('builtins.print')
    def test_determine_winner_tie(self, mock_print):
        determine_winner(Action.Rock, Action.Rock)
        mock_print.assert_called_once_with("Both players selected Rock. It's a tie!")

    @patch('builtins.print')
    def test_determine_winner_win(self, mock_print):
        determine_winner(Action.Rock, Action.Scissors)
        mock_print.assert_called_once_with("Rock beats Scissors! You win!")

    @patch('builtins.print')
    def test_determine_winner_lose(self, mock_print):
        determine_winner(Action.Rock, Action.Paper)
        mock_print.assert_called_once_with("Paper beats Rock! You lose.")

if __name__ == '__main__':
    unittest.main()