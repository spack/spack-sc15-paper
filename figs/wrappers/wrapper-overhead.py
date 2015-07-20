#!/usr/bin/env python
import sys
import yaml
import numpy as np
import matplotlib.pyplot as plt

with open('overhead.yaml') as f:
    data = yaml.load(f)

N = len(data)

keys = sorted(data.keys())

wrapper_means = []
no_wrap_means = []
for pkg in keys:
    wrapper = [float(f) for f in data[pkg]['wrapper']]
    no_wrap = [float(f) for f in data[pkg]['no_wrapper']]

    wrapper_means.append(sum(wrapper) / N)
    no_wrap_means.append(sum(no_wrap) / N)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()


wrapper_rects = ax.bar(ind,       wrapper_means, width, color='r')
no_wrap_rects = ax.bar(ind+width, no_wrap_means, width, color='b')

# add some text for labels, title and axes ticks
ax.set_xlabel('Libraries')
ax.set_ylabel('Build time (s)')
ax.set_xticks(ind+width)
ax.set_xticklabels(keys)

ax.legend( (wrapper_rects[0], no_wrap_rects[0]), ('Wrapper', 'No Wrapper') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height,
                '%d'%int(height),
                ha='center', va='bottom')

#autolabel(wrapper_rects)
#autolabel(no_wrap_rects)

ax.set_aspect(.25 * 1/ax.get_data_ratio())

plt.savefig('wrapper-overhead.pdf')
