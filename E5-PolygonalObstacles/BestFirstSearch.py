from PriorityQueue import PriorityQueue 
from copy import deepcopy

from StateFormulation import *
from search_utils import *


def heuristic(state, goal_state):
	# SLD heuristic is used
	return state.distance_to(goal_state)


def evaluate_priority(state, context):
	# 'context' contains data reqd to evaluate priority of state
	# Here, it is the goal_state
	(goal_state,) = context
	return heuristic(state, goal_state)


def search(state_space):

	# Priority Queue of fringe states and their respective paths as payloads
	state_queue = PriorityQueue(evaluate_priority)
	state_queue.enqueue(
		elems=[state_space.start], 
		contexts=[(state_space.end,)],
		payloads=[Path([state_space.start])]
	)
	
	while(not state_queue.is_empty()):
		# PRE-VISIT
		state, path_to_state = state_queue.dequeue()
		if state_space.is_visited(state):
			continue
		# VISIT		
		# Move to state and do goal test
		state_space.move_to_state(state)
		if state_space.at_goal_state():
			return path_to_state
		# POST-VISIT
		# Find fringe and add to queue
		# Store paths to each fringe as its payload
		fringe = state_space.get_next_states(include_visited=False)
		for next_state in fringe:
			next_path = deepcopy(path_to_state)
			next_path.add_state(next_state)
			state_queue.enqueue(
				elems=[next_state], 
				contexts=[(state_space.end,)],
				payloads=[next_path]
			)
	
	return False 


"""
polygons = [
	Polygon([(5,2), (6,4), (4,5)]),
	Polygon([(1,1), (1,3), (4,3), (4,1)]),
]
"""
# Solution Found
# (120,650), (151,670), (251,670), (359,667), (374,651), (380,560)
# Cost: 358.0626920104638