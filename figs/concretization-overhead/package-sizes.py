#!/usr/bin/env spack-python

from external import yaml
import matplotlib.pyplot as plt
import numpy as np

with open('merl.yaml') as stream:
    timings = yaml.load(stream)

sizes = [t[1] for t in timings]

#plt.yscale('log')

plt.axes().set_aspect(.25)
plt.hist(sizes, 25)

plt.ylabel('Count', fontsize=18)
plt.xlabel('Package DAG size (nodes)', fontsize=18)

plt.savefig('package-sizes.pdf')
