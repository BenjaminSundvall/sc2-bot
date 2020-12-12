# ============================================================================
#  sc2-bot
#
#  Author: Benjamin Sundvall
#  Module: productionstrategies.py
#  Dependencies:
#    extendedlib.py
#
# ============================================================================



# ============================================================================
#  1. Superclass to all production strategies.
# ============================================================================


class ProductionStrategy:
    def __init__(self):
        pass


# ============================================================================
#  2. Default production strategy.
# ============================================================================


class DefaultProductionStrategy(ProductionStrategy):
    """ The default production strategy. """
    def __init__(self):
        super().__init__()