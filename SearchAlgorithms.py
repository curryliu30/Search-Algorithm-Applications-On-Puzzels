#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import collections
import os, sys
import numpy as np


# # Helper Functions

# # Read Input File

# # A star Search

# In[ ]:


def get_cost(moves):
    return len(moves)+1

def get_heuristic(state):
    pos = get_piece_locations(state)
    x = abs(3-pos['1'][0][0])
    y = abs(1-pos['1'][0][1])
    return x+y


# In[ ]:


def a_star(state):
    seen = set()
    q = collections.deque([(state, [], get_heuristic(state))])
    nodes_expanded = 0
    while len(q) > 0:
        
        q = collections.deque(sorted(q, key=lambda q1: q1[2]))

        kstate, kmoves, f = q.popleft()
        nodes_expanded=nodes_expanded+1
        for nstate, nmove in get_successors(kstate):
            return_state = get_forms(nstate)
            if return_state not in seen:
                if is_goal(nstate):
                    print ('Solution Found!' ,"\n", 'Cost:', len(kmoves)+1, "\n" ,
                           'Number of states expanded:', nodes_expanded, "\n",
                           'Number of states generated:', len(seen), "\n") 
                    return nstate, kmoves+[nmove], nodes_expanded, seen
                seen.add(return_state)
                g = get_cost(kmoves)
                h = get_heuristic(nstate)
                
                q.append((nstate, kmoves+[nmove], g+h))                        
                
    return None


# In[ ]:





# In[ ]:


import time
start_time = time.time()
a_star(initial_state)
print("--- %s seconds ---" % (time.time() - start_time))


# # A star Output for puzzel1

# In[ ]:


final_state, moves_list, nodes_expanded, seen_nodes = a_star(initial_state)
file = open('puzzel1sol_astar.txt', "a")
file.write(f'Initial state:\n')
output_puzzle(initial_state)
file.write(f'\nCost of the (optimal) solution: {len(moves_list)}\n')
file.write(f'\nNumber of states expanded: {nodes_expanded}')
file.write(f'\nNumber of states generated: {len(seen_nodes)}\n')
file.write(f'\n(Optimal) solution:\n\n0\n')
output_puzzle(initial_state)
state=initial_state
for move in moves_list:
    file.write(f'\n{x}\n')
    state = move_piece(state, move[0], move[1], move[2])
    output_puzzle(state)
file.close()


# # Breadth-First Search

# In[ ]:


def bfs(state):
    seen = set()
    q = collections.deque([(state, [])])
    nodes_expanded = 0
    while len(q) > 0:
        kstate, kmoves = q.popleft()
        nodes_expanded=nodes_expanded+1
        for nstate, nmove in get_successors(kstate):
            return_state = get_forms(nstate)
            if return_state not in seen:
                if is_goal(nstate):
                    print ('Solution Found!' ,"\n", 'Cost:', len(kmoves)+1, "\n" ,
                           'Number of states expanded:', nodes_expanded, "\n",
                           'Number of states generated:', len(seen), "\n") 
                    return nstate, kmoves+[nmove], nodes_expanded, seen
                seen.add(return_state)
                
                q.append((nstate, kmoves+[nmove]))        
                
    return None


# # BFS Output for puzzel1

# In[ ]:


final_state, moves_list, nodes_expanded, seen_nodes = bfs(initial_state)


file = open('puzzel1sol_bfs.txt', "a")
file.write(f'Initial state:\n')
output_puzzle(initial_state)
file.write(f'\nCost of the (optimal) solution: {len(moves_list)}\n')
file.write(f'\nNumber of states expanded: {nodes_expanded}')
file.write(f'\nNumber of states generated: {len(seen_nodes)}\n')
file.write(f'\n(Optimal) solution:\n\n0\n')
output_puzzle(initial_state)
state=initial_state
for move in moves_list:
    file.write(f'\n{x}\n')
    state = move_piece(state, move[0], move[1], move[2])
    output_puzzle(state)
file.close()


# # Depth-First Search

# In[ ]:


def dfs(state):
    seen = set()
    q = collections.deque([(state, [])])
    nodes_expanded = 0
    while len(q) > 0:
        kstate, kmoves = q.popleft()
        nodes_expanded=nodes_expanded+1
        for nstate, nmove in get_successors(kstate):
            return_state = get_forms(nstate)
            if return_state not in seen:
                if is_goal(nstate):
                    print ('Solution Found!' ,"\n", 'Cost:', len(kmoves)+1, "\n" ,
                           'Number of states expanded:', nodes_expanded, "\n",
                           'Number of states generated:', len(seen), "\n") 
                    return nstate, kmoves+[nmove], nodes_expanded, seen
                seen.add(return_state)
                q.appendleft((nstate, kmoves+[nmove]))   
    return None


# In[ ]:


import time
start_time = time.time()
dfs(initial_state)
print("--- %s seconds ---" % (time.time() - start_time))


# # DFS Output for puzzel1

# In[ ]:


final_state, moves_list, nodes_expanded, seen_nodes = dfs(initial_state)

file = open('puzzel1sol_dfs.txt', "a")
file.write(f'Initial state:\n')
output_puzzle(initial_state)
file.write(f'\nCost of the (optimal) solution: {len(moves_list)}\n')
file.write(f'\nNumber of states expanded: {nodes_expanded}')
file.write(f'\nNumber of states generated: {len(seen_nodes)}\n')
file.write(f'\n(Optimal) solution:\n\n0\n')
output_puzzle(initial_state)
state=initial_state
for move in moves_list:
    file.write(f'\n{x}\n')
    state = move_piece(state, move[0], move[1], move[2])
    output_puzzle(state)
file.close()

