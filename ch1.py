
from random import sample


sample_space = {'Heads', 'Tails'}

probability_heads = 1 / len(sample_space)
print(f"Probability of choosing heads is {probability_heads}")

def is_heads_or_tails(outcome):
    return outcome in sample_space

def is_neither(outcome):
    return not is_heads_or_tails(outcome)

def is_heads(outcome):
    return outcome == 'Heads'

def is_tails(outcome):
    return outcome == 'Tails'

event_conditions = [is_heads_or_tails, is_heads, is_tails, is_neither]

def get_matching_event(event_condition, generic_sample_space):
    return set([outcome for outcome in generic_sample_space if event_condition(outcome)])

for event_condition in event_conditions:
    print(f"Event Condition: {event_condition.__name__}")
    event = get_matching_event(event_condition, sample_space)
    print(f"Event: {event}")
    
def compute_probability(even_condition, generic_sample_space):
    event = get_matching_event(even_condition, generic_sample_space)
    return len(event)/len(generic_sample_space)

for event_condition in event_conditions:
    prob = compute_probability(event_condition, sample_space)
    name = event_condition.__name__
    print(f"Probability of event arising from '{name}' is {prob}")