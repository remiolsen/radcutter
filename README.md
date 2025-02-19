# radcutter
Simplistic in silico sim for NGI RAD-seq (EZ-RADish) protocol 

## Installation

To install radcutter, use the following command:

```sh
pip install -e .
```

## Usage

E.g., for a EcoRI (but we're also testing how SbfI would behave) library with 420-720 size selection window (300-600 w.o. adapters)

```sh
radcutter -f /path/to/genome.fasta -l 300 -u 600 -e EcoRI SbfI
```
