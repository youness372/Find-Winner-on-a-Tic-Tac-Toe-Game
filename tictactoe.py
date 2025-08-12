class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        wining_cases =  [   
            {tuple([0, 0]), tuple([0, 1]), tuple([0, 2])},
            {tuple([1, 0]), tuple([1, 1]), tuple([1, 2])},
            {tuple([2, 0]), tuple([2, 1]), tuple([2, 2])},
            {tuple([0, 0]), tuple([1, 0]), tuple([2, 0])},
            {tuple([0, 1]), tuple([1, 1]), tuple([2, 1])},
            {tuple([0, 2]), tuple([1, 2]), tuple([2, 2])},
            {tuple([0, 0]), tuple([1, 1]), tuple([2, 2])},
            {tuple([0, 2]), tuple([1, 1]), tuple([2, 0])}
        ]   

        player1_moves =  set()   
        player2_moves =  set()   

        for i , move in  enumerate(moves) :   
            if i % 2 == 0  :  
                player1_moves.add(tuple(move))   
            else :   
                player2_moves.add(tuple(move))   
        
        for win in  wining_cases :   
            if win.issubset(player1_moves) :  
                return  "A"   
            if win.issubset(player2_moves) :   
                return "B"   
        if len(moves) == 9 :   
            return  "Draw"   
        else :   
            return  "Pending"
