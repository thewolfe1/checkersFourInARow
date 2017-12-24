import unittest,game

class TestGame(unittest.TestCase):
    
    def testChange_caseOne(self):
        print('testing the change function by testing if 1 will return 2')
        self.assertEqual(game.change(1), 2,"change function falied returns the same value")
    
    def testChange_caseTwo(self):
        print('testing the change function by testing if 2 will return 1')
        self.assertEqual(game.change(2), 1,"change function falied returns the same value")
         
    def testGet_index_fail(self):
        print('testing the get_index function to see if the fail check works')
        self.assertEqual(game.get_index(50),-1,"change function falied returns an incorrect value")
        
    def testGet_index_work_vs1(self):
        print('testing the get_index function to see if the fail check works')
        self.assertEqual(game.get_index(2),2,"change function falied returns an incorrect value")   
    
    def testGet_index_work_vs2(self):
        print('testing the get_index function to see if the fail check works')
        self.assertEqual(game.get_index(23),2,"change function falied returns an incorrect value")

    def testPlayer_one_true(self):
        print('testing the player_one function to see if returns false value')
        self.assertEqual(game.player_one(3),True,'returns incorrect boolean')
    
    def testPlayer_two_true(self):
        print('testing the player_one function to see if returns false value')
        self.assertEqual(game.player_two(5),True,'returns incorrect boolean')      