#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple parser ... of cf playground :)

"""

from __future__ import print_function
import sys
import pymzml
import get_example_file
import os
import glob
    
def main():
    answer = False
    pymzmlRun = pymzml.run.Reader(get_example_file.open_example('small.pwiz.1.1.mzML'))
    if pymzmlRun['TIC'].profile == [(0.004935, 15245068.0), (0.007896666666666666, 12901166.0), (0.011218333333333334, 586279.0), (0.022838333333333332, 441570.15625), (0.034925, 114331.703125), (0.04862, 130427.3046875), (0.06192333333333334, 580561.0625), (0.075015, 15148302.0), (0.07778833333333333, 10349958.0), (0.08120333333333334, 848427.3125), (0.09290333333333332, 456143.4375), (0.10480333333333333, 124170.3828125), (0.11721500000000001, 104264.796875), (0.13002166666666667, 147409.234375), (0.14345166666666667, 18257344.0), (0.14640833333333333, 11037852.0), (0.149755, 1102582.125), (0.16144166666666668, 360250.96875), (0.17337, 125874.828125), (0.18665833333333332, 142243.390625), (0.200695, 147414.578125), (0.2136733333333333, 17613074.0), (0.21674666666666667, 1597410.5), (0.22007333333333332, 990298.5), (0.23292333333333332, 447647.96875), (0.244745, 71677.03125), (0.2591716666666667, 119999.7421875), (0.2726633333333333, 152281.25), (0.28548333333333337, 22136832.0), (0.2888983333333333, 12434530.0), (0.3037033333333333, 379009.78125), (0.31565, 120473.4296875), (0.32852666666666663, 113763.3515625), (0.342915, 73607.4921875), (0.35855833333333337, 16495375.0), (0.36142833333333335, 6548706.5), (0.364755, 1041573.75), (0.37657833333333335, 626711.3125), (0.3886733333333333, 109042.7265625), (0.40196166666666666, 156294.984375), (0.4151316666666667, 79339.078125), (0.4284833333333333, 12015003.0), (0.4332216666666666, 13332331.0), (0.4365666666666667, 925073.25), (0.44832, 419351.46875), (0.46056499999999995, 88901.921875), (0.47310333333333326, 100616.1953125), (0.48723666666666665, 77939.0078125)]:
        answer = True

    return answer
        
if __name__ == '__main__':
    print(main())
