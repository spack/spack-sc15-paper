#!/usr/bin/env spack-python

from external import yaml
import matplotlib.pyplot as plt

files = { 'macbook.yaml' : 'MacBook Pro, Haswell, 2.6Ghz',
          'merl.yaml'    : 'Linux, Sandy Bridge, 2.6Ghz'}


styles = ['bd', 'r^']

plt.axes().set_aspect(3)

for i, (f, label) in enumerate(files.items()):
    with open(f) as stream:
        timings = yaml.load(stream)

    timings.sort(key=lambda x:int(x[1]))

    timings = [(name, size, sum(t)/len(t)) for name, size, t in timings]
    sizes = [t[1] for t in timings]
    times = [t[2] for t in timings]

    plt.plot(sizes, times, styles[i], label=label)

plt.ylabel('Time (seconds)')
plt.xlabel('Package DAG size (nodes)')
plt.legend(loc=2)

plt.savefig('concretization-times.pdf')
