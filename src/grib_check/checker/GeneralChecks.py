#
# (C) Copyright 2025- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import logging

import numpy as np

from grib_check.Assert import (
    AssertTrue,
    Eq,
    EqDbl,
    Exists,
    Fail,
    Ge,
    IsIn,
    Le,
    Lt,
    Missing,
    Ne,
    Pass,
)
from grib_check.CheckEngine import CheckEngine
from grib_check.Grib import get_gaussian_latitudes
from grib_check.Report import Report


class GeneralChecks(CheckEngine):
    def __init__(self, lookup_table, check_limits=False, check_validity=True):
        super().__init__(lookup_table)
        self.logger = logging.getLogger(__class__.__name__)

        self.register_checks(
            {
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
                "resolution_s2s": self._resolution_s2s,
                "resolution_s2s_ocean": self._resolution_s2s_ocean,
                "since_prev_pp": self._since_prev_pp,
                "six_hourly": self._six_hourly,
                "three_hourly": self._three_hourly,
            }
        )
        self.last_n = 0
        self.values = None
        self.check_limits = check_limits
        self.check_validity = check_validity

    # def register_check(self, name, func):
    #     if name in self._check_map:
    #         raise ValueError(f"Check {name} already registered.")
    #     else:
    #         self._check_map[name] = func
    #
    # def override_check(self, name, func):
    #     if name not in self._check_map:
    #         raise ValueError(f"Check {name} not registered.")
    #     else:
    #         self._check_map[name] = func
    #
    # def get_check(self, name):
    #     if name not in self._check_map:
    #         raise ValueError(f"Check {name} not registered.")
    #     else:
    #         return self._check_map[name]

    def _check_date(self, message, p):
        report = Report("Check Date")
        # todo check for how many years back the reforecast is done? Is it coded in the grib???
        # Check if the date is OK
        date = message["date"]
        # report.add(Ge(message["date"], 20060101))

        report.add(Eq((date / 10000).to_int(), message["year"]))
        report.add(Eq(((date % 10000) / 100).to_int(), message["month"]))
        report.add(Eq((date % 100).to_int(), message["day"]))

        return report

    # not registered in the lookup table
    def _statistical_process(self, message, p) -> Report:
        report = Report("Statistical Process")

        topd = message.get("typeOfProcessedData", int)

        if topd.value() in [0, 1]:  # Analysis, Forecast
            report.add(Eq(message["productDefinitionTemplateNumber"], 8, f"topd={topd}"))
        elif topd == 2:  # Analysis and forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 8, f"topd={topd}"))
        elif topd in [3, 4]:  # Control forecast products
            pass
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return report

        report.add(Eq(message["numberOfMissingInStatisticalProcess"], 0))
        report.add(Eq(message["typeOfTimeIncrement"], 2))
        # report.add(Eq(message["indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed"], 255))
        report.add(Eq(message["minuteOfEndOfOverallTimeInterval"], 0))
        report.add(Eq(message["secondOfEndOfOverallTimeInterval"], 0))

        report.add(Eq(message["numberOfTimeRange"], 1))

        if message["indicatorOfUnitForTimeRange"] == 11:
            # Six hourly is OK
            report.add(
                Eq(
                    message["lengthOfTimeRange"] * 6 + message["startStep"],
                    message["endStep"],
                )
            )

        elif message["indicatorOfUnitForTimeRange"] == 10:
            # Three hourly is OK
            report.add(
                Eq(
                    message["lengthOfTimeRange"] * 3 + message.get("startStep", int),
                    message.get("endStep", int)
                )
            )
        else:
            report.add(Eq(message["indicatorOfUnitForTimeRange"], 1))
            report.add(
                Eq(
                    message["lengthOfTimeRange"] + message.get("startStep", int),
                    message.get("endStep", int),
                )
            )

        return report

    # not registered in the lookup table
    def _check_range(self, message, p):
        report = Report("Range check")

        if self.check_limits:
            count = 0
            try:
                count = message.get_size("values")
            except Exception as e:
                report.add(Fail(f"Cannot get number of values: {e}"))
                return report

            report.add(Eq(message["numberOfDataPoints"], count))

            try:
                values = message.get_double_array("values")
            except Exception as e:
                report.add(Fail(f"Cannot get values: {e}"))
                return report

            n = count
            count = len(values)
            if n != count:
                report.add(Fail(f"Value count changed {count} -> {n}"))
                return report

            endStep = message.get("endStep", int)
            missing = message.get("missingValue", float)

            is_accumulated = message.get("typeOfStatisticalProcessing", int) == 1
            min_value, max_value = message.minmax()
            if endStep != 0 and is_accumulated:
                min_value /= endStep
                max_value /= endStep

            for entry in p["expected"]:
                if entry["key"] == "values":
                    mi1 = entry["min"][0]
                    mi2 = entry["min"][1]
                    ma1 = entry["max"][0]
                    ma2 = entry["max"][1]

                    if (
                        not message["bitMapIndicator"] == 0
                        and min_value != missing
                        and max_value != missing
                    ):
                        if min_value < mi1 or min_value > mi2:
                            report.add(
                                Fail(
                                    f"Minimum value {min_value} is not in range [{mi1}, {mi2}]"
                                )
                            )
                        else:
                            report.add(
                                Pass(
                                    f"Minimum value {min_value} is in range [{mi1}, {mi2}]"
                                )
                            )

                        if max_value < ma1 or max_value > ma2:
                            report.add(
                                Fail(
                                    f"Maximum value {max_value} is not in range [{ma1}, {ma2}]]"
                                )
                            )
                        else:
                            report.add(
                                Pass(
                                    f"Maximum value {max_value} is in range [{ma1}, {ma2}]"
                                )
                            )
        else:
            report.add("Check disabled. Use the option -L or --check_limits to enable it.")
        return report

    # not registered in the lookup table
    def _gaussian_grid(self, message):
        report = Report("Gaussian grid")

        tolerance = 1.0 / 1000000.0  # angular tolerance for grib2: micro degrees
        n = message["numberOfParallelsBetweenAPoleAndTheEquator"]  # This is the key N

        north = message.get("latitudeOfFirstGridPointInDegrees", float)
        south = message.get("latitudeOfLastGridPointInDegrees", float)

        west = message.get("longitudeOfFirstGridPointInDegrees", float)
        east = message.get("longitudeOfLastGridPointInDegrees", float)

        if Ne(n, self.last_n):
            try:
                self.values = get_gaussian_latitudes(n.value())
            except TypeError as e:
                raise e
            except Exception as e:
                report.add(
                    Fail(
                        f"Error: Cannot get gaussian latitudes for N{n.value()}, {str(e)}"
                    )
                )
                self.last_n = 0
                return report
            self.last_n = n

        # TODO
        if self.values is None:
            assert 0
            return report

        if self.values is not None:
            self.values[0] = np.rint(self.values[0] * 1e6) / 1e6

        report.add(
            EqDbl(north, self.values[0], tolerance)
            | EqDbl(south, -self.values[0], tolerance)
        )
        report.add(EqDbl(north, self.values[0], tolerance, "north == self.values[0]"))
        report.add(EqDbl(south, -self.values[0], tolerance, "south == -self.values[0]"))

        if message.is_missing("numberOfPointsAlongAParallel"):  # same as key Ni
            # If missing, this is a REDUCED gaussian grid
            MAXIMUM_RESOLUTION = 640
            report.add(Ne(message["PLPresent"], 0))  # TODO: check this
            report.add(EqDbl(west, 0.0, tolerance, "west == 0.0"))
            report.add(
                Le(
                    n,
                    MAXIMUM_RESOLUTION,
                    f"Gaussian number N (={n}) cannot exceed {MAXIMUM_RESOLUTION}",
                )
            )
        else:
            # REGULAR gaussian grid
            l_west = message["longitudeOfFirstGridPoint"]
            l_east = message["longitudeOfLastGridPoint"]
            parallel = message["numberOfPointsAlongAParallel"]
            we = message["iDirectionIncrement"]
            dwest = message.get("longitudeOfFirstGridPointInDegrees", float)
            deast = message.get("longitudeOfLastGridPointInDegrees", float)
            dwe = message.get("iDirectionIncrementInDegrees", float)
            # printf("parallel=%ld east=%ld west=%ld we=%ld",parallel,east,west,we)

            report.add(
                Eq(
                    parallel,
                    (l_east - l_west) / we + 1,
                    "parallel == (l_east - l_west) / we + 1",
                )
            )
            report.add(
                Lt(
                    ((deast - dwest) / dwe + 1 - parallel).abs(),
                    1e-10,
                    "abs((deast-dwest)/dwe + 1 - parallel) < 1e-10",
                )
            )
            report.add(Eq(message["PLPresent"], 0, "not message.get('PLPresent')"))

        report.add(Ne(message["Nj"], 0))

        if message["PLPresent"] != 0:
            count = message.get_size("pl")
            expected_lon2 = 0
            total = 0
            max_pl = 0
            numberOfValues = message["numberOfValues"]
            numberOfDataPoints = message["numberOfDataPoints"]

            pl = message.get_double_array("pl")

            report.add(
                AssertTrue(len(pl) == count, f"len(pl)({len(pl)}) == count({count})")
            )
            report.add(
                AssertTrue(len(pl) == n * 2, f"len(pl)({len(pl)}) == 2 * n({n})")
            )

            total = 0
            max_pl = pl[0]  # max elem of pl array = num points at equator

            for p in pl:
                total = total + p
                if p > max_pl:
                    max_pl = p

            # Do not assume maximum of pl array is 4N! not true for octahedral
            expected_lon2 = 360.0 - 360.0 / max_pl

            if not EqDbl(east, expected_lon2, tolerance):
                report.add(
                    Fail(
                        f"east actual={east} expected={expected_lon2} diff={expected_lon2-east}"
                    )
                )

            report.add(EqDbl(east, expected_lon2, tolerance, "expected_lon2 == east"))
            report.add(
                Eq(
                    message["numberOfDataPoints"],
                    total,
                    f"GAUSS numberOfValues={numberOfValues} numberOfDataPoints={numberOfDataPoints} sum(pl)={total}",
                )
            )
            report.add(Missing(message, "iDirectionIncrement"))
            report.add(Missing(message, "iDirectionIncrementInDegrees"))
            report.add(Eq(message["iDirectionIncrementGiven"], 0))
            report.add(Eq(message["jDirectionIncrementGiven"], 1))

        report.add(Eq(message["resolutionAndComponentFlags1"], 0))
        report.add(Eq(message["resolutionAndComponentFlags2"], 0))
        report.add(Eq(message["resolutionAndComponentFlags6"], 0))
        report.add(Eq(message["resolutionAndComponentFlags7"], 0))
        report.add(Eq(message["resolutionAndComponentFlags8"], 0))

        return report

    # not registered in the lookup table
    def _latlon_grid(self, message):
        report = Report("latlon grid")

        # tolerance = 1.0/1000000.0 # angular tolerance for grib2: micro degrees
        data_points = message["numberOfDataPoints"]
        meridian = message["numberOfPointsAlongAMeridian"]
        parallel = message["numberOfPointsAlongAParallel"]

        north = message["latitudeOfFirstGridPoint"]
        south = message["latitudeOfLastGridPoint"]
        west = message["longitudeOfFirstGridPoint"]
        east = message["longitudeOfLastGridPoint"]

        # ns= message["jDirectionIncrement"]
        # we= message["iDirectionIncrement"]

        dnorth = message.get("latitudeOfFirstGridPointInDegrees", float)
        dsouth = message.get("latitudeOfLastGridPointInDegrees", float)
        dwest = message.get("longitudeOfFirstGridPointInDegrees", float)
        deast = message.get("longitudeOfLastGridPointInDegrees", float)

        # dns = message.get("jDirectionIncrementInDegrees", float)
        # dwe = message.get("iDirectionIncrementInDegrees", float)

        if message["basicAngleOfTheInitialProductionDomain"] == 0:
            report.add(Missing(message, "subdivisionsOfBasicAngle"))
        else:
            # long basic    = get(h,"basicAngleOfTheInitialProductionDomain")
            # long division = get(h,"subdivisionsOfBasicAngle")
            report.add(Exists(message, "subdivisionsOfBasicAngle"))
            report.add(Ne(message["subdivisionsOfBasicAngle"], 0))

        if message.is_missing("subdivisionsOfBasicAngle"):
            report.add(Eq(message["basicAngleOfTheInitialProductionDomain"], 0))

        report.add(
            Eq(meridian * parallel, data_points, "meridian * parallel == data_points")
        )

        report.add(Eq(message["resolutionAndComponentFlags1"], 0))
        report.add(Eq(message["resolutionAndComponentFlags2"], 0))
        report.add(Eq(message["resolutionAndComponentFlags6"], 0))
        report.add(Eq(message["resolutionAndComponentFlags7"], 0))
        report.add(Eq(message["resolutionAndComponentFlags8"], 0))

        report.add(Eq(message["iDirectionIncrementGiven"], 1))
        report.add(Eq(message["jDirectionIncrementGiven"], 1))
        # https://jira.ecmwf.int/browse/SD-39816
        # 96-97 codeflag resolutionAndComponentFlags = 48 [00110000:(3=1) i direction increments given;(4=1) j direction increments given;(5=0)...
        report.add(Eq(message["resolutionAndComponentFlags"], 48))

        report.add(Eq(message["numberOfOctectsForNumberOfPoints"], 0))
        report.add(Eq(message["interpretationOfNumberOfPoints"], 0))

        if message["iScansNegatively"] != 0:
            tmp = east
            dtmp = deast

            east = west
            west = tmp

            deast = dwest
            dwest = dtmp

        if message["jScansPositively"] != 0:
            tmp = north
            dtmp = dnorth

            north = south
            south = tmp

            dnorth = dsouth
            dsouth = dtmp

        # GRIB2 requires longitudes are always positive */
        report.add(Ge(east, 0, "east >= 0"))
        report.add(Ge(west, 0, "west >= 0"))

        # printf("meridian=%ld north=%ld south=%ld ns=%ld ",meridian,north,south,ns)
        # printf("meridian=%ld north=%f south=%f ns=%f ",meridian,dnorth,dsouth,dns)
        # printf("parallel=%ld east=%ld west=%ld we=%ld ",parallel,east,west,we)
        # printf("parallel=%ld east=%f west=%f we=%f ",parallel,deast,dwest,dwe)

        return report

    # not registered in the lookup table
    def _check_packing(self, message):
        # ECC-1009: Warn if not using simple packing
        report = Report("Check packing")
        report.add(Eq(message["packingType"], "grid_simple"))
        return report

    # not registered in the lookup table
    def _check_validity_datetime(self, message):
        # If we just set the stepRange (for non-instantaneous fields) to its
        # current value, then this causes the validity date and validity time
        # keys to be correctly computed.
        # Then we can compare the previous (possibly wrongly coded) value with
        # the newly computed one

        report = Report("Check Validity Datetime")
        stepType = message.get("stepType", str)

        if stepType != "instant":  # not instantaneous
            # Check only applies to accumulated, max etc.
            # stepRange = message.get("stepRange", str)

            saved_validityDate = message["validityDate"]
            saved_validityTime = message["validityTime"]

            # message.set("stepRange", stepRange)

            validityDate = message["validityDate"]
            validityTime = message["validityTime"]
            if validityDate != saved_validityDate or validityTime != saved_validityTime:
                # print("warning: %s, field %d [%s]: invalid validity Date/Time (Should be %ld and %ld)" % (cfg['filename'], cfg['field'], cfg['param'], validityDate, validityTime))
                report.add(
                    Fail(
                        f"Invalid validity Date/Time (Should be {validityDate} and {validityTime})"
                    )
                )
                # cfg['warning'] += 1

        return report

    def _basic_checks_2(self, message, p):
        report = Report("Basic Checks 2")
        # 2 = analysis or forecast , 3 = control forecast, 4 = perturbed forecast
        report.add(IsIn(message["typeOfProcessedData"], [2, 3, 4]))
        return report

    def _basic_checks(self, message, p):
        report = Report("Basic checks")
        report.add(Eq(message["editionNumber"], 2))
        report.add(Missing(message, "reserved") | Eq(message["reserved"], 0))
        if self.check_validity:
            report.add(Eq(message["isMessageValid"], 1, "Use: grib_get -p isMessageValid file.grib to see the output if you get a failure here."))

        report.add(self._check_range(message, p))

        # reports += self._check_packing(message)

        # Section 1

        report.add(Ge(message["gribMasterTablesVersionNumber"], 4))
        report.add(Eq(message["significanceOfReferenceTime"], 1))

        report.add(Eq(message["minute"], 0))
        report.add(Eq(message["second"], 0))
        stream = message.get("stream", str)
        if stream != "moda":
            report.add(Ge(message["startStep"], 0))

        # TODO: validate local usage. Empty for now xxx
        # report.add(Eq(message, "section2.sectionLength", 5)

        # Section 3
        report.add(
            Eq(message["sourceOfGridDefinition"], 0)
        )  # Specified in Code table 3.1

        dtn = message["gridDefinitionTemplateNumber"]

        if dtn in [0, 1]:
            # dtn == 1: rotated latlon
            report.add(self._latlon_grid(message))
        elif dtn == 20:  # Polar stereographic projection
            report.add("Polar stereographic projection checks not implemented!")
        elif dtn == 30:  # Lambert conformal
            report.add("Lambert conformal projection checks not implemented!")
            # lambert_grid(h); # TODO xxx
            # print("warning: Lambert grid - geometry checking not implemented yet!")
            # report.add(Eq(message["scanningMode"], 64)) # M-F data used to have it wrong.. but it might depends on other projection set up as well!
            pass
        elif dtn == 40:  # gaussian grid (regular or reduced)
            report.add(self._gaussian_grid(message))
        else:
            report.add(Fail(f"Unsupported gridDefinitionTemplateNumber {dtn}"))
            return report

        # If there is no bitmap, this should be true
        # CHECK('eq(h,"bitMapIndicator",255)', eq(h,"bitMapIndicator",255))

        if message["bitMapIndicator"] == 255:
            report.add(Eq(message["numberOfValues"], message["numberOfDataPoints"]))
        else:
            report.add(Le(message["numberOfValues"], message["numberOfDataPoints"]))

        # Check values
        report.add(Eq(message["typeOfOriginalFieldValues"], 0))  # Floating point

        report.add(self._check_validity_datetime(message))

        # do not store empty values e.g. fluxes at step 0
        #    todo ?? now it's allowed in the code here!
        #    if not missing(h,"typeOfStatisticalProcessing"):
        #      CHECK('ne(h,"stepRange",0)', ne(h,"stepRange",0))

        return report

    def _daily_average(self, message, p):
        report = Report("Daily Average")
        start_step = message["startStep"]
        end_step = message["endStep"]
        report.add(Eq(start_step, end_step - 24))
        min_value, max_value = message.minmax()
        if end_step == 0:
            report.add(
                AssertTrue(
                    min_value == 0 and max_value() == 0,
                    "min_value == 0 and max_value == 0",
                )
            )
        report.add(self._statistical_process(message, p))

        return report

    def _from_start(self, message, p):
        report = Report("From Start")
        report.add(Eq(message["startStep"], 0))
        report.add(self._statistical_process(message, p))

        return report

    def _point_in_time(self, message, p):
        report = Report("Point in time")
        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]:  # Analysis, Forecast
            pass
        elif topd == 2:  # Analysis and forecast products
            report.add(
                Eq(message["productDefinitionTemplateNumber"], 0, f"topd={topd}")
            )
        elif topd == 3:  # Control forecast products
            report.add(Eq(message["perturbationNumber"], 0, f"topd={topd}"))
            report.add(Ne(message["numberOfForecastsInEnsemble"], 0, f"topd={topd}"))
        elif topd == 4:  # Perturbed forecast products
            report.add(Ne(message["perturbationNumber"], 0, f"topd={topd}"))
            report.add(Ne(message["numberOfForecastsInEnsemble"], 0, f"topd={topd}"))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        return report

    def _given_thickness(self, message, p):
        report = Report("Given thickness")
        report.add(Ne(message["typeOfSecondFixedSurface"], 255))
        report.add(Exists(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Exists(message, "scaledValueOfSecondFixedSurface"))

        report.add(Ne(message["typeOfFirstFixedSurface"], 255))
        report.add(Exists(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Exists(message, "scaledValueOfFirstFixedSurface"))
        return report

    def _has_bitmap(self, message, p):
        report = Report("Has bitmap")
        report.add(Eq(message["bitMapIndicator"], 0))
        return report

    def _has_soil_layer(self, message, p):
        report = Report("Has soil layer")
        report.add(Eq(message["topLevel"], message["bottomLevel"] - 1))
        report.add(Le(message["level"], 14))  # max in UERRA
        return report

    def _has_soil_level(self, message, p):
        report = Report("Has soil level")
        report.add(Eq(message["topLevel"], message["bottomLevel"]))
        report.add(Le(message["level"], 14))  # max in UERRA
        return report

    def _height_level(self, message, p):
        report = Report("Height level")
        return report

    def _given_level(self, message, p):
        report = Report("Given level")
        report.add(Ne(message["typeOfFirstFixedSurface"], 255))
        report.add(Exists(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Exists(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message["typeOfSecondFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return report

    def _potential_temperature_level(self, message, p):
        report = Report("Potential temperature level")
        report.add(
            Eq(
                message["level"],
                320,
                f'invalid potential temperature level {message["level"]}',
            )
        )
        return report

    def _potential_vorticity_level(self, message, p):
        report = Report("Potential vorticity level")
        report.add(
            Eq(
                message["level"],
                2,
                f'invalid potential vorticity level {message["level"]}',
            )
        )
        return report

    def _predefined_level(self, message, p):
        report = Report("Predefined level")
        report.add(Ne(message["typeOfFirstFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Missing(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message["typeOfSecondFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return report

    def _predefined_thickness(self, message, p):
        report = Report("Predefined thickness")
        report.add(Ne(message["typeOfFirstFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Missing(message, "scaledValueOfFirstFixedSurface"))
        report.add(Ne(message["typeOfSecondFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return report

    def _resolution_s2s(self, message, p):
        report = Report("Resolution S2S")
        report.add(Eq(message["iDirectionIncrement"], 1500000))
        report.add(Eq(message["jDirectionIncrement"], 1500000))
        return report

    def _resolution_s2s_ocean(self, message, p):
        report = Report("Resolution S2S Ocean")
        report.add(Eq(message["iDirectionIncrement"], 1000000))
        report.add(Eq(message["jDirectionIncrement"], 1000000))
        return report

    def _since_prev_pp(self, message, p):
        report = Report("Since previous post-processing")
        report.add(Eq(message["indicatorOfUnitForTimeRange"], 1))
        report.add(
            Eq(message["endStep"], message["startStep"] + message["lengthOfTimeRange"])
        )
        report.add(self._statistical_process(message, p))
        return report

    def _six_hourly(self, message, p):
        report = Report("Six hourly")
        if message["indicatorOfUnitForTimeRange"] == 11:
            report.add(Eq(message["lengthOfTimeRange"], 1))
        else:
            report.add(Eq(message["lengthOfTimeRange"], 6))
        report.add(Eq(message["endStep"], message["startStep"] + 6))

        report.add(self._statistical_process(message, p))
        return report

    def _three_hourly(self, message, p):
        report = Report("Three hourly")
        if message["indicatorOfUnitForTimeRange"] == 11:
            report.add(Eq(message["lengthOfTimeRange"], 1))
        else:
            report.add(Eq(message["lengthOfTimeRange"], 3))
        report.add(Eq(message["endStep"], message["startStep"] + 3))

        report.add(self._statistical_process(message, p))
        return report
