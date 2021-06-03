from autotest import TestSet

import testrunners

import sys
from importlib import import_module
from io import StringIO

defaults = {'modulename':'ex7',
            'runner':testrunners.functionname_runner,
            'ans':[True],
            }

cases = {s:{'fname':s} for s in ('print_to_n',
                                 'print_reversed',
                                 'is_prime',
                                 'exp_n_x',
                                 'play_hanoi',
                                 'print_sequences',
                                 'print_no_repetition_sequences',
                                 'parentheses',
                                 'up_and_right',
                                 'flood_fill',)
     }

tsets = {'ex7':TestSet({},cases),
}
