# Expert_system_Inference_engine

Implemented a protocol for navigating through the rules and data in a knowledge system in order to solve the problem. 
Used Backward chaining mode to determine what facts must be asserted so that the goals can be achieved.

Knowledge bases contains only the following defined operators:

NOT X
X OR Y

1. Each query will be a single literal of the form Predicate(Constant) or ~Predicate(Constant).
2. Variables are all single lowercase letters.
3. All predicates (such as Sibling) and constants (such as John) are case-sensitive alphabetical strings that
begin with an uppercase letter.
4. Each predicate takes at least one argument.

You can have look on homework_3.pdf for more detailed Explanation and examples.
