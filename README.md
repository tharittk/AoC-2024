# AoC-2024


 ▗▄▖ ▗▄▄▄ ▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖     ▗▄▖ ▗▄▄▄▖     ▗▄▄▖ ▗▄▖ ▗▄▄▄ ▗▄▄▄▖
▐▌ ▐▌▐▌  █▐▌  ▐▌▐▌   ▐▛▚▖▐▌  █      ▐▌ ▐▌▐▌       ▐▌   ▐▌ ▐▌▐▌  █▐▌   
▐▛▀▜▌▐▌  █▐▌  ▐▌▐▛▀▀▘▐▌ ▝▜▌  █      ▐▌ ▐▌▐▛▀▀▘    ▐▌   ▐▌ ▐▌▐▌  █▐▛▀▀▘
▐▌ ▐▌▐▙▄▄▀ ▝▚▞▘ ▐▙▄▄▖▐▌  ▐▌  █      ▝▚▄▞▘▐▌       ▝▚▄▄▖▝▚▄▞▘▐▙▄▄▀▐▙▄▄▖
                                                                      
                                                                      
                                                                      

Advent of Code 2024
Day 1:
Day 2:
Day 3:
Day 4:
Day 5:
Day 6: Guard Patroling
Part 1: simple while loop until out-of-bound position detected. Refactoring turning logic helps code clean
Part 2: keeps track every obstacle on which side it has been hit. If the same side was hit twice, the loop is detected.
Day 7: Operator Serach
Part 1: Recursion for O(2^n) with optimization via early termination, which was possible because + and * only increase the value
Part 2: From O(2^n) to O(3^n). The same optimization is applied as concatenation has the same nature as + and *
Day 8: Antenna Harmonic
Part 1: Use the vector notation to find the antinode location. Leaving the out-of-grid check until we are going to add the location to final output. The final output handles duplication naturally through built-in set
Part 2: Code changes by having the out-of-grid check embedded inside the antinode finding function. The while loop keeps adding the antinode as long as it is still inside grid.
Day 9: File array compaction
Part 1: Use two pointers to swap the empty space with file block.
Part 2: Quite lots more complex than part 1. Settled with LinkedList approach in which every link node store the free space information: space left and the files that end up moving to this node (for later full expansion to get checksum). Every file moves from right-most tto left-most-that-fits cost O(n free node) so the overall is O(n2).


