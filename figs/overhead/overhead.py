#!/usr/bin/env python
import sys
import yaml
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

with open('overhead.yaml') as f:
    data = yaml.load(f)

N = len(data)
keys = ['libelf', 'libpng', 'mpileaks',
        'libdwarf', 'python', 'dyninst', 'lapack']

nfs_color='RoyalBlue'
wrap_color='Orange'
orig_color='SeaGreen'

nfs_label='Wrappers, NFS'
wrap_label='Wrappers, Temp FS'
orig_label='No Wrappers, Temp FS'

fsize = 14

wrapper_means = []
tmp_means = []       # same configuration as 'wrapper'
no_wrap_means = []
nfs_means = []
for pkg in keys:
    wrapper = [float(f) for f in data[pkg]['wrapper']]
    tmp     = [] #[float(f) for f in data[pkg]['tmp']]
    no_wrap = [float(f) for f in data[pkg]['no_wrapper']]
    nfs     = [float(f) for f in data[pkg]['home']]

    no_wrap_means.append(sum(no_wrap) / len(no_wrap))
    nfs_means.append(sum(nfs) / len(nfs))
    wrapper_means.append(
        (sum(wrapper) + sum(tmp))
        / (len(wrapper) + len(tmp)))

wrap = np.array(wrapper_means)
orig = np.array(no_wrap_means)
nfs = np.array(nfs_means)

nfs_overhead = (nfs - orig) / orig
wrap_overhead = (wrap - orig) / orig

ind = np.arange(N,dtype=float)  # the x locations for the groups
ind += .1


# ==============================================================
# first figure: build times.
# ==============================================================
plt.figure()
fig, ax = plt.subplots()
width = 0.25       # the width of the bars

nfs_rects     = ax.bar(ind,         nfs_means, width,     color=nfs_color)
wrapper_rects = ax.bar(ind+width,   wrapper_means, width, color=wrap_color)
no_wrap_rects = ax.bar(ind+2*width, no_wrap_means, width, color=orig_color)

# add some text for labels, title and axes ticks
ax.set_xlabel('Libraries', fontsize=fsize)
ax.set_ylabel('Build time (s)', fontsize=fsize)
ax.set_xticks(ind+width)
ax.set_xticklabels(keys, fontsize=(fsize-1))

l = ax.legend((nfs_rects[0], wrapper_rects[0], no_wrap_rects[0]),
          (nfs_label, wrap_label, orig_label),
              loc=2, framealpha=0, fontsize=14)
l.get_frame().set_linewidth(0)

def autolabel(rects):
    # attach some text labels
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2. + .1, 1.05*height,
                #'%d'%int(height),
                '%.1f%%' % (wrap_overhead[i] * 100),
                ha='center', va='bottom')

#autolabel(wrapper_rects)
#autolabel(no_wrap_rects)

#plt.gca().set_ylim(top=400)
#plt.yscale('log')
#ax.yaxis.set_major_formatter(ScalarFormatter())

ax.set_aspect(.3 * 1/ax.get_data_ratio())

plt.savefig('build-time.pdf')


# ==============================================================
# second figure: overheads
# ==============================================================
plt.figure()
fig, ax = plt.subplots()
width = 0.3       # the width of the bars

nfs_rects     = ax.bar(ind,       nfs_overhead  * 100, width, color=nfs_color)
wrapper_rects = ax.bar(ind+width, wrap_overhead * 100, width, color=wrap_color)
plt.axhline(y=0, color='k')

ax.set_xlabel('Libraries', fontsize=fsize)
ax.set_ylabel('Overhead (% time)', fontsize=fsize)
ax.set_xticks(ind+width)
ax.set_xticklabels(keys, fontsize=(fsize-1))

l = ax.legend((nfs_rects[0], wrapper_rects[0]), ('Wrappers, NFS', 'Wrappers'),
              loc=1, framealpha=0, fontsize=14)
l.get_frame().set_linewidth(0)

def autolabel(rects, overhead):
    # attach some text labels
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if overhead[i] < 0:
            height = -(height*2.2)
        ax.text(rect.get_x()+rect.get_width()/2. + .1, 1.05*height,
                #'%d'%int(height),
                '%.1f%%' % (overhead[i] * 100),
                ha='center', va='bottom', fontsize=10)

autolabel(nfs_rects, nfs_overhead)
autolabel(wrapper_rects, wrap_overhead)

plt.gca().set_ylim(top=80, bottom=-5)
#plt.yscale('log')
ax.yaxis.set_major_formatter(ScalarFormatter())

ax.set_aspect(.3 * 1/ax.get_data_ratio())

plt.savefig('overhead.pdf')
