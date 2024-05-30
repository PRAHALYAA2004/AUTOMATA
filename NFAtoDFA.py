from graphviz import Digraph

class NFAtoDFAConverter:
    def __init__(self, nfa):
        self.nfa = nfa
        self.alphabet = nfa['alphabet']
        self.dfa_states = []
        self.dfa_transitions = {}
        self.dfa_accepting_states = []

        
        self.convert()

    
    def convert(self):
        initial_state = self.epsilon_closure([self.nfa['initialState']])
        self.dfa_states.append(initial_state)

        unprocessed_states = [initial_state]

        
        while unprocessed_states:
            current_state = unprocessed_states.pop()
            self.dfa_transitions[",".join(current_state)] = {}

            for symbol in self.alphabet:
                next_state = self.epsilon_closure(self.move(current_state, symbol))
                if next_state and not any(self.are_sets_equal(state, next_state) for state in self.dfa_states):
                    self.dfa_states.append(next_state)
                    unprocessed_states.append(next_state)
                self.dfa_transitions[",".join(current_state)][symbol] = ",".join(next_state)

            
            is_accepting_state = any(state in self.nfa['acceptingStates'] for state in current_state)
            if is_accepting_state:
                self.dfa_accepting_states.append(current_state)

        
        reachable_states = set()
        for state in self.dfa_states:
            reachable_states.update(state)
        self.dfa_states = [state for state in self.dfa_states if set(state) & reachable_states]

        
        self.dfa_transitions = {state: transitions for state, transitions in self.dfa_transitions.items() if set(state.split(',')) & reachable_states}
        self.dfa_transitions = {state: {symbol: next_state for symbol, next_state in transitions.items() if set(next_state.split(',')) & reachable_states} for state, transitions in self.dfa_transitions.items()}

        
        self.dfa_accepting_states = [state for state in self.dfa_accepting_states if set(state) & reachable_states]

    
    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)

        while stack:
            current_state = stack.pop()
            current_state_transitions = self.nfa['transitions'].get(current_state, {})

            for next_state in current_state_transitions.get('ε', []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state) 

        return list(closure)

    
    def move(self, states, symbol):
        move_result = []
        for state in states:
            state_transitions = self.nfa['transitions'].get(state, {})

            
            if symbol == 'ε':
                move_result.extend(state_transitions.get('', []))

            
            move_result.extend(state_transitions.get(symbol, []))

        return move_result

   
    def are_sets_equal(self, set1, set2):
        return set(set1) == set(set2)

    
    def display_dfa(self):
        print('DFA States:', [",".join(state) for state in self.dfa_states])
        print('DFA Accepting States:', [",".join(state) for state in self.dfa_accepting_states])
        print('DFA Transitions:')
        print('{:<15} {:<10} {}'.format('State', 'Symbol', 'Next State'))
        print('-' * 35)
        for from_state, transitions in self.dfa_transitions.items():
            for symbol, to_state in transitions.items():
                print('{:<15} {:<10} {}'.format(from_state, symbol, to_state))

    
    def generate_dfa_graph(self, filename='dfa_graph'):
        dfa_graph = Digraph(graph_attr={'bgcolor': '#22092C'})
        for state in self.dfa_states:
            state_name = ','.join(state)
            if state in self.dfa_accepting_states:
                dfa_graph.node(state_name, shape='doublecircle', style='filled', fillcolor='#F05941', color='white', fontcolor='white')
            else:
                dfa_graph.node(state_name, shape='circle', style='filled', fillcolor='#872341', color='white', fontcolor='white')
        for from_state, transitions in self.dfa_transitions.items():
            for symbol, to_state in transitions.items():
                dfa_graph.edge(from_state, to_state, label=symbol, color='white', fontcolor='white')
        dfa_graph.render(filename, view=True)


    def generate_nfa_graph(self, filename='nfa_graph'):
        nfa_graph = Digraph(graph_attr={'bgcolor': '#22092C'})
        for state in self.nfa['states']:
            if state == self.nfa['initialState']:
                nfa_graph.node(state, shape='point')
            if state in self.nfa['acceptingStates']:
                nfa_graph.node(state, shape='doublecircle',style='filled', fillcolor='#F05941', color='white', fontcolor='white')
            else:
                nfa_graph.node(state, shape='circle',style='filled', fillcolor='#872341', color='white', fontcolor='white')
        for from_state, transitions in self.nfa['transitions'].items():
            for symbol, to_states in transitions.items():
                for to_state in to_states:
                    nfa_graph.edge(from_state, to_state, label=symbol, color='white', fontcolor='white')
        nfa_graph.render(filename, view=True)


nfa = {}
nfa['states'] = input("Enter NFA states separated by space: ").split()
nfa['alphabet'] = input("Enter alphabet symbols separated by space: ").split()
nfa['transitions'] = {}
for state in nfa['states']:
    nfa['transitions'][state] = {}
    transitions = input(f"Enter transitions for state {state} (comma separated, e.g., 'a:q1,q2 b:q2'): ").split()
    for transition in transitions:
        symbol, next_states = transition.split(':')
        nfa['transitions'][state][symbol] = next_states.split(',')
nfa['initialState'] = input("Enter initial state: ")
nfa['acceptingStates'] = input("Enter accepting states separated by space: ").split()


converter = NFAtoDFAConverter(nfa)
converter.display_dfa()
converter.generate_dfa_graph()
converter.generate_nfa_graph()