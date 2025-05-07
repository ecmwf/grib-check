from CheckEngine import CheckEngine
from LookupTable import SimpleLookupTable
from checker.CheckPool import CheckPool
import os
import logging


class Wmo(CheckEngine, CheckPool):
    def __init__(self, param_lookup_table=None, valueflg=False):
        self.logger = logging.getLogger(__class__.__name__)

        self.set_checks({
            "basic_checks_2": self._basic_checks_2,
            "basic_checks": self._basic_checks,
            "daily_average": self._daily_average,
            "from_start": self._from_start,
            "given_level": self._given_level,
            "given_thickness": self._given_thickness,
            "has_bitmap": self._has_bitmap,
            "has_soil_layer": self._has_soil_layer,
            "has_soil_level": self._has_soil_level,
            "height_level": self._height_level,
            "point_in_time": self._point_in_time,
            "potential_temperature_level": self._potential_temperature_level,
            "potential_vorticity_level": self._potential_vorticity_level,
            "predefined_level": self._predefined_level,
            "predefined_thickness": self._predefined_thickness,
            "pressure_level": self._pressure_level,
            "resolution_s2s": self._resolution_s2s,
            "resolution_s2s_ocean": self._resolution_s2s_ocean,
            "since_prev_pp": self._since_prev_pp,
            "six_hourly": self._six_hourly,
            "three_hourly": self._three_hourly,
        })
        self.last_n = 0
        self.values = None
        self.valueflg = valueflg

        script_path = os.path.dirname(os.path.realpath(__file__))
        param_lookup_table = param_lookup_table if param_lookup_table is not None else SimpleLookupTable(f"{script_path}/TiggeParameters.json")
        super().__init__(param_lookup_table)
