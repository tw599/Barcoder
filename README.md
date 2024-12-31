# About

- Generates random barcode sequences for indexing/barcoding/NGS applications
- Random barcodes generated can be of specified length & within specified GC% ranges

# Pre-Requisites

Install python modules *random* and *argparse*
```
pip install argparse
pip install random
```

# Usage

```
python Barcoder.py [-h] -l LENGTH -min GC_MIN -max GC_MAX [-n NUM_BARCODES]
```

*Note: Recommendation for -min is 0.45 and -max is 0.55 for generation of balanced barcodes*

*Note: For any generated barcodes, it is important to cross-check barcodes for any existing DNA motifs, restriction enzyme sites or other functionally relevant DNA sequences by using appropriate databases [JASPAR](https://jaspar.elixir.no/), [NEBcutter] (https://www.hsls.pitt.edu/obrc/index.php?page=URL1043859167), depending on the purpose and design of the barcode containing sequences.* 
