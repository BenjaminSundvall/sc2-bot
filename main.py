# ============================================================================
#  sc2-bot
#
#  Author: Benjamin Sundvall
#  Module: main.py
#  Dependencies:
#
# ============================================================================


import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId
from sc2.ids.upgrade_id import UpgradeId
from sc2.ids.buff_id import BuffId
from sc2.unit import Unit
from sc2.units import Units
from sc2.position import Point2
from sc2.player import Bot, Computer
from sc2.client import Client


class TestBot(sc2.BotAI):
    async def on_step(self, iteration: int):
        if iteration == 0:
            await self.chat_send("Hello there! :D")
        await self.distribute_workers()
        for worker in self.workers:
            self.client.debug_text_world("worker", worker.position3d)
        # if self.can_afford(UnitTypeId.REFINERY) \
        #         and not self.already_pending(UnitTypeId.REFINERY) \
        #         and not self.units(UnitTypeId.REFINERY):
        #     target_geyser = self.
        #     await self.workers[0].build_gas(target_geyser)

        # Build SCVs
        for cc in self.townhalls.ready:
            if self.supply_workers + self.already_pending(UnitTypeId.SCV) < self.townhalls.amount * 22 and cc.is_idle:
                if self.can_afford(UnitTypeId.SCV):
                    cc.train(UnitTypeId.SCV)

        # Build refineries
        for cc in self.townhalls.ready:
            vgs = self.vespene_geyser.closer_than(15, cc)
            for vg in vgs:
                if not self.can_afford(UnitTypeId.REFINERY):
                    break

                worker = self.select_build_worker(vg.position)
                if worker is None:
                    return

                if not self.gas_buildings or not self.gas_buildings.closer_than(1, vg):
                    worker.build(UnitTypeId.REFINERY, vg)
                    worker.stop(queue=True)


if __name__ == "__main__":
    participant_1 = Bot(Race.Terran, TestBot())
    participant_2 = Bot(Race.Terran, TestBot())
    # participant_2 = Computer(Race.Random, Difficulty.Medium)

    run_game(maps.get("Simple128"), [
        participant_1,
        participant_2
    ], realtime=False)


