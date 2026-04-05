% Capacities
cap(12,8,5,3).

% Goal condition
goal((6,6,0,0)).

% Empty a jug to fountain
move((A,B,C,D),(0,B,C,D),'Empty Jug1').
move((A,B,C,D),(A,0,C,D),'Empty Jug2').
move((A,B,C,D),(A,B,0,D),'Empty Jug3').
move((A,B,C,D),(A,B,C,0),'Empty Jug4').

% Pour Jug1 -> Jug2
move((A,B,C,D),(A1,B1,C,D),'Pour J1->J2') :-
    cap(_,C2,_,_),
    T is min(A, C2-B),
    T>0,
    A1 is A-T,
    B1 is B+T.

% Pour Jug1 -> Jug3
move((A,B,C,D),(A1,B,C1,D),'Pour J1->J3') :-
    cap(_,_,C3,_),
    T is min(A, C3-C),
    T>0,
    A1 is A-T,
    C1 is C+T.

% Pour Jug1 -> Jug4
move((A,B,C,D),(A1,B,C,D1),'Pour J1->J4') :-
    cap(_,_,_,C4),
    T is min(A, C4-D),
    T>0,
    A1 is A-T,
    D1 is D+T.

% Pour Jug2 -> Jug1
move((A,B,C,D),(A1,B1,C,D),'Pour J2->J1') :-
    cap(C1,_,_,_),
    T is min(B, C1-A),
    T>0,
    B1 is B-T,
    A1 is A+T.

% Pour Jug2 -> Jug3
move((A,B,C,D),(A,B1,C1,D),'Pour J2->J3') :-
    cap(_,_,C3,_),
    T is min(B, C3-C),
    T>0,
    B1 is B-T,
    C1 is C+T.

% Pour Jug2 -> Jug4
move((A,B,C,D),(A,B1,C,D1),'Pour J2->J4') :-
    cap(_,_,_,C4),
    T is min(B, C4-D),
    T>0,
    B1 is B-T,
    D1 is D+T.

% BFS search
bfs([[State,Path]|_],[State,Path]) :-
    goal(State).

bfs([[State,Path]|Rest],Solution) :-
    findall([Next,[Action,Next|Path]],
        (move(State,Next,Action),
        \+ member(Next,Path)),
    Children),
    append(Rest,Children,Queue),
    bfs(Queue,Solution).

solve :-
    bfs([[(12,0,0,0),[(12,0,0,0)]]],[Goal,Path]),
    reverse(Path,Steps),
    print_steps(Steps,0).

print_steps([], _).
print_steps([H|T], N) :-
    write('Step '), write(N), write(' : '),
    write(H), nl,
    N1 is N+1,
    print_steps(T,N1).
