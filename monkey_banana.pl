location(at_door).
location(at_window).
location(middle).

initial_state(state(at_door, at_window, no, no)).
goal_state(state(_, _, _, yes)).

move(
    state(M, B, no, H),
    walk(M, X),
    state(X, B, no, H)
) :-
    location(X),
    M \= X.

% Push box
move(
    state(M, M, no, H),
    push(M, X),
    state(X, X, no, H)
) :-
    location(X),
    M \= X.

% Climb
move(
    state(M, M, no, H),
    climb,
    state(M, M, yes, H)
).

% Grab banana
move(
    state(middle, middle, yes, no),
    grab,
    state(middle, middle, yes, yes)
).

solve(State, _, []) :-
    goal_state(State).

solve(State, Visited, [Action | Plan]) :-
    move(State, Action, NewState),
    \+ member(NewState, Visited),
    solve(NewState, [NewState | Visited], Plan).

start :-
    initial_state(Initial),
    solve(Initial, [Initial], Plan),
    write('Solution Plan:'), nl,
    print_plan(Plan),
    !.

print_plan([]).
print_plan([H|T]) :-
    write(H), nl,
    print_plan(T).
