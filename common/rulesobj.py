
#original author:Utsav Poddar(utsav.vicky@gmail.com)
import json
board = json.load(open("initial_state.json"))
opposite_army ={"white" : "black" , "black" : "white"}
class king:
	'Class for king'
	def legal_moves(self,board,color,king='king'):
		x,y = board[color][king]

		king_moves = []
		for i in xrange(3):
			for j in xrange(3):
				if 9> x+i-1 > 0 and 9>y+j-1 > 0:
					if x+i-1 != x or y+j-1 != y:
						king_moves = king_moves + [[x+i-1,y+j-1]]
		return [x for x in king_moves if x not in board[color].values()]
class pawn:
	'Class for pawn'
	def legal_moves(self, board, color, pawn):
       		x , y = board[color][pawn]
        	pawn_moves = []
		if color == "white" :
			if x==2:
				if 9 > y > 0:
					if [x+2,y] not in board[opposite_army[color]].values():
						pawn_moves = pawn_moves + [[x+2,y]]
			if x<8:
				if 9 > y > 0:
					if [x+1,y] not in board[opposite_army[color]].values():
						pawn_moves = pawn_moves+ [[x+1,y]]
				if y>1:
					if [x+1, y-1] in board[opposite_army[color]].values():
                                                pawn_moves = pawn_moves+ [[x+1,y-1]]
				if y<8:
					if [x+1, y+1] in board[opposite_army[color]].values():
                                                pawn_moves = pawn_moves+ [[x+1,y+1]]
			
		else:
                        if x==7:
                                if 9 > y > 0:
                                        if [x-2,y] not in board[opposite_army[color]].values():
                                                pawn_moves = pawn_moves + [[x-2,y]]

                        if x>1:
                                if 9 > y > 0:
                                        if [x-1,y] not in board[opposite_army[color]].values():
                                                pawn_moves = pawn_moves+ [[x-1,y]]
                                if y>1:
                                        if [x-1, y-1] in board[opposite_army[color]].values():
                                                pawn_moves = pawn_moves+ [[x-1,y-1]]
                                if y<8:
                                        if [x-1, y+1] in board[opposite_army[color]].values():
                                                pawn_moves = pawn_moves+ [[x-1,y+1]]


		return[x for x in pawn_moves if x not in board[color].values()]

class bishop:
	'Class for bishop'
	def legal_moves(self,board,color,bishop):
		x , y = board[color][bishop]
		bishop_moves = []
	        for i in xrange(8):
                	if x-i-1>0 and y+i+1<9:
                        	if [x-i-1,y+i+1] in board[color].values(): break
	                        bishop_moves = bishop_moves + [[x-i-1,y+i+1]]
        	                if [x-i-1,y+i+1] in board[opposite_army[color]].values(): break

	        for i in xrange(8):
        	        if x-i-1 > 0 and y-i-1 > 0:
                	        if [x-i-1,y-i-1] in board[color].values(): break
                	        bishop_moves = bishop_moves + [[x-i-1,y-i-1]]
                        	if [x-i-1,y-i-1] in board[opposite_army[color]].values(): break

	        for i in xrange(8):
	                if x+i+1 < 9 and y-i-1 > 0:
        	                if [x+i+1,y-i-1] in board[color].values(): break
                	        bishop_moves = bishop_moves + [[x+i+1,y-i-1]]
                	        if [x+i+1,y-i-1] in board[opposite_army[color]].values(): break

	        for i in xrange(8):
	                if x+i+1 < 9 and y+i+1 < 9:
        	                if [x+i+1,y+i+1] in board[color].values(): break
                	        bishop_moves = bishop_moves + [[x+i+1,y+i+1]]
                        	if [x+i+1,y+i+1] in board[opposite_army[color]].values(): break

	        return [x for x in bishop_moves if x not in board[color].values()]

class knight:
	'class for knight'
	def legal_moves(self,board, color, knight):

        	x , y = board[color][knight]

	        knight_moves = []

        	if x+2 < 9 and y+1 < 9:
                	knight_moves = knight_moves + [[x+2,y+1]]

	        if x+1 < 9 and y+2 < 9:
	                knight_moves = knight_moves + [[x+1,y+2]]

	        if x-1 > 0 and y+2 < 9:
        	        knight_moves = knight_moves + [[x-1,y+2]]

	        if x-1 > 0 and y-2 > 0:
        	        knight_moves = knight_moves + [[x-1,y-2]]

	        if x+2 < 9 and y-1 > 0:
	                knight_moves = knight_moves + [[x+2,y-1]]

	        if x+1 < 9 and y-2 > 0:
        	        knight_moves = knight_moves + [[x+1,y-2]]

	        if x-2 > 0 and y-1 > 0:
       	        	knight_moves = knight_moves + [[x-2,y-1]]

	        if x-2 > 0 and y+1 < 9:
        	        knight_moves = knight_moves + [[x-2,y+1]]

	        return [x for x in knight_moves if x not in board[color].values()]
class rook:
	'Class for rook'
	def legal_moves(self,board,color,rook):

        	x , y = board[color][rook]

	        rook_moves = []

	        for i in xrange(8):
	                if x+i+1 < 9:
	                        if [x+i+1,y] in board[color].values(): break
	                        rook_moves = rook_moves + [[x+i+1,y]]
	                        if [x+i+1,y] in board[opposite_army[color]].values(): break

	        for i in xrange(8):
        	        if x-i-1 > 0:
                	        if [x-i-1,y] in board[color].values(): break
                        	rook_moves = rook_moves + [[x-i-1,y]]
	                        if [x-i-1,y] in board[opposite_army[color]].values(): break

	        for i in xrange(8):
	                if y+i+1 < 9:
        	                if [x,y+i+1] in board[color].values(): break
                	        rook_moves = rook_moves + [[x,y+i+1]]
                        	if [x,y+i+1] in board[opposite_army[color]].values(): break

	        for i in xrange(8):
        	        if y-i-1 > 0:
                	        if [x,y-i-1] in board[color].values(): break
                        	rook_moves = rook_moves + [[x,y-i-1]]
                        	if [x,y-i-1] in board[opposite_army[color]].values(): break

	        return [x for x in rook_moves if x not in board[color].values()]

class queen:
	'class for queen'
	def legal_moves(self,board, color,queen="queen"):

	        x , y = board[color][queen]
		rook1=rook()
		bishop1=bishop()
        	queen_moves = rook1.legal_moves(board,color,queen) + bishop1.legal_moves(board,color,queen)

	        return [x for x in queen_moves if x not in board[color].values()]
class main:
	'tester class'
	p1=pawn()
	k=knight()
	print knight().legal_moves(board,"white","knight_1")
	print p1.legal_moves(board,"black","pawn_2")
	print p1.legal_moves(board,"white","pawn_1")
