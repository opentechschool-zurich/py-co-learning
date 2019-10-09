# Game of life

- You have an `n x m` board (as an example `10 x 10`)
- Generate an initial pattern
  - `1` when a cell is alive
  - `0` when a cell is dead
- Rules for the next generation:
  - a _living_ cell with less than 2 neighbourgs _dies_
  - a _living_ cell with 2 or 3 neighbourgs _lives on_
  - a _living_ cell with more than 3 neighbourgs _dies_
  - a _dead_ cell with 3 neighbourgs _becomes alive_

References:

- <https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life>
- <https://bitstorm.org/gameoflife/>
