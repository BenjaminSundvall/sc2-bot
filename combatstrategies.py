# ============================================================================
#  sc2-bot
#
#  Author: Benjamin Sundvall
#  Module: combatstrategies.py
#  Dependencies:
#    extendedlib.py
#
# ============================================================================



# ============================================================================
#  1. Superclass to all combat strategies.
# ============================================================================


class CombatStrategy:
    def __init__(self):
        pass


# ============================================================================
#  2. Default combat strategy.
# ============================================================================


class DefaultCombatStrategy(CombatStrategy):
    """ The default combat strategy. """
    def __init__(self):
        super().__init__()
