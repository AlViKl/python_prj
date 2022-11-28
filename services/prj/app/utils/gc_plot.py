import matplotlib.pyplot as plt
import numpy as np
from app.utils.gen_functions import calculation_gc_content


def tick_calculation(data: str, step: int = 100):
    '''
    Calculates ration per fragment
    '''
    amount_per_tick = list()
    for i in range(0, len(data), step):
        tick = data[i:i+step]
        amount_per_tick.append(calculation_gc_content(tick))
    return amount_per_tick


def plot_gc_calcution(gc_list: list[int],
                      step: int = 100,
                      filename: str = "gc_ratio_plot",
                      file_ext: str = "png"):
    '''
    Plots DNA sequence distribution and save to output file
    '''
    x = np.arange(0, len(gc_list))
    print(x)
    print(gc_list)
    plt.step(x, gc_list, where='post')
    plt.suptitle("GC content distribution")
    plt.xlabel("Genome position")
    plt.ylabel("GC-content, %")
    plt.savefig(f"{filename}.{file_ext}")


def generate_plot_with_data(set_size: int = 1000):
    '''
    Generate test data for plot and calculate GC ratio
    '''
    dna_bases = ['A', 'C', 'G', 'T']
    test_data = str()
    for i in range(set_size):
        base = np.random.choice(dna_bases)
        test_data += base
    plot_gc_calcution(tick_calculation(test_data))
