from stp_core.common.log import getlogger
from collections import deque
from common.exceptions import PlenumValueError, LogicError

logger = getlogger()


class Tracker:

    def __init__(self):
        self.un_committed = deque()

    def apply_batch(self, state_root, ledger_size):

        un_committed_state = ()

        if state_root != "":
            un_committed_state += (state_root,)
        else:
            raise PlenumValueError('state_root',
                                   state_root,
                                   "No state root given")

        if ledger_size > 0:
            un_committed_state += (ledger_size,)
        else:
            raise PlenumValueError('ledger_size',
                                   ledger_size,
                                   "Incorrect size of ledger given")

        self.un_committed.append(un_committed_state)

    def reject_batch(self):
        # what is the output of a one variable  array from this

        if len(self.un_committed) != 0:
            self.un_committed = self.un_committed[:-1]
        else:
            raise LogicError("No items to revert in Tracker")
