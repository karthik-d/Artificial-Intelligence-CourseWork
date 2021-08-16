from Stack import *
from StateFormulation import *

def deduce_path(state, parents):
	
	def deduce_path_rec(state, path_seq):
		this_parent = parents[state]
		# Reached the root node
		if this_parent is None:
			return path_seq
		# Prepend node
		path_seq = [this_parent] + path_seq[:]
		return deduce_path_rec(this_parent, path_seq)

	return deduce_path_rec(state, [])


def make_path_string(path, depths):
	string_path = list()
	for state in path:
		string_path.append("{state} (Depth: {depth})".format(state=state, depth=depths[state]))
	return string_path


def IterativeDeepening(num_solns_reqd):

	def SearchDepth():

		state_space = Stack([INITIAL_STATE])
		depth_track = Stack([0])
		goal_states = list()
		explored_states = set()
		parents = {INITIAL_STATE: None}
		depths = {INITIAL_STATE: 0}

		while not state_space.is_empty():
			# Get next state and its path
			state = state_space.pop()
			curr_depth = depth_track.pop()
			# Skip iteration if state already explored
			if state in explored_states:
				continue
			if curr_depth > limit:
				continue
			explored_states.add(state)
			# Check if the state is a goal-state
			if is_goal_state(state):
				goal_states.append(state)
			# Find the next states
			fringe = get_next_states(state)
			state_space.push(fringe)
			# Add parent and depth of each fringe state, if not already added
			fringe_depths_list = list()
			for new_state in fringe:
				if new_state not in parents:
					parents[new_state] = state 
					depths[new_state] = curr_depth+1
					fringe_depths_list.append(curr_depth+1)
				else:
					fringe_depths_list.append(depths[new_state])
			depth_track.push(fringe_depths_list)

		return goal_states, explored_states, parents, depths

	limit = -1
	num_solns = 0
	while(num_solns<num_solns_reqd):
		limit += 1
		goal_states, explored_states, parents, depths = SearchDepth()
		num_solns = len(goal_states)
		print("{num_solns} solutions found with depth limit {limit}".format(num_solns=num_solns, limit=limit))
	return goal_states, explored_states, parents, depths