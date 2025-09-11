# Define action structure
class Action:
    def __init__(self, name, precond, effect):
        self.name = name
        self.precond = set(precond)
        self.effect = set(effect)

# Setup
actions = [
    Action("Move(A→B)", ["At(A)"], ["At(B)"]),
    Action("Move(B→C)", ["At(B)"], ["At(C)"])
]

# Initial state
state_levels = [set(["At(A)"])]
action_levels = []

# Build planning graph for 3 levels
for level in range(2):  # 2 steps = 3 state levels
    applicable_actions = []
    next_state = set(state_levels[-1])  # carry over existing literals

    for action in actions:
        if action.precond.issubset(state_levels[-1]):
            applicable_actions.append(action)
            next_state.update(action.effect)

    action_levels.append(applicable_actions)
    state_levels.append(next_state)

# Display result
for i, s in enumerate(state_levels):
    print(f"State Level S{i}: {s}")
    if i < len(action_levels):
        print(f"Action Level A{i}: {[a.name for a in action_levels[i]]}")
