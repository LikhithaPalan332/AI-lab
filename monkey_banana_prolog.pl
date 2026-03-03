at(monkey, c).
at(box, c).
at(bananas, c).

same_place :-
    at(monkey, X),
    at(box, X).

on_box :-
    same_place.

under_bananas :-
    at(monkey, c).

can_push :-
    same_place.

can_climb :-
    same_place.

can_grab :-
    same_place,
    under_bananas.

can_reach(monkey, bananas) :-
    can_grab.

% -------- Queries --------
?-at(monkey, X).
?-on_box.
?-can_push.
?-under_bananas.
?-can_grab.
?-can_reach(monkey, bananas).
