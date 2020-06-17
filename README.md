# Computer Architecture

## Project

* [Implement the LS-8 Emulator](ls8/)

## Task List: add this to the first comment of your Pull Request

### Day 1: Get `print8.ls8` running

- [Y] Inventory what is here
- [Y] Implement the `CPU` constructor
- [Y] Add RAM functions `ram_read()` and `ram_write()`
- [Y] Implement the core of `run()`
- [Y] Implement the `HLT` instruction handler
- [Y] Add the `LDI` instruction
- [Y] Add the `PRN` instruction

### Day 2: Add the ability to load files dynamically, get `mult.ls8` running

- [Y] Un-hardcode the machine code
- [Y] Implement the `load()` function to load an `.ls8` file given the filename
      passed in as an argument
- [Y] Implement a Multiply instruction (run `mult.ls8`)

### Day 3: Stack

- [Y] Implement the System Stack and be able to run the `stack.ls8` program

### Day 4: Get `call.ls8` running

- [ ] Implement the CALL and RET instructions
- [ ] Implement Subroutine Calls and be able to run the `call.ls8` program

### Stretch

- [ ] Add the timer interrupt to the LS-8 emulator
- [ ] Add the keyboard interrupt to the LS-8 emulator
- [ ] Write an LS-8 assembly program to draw a curved histogram on the screen
