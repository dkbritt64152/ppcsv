# /bin/python/env/python
# -*- coding: utf-8 -*-

""" Displays a list of Pmres from 1 to N."""
from __future__ import print_function
import csv
import sys
import time
from pyprimesieve import primes

__author__ = "David Kevin Britt"
__copyright__ = "Copyright (C) 2017 David Kevin Britt"
__license__ = "GPL 3.1"
__version__ = "1.1.0"
__maintainer__ = "David Kevin Britt"
__email__ = "dkbritt64118@gmail.com"
__status__ = "Production"

# This program is free software and can be edited and modified.
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


if len(sys.argv) < 2:
    sys.stderr.write('Usage: ppcsvbp (N) an integer, as upper limit.')
    print('List also written to primelist.csv')
    sys.exit(1)
else:
    limit_max = sys.argv[1]
answer = [primes(int(limit_max))]


def main():
    """    Will print the list to the screen.. """


start_time = time.clock()
limit_max = sys.argv[1]
print(answer)
with open('primelist.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([primes(int(limit_max))])
run_time = ((time.clock() - start_time)*1000)
if run_time < 1000:
    print('\n', run_time, ' milliseconds')
else:
    print('\n', run_time/1000, ' seconds')
