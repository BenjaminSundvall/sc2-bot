import os

from typing import Optional, Union

from extendedlib import *
from base import Base
from army import Army
from combatstrategies import DefaultCombatStrategy
from productionstrategies import *
from productionorder import *


class MyAgent(IDABot):
    def __init__(self):
        IDABot.__init__(self)
        self.is_first_step = True

# ============================================================================
#   Hello
# ============================================================================

    def on_game_start(self):
        """ Runs once one game start. """
        IDABot.on_game_start(self)

    def on_first_step(self):
        """ Code to run on the first step only. """
        pass

    def on_step(self):
        """ Runs every game step. """
        IDABot.on_step(self)

        # First step
        if self.is_first_step:
            self.on_first_step()
            self.is_first_step = False

# ============================================================================
#   :D
# ============================================================================

def main():
    coordinator = Coordinator(r"D:\StarCraft II\Versions\Base82457\SC2_x64.exe")

    bot1 = MyAgent()
    # bot2 = MyAgent()

    participant_1 = create_participants(Race.Terran, bot1)
    # participant_2 = create_participants(Race.Terran, bot2)
    participant_2 = create_computer(Race.Random, Difficulty.Easy)

    coordinator.set_real_time(False)
    coordinator.set_participants([participant_1, participant_2])
    coordinator.launch_starcraft()

    path = os.path.join(os.getcwd(), "maps", "InterloperTest.SC2Map")
    coordinator.start_game(path)

    while coordinator.update():
        pass


if __name__ == "__main__":
    main()