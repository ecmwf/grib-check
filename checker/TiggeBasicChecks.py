from CheckEngine import CheckEngine
from LookupTable import SimpleLookupTable
from Test import Test
from Grib import get_gaussian_latitudes
from Message import Message
from Assert import Ge, Le, Ne, Eq, Exists, Missing, Fail, AssertTrue, IsIn, EqDbl
from Report import Report
import numpy as np
import logging


class TiggeBasicChecks(CheckEngine):
    class TiggeTest(Test):
        def __init__(self, message: Message, parameter: dict, check_map: dict):
            self.logger = logging.getLogger(__class__.__name__)
            assert parameter is not None
            assert message is not None
            assert check_map is not None

            self.__message = message
            self.__parameter = parameter
            self.__check_map = check_map

        def run(self) -> Report:
            data = self.__parameter
            report = Report(f'Checks defined in parameter "{data['name']}"')
            for check_func in data["checks"]:
                check_reports = self.__check_map[check_func](self.__message, data)
                merged_report = Report(f'{check_func}')
                for check_report in check_reports:
                    merged_report.add(check_report)


                report.add(merged_report)

            return report


    def __init__(self, param_file=None, valueflg=False):
        self.logger = logging.getLogger(__class__.__name__)
        self.__check_map = {
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
        }
        self.last_n = 0
        self.values = None
        self.valueflg = valueflg

        parameters = SimpleLookupTable(param_file if param_file is not None else"checker/TiggeParameters.json")
        super().__init__(tests=parameters)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        assert parameters is not None
        return self.TiggeTest(message, parameters, self.__check_map)

    # not registered in the lookup table
    def _statistical_process(self, message, p):
        report = Report(f"{__class__.__name__}.statistical_process")

        topd = message.get("typeOfProcessedData", int)

        if topd.value() in [0, 1]: # Analysis, Forecast
            pass
        elif topd == 2: # Analysis and forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 8))
        elif topd in [3, 4]: # Control forecast products
            pass
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return [report]

        report.add(Eq(message["numberOfTimeRange"], 1))
        report.add(Eq(message["numberOfMissingInStatisticalProcess"], 0))
        report.add(Eq(message["typeOfTimeIncrement"], 2))
        # report.add(Eq(message["indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed"], 255))
        report.add(Eq(message["minuteOfEndOfOverallTimeInterval"], 0))
        report.add(Eq(message["secondOfEndOfOverallTimeInterval"], 0))

        if message["indicatorOfUnitForTimeRange"] == 11:
            # Six hourly is OK
            report.add(Eq(message["lengthOfTimeRange"] * 6 + message["startStep"], message["endStep"]))

        elif message["indicatorOfUnitForTimeRange"] == 10:
            # Three hourly is OK
            report.add(Eq(message["lengthOfTimeRange"] * 3 + message["startStep"], message["endStep"]))
        else:
            report.add(Eq(message["indicatorOfUnitForTimeRange"], 1))
            report.add(Eq(message["lengthOfTimeRange"] + message["startStep"], message["endStep"]))

        return [report]

    # not registered in the lookup table
    def _check_range(self, message, p):
        report = Report("Range check")

        # TODO:: Enable only if valueflg = 1
        
        # See ECC-437
        missing = message.get("missingValue", float)
        min_value, max_value = message.minmax()
        if not message["bitMapIndicator"] == 0 and min_value == missing and max_value == missing:
            if min_value < p['min1'] or min_value > p['min2']: 
                min1 = min_value if min_value < p['min1'] else p['min1']
                min2 = min_value if min_value > p['min2'] else p['min2']
                report.add(Fail(f"Missing value {min_value} is not in range [{p['min1']},{p['min2']}] => [{min1},{min2}]"))

            if max_value < p['max1'] or max_value > p['max2']:
                max1 = max_value if max_value < p['max1'] else p['max1']
                max2 = max_value if max_value > p['max2'] else p['max2']
                report.add(Fail(f"Missing value {max_value} is not in range [{p['max1']},{p['max2']}] => [{max1},{max2}]"))
        return [report]

    # not registered in the lookup table
    def _gaussian_grid(self, message):
        report = Report("Gaussian grid")

        tolerance = 1.0/1000000.0 # angular tolerance for grib2: micro degrees
        n = message["numberOfParallelsBetweenAPoleAndTheEquator"] # This is the key N

        north = message.get("latitudeOfFirstGridPointInDegrees", float)
        south = message.get("latitudeOfLastGridPointInDegrees", float)

        west = message.get("longitudeOfFirstGridPointInDegrees", float)
        east = message.get("longitudeOfLastGridPointInDegrees", float)

        if n.value() != self.last_n:
            try:
                self.values = get_gaussian_latitudes(n.value())
            except TypeError as e:
                raise e
            except Exception as e:
                # print("%s, field %d [%s]: cannot get gaussian latitudes for N%ld: %s" % (cfg['filename'], cfg['field'], cfg['param'],n, str(e)))
                # cfg['error'] += 1
                # report.error(f"Cannot get gaussian latitudes for N{n}")
                report.add(Fail(f"Error: Cannot get gaussian latitudes for N{n.value()}, {str(e)}"))
                self.last_n = 0
                return [report]
            self.last_n = n

        # TODO
        if self.values is None:
            assert(0)
            return [report]

        if self.values is not None:
            self.values[0] = np.rint(self.values[0] * 1e6) / 1e6


        # if not DBL_EQUAL(north, self.values[0], tolerance) or not DBL_EQUAL(south, -self.values[0], tolerance):
        # if (EqDbl(north, self.values[0], tolerance) | EqDbl(south, -self.values[0], tolerance)).status():
        #     report.add(Fail(f"N={n} north={north} south={south} v(=gauss_lat[0])={self.values[0]} north-v={north-self.values[0]} south-v={south+self.values[0]}"))
        report.add(EqDbl(north, self.values[0], tolerance) | EqDbl(south, -self.values[0], tolerance))

        report.add(EqDbl(north, self.values[0], tolerance, "north == self.values[0]"))
        report.add(EqDbl(south, -self.values[0], tolerance, "south == -self.values[0]"))

        if(message.is_missing("numberOfPointsAlongAParallel")): # same as key Ni 
            # If missing, this is a REDUCED gaussian grid 
            MAXIMUM_RESOLUTION = 640
            # report.add(Eq(message["PLPresent"], True)) # TODO: check this
            report.add(EqDbl(west, 0.0, tolerance, "west == 0.0"))
            report.add(AssertTrue(n <= MAXIMUM_RESOLUTION, f"Gaussian number N (={n}) cannot exceed {MAXIMUM_RESOLUTION}"))
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

            report.add(AssertTrue(parallel == (l_east-l_west)/we + 1, "parallel == (l_east-l_west)/we + 1"))
            report.add(AssertTrue(abs((deast-dwest)/dwe + 1 - parallel) < 1e-10, "abs((deast-dwest)/dwe + 1 - parallel) < 1e-10"))
            report.add(AssertTrue(not message["PLPresent"], "not message.get('PLPresent')"))

        report.add(Ne(message["Nj"], 0))

        if message["PLPresent"]:
            i = 0
            count = message.get_size("pl")
            expected_lon2 = 0
            total = 0
            max_pl = 0
            numberOfValues = message["numberOfValues"]
            numberOfDataPoints = message["numberOfDataPoints"]

            pl = message.get_double_array("pl")

            if len(pl) != count:
                print("len(pl)=%ld count=%ld" % (len(pl), count))

            report.add(AssertTrue(len(pl) == count, "len(pl) == count"))
            report.add(AssertTrue(len(pl) == n * 2, "len(pl) == 2*n"))

            total = 0;
            max_pl = pl[0]; #  max elem of pl array = num points at equator

            for p in pl:
                total = total + p
                if p > max_pl:
                    max_pl = p


            # Do not assume maximum of pl array is 4N! not true for octahedral

            expected_lon2 = 360.0 - 360.0/max_pl;
            # if not DBL_EQUAL(expected_lon2, east, tolerance):
            if not EqDbl(east, expected_lon2, tolerance).status():
                report.add(Fail(f"east actual={east} expected={expected_lon2} diff={expected_lon2-east}"))

            report.add(EqDbl(east, expected_lon2, tolerance, "expected_lon2 == east"))

            if numberOfDataPoints != total:
                print("GAUSS numberOfValues=%ld numberOfDataPoints=%ld sum(pl)=%ld" % (
                        numberOfValues,
                        numberOfDataPoints,
                        total))

            # report.add(AssertTrue(numberOfDataPoints == total, "numberOfDataPoints == total"))
            report.add(Eq(message["numberOfDataPoints"], total))

            report.add(Missing(message, "iDirectionIncrement"))
            report.add(Missing(message, "iDirectionIncrementInDegrees"))

            report.add(Eq(message["iDirectionIncrementGiven"], 0))
            report.add(Eq(message["jDirectionIncrementGiven"], 1))

        report.add(Eq(message["resolutionAndComponentFlags1"], 0))
        report.add(Eq(message["resolutionAndComponentFlags2"], 0))
        report.add(Eq(message["resolutionAndComponentFlags6"], 0))
        report.add(Eq(message["resolutionAndComponentFlags7"], 0))
        report.add(Eq(message["resolutionAndComponentFlags8"], 0))

        return [report]


    # not registered in the lookup table
    def _latlon_grid(self, message):
        report = Report("Latlon grid")

        tolerance = 1.0/1000000.0; # angular tolerance for grib2: micro degrees
        data_points = message["numberOfDataPoints"]
        meridian = message["numberOfPointsAlongAMeridian"]
        parallel = message["numberOfPointsAlongAParallel"]

        north = message["latitudeOfFirstGridPoint"]
        south = message["latitudeOfLastGridPoint"]
        west = message["longitudeOfFirstGridPoint"]
        east = message["longitudeOfLastGridPoint"]

        ns= message["jDirectionIncrement"]
        we= message["iDirectionIncrement"]

        dnorth = message.get("latitudeOfFirstGridPointInDegrees", float)
        dsouth = message.get("latitudeOfLastGridPointInDegrees", float)
        dwest = message.get("longitudeOfFirstGridPointInDegrees", float)
        deast = message.get("longitudeOfLastGridPointInDegrees", float)

        dns = message.get("jDirectionIncrementInDegrees", float)
        dwe = message.get("iDirectionIncrementInDegrees", float)

        if message["basicAngleOfTheInitialProductionDomain"] == 0:
            report.add(Missing(message, "subdivisionsOfBasicAngle"))    
        else:
            # long basic    = get(h,"basicAngleOfTheInitialProductionDomain")
            # long division = get(h,"subdivisionsOfBasicAngle")
            report.add(Exists(message, "subdivisionsOfBasicAngle"))
            report.add(Ne(message["subdivisionsOfBasicAngle"], 0))

        if message.is_missing("subdivisionsOfBasicAngle"):
            report.add(Eq(message["basicAngleOfTheInitialProductionDomain"], 0))

        report.add(Eq(meridian * parallel, data_points, "meridian * parallel == data_points"))

        report.add(Eq(message["resolutionAndComponentFlags1"], 0))
        report.add(Eq(message["resolutionAndComponentFlags2"], 0))
        report.add(Eq(message["resolutionAndComponentFlags6"], 0))
        report.add(Eq(message["resolutionAndComponentFlags7"], 0))
        report.add(Eq(message["resolutionAndComponentFlags8"], 0))

        report.add(Eq(message["iDirectionIncrementGiven"], 1))
        report.add(Eq(message["jDirectionIncrementGiven"], 1))

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

        #printf("meridian=%ld north=%ld south=%ld ns=%ld ",meridian,north,south,ns)
        #printf("meridian=%ld north=%f south=%f ns=%f ",meridian,dnorth,dsouth,dns)
        #printf("parallel=%ld east=%ld west=%ld we=%ld ",parallel,east,west,we)
        #printf("parallel=%ld east=%f west=%f we=%f ",parallel,deast,dwest,dwe)

        return [report]

    # not registered in the lookup table
    def _check_packing(self, message):
        # ECC-1009: Warn if not using simple packing
        report = Report("Check packing")
        report.add(Eq(message["packingType"], "grid_simple"))
        return [report]

    # not registered in the lookup table
    def _check_validity_datetime(self, message):
        # If we just set the stepRange (for non-instantaneous fields) to its
        # current value, then this causes the validity date and validity time
        # keys to be correctly computed.
        # Then we can compare the previous (possibly wrongly coded) value with
        # the newly computed one

        report = Report()
        stepType = message.get("stepType", str)

        if stepType != "instant": # not instantaneous
            # Check only applies to accumulated, max etc.
            stepRange = message.get("stepRange", str)

            saved_validityDate = message["validityDate"]
            saved_validityTime = message["validityTime"]

            message.set("stepRange", stepRange)

            validityDate = message["validityDate"]
            validityTime = message["validityTime"]
            if validityDate!=saved_validityDate or validityTime!=saved_validityTime:
                # print("warning: %s, field %d [%s]: invalid validity Date/Time (Should be %ld and %ld)" % (cfg['filename'], cfg['field'], cfg['param'], validityDate, validityTime))
                report.add(Fail(f"Invalid validity Date/Time (Should be {validityDate} and {validityTime})"))
                # cfg['warning'] += 1

        return [report]
    

    def _basic_checks_2(self, message, p):
        report = Report()
        # 2 = analysis or forecast , 3 = control forecast, 4 = perturbed forecast
        report.add(IsIn(message["typeOfProcessedData"], [2, 3, 4]))
        return [report]

    def _basic_checks(self, message, p):
        reports = list()
        report = Report()
        report.add(Eq(message["editionNumber"], 2))
        report.add(Missing(message, "reserved") | Eq(message["reserved"], 0))

        if self.valueflg:
            values_report = Report("Check values")
            count = 0
            try:
                count = message.get_size("values")
            except Exception as e:
                values_report.error(Fail(f"Cannot get number of values: {e}")) 
                return [values_report]

            values_report.add(Eq(message["numberOfDataPoints"], count))

            try:
                values = message.get_double_array("values")
            except Exception as e:
                values_report.error(Fail(f"Cannot get values: {e}"))
                return [values_report]

            n = count
            count = len(values)
            if n != count:
                values_report.add(Fail(f"Value count changed {count} -> {n}"))
                return [values_report]
            
            reports += [values_report]
        
        
        # reports += self._check_packing(message)

        # Section 1

        report.add(Ge(message["gribMasterTablesVersionNumber"], 4))
        report.add(Eq(message["versionNumberOfGribLocalTables"], 0))
        report.add(Eq(message["significanceOfReferenceTime"], 1))

        report.add(Eq(message["minute"], 0))
        report.add(Eq(message["second"], 0))
        report.add(Ge(message["startStep"], 0))

        # TODO: validate local usage. Empty for now xxx
        # report.add(Eq(message, "section2.sectionLength", 5)

        # Section 3
        report.add(Eq(message["sourceOfGridDefinition"], 0)) # Specified in Code table 3.1

        dtn = message["gridDefinitionTemplateNumber"]

        if dtn in [0, 1]:
            # dtn == 1: rotated latlon
            reports += self._latlon_grid(message)
        elif dtn == 30: #Lambert conformal
            # lambert_grid(h); # TODO xxx
            # print("warning: Lambert grid - geometry checking not implemented yet!")
            # report.add(Eq(message["scanningMode"], 64)) # M-F data used to have it wrong.. but it might depends on other projection set up as well!
            pass
        elif dtn == 40: # gaussian grid (regular or reduced)
            reports += self._gaussian_grid(message)
        else:
            report.add(Fail(f"Unsupported gridDefinitionTemplateNumber {dtn}"))
            # print("%s, field %d [%s]: Unsupported gridDefinitionTemplateNumber %ld" %
            #         (cfg['filename'], cfg['field'], cfg['param'], get(h,"gridDefinitionTemplateNumber")))
            # cfg['error'] += 1
            return [report]

        # If there is no bitmap, this should be true
        # CHECK('eq(h,"bitMapIndicator",255)', eq(h,"bitMapIndicator",255))

        if message["bitMapIndicator"] == 255:
            report.add(Eq(message["numberOfValues"], message["numberOfDataPoints"]))
        else:
            report.add(Le(message["numberOfValues"], message["numberOfDataPoints"]))

        # Check values 
        report.add(Eq(message["typeOfOriginalFieldValues"], 0)) # Floating point

        reports += self._check_validity_datetime(message)

        # do not store empty values e.g. fluxes at step 0
        #    todo ?? now it's allowed in the code here!
        #    if not missing(h,"typeOfStatisticalProcessing"):
        #      CHECK('ne(h,"stepRange",0)', ne(h,"stepRange",0))
        
        return reports + [report]

    def _daily_average(self, message, p):
        reports = list()
        report = Report()
        start_step = message["startStep"]
        end_step = message["endStep"]
        report.add(AssertTrue(start_step == end_step - 24, "startStep == endStep - 24"))
        min_value, max_value = message.minmax()
        if end_step == 0:
            report.add(AssertTrue(min_value == 0 and max_value() == 0, "min_value == 0 and max_value == 0"))
            pass
        else:
            reports += self._check_range(message, p)

        reports += self._statistical_process(message ,p)
        reports = [report] + reports

        return reports

    def _from_start(self, message, p):
        reports = list()
        report = Report()
        report.add(Eq(message["startStep"], 0))

        reports += self._statistical_process(message, p)
        reports = [report] + reports

        return reports

    def _point_in_time(self, message, p):
        report = Report(__class__.__name__)
        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]: # Analysis, Forecast
            pass
        elif topd == 2: # Analysis and forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 0))
        elif topd == 3: # Control forecast products
            report.add(Eq(message["perturbationNumber"], 0))
            report.add(Ne(message["numberOfForecastsInEnsemble"], 0))
        elif topd == 4: #Perturbed forecast products
            report.add(Ne(message["perturbationNumber"], 0))
            report.add(Ne(message["numberOfForecastsInEnsemble"], 0))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        return [report]

    def _given_thickness(self, message, p):
        report = Report()
        report.add(Ne(message["typeOfSecondFixedSurface"], 255))
        report.add(Exists(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Exists(message, "scaledValueOfSecondFixedSurface"))

        report.add(Ne(message["typeOfFirstFixedSurface"], 255))
        report.add(Exists(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Exists(message, "scaledValueOfFirstFixedSurface"))
        return [report]

    def _has_bitmap(self, message, p):
        report = Report()
        report.add(Eq(message["bitMapIndicator"], 0))
        return [report]

    def _has_soil_layer(self, message, p):
        report = Report()
        report.add(AssertTrue(message["topLevel"] == message["bottomLevel"] - 1, "topLevel == bottomLevel - 1"))
        report.add(Le(message["level"], 14)) # max in UERRA
        return [report]

    def _has_soil_level(self, message, p):
        report = Report()
        report.add(AssertTrue(message["topLevel"] == message["bottomLevel"], "topLevel == bottomLevel"))
        report.add(Le(message["level"], 14)) # max in UERRA
        return [report]

    def _height_level(self, message, p):
        report = Report()
        return [report]

    def _given_level(self, message, p):
        report = Report()
        report.add(Ne(message["typeOfFirstFixedSurface"], 255))
        report.add(Exists(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Exists(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message["typeOfSecondFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return [report]

    def _potential_temperature_level(self, message, p):
        report = Report()
        report.add(Eq(message["level"], 320, f'invalid potential temperature level {message["level"]}' ))
        return [report]

    def _potential_vorticity_level(self, message, p):
        report = Report()
        report.add(Eq(message["level"], 2, f'invalid potential vorticity level {message["level"]}'))
        return [report]

    def _predefined_level(self, message, p):
        report = Report()
        report.add(Ne(message["typeOfFirstFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Missing(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message["typeOfSecondFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return [report]

    def _predefined_thickness(self, message, p):
        report = Report()
        report.add(Ne(message["typeOfFirstFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Missing(message, "scaledValueOfFirstFixedSurface"))
        report.add(Ne(message["typeOfSecondFixedSurface"], 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return [report]

    def _pressure_level(self, message, p):
        report = Report()
        levels = [1000, 200, 250, 300, 500, 700, 850, 925, 50]
        report.add(IsIn(message["level"], levels, 'invalid pressure level'))
        return [report]

    def _resolution_s2s(self, message, p):
        report = Report()
        report.add(Eq(message["iDirectionIncrement"], 1500000))
        report.add(Eq(message["jDirectionIncrement"], 1500000))
        return [report]

    def _resolution_s2s_ocean(self, message, p):
        report = Report()
        report.add(Eq(message["iDirectionIncrement"], 1000000))
        report.add(Eq(message["jDirectionIncrement"], 1000000))
        return [report]

    def _since_prev_pp(self, message, p):
        report = Report()
        report.add(Eq(message["indicatorOfUnitForTimeRange"], 1))
        report.add(AssertTrue(message["endStep"] == message["startStep"] + message["lengthOfTimeRange"], "endStep == startStep + lengthOfTimeRange"))

        stats_report = self._statistical_process(message, p)
        check_report = self._check_range(message, p)
        return [report] + stats_report + check_report

    def _six_hourly(self, message, p):
        report = Report()
        if message["indicatorOfUnitForTimeRange"] == 11:
            report.add(Eq(message["lengthOfTimeRange"], 1))
        else:
            report.add(Eq(message["lengthOfTimeRange"], 6))
        report.add(AssertTrue(message["endStep"] == message["startStep"] + 6, "endStep == startStep + 6"))

        stats_report = self._statistical_process(message, p)
        check_report = self._check_range(message, p)
        return [report] + stats_report + check_report

    def _three_hourly(self, message, p):
        report = Report()
        if message["indicatorOfUnitForTimeRange"] == 11:
            report.add(Eq(message["lengthOfTimeRange"], 1))
        else:
            report.add(Eq(message["lengthOfTimeRange"], 3))
        report.add(AssertTrue(message["endStep"] == message["startStep"] + 3, "endStep == startStep + 3"))

        stats_report = self._statistical_process(message, p)
        check_report = self._check_range(message, p)
        return [report] + stats_report + check_report
