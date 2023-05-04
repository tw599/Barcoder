import argparse
import random

def generate_barcode(length, gc_min, gc_max):
    """
    Generates a random DNA barcode of the specified length with GC content between gc_min and gc_max.
    """
    bases = ['A', 'C', 'G', 'T']
    gc_count = int(length * random.uniform(gc_min, gc_max))
    barcode = [random.choice(['G', 'C']) if i < gc_count else random.choice(['A', 'T']) for i in range(length)]
    random.shuffle(barcode)
    return ''.join(barcode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate random DNA barcodes with specified GC content range.')
    parser.add_argument('-l', '--length', type=int, required=True, help='Length of the barcode.')
    parser.add_argument('-min', '--gc_min', type=float, required=True, help='Minimum desired GC content as a decimal fraction.')
    parser.add_argument('-max', '--gc_max', type=float, required=True, help='Maximum desired GC content as a decimal fraction.')
    parser.add_argument('-n', '--num_barcodes', type=int, default=1, help='Number of barcodes to generate (default: 1)')
    args = parser.parse_args()

    for i in range(args.num_barcodes):
        barcode = generate_barcode(args.length, args.gc_min, args.gc_max)
        print(barcode)
