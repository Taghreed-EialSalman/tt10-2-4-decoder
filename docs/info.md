## How it works

The 2-to-4 line binary decoder consists of an array of four AND gates. The 2 binary inputs labelled A and B are decoded into one of 4 outputs, hence the description of 2-to-4 binary decoder. Each output represents one of the minterms of the 2 input variables, (each output = a minterm). There is an enable signal, E, which dictates whether all outputs are 1, or a specific output (based on the inputs) is coded as 0. 

## How to test

You test it by running all possible inputs and checking if the outputs match the expected values. Refer to the truth table of an active-high logic 2-4 decoder below. 

When E=1 -> D[3:0]=1

| E | A | B | D3 | D2 | D1 | D0 |
|---|---|---|----|----|----|----|
| 0 | 0 | 0 |  1 |  1 |  1 |  0 |
| 1 | 0 | 0 |  1 |  1 |  1 |  1 |
| 0 | 0 | 1 |  1 |  1 |  0 |  1 |
| 1 | 0 | 1 |  1 |  1 |  1 |  1 |
| 0 | 1 | 0 |  1 |  0 |  1 |  1 |
| 1 | 1 | 0 |  1 |  1 |  1 |  1 |
| 0 | 1 | 1 |  0 |  1 |  1 |  1 |
| 1 | 1 | 1 |  1 |  1 |  1 |  1 |

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any

NONE

## Pinout

### Inputs

| Pin     | Name |
|---------|------|
| ui[0]   | A    |
| ui[1]   | B    |
| ui[2]   | E (enable)    |
| ui[3]   |      |
| ui[4]   |      |
| ui[5]   |      |
| ui[6]   |      |
| ui[7]   |      |

### Outputs

| Pin     | Name |
|---------|------|
| uo[0]   | D[0]     |
| uo[1]   | D[1]     |
| uo[2]   | D[2]     |
| uo[3]   | D[3]     |
| uo[4]   |      |
| uo[5]   |      |
| uo[6]   |      |
| uo[7]   |      |
