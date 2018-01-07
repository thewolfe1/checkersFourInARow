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
        
    def testCheckWinP1(self):
        print('testing the check_win for player 1 to see if returns false')
        self.assertEqual(game.check_win(1),False,'returns incorrect boolean')     
        
    def testCheckWinP2(self):
        print('testing the check_win for player 2 to see if returns false')
        self.assertEqual(game.check_win(2),False,'returns incorrect boolean') 
        
    def testCheckOnePlayerP1(self):
        print('testing the check_one_player for player 1 to see if returns false')
        self.assertEqual(game.check_one_player(1),False,'returns incorrect boolean')
        
    def testCheckOnePlayerP2(self):
        print('testing the check_one_player for player 2 to see if returns false')
        self.assertEqual(game.check_one_player(2),False,'returns incorrect boolean')
        
    def testCheckMove(self):
        print('testing the check_move function to see if return true movement cordinates')
        self.assertEqual(game.check_move((0,5)),((-1,0),(1,4)),'returns incorrect cordinated')  
        
    def testCheckMoveAI(self):
        print('testing the check_move_ai function to see if return true movement cordinates')
        self.assertEqual(game.check_move((1,0)),((-1,0),(-1,0)),'returns incorrect cordinated')
        
    def testCheckEat(self):
        print('testing the check_eat function to see if return true movement cordinates')
        self.assertEqual(game.check_eat((0,5)),((-1,0),(-1,0)),'returns incorrect cordinated')
        
    def testCheckEatAI(self):
        print('testing the check_eat_ai function to see if return true movement cordinates')
        self.assertEqual(game.check_eat_ai((0,1)),((-1,0),(-1,0)),'returns incorrect cordinated')
        
    def testWinner(self):
        print('testing the winner function to see if returns -1 beacuse theres no winner')
        self.assertEqual(game.winner(),-1,'returns incorrect number')
        
    def testUpdateKing(self):
        print('testing the update_king function to see if returns false no king on boared')
        self.assertEqual(game.update_king(),False,'returns incorrect bolean')
    