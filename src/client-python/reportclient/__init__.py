# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
import sys

if sys.version_info[0] == 2:
    from reportclient._reportclient import *
else:
    from reportclient._reportclient3 import *

tmpdir = None

# everything was ok
RETURN_OK = 0
# serious problem, should be logged somewhere
RETURN_FAILURE = 2
# user canceled processing
from report import EXIT_CANCEL_BY_USER as RETURN_CANCEL_BY_USER
# event canceled processing
from report import EXIT_STOP_EVENT_RUN as RETURN_STOP_EVENT_RUN

# internal functions
from report import verbose, set_verbosity, _

def log(fmt, *args):
    sys.stderr.write("%s\n" % (fmt % args))


def log1(fmt, *args):
    """ prints log message if verbosity >= 1 """
    if verbose >= 1:
        sys.stderr.write("%s\n" % (fmt % args))


def log2(fmt, *args):
    """ prints log message if verbosity >= 2 """
    if verbose >= 2:
        sys.stderr.write("%s\n" % (fmt % args))


def error_msg(fmt, *args):
    sys.stderr.write("%s\n" % (fmt % args))


def error_msg_and_die(fmt, *args):
    sys.stderr.write("%s\n" % (fmt % args))
    sys.exit(1)
