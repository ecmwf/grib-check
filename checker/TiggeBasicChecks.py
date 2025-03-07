from CheckEngine import CheckEngine
from LookupTable import SimpleLookupTable
from Test import Test, TiggeTest
from Grib import get_gaussian_latitudes
from Message import Message
from Assert import Le, Ne, Eq, Exists, Missing, Fail, Pass, AssertTrue, IsIn, DBL_EQUAL
from Report import Report
import numpy as np
import logging
import math


class TiggeBasicChecks(CheckEngine):
    def __init__(self, param_file=None):
        self.logger = logging.getLogger(__class__.__name__)
        self.__check_map = {
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



        parameters = SimpleLookupTable(param_file if param_file is not None else"checker/TiggeParameters.json")
        super().__init__(tests=parameters)

    def _create_test(self, message: Message, parameters: dict) -> Test:
        assert parameters is not None
        return TiggeTest(message, parameters, self.__check_map)

    # not registered in the lookup table
    def _statistical_process(self, message, p):
        report = Report(f"{__class__.__name__}.statistical_process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1]: # Analysis, Forecast
            pass
        elif topd == 2: # Analysis and forecast products
            report.add(Eq(message, "productDefinitionTemplateNumber", 8))
        elif topd in [3, 4]: # Control forecast products
            pass
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return [report]

        report.add(Eq(message, "numberOfTimeRange", 1))
        report.add(Eq(message, "numberOfMissingInStatisticalProcess", 0))
        report.add(Eq(message, "typeOfTimeIncrement", 2))
        # report.add(Eq(message, "indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed", 255))
        report.add(Eq(message, "minuteOfEndOfOverallTimeInterval", 0))
        report.add(Eq(message, "secondOfEndOfOverallTimeInterval", 0))

        if message.get("indicatorOfUnitForTimeRange") == 11:
            # Six hourly is OK
            report.add(AssertTrue(message.get("lengthOfTimeRange")*6 + message.get("startStep") == message.get("endStep"), "lengthOfTimeRange*6 + startStep == endStep"))

        elif message.get("indicatorOfUnitForTimeRange") == 10:
            # Three hourly is OK
            report.add(AssertTrue(message.get("lengthOfTimeRange")*3 + message.get("startStep") == message.get("endStep"), "lengthOfTimeRange*3 + startStep == endStep"))
        else:
            report.add(Eq(message, "indicatorOfUnitForTimeRange", 1))
            report.add(AssertTrue(message.get("lengthOfTimeRange") + message.get("startStep") == message.get("endStep"), "lengthOfTimeRange + startStep == endStep"))

        return [report]

    # not registered in the lookup table
    def _check_range(self, message, p):
        report = Report("Range check")

        # TODO:: Enable only if valueflg = 1
        
        # See ECC-437
        missing = message.get("missingValue", float)
        min_value, max_value = message.minmax()
        if not message.get("bitMapIndicator") == 0 and min_value == missing and max_value == missing:
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
    def _gaussian_grid(self, message, p):
        report = Report()

        tolerance = 1.0/1000000.0; # angular tolerance for grib2: micro degrees
        n = message.get("numberOfParallelsBetweenAPoleAndTheEquator") # This is the key N

        north = message.get("latitudeOfFirstGridPointInDegrees", float)
        south = message.get("latitudeOfLastGridPointInDegrees", float)

        west = message.get("longitudeOfFirstGridPointInDegrees", float)
        east = message.get("longitudeOfLastGridPointInDegrees", float)

        if n != self.last_n:
            try:
                self.values = get_gaussian_latitudes(n)
            except:
                # print("%s, field %d [%s]: cannot get gaussian latitudes for N%ld: %s" % (cfg['filename'], cfg['field'], cfg['param'],n, str(e)))
                # cfg['error'] += 1
                report.error(f"Cannot get gaussian latitudes for N{n}")
                self.last_n = 0
                return
            self.last_n = n;

        # TODO
        if self.values is None:
            assert(0)
            return

        if self.values is not None:
            self.values[0] = np.rint(self.values[0] * 1e6) / 1e6;


        if not DBL_EQUAL(north, self.values[0], tolerance) or not DBL_EQUAL(south, -self.values[0], tolerance):
            report.add(Fail(f"N={n} north={north} south={south} v(=gauss_lat[0])={self.values[0]} north-v={north-self.values[0]} south-v={south+self.values[0]}"))

        report.add(AssertTrue(DBL_EQUAL(north, self.values[0], tolerance), "north == self.values[0]"))
        report.add(AssertTrue(DBL_EQUAL(south, -self.values[0], tolerance), "south == -self.values[0]"))

        if(message.is_missing("numberOfPointsAlongAParallel")): # same as key Ni 
            # If missing, this is a REDUCED gaussian grid 
            MAXIMUM_RESOLUTION = 640;
            report.add(Eq(message, "PLPresent", True))
            report.add(AssertTrue(DBL_EQUAL(west, 0.0, tolerance), "west == 0.0"))
            report.add(AssertTrue(n <= MAXIMUM_RESOLUTION, f"Gaussian number N (={n}) cannot exceed {MAXIMUM_RESOLUTION}"))
        else:
            # REGULAR gaussian grid 
            l_west = message.get("longitudeOfFirstGridPoint")
            l_east = message.get("longitudeOfLastGridPoint")
            parallel = message.get("numberOfPointsAlongAParallel")
            we = message.get("iDirectionIncrement")
            dwest = message.get("longitudeOfFirstGridPointInDegrees", float)
            deast = message.get("longitudeOfLastGridPointInDegrees", float)
            dwe = message.get(h,"iDirectionIncrementInDegrees", float)
            # printf("parallel=%ld east=%ld west=%ld we=%ld",parallel,east,west,we)

            report.add(AssertTrue(parallel == (l_east-l_west)/we + 1, "parallel == (l_east-l_west)/we + 1"))
            report.add(AssertTrue(abs((deast-dwest)/dwe + 1 - parallel) < 1e-10, "abs((deast-dwest)/dwe + 1 - parallel) < 1e-10"))
            report.add(AssertTrue(not message.get("PLPresent"), "not message.get('PLPresent')"))

        report.add(Ne(message, "Nj", 0))

        if message.get("PLPresent"):
            i = 0
            count = message.get_size("pl")
            expected_lon2 = 0
            total = 0
            max_pl = 0
            numberOfValues = message.get("numberOfValues")
            numberOfDataPoints = message.get("numberOfDataPoints")

            pl = message.get_double_array("pl")

            if len(pl) != count:
                print("len(pl)=%ld count=%ld" % (len(pl), count))

            report.add(AssertTrue(len(pl) == count, "len(pl) == count"))
            report.add(AssertTrue(len(pl) == 2*n, "len(pl) == 2*n"))

            total = 0;
            max_pl = pl[0]; #  max elem of pl array = num points at equator

            for p in pl:
                total = total + p
                if p > max_pl:
                    max_pl = p


            # Do not assume maximum of pl array is 4N! not true for octahedral

            expected_lon2 = 360.0 - 360.0/max_pl;
            if not DBL_EQUAL(expected_lon2, east, tolerance):
                report.add(Fail(f"east actual={east} expected={expected_lon2} diff={expected_lon2-east}"))

            report.add(AssertTrue(DBL_EQUAL(expected_lon2, east, tolerance), "DBL_EQUAL(expected_lon2, east, tolerance)"))

            if numberOfDataPoints != total:
                print("GAUSS numberOfValues=%ld numberOfDataPoints=%ld sum(pl)=%ld" % (
                        numberOfValues,
                        numberOfDataPoints,
                        total))

            report.add(AssertTrue(numberOfDataPoints == total, "numberOfDataPoints == total"))

            report.add(Missing(message, "iDirectionIncrement"))
            report.add(Missing(message, "iDirectionIncrementInDegrees"))

            report.add(Eq(message, "iDirectionIncrementGiven", 0))
            report.add(Eq(message, "jDirectionIncrementGiven", 1))

        report.add(Eq(message, "resolutionAndComponentFlags1", 0))
        report.add(Eq(message, "resolutionAndComponentFlags2", 0))
        report.add(Eq(message, "resolutionAndComponentFlags6", 0))
        report.add(Eq(message, "resolutionAndComponentFlags7", 0))
        report.add(Eq(message, "resolutionAndComponentFlags8", 0))

        return [report]


    # not registered in the lookup table
    def _latlon_grid(self, message, p):
        report = Report()

        tolerance = 1.0/1000000.0; # angular tolerance for grib2: micro degrees
        data_points = message.get("numberOfDataPoints")
        meridian = message.get("numberOfPointsAlongAMeridian")
        parallel = message.get("numberOfPointsAlongAParallel")

        north = message.get("latitudeOfFirstGridPoint")
        south = message.get("latitudeOfLastGridPoint")
        west = message.get("longitudeOfFirstGridPoint")
        east = message.get("longitudeOfLastGridPoint")

        ns= message.get("jDirectionIncrement")
        we= message.get("iDirectionIncrement")

        dnorth = message.get("latitudeOfFirstGridPointInDegrees", float)
        dsouth = message.get("latitudeOfLastGridPointInDegrees", float)
        dwest = message.get("longitudeOfFirstGridPointInDegrees", float)
        deast = message.get("longitudeOfLastGridPointInDegrees", float)

        dns = message.get("jDirectionIncrementInDegrees", float)
        dwe = message.get("iDirectionIncrementInDegrees", float)

        if message.get("basicAngleOfTheInitialProductionDomain") == 0:
            report.add(Missing(message, "subdivisionsOfBasicAngle"))    
        else:
            # long basic    = get(h,"basicAngleOfTheInitialProductionDomain")
            # long division = get(h,"subdivisionsOfBasicAngle")
            report.add(Exists(message, "subdivisionsOfBasicAngle"))
            report.add(Ne(message, "subdivisionsOfBasicAngle", 0))

        if message.is_missing("subdivisionsOfBasicAngle"):
            report.add(Eq(message, "basicAngleOfTheInitialProductionDomain", 0))

        report.add(AssertTrue(meridian*parallel == data_points, "meridian*parallel == data_points"))

        report.add(Eq(message, "resolutionAndComponentFlags1", 0))
        report.add(Eq(message, "resolutionAndComponentFlags2", 0))
        report.add(Eq(message, "resolutionAndComponentFlags6", 0))
        report.add(Eq(message, "resolutionAndComponentFlags7", 0))
        report.add(Eq(message, "resolutionAndComponentFlags8", 0))

        report.add(Eq(message, "iDirectionIncrementGiven", 1))
        report.add(Eq(message, "jDirectionIncrementGiven", 1))

        report.add(Eq(message, "numberOfOctectsForNumberOfPoints", 0))
        report.add(Eq(message, "interpretationOfNumberOfPoints", 0))

        if message.get("iScansNegatively") != 0:
            tmp = east
            dtmp = deast

            east = west
            west = tmp

            deast = dwest
            dwest = dtmp

        if message.get("jScansPositively") != 0:
            tmp = north
            dtmp = dnorth

            north = south
            south = tmp

            dnorth = dsouth
            dsouth = dtmp

        # GRIB2 requires longitudes are always positive */
        report.add(AssertTrue(east >= 0, "east >= 0"))
        report.add(AssertTrue(west >= 0, "west >= 0"))

        #printf("meridian=%ld north=%ld south=%ld ns=%ld ",meridian,north,south,ns)
        #printf("meridian=%ld north=%f south=%f ns=%f ",meridian,dnorth,dsouth,dns)
        #printf("parallel=%ld east=%ld west=%ld we=%ld ",parallel,east,west,we)
        #printf("parallel=%ld east=%f west=%f we=%f ",parallel,deast,dwest,dwe)

        return [report]

    # not registered in the lookup table
    def _check_validity_time(self, message, p):
        report = Report()
        report.add(Fail("Not implemented: dummy check_validity_time()"))
        return [report]

    def _daily_average(self, message, p):
        reports = list()
        report = Report()
        start_step = message.get("startStep")
        end_step = message.get("endStep")
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
        checks = Report()
        checks.add(Eq(message, "startStep", 0))

        reports += self._statistical_process(message, p)
        reports = [checks] + reports

        return reports

    def _point_in_time(self, message, p):
        checks = Report(__class__.__name__)
        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]: # Analysis, Forecast
            pass
        elif topd == 2: # Analysis and forecast products
            checks.add(Eq(message, "productDefinitionTemplateNumber", 0))
        elif topd in [3, 4]: # Control forecast products, Perturbed forecast products
            checks.add(Ne(message, "perturbationNumber", 0))
            checks.add(Ne(message, "numberOfForecastsInEnsemble", 0))
        else:
            checks.add(Fail(f"Unsupported typeOfProcessedData {topd}"))

        return [checks]

    def _given_thickness(self, message, p):
        report = Report()
        report.add(Fail("Not implemented: dummy given_thickness()"))
        return [report]

    def _has_bitmap(self, message, p):
        report = Report()
        report.add(Fail("Not implemented: dummy has_bitmap()"))
        return [report]

    def _has_soil_layer(self, message, p):
        report = Report()
        report.add(AssertTrue(message.get("topLevel") == message.get("bottomLevel") - 1, "topLevel == bottomLevel - 1"))
        report.add(Le(message, "level", 14)) # max in UERRA
        return [report]

    def _has_soil_level(self, message, p):
        report = Report()
        report.add(AssertTrue(message.get("topLevel") == message.get("bottomLevel"), "topLevel == bottomLevel"))
        report.add(Le(message, "level", 14)) # max in UERRA
        return [report]

    def _height_level(self, message, p):
        report = Report()
        return [report]

    def _given_level(self, message, p):
        report = Report()
        report.add(Ne(message, "typeOfFirstFixedSurface", 255))
        report.add(Exists(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Exists(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message, "typeOfSecondFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return [report]

    def _potential_temperature_level(self, message, p):
        report = Report()
        report.add(Eq(message, 'level', 320, f'invalid potential temperature level {message.get("level")}' ))
        return [report]

    def _potential_vorticity_level(self, message, p):
        report = Report()
        report.add(Eq(message, 'level', 2, f'invalid potential vorticity level {message.get("level")}'))
        return [report]

    def _predefined_level(self, message, p):
        report = Report()
        report.add(Ne(message, "typeOfFirstFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Missing(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message, "typeOfSecondFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return [report]

    def _predefined_thickness(self, message, p):
        report = Report()
        report.add(Ne(message, "typeOfFirstFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfFirstFixedSurface"))
        report.add(Missing(message, "scaledValueOfFirstFixedSurface"))
        report.add(Eq(message, "typeOfSecondFixedSurface", 255))
        report.add(Missing(message, "scaleFactorOfSecondFixedSurface"))
        report.add(Missing(message, "scaledValueOfSecondFixedSurface"))
        return [report]

    def _pressure_level(self, message, p):
        checks = Report()
        levels = [1000, 200, 250, 300, 500, 700, 850, 925, 50]
        checks.add(IsIn(message, 'level', levels, 'invalid pressure level'))
        return [checks]

    def _resolution_s2s(self, message, p):
        report = Report()
        report.add(Eq(message, "iDirectionIncrement", 1500000))
        report.add(Eq(message, "jDirectionIncrement", 1500000))
        return [report]

    def _resolution_s2s_ocean(self, message, p):
        report = Report()
        report.add(Eq(message, "iDirectionIncrement", 1000000))
        report.add(Eq(message, "jDirectionIncrement", 1000000))
        return [report]

    def _since_prev_pp(self, message, p):
        report = Report()
        report.add(Eq(message, "indicatorOfUnitForTimeRange", 1))
        report.add(AssertTrue(message.get("endStep") == message.get("startStep") + message.get("lengthOfTimeRange"), "endStep == startStep + lengthOfTimeRange"))

        stats_report = self._statistical_process(message, p)
        check_report = self._check_range(message, p)
        return [report, stats_report, check_report]

    def _six_hourly(self, message, p):
        report = Report()
        if message.get("indicatorOfUnitForTimeRange") == 11:
            report.add(Eq(message, "lengthOfTimeRange", 1))
        else:
            report.add(Eq(message, "lengthOfTimeRange", 6))
        report.add(AssertTrue(message.get("endStep") == message.get("startStep") + 6, "endStep == startStep + 6"))

        stats_report = self._statistical_process(message, p)
        check_report = self._check_range(message, p)
        return [report, stats_report, check_report]

    def _three_hourly(self, message, p):
        report = Report()
        if message.get("indicatorOfUnitForTimeRange") == 11:
            report.add(Eq(message, "lengthOfTimeRange", 1))
        else:
            report.add(Eq(message, "lengthOfTimeRange", 3))
        report.add(AssertTrue(message.get("endStep") == message.get("startStep") + 3, "endStep == startStep + 3"))

        stats_report = self._statistical_process(message, p)
        check_report = self._check_range(message, p)
        return [report, stats_report, check_report]
