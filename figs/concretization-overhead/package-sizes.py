#!/usr/bin/env spack-python

from external import yaml
import numpy as np
from matplotlib import rcParams as rc
rc['ps.useafm'] = True
rc['pdf.use14corefonts'] = True
rc['text.usetex'] = True
import matplotlib.pyplot as plt


with open('merl.yaml') as stream:
    timings = yaml.load(stream)

sizes = [t[1] for t in timings]

#plt.yscale('log')
plt.axes().set_aspect(.15)
plt.hist(sizes, 20)


plt.ylabel('Count')
plt.xlabel('Package DAG size (nodes)')

plt.savefig('package-sizes.pdf')
