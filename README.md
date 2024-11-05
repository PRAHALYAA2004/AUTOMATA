
# NFA to DFA Converter

This project provides a tool to convert a Non-deterministic Finite Automaton (NFA) into a Deterministic Finite Automaton (DFA) using Python. It also generates graphical representations of both the NFA and DFA using Graphviz.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [Notes](#notes)

## Features

- Convert an NFA to an equivalent DFA
- Display the states, transitions, and accepting states of the resulting DFA
- Generate graphical representations of both the NFA and DFA using Graphviz, with custom styling for nodes and edges

## Requirements

- Python 3.x
- [Graphviz](https://graphviz.gitlab.io/) (for graphical output)

### Python Libraries

To install required libraries, use:
```bash
pip install graphviz
```

## Usage

1. Define your NFA by providing states, alphabet symbols, transitions, initial state, and accepting states.
2. Run the script to see a printed representation of the DFA.
3. Generate visualizations for both the NFA and DFA.

### Input Structure

The script will prompt you to enter:
- **States**: List of states in the NFA (e.g., `q0 q1 q2`).
- **Alphabet**: Input symbols used by the NFA (e.g., `a b`).
- **Transitions**: Transition table specifying the state transitions for each symbol. Each transition for a state should be entered in the format `symbol:next_state1,next_state2`.
- **Initial State**: Starting state of the NFA.
- **Accepting States**: List of accepting states in the NFA.

### Sample Input

```plaintext
Enter NFA states separated by space: q0 q1 q2
Enter alphabet symbols separated by space: a b
Enter transitions for state q0 (comma separated, e.g., 'a:q1,q2 b:q2'): a:q1 b:q2
Enter transitions for state q1 (comma separated, e.g., 'a:q1,q2 b:q2'): a:q2 b:q0
Enter transitions for state q2 (comma separated, e.g., 'a:q1,q2 b:q2'): a:q0 b:q1
Enter initial state: q0
Enter accepting states separated by space: q2
```

### Running the Script

After defining the NFA, run the script. It will display the DFA states, transitions, and accepting states, and generate graphical representations for both the NFA and DFA.

```python
converter = NFAtoDFAConverter(nfa)
converter.display_dfa()
converter.generate_dfa_graph()  # Generates DFA graph
converter.generate_nfa_graph()  # Generates NFA graph
```

### Graph Files
The visual representations of the NFA and DFA are saved as `.pdf` files:
- `dfa_graph.pdf`
- `nfa_graph.pdf`

## Example

Here’s an example of the output format in the console:
```plaintext
DFA States: ['q0', 'q1', 'q0,q2']
DFA Accepting States: ['q0,q2']
DFA Transitions:
State           Symbol     Next State
-----------------------------------
q0              a          q1
q0              b          q2
...
```

## Notes

- The **Graphviz** package must be installed separately on your system for the script to generate graphical output. You can download it from the [official Graphviz site](https://graphviz.gitlab.io/download/).
- The `.render()` function in `generate_dfa_graph()` and `generate_nfa_graph()` will automatically open the generated graph if `view=True` is set.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
