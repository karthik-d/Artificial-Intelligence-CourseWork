# A random-restart version of the Hill-Climbing search algorithm
# No sideways moves are allowed. If plateau is reacheed, restart is applied

from StateFormulation import *

def search():
	while True:
		state = generate_random_state()
		while True:
			curr_attacks = count_attacks(state)
			if curr_attacks == 0:
				# Goal reached
				return state
			# Generate next best state
			move, next_attacks = get_next_best_move(state)
			if next_attacks >= curr_attacks:
				# At some local maxima or plateau
				# Restart search
				break
			# Move to the best successor state
			in_col, to_row = move
			state[in_col] = to_row 
		# Restart search with new random start
		state = generate_random_state()
	
print(display_state(search()))
