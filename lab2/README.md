# Intro to computing theory lab problem 2

## Minimizing deterministic finite automata


Pseudo code for finding reachable states:
`let reachable_states := {q0}
let new_states := {q0}

do {
    temp := the empty set
    for each q in new_states do
        for each c in Σ do
            temp := temp ∪ {δ(q,c)}
    new_states := temp \ reachable_states
    reachable_states := reachable_states ∪ new_states
} while (new_states ≠ the empty set)

unreachable_states := Q \ reachable_states`