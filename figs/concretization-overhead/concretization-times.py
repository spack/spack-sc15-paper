#!/usr/bin/env python

import yaml
import matplotlib.pyplot as plt

files = (
#    ('macbook.yaml' , 'MacBook Pro, Haswell, 2.6Ghz'),
    ('rzuseqlac2-timings.yaml'    , 'Linux, IBM Power7, 3.6Ghz'),
    ('rzmerl156-timings.yaml'     , 'Linux, Intel Sandy Bridge, 2.6Ghz'),
    ('rzoz14-timings.yaml'        , 'Linux, Intel Haswell, 2.3Ghz'),
#    ('cab688-timings.yaml'       , 'Linux, Intel Sandy Bridge, 2.6Ghz'),
#    ('catalyst160-timings.yaml'  , 'Linux, Intel Ivy Bridge, 2.4Ghz'),
#    ('vulcanlac3-timings.yaml'   , 'Linux, IBM Power7, 3.6Ghz'),
)


styles = ['bd', 'r^', 'gv', 'bs', 'b*']

#plt.axes().set_aspect(3)


for i, (f, label) in enumerate(files):
    with open(f) as stream:
        timings = yaml.load(stream)

    timings.sort(key=lambda x:int(x[1]))

    timings = [(name, size, sum(t)/len(t)) for name, size, t in timings]
    sizes = [t[1] for t in timings]
    times = [t[2] for t in timings]

    plt.plot(sizes, times, styles[i], label=label)

plt.ylabel('Time (seconds)', fontsize=14)
plt.xlabel('Package DAG size (nodes)', fontsize=14)
l = plt.legend(loc=2, framealpha=0)
l.get_frame().set_linewidth(0)

plt.gca().set_xlim(right=55)

plt.axes().set_aspect(.3 * 1/plt.axes().get_data_ratio())

plt.savefig('concretization-times.pdf')
