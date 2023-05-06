from enum import Enum

from .parts import *


class _ModelsPaths(Enum):
    xgb_fuel_130_v1 = "./units/models/saves/fuel/xgb_fuelTA130_099889.bf"
    catboost_fuel_130_v1 = "./units/models/saves/fuel/cat_boost_fuelTA130_09924.bf"


class Models(object):
    def __init__(self):
        self.xgb_fuel_130_v1 = XGBFuelModelV1(_ModelsPaths.xgb_fuel_130_v1.value)
        self.catboost_fuel_130_v1 = CatBoostFuelModelV1(_ModelsPaths.catboost_fuel_130_v1.value)
        self.__all_models = {
            "xgb_fuel_130_v1": self.xgb_fuel_130_v1,
            "catboost_fuel_130_v1": self.catboost_fuel_130_v1
        }

    def __getitem__(self, item: str) -> XGBFuelModelV1 | CatBoostFuelModelV1:
        if item == "xgb_fuel_130":
            return self.__all_models["xgb_fuel_130_v1"]
        elif item == "catboost_fuel_130":
            return self.__all_models["catboost_fuel_130_v1"]
        return self.__all_models[item]