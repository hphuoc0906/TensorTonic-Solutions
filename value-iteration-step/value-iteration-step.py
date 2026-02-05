def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    new_values = values.copy()

    for state in range(len(values)):
        new_values[state] = 0
        for action in range(len(transitions[state])):
            s = 0
            for new_state in range(len(transitions[state][action])):
                s += transitions[state][action][new_state] * values[new_state]
            new_values[state] = max(new_values[state], rewards[state][action] + gamma * s)
    
    return new_values