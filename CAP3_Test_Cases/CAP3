# testing the code
import unittest
import pygame
from Game1 import start_game  # Replace 'your_puzzle_game_file' with the actual file name

class TestPuzzleGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.mode = 3  # You can set the mode for testing

    def test_start_game(self):
        # Set up the game and check if the cells are created correctly
        start_game(self.mode)
 
        # Add your assertions based on the expected behavior of start_game
        self.assertEqual(len(cells), self.mode ** 2)  # Assuming cells is a global variable

        for cell in cells:
            self.assertIn('rect', cell)
            self.assertIn('border', cell)
            self.assertIn('order', cell)
            self.assertIn('pos', cell)

            self.assertIsInstance(cell['rect'], pygame.Rect)
            self.assertEqual(cell['border'], WHITE)
            self.assertIsInstance(cell['order'], int)
            self.assertIsInstance(cell['pos'], int)

            # You may add more specific assertions based on your game's logic

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()