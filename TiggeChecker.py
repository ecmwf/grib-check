#!/usr/bin/env python3

from eccodes import (
    codes_grib_new_from_file,
    codes_release,
    codes_is_missing,
    codes_get_version_info,
    codes_get_message,
    codes_get_size,
    codes_get_long,
    codes_get_double,
    codes_get_string,
    codes_get_double_array,
    codes_get_gaussian_latitudes,
    codes_set_string,
    KeyValueNotFoundError,
)
import sys
import math
import numpy as np
from CheckEngine import CheckEngine
from TiggeCheckParameters import parameters


class TiggeChecker(CheckEngine):
    def __init__(
        self,
        valueflg=False,
        warnflg=False,
        lam=False,
        s2s=False,
        s2s_refcst=False,
        uerra=False,
        crra=False,
        good=None,
        bad=None,
    ):
        print("init()")
        check_map = {
            "daily_average": self.__daily_average,
            "from_start": self.__from_start,
            "given_level": self.__given_level,
            "given_thickness": self.__given_thickness,
            "has_bitmap": self.__has_bitmap,
            "has_soil_layer": self.__has_soil_layer,
            "has_soil_level": self.__has_soil_level,
            "height_level": self.__height_level,
            "point_in_time": self.__point_in_time,
            "potential_temperature_level": self.__potential_temperature_level,
            "potential_vorticity_level": self.__potential_vorticity_level,
            "predefined_level": self.__predefined_level,
            "predefined_thickness": self.__predefined_thickness,
            "pressure_level": self.__pressure_level,
            "resolution_s2s": self.__resolution_s2s,
            "resolution_s2s_ocean": self.__resolution_s2s_ocean,
            "since_prev_pp": self.__since_prev_pp,
            "six_hourly": self.__six_hourly,
            "three_hourly": self.__three_hourly,
        }

        super().__init__(
            valueflg=valueflg,
            warnflg=warnflg,
            good=good,
            bad=bad,
            parameters=parameters,
            check_map=check_map,
        )
        self.__last_n = 0
        self.__values = None

        self.__filename = ""
        self.__error = 0
        self.__warning = 0
        self.__field = 0
        self.__param = "unknown"

        self.__valueflg = valueflg
        self.__warnflg = warnflg
        self.__is_lam = lam
        self.__is_s2s = s2s
        self.__is_s2s_refcst = s2s_refcst
        self.__is_uerra = uerra
        self.__is_crra = crra

    def __gaussian_grid(self, h):
        tolerance = 1.0 / 1000000.0  # angular tolerance for grib2: micro degrees
        n = self._get(
            h, "numberOfParallelsBetweenAPoleAndTheEquator"
        )  # This is the key N

        north = self._dget(h, "latitudeOfFirstGridPointInDegrees")
        south = self._dget(h, "latitudeOfLastGridPointInDegrees")

        west = self._dget(h, "longitudeOfFirstGridPointInDegrees")
        east = self._dget(h, "longitudeOfLastGridPointInDegrees")

        if n != self.__last_n:
            try:
                self.__values = codes_get_gaussian_latitudes(n)
            except Exception as e:
                print(
                    "%s, field %d [%s]: cannot get gaussian latitudes for N%ld: %s"
                    % (self.__filename, self.__field, self.__param, n, str(e))
                )
                self.__error += 1
                self.__last_n = 0
                return
            self.__last_n = n

        # TODO
        if self.__values is None:
            assert 0
            return

        if self.__values is not None:
            self.__values[0] = np.rint(self.__values[0] * 1e6) / 1e6

        if not self._dbl_equal(
            north, self.__values[0], tolerance
        ) or not self._dbl_equal(south, -self.__values[0], tolerance):
            print(
                "N=%ld north=%f south=%f v(=gauss_lat[0])=%f north-v=%0.30f south-v=%0.30f"
                % (
                    n,
                    north,
                    south,
                    self.__values[0],
                    north - self.__values[0],
                    south + self.__values[0],
                )
            )

        self._check(
            "DBL_EQUAL(north, values[0], tolerance)",
            self._dbl_equal(north, self.__values[0], tolerance),
        )
        self._check(
            "DBL_EQUAL(south, -values[0], tolerance)",
            self._dbl_equal(south, -self.__values[0], tolerance),
        )

        if self._missing(h, "numberOfPointsAlongAParallel"):  # same as key Ni
            # If missing, this is a REDUCED gaussian grid
            MAXIMUM_RESOLUTION = 640
            self._check('get(h,"PLPresent")', self._get(h, "PLPresent"))
            self._check(
                "DBL_EQUAL(west, 0.0, tolerance)",
                self._dbl_equal(west, 0.0, tolerance),
            )
            if n > MAXIMUM_RESOLUTION:
                print(
                    "Gaussian number N (=%ld) cannot exceed %ld"
                    % (n, MAXIMUM_RESOLUTION)
                )
                self._check("n <= MAXIMUM_RESOLUTION", n <= MAXIMUM_RESOLUTION)
        else:
            # REGULAR gaussian grid
            l_west = self._get(h, "longitudeOfFirstGridPoint")
            l_east = self._get(h, "longitudeOfLastGridPoint")
            parallel = self._get(h, "numberOfPointsAlongAParallel")
            we = self._get(h, "iDirectionIncrement")
            dwest = self._dget(h, "longitudeOfFirstGridPointInDegrees")
            deast = self._dget(h, "longitudeOfLastGridPointInDegrees")
            dwe = self._dget(h, "iDirectionIncrementInDegrees")
            # print('parallel=%ld east=%ld west=%ld we=%ld' % (parallel, east, west, we))

            self._check(
                "parallel == (l_east-l_west)/we + 1",
                parallel == (l_east - l_west) / we + 1,
            )
            self._check(
                "abs((deast-dwest)/dwe + 1 - parallel) < 1e-10",
                abs((deast - dwest) / dwe + 1 - parallel) < 1e-10,
            )
            self._check('!get(h,"PLPresent")', not self._get(h, "PLPresent"))

        self._check('ne(h,"Nj",0)', self._ne(h, "Nj", 0))

        self._get(h, "PLPresent")

        count = codes_get_size(h, "pl")
        expected_lon2 = 0
        total = 0
        max_pl = 0
        numberOfValues = self._get(h, "numberOfValues")
        numberOfDataPoints = self._get(h, "numberOfDataPoints")

        pl = codes_get_double_array(h, "pl")

        if len(pl) != count:
            print("len(pl)=%ld count=%ld" % (len(pl), count))

        self._check("len(pl) == count", len(pl) == count)
        self._check("len(pl) == 2*n", len(pl) == 2 * n)

        total = 0
        max_pl = pl[0]  #  max elem of pl array = num points at equator

        for p in pl:
            total = total + p
            if p > max_pl:
                max_pl = p

        # Do not assume maximum of pl array is 4N! not true for octahedral

        expected_lon2 = 360.0 - 360.0 / max_pl
        if not self._dbl_equal(expected_lon2, east, tolerance):
            print(
                "east actual=%g expected=%g diff=%g",
                east,
                expected_lon2,
                expected_lon2 - east,
            )

        self._check(
            "DBL_EQUAL(expected_lon2, east, tolerance)",
            self._dbl_equal(expected_lon2, east, tolerance),
        )

        if numberOfDataPoints != total:
            print(
                "GAUSS numberOfValues=%ld numberOfDataPoints=%ld sum(pl)=%ld"
                % (numberOfValues, numberOfDataPoints, total)
            )

        self._check("numberOfDataPoints == total", numberOfDataPoints == total)

        self._check(
            'missing(h,"iDirectionIncrement")', self._missing(h, "iDirectionIncrement")
        )
        self._check(
            'missing(h,"iDirectionIncrementInDegrees")',
            self._missing(h, "iDirectionIncrementInDegrees"),
        )

        self._check(
            'eq(h,"iDirectionIncrementGiven",0)',
            self._eq(h, "iDirectionIncrementGiven", 0),
        )
        self._check(
            'eq(h,"jDirectionIncrementGiven",1)',
            self._eq(h, "jDirectionIncrementGiven", 1),
        )

        self._check(
            'eq(h,"resolutionAndComponentFlags1",0)',
            self._eq(h, "resolutionAndComponentFlags1", 0),
        )
        self._check(
            'eq(h,"resolutionAndComponentFlags2",0)',
            self._eq(h, "resolutionAndComponentFlags2", 0),
        )
        self._check(
            'eq(h,"resolutionAndComponentFlags6",0)',
            self._eq(h, "resolutionAndComponentFlags6", 0),
        )
        self._check(
            'eq(h,"resolutionAndComponentFlags7",0)',
            self._eq(h, "resolutionAndComponentFlags7", 0),
        )
        self._check(
            'eq(h,"resolutionAndComponentFlags8",0)',
            self._eq(h, "resolutionAndComponentFlags8", 0),
        )

    def __check_validity_datetime(self, h):
        # If we just set the stepRange (for non-instantaneous fields) to its
        # current value, then this causes the validity date and validity time
        # keys to be correctly computed.
        # Then we can compare the previous (possibly wrongly coded) value with
        # the newly computed one

        stepType = codes_get_string(h, "stepType")

        if stepType != "instant":  # not instantaneous
            # Check only applies to accumulated, max etc.
            stepRange = codes_get_string(h, "stepRange")

            saved_validityDate = self._get(h, "validityDate")
            saved_validityTime = self._get(h, "validityTime")

            codes_set_string(h, "stepRange", stepRange)
            validityDate = self._get(h, "validityDate")
            validityTime = self._get(h, "validityTime")
            if validityDate != saved_validityDate or validityTime != saved_validityTime:
                print(
                    "warning: %s, field %d [%s]: invalid validity Date/Time (Should be %ld and %ld)"
                    % (
                        self.__filename,
                        self.__field,
                        self.__param,
                        validityDate,
                        validityTime,
                    )
                )
                self.__warning += 1

    def __check_range(self, h, p, min_value, max_value):
        missing = 0
        if self.__valueflg != 0:
            return

        missing = self._dget(h, "missingValue")

        # See ECC-437
        if (
            not self._get(h, "bitMapIndicator") == 0
            and min_value == missing
            and max_value == missing
        ):
            if min_value < p["min1"] or min_value > p["min2"]:
                print(
                    "warning: %s, field %d [%s]: %s minimum value %g is not in [%g,%g]"
                    % (
                        self.__filename,
                        self.__field,
                        self.__param,
                        p["name"],
                        min_value,
                        p["min1"],
                        p["min2"],
                    )
                )
                print(
                    "  => [%g,%g]"
                    % (
                        min_value if min_value < p["min1"] else p["min1"],
                        min_value if min_value > p["min2"] else p["min2"],
                    )
                )
                self.__warning += 1

            if max_value < p["max1"] or max_value > p["max2"]:
                print(
                    "warning: %s, field %d [%s]: %s maximum value %g is not in [%g,%g]"
                    % (
                        self.__filename,
                        self.__field,
                        self.__param,
                        p["name"],
                        max_value,
                        p["max1"],
                        p["max2"],
                    )
                )
                print(
                    "  => [%g,%g]"
                    % (
                        max_value if max_value < p["max1"] else p["max1"],
                        max_value if max_value > p["max2"] else p["max2"],
                    )
                )
                self.__warning += 1

    def __point_in_time(self, h, p, min_value, max_value):
        topd = self._get(h, "typeOfProcessedData")

        if topd == 0:  # Analysis
            if self.__is_uerra:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",0)||eq(h,"productDefinitionTemplateNumber",1)',
                    self._eq(h, "productDefinitionTemplateNumber", 0)
                    or self._eq(h, "productDefinitionTemplateNumber", 1),
                )
            if self._get(h, "productDefinitionTemplateNumber") == 1:
                self._check(
                    'ne(h,"numberOfForecastsInEnsemble",0)',
                    self._ne(h, "numberOfForecastsInEnsemble", 0),
                )
                self._check(
                    'le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble"))',
                    self._le(
                        h,
                        "perturbationNumber",
                        self._get(h, "numberOfForecastsInEnsemble"),
                    ),
                )
        elif topd == 1:  # Forecast
            if self.__is_uerra:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",0)||eq(h,"productDefinitionTemplateNumber",1)',
                    self._eq(h, "productDefinitionTemplateNumber", 0)
                    or self._eq(h, "productDefinitionTemplateNumber", 1),
                )
            if self._get(h, "productDefinitionTemplateNumber") == 1:
                self._check(
                    'ne(h,"numberOfForecastsInEnsemble",0)',
                    self._ne(h, "numberOfForecastsInEnsemble", 0),
                )
                self._check(
                    'le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble"))',
                    self._le(
                        h,
                        "perturbationNumber",
                        self._get(h, "numberOfForecastsInEnsemble"),
                    ),
                )
        elif topd == 2:  # Analysis and forecast products
            self._check(
                'eq(h,"productDefinitionTemplateNumber",0)',
                self._eq(h, "productDefinitionTemplateNumber", 0),
            )
        elif topd == 3:  # Control forecast products
            self._check(
                'eq(h,"perturbationNumber",0)', self._eq(h, "perturbationNumber", 0)
            )
            self._check(
                'ne(h,"numberOfForecastsInEnsemble",0)',
                self._ne(h, "numberOfForecastsInEnsemble", 0),
            )
            if self.__is_s2s_refcst:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",60)',
                    self._eq(h, "productDefinitionTemplateNumber", 60),
                )
            elif self.__is_s2s:
                # self._check('eq(h,"productDefinitionTemplateNumber",60)||eq(h,"productDefinitionTemplateNumber",11)||eq(h,"productDefinitionTemplateNumber",1)',
                #              self.__eq(h, 'productDefinitionTemplateNumber', 60) or self.__eq(h, 'productDefinitionTemplateNumber', 11) or self.__eq(h, 'productDefinitionTemplateNumber', 1))
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",1)',
                    self._eq(h, "productDefinitionTemplateNumber", 1),
                )
            else:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",1)',
                    self._eq(h, "productDefinitionTemplateNumber", 1),
                )
        elif topd == 4:  # Perturbed forecast products
            self._check(
                'ne(h,"perturbationNumber",0)', self._ne(h, "perturbationNumber", 0)
            )
            self._check(
                'ne(h,"numberOfForecastsInEnsemble",0)',
                self._ne(h, "numberOfForecastsInEnsemble", 0),
            )
            if self.__is_s2s_refcst:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",60)',
                    self._eq(h, "productDefinitionTemplateNumber", 60),
                )
            elif self.__is_s2s:
                # self._check('eq(h,"productDefinitionTemplateNumber",60)||eq(h,"productDefinitionTemplateNumber",11)||eq(h,"productDefinitionTemplateNumber",1)',
                #              self.__eq(h, 'productDefinitionTemplateNumber', 60) or self.__eq(h, 'productDefinitionTemplateNumber', 11) or self.__eq(h, 'productDefinitionTemplateNumber', 1))
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",1)',
                    self._eq(h, "productDefinitionTemplateNumber", 1),
                )
            else:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",1)',
                    self._eq(h, "productDefinitionTemplateNumber", 1),
                )
            if self.__is_lam:
                self._check(
                    'le(h,"perturbationNumber", get(h,"numberOfForecastsInEnsemble"))',
                    self._le(
                        h,
                        "perturbationNumber",
                        self._get(h, "numberOfForecastsInEnsemble"),
                    ),
                )
            else:
                # Is there always cf in tigge global datasets??
                self._check(
                    'le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")-1)',
                    self._le(
                        h,
                        "perturbationNumber",
                        self._get(h, "numberOfForecastsInEnsemble") - 1,
                    ),
                )
        else:
            print(
                "Unsupported typeOfProcessedData %ld"
                % self._get(h, "typeOfProcessedData")
            )
            self._check("0", 0)

        if self.__is_lam:
            if self._get(h, "indicatorOfUnitOfTimeRange") == 10:  # three hours
                # Three hourly is OK
                pass
            else:
                self._check(
                    'eq(h,"indicatorOfUnitOfTimeRange",1)',
                    self._eq(h, "indicatorOfUnitOfTimeRange", 1),
                )  # Hours
                self._check(
                    '(get(h,"forecastTime") % 3) == 0',
                    (self._get(h, "forecastTime") % 3) == 0,
                )  # Every three hours
        elif self.__is_uerra:
            if self._get(h, "indicatorOfUnitOfTimeRange") == 1:  # hourly
                self._check(
                    '(eq(h,"forecastTime",1)||eq(h,"forecastTime",2)||eq(h,"forecastTime",4)||eq(h,"forecastTime",5))||(get(h,"forecastTime") % 3) == 0',
                    (
                        self._eq(h, "forecastTime", 1)
                        or self._eq(h, "forecastTime", 2)
                        or self._eq(h, "forecastTime", 4)
                        or self._eq(h, "forecastTime", 5)
                    )
                    or (self._get(h, "forecastTime") % 3) == 0,
                )
        else:
            if self._get(h, "indicatorOfUnitOfTimeRange") == 11:  # six hour
                # Six hourly is OK
                pass
            else:
                self._check(
                    'eq(h,"indicatorOfUnitOfTimeRange",1)',
                    self._eq(h, "indicatorOfUnitOfTimeRange", 1),
                )  # Hours
                self._check(
                    '(get(h,"forecastTime") % 6) == 0',
                    (self._get(h, "forecastTime") % 6) == 0,
                )  # Every six hours

        self.__check_range(h, p, min_value, max_value)

    def __height_level(self, h, p, min_value, max_value):
        level = self._get(h, "level")
        levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500]
        if self.__is_uerra:
            if level in levels:
                pass
            else:
                print(
                    "%s, field %d [%s]: invalid height level %ld"
                    % (self.__filename, self.__field, self.__param, level)
                )
                self.__error += 1

    def __pressure_level(self, h, p, min_value, max_value):
        level = self._get(h, "level")
        if self.__is_uerra and not self.__is_crra:
            if level in [
                1000,
                975,
                950,
                925,
                900,
                875,
                850,
                825,
                800,
                750,
                700,
                600,
                500,
                400,
                300,
                250,
                200,
                150,
                100,
                70,
                50,
                30,
                20,
                10,
            ]:
                pass
            else:
                print(
                    "%s, field %d [%s]: invalid pressure level %ld"
                    % (self.__filename, self.__field, self.__param, level)
                )
                self.__error += 1
        elif self.__is_uerra and self.__is_crra:
            if level in [
                1000,
                975,
                950,
                925,
                900,
                875,
                850,
                825,
                800,
                750,
                700,
                600,
                500,
                400,
                300,
                250,
                200,
                150,
                100,
                70,
                50,
                30,
                20,
                10,
                7,
                5,
                3,
                2,
                1,
            ]:
                pass
            else:
                print(
                    "%s, field %d [%s]: invalid pressure level %ld"
                    % (self.__filename, self.__field, self.__param, level)
                )
                self.__error += 1
        elif self.__is_s2s:
            if level in [1000, 925, 850, 700, 500, 300, 200, 100, 50, 10]:
                pass
            else:
                print(
                    "%s, field %d [%s]: invalid pressure level %ld"
                    % (self.__filename, self.__field, self.__param, level)
                )
                self.__error += 1
        else:
            if level in [1000, 200, 250, 300, 500, 700, 850, 925, 50]:
                pass
            else:
                print(
                    "%s, field %d [%s]: invalid pressure level %ld"
                    % (self.__filename, self.__field, self.__param, level)
                )
                self.__error += 1

    def __potential_vorticity_level(self, h, p, min_value, max_value):
        level = self._get(h, "level")
        if level == 2:
            pass
        else:
            print(
                "%s, field %d [%s]: invalid potential vorticity level %ld"
                % (self.__filename, self.__field, self.__param, level)
            )
            self.__error += 1

    def __potential_temperature_level(self, h, p, min_value, max_value):
        level = self._get(h, "level")
        if level == 320:
            pass
        else:
            print(
                "%s, field %d [%s]: invalid potential temperature level %ld"
                % (self.__filename, self.__field, self.__param, level)
            )
            self.__error += 1

    def __statistical_process(self, h, p, min_value, max_value):
        topd = self._get(h, "typeOfProcessedData")

        if topd == 0:  # Analysis
            if self.__is_uerra:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",8)||eq(h,"productDefinitionTemplateNumber",11)',
                    self._eq(h, "productDefinitionTemplateNumber", 8)
                    or self._eq(h, "productDefinitionTemplateNumber", 11),
                )
        elif topd == 1:  # Forecast
            if self.__is_uerra:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",8)||eq(h,"productDefinitionTemplateNumber",11)',
                    self._eq(h, "productDefinitionTemplateNumber", 8)
                    or self._eq(h, "productDefinitionTemplateNumber", 11),
                )
        elif topd == 2:  # Analysis and forecast products
            self._check(
                'eq(h,"productDefinitionTemplateNumber",8)',
                self._eq(h, "productDefinitionTemplateNumber", 8),
            )
        elif topd == 3:  # Control forecast products
            if not self.__is_s2s_refcst:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",11)',
                    self._eq(h, "productDefinitionTemplateNumber", 11),
                )
            else:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",61)',
                    self._eq(h, "productDefinitionTemplateNumber", 61),
                )
        elif topd == 4:  # Perturbed forecast products
            if not self.__is_s2s_refcst:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",11)',
                    self._eq(h, "productDefinitionTemplateNumber", 11),
                )
            else:
                self._check(
                    'eq(h,"productDefinitionTemplateNumber",61)',
                    self._eq(h, "productDefinitionTemplateNumber", 61),
                )
        else:
            print(
                "Unsupported typeOfProcessedData %ld"
                % (self._get(h, "typeOfProcessedData"))
            )
            self.__error += 1
            return

        if self.__is_lam:
            if self._get(h, "indicatorOfUnitOfTimeRange") == 10:  # three hours
                # Three hourly is OK
                pass
            else:
                self._check(
                    'eq(h,"indicatorOfUnitOfTimeRange",1)',
                    self._eq(h, "indicatorOfUnitOfTimeRange", 1),
                )  # Hours
                self._check(
                    '(get(h,"forecastTime"', (self._get(h, "forecastTime") % 3) == 0
                )  # Every three hours
        elif self.__is_uerra:
            # forecastTime for uerra might be all steps decreased by 1 i.e 0,1,2,3,4,5,8,11...29 too many...
            if self._get(h, "indicatorOfUnitOfTimeRange") == 1:
                self._check('le(h,"forecastTime",30)', self._le(h, "forecastTime", 30))
        else:
            if self._get(h, "indicatorOfUnitOfTimeRange") == 11:  # six hours
                # Six hourly is OK
                pass
            else:
                self._check(
                    'eq(h,"indicatorOfUnitOfTimeRange",1)',
                    self._eq(h, "indicatorOfUnitOfTimeRange", 1),
                )  # Hours
                self._check(
                    '(get(h,"forecastTime"', (self._get(h, "forecastTime") % 6) == 0
                )  # Every six hours

        self._check('eq(h,"numberOfTimeRange",1)', self._eq(h, "numberOfTimeRange", 1))
        self._check(
            'eq(h,"numberOfMissingInStatisticalProcess",0)',
            self._eq(h, "numberOfMissingInStatisticalProcess", 0),
        )
        self._check(
            'eq(h,"typeOfTimeIncrement",2)', self._eq(h, "typeOfTimeIncrement", 2)
        )
        # self._check('eq(h,"indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed",255)',
        # self.__eq(h, 'indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed', 255))

        if self.__is_s2s:
            if self._get(h, "typeOfStatisticalProcessing") == 0:
                self._check(
                    'eq(h,"timeIncrementBetweenSuccessiveFields",1)||eq(h,"timeIncrementBetweenSuccessiveFields",4)',
                    self._eq(h, "timeIncrementBetweenSuccessiveFields", 1)
                    or self._eq(h, "timeIncrementBetweenSuccessiveFields", 4),
                )
            else:
                self._check(
                    'eq(h,"timeIncrementBetweenSuccessiveFields",0)',
                    self._eq(h, "timeIncrementBetweenSuccessiveFields", 0),
                )
        else:
            self._check(
                'eq(h,"timeIncrementBetweenSuccessiveFields",0)',
                self._eq(h, "timeIncrementBetweenSuccessiveFields", 0),
            )

        self._check(
            'eq(h,"minuteOfEndOfOverallTimeInterval",0)',
            self._eq(h, "minuteOfEndOfOverallTimeInterval", 0),
        )
        self._check(
            'eq(h,"secondOfEndOfOverallTimeInterval",0)',
            self._eq(h, "secondOfEndOfOverallTimeInterval", 0),
        )

        if self.__is_uerra:
            self._check(
                '(eq(h,"endStep",1)||eq(h,"endStep",2)||eq(h,"endStep",4)||eq(h,"endStep",5))||(get(h,"endStep"',
                (
                    self._eq(h, "endStep", 1)
                    or self._eq(h, "endStep", 2)
                    or self._eq(h, "endStep", 4)
                    or self._eq(h, "endStep", 5)
                )
                or (self._get(h, "endStep") % 3) == 0,
            )
        elif self.__is_lam:
            self._check(
                '(get(h,"endStep") % 3) == 0', (self._get(h, "endStep") % 3) == 0
            )  # Every three hours
        else:
            self._check(
                '(get(h,"endStep") % 6) == 0', (self._get(h, "endStep") % 6) == 0
            )  # Every six hours

        if self._get(h, "indicatorOfUnitForTimeRange") == 11:
            # Six hourly is OK
            self._check(
                'get(h,"lengthOfTimeRange")*6 + get(h,"startStep") == get(h,"endStep")',
                self._get(h, "lengthOfTimeRange") * 6 + self._get(h, "startStep")
                == self._get(h, "endStep"),
            )
        elif self._get(h, "indicatorOfUnitForTimeRange") == 10:
            # Three hourly is OK
            self._check(
                'get(h,"lengthOfTimeRange")*3 + get(h,"startStep") == get(h,"endStep")',
                self._get(h, "lengthOfTimeRange") * 3 + self._get(h, "startStep")
                == self._get(h, "endStep"),
            )
        else:
            self._check(
                'eq(h,"indicatorOfUnitForTimeRange",1)',
                self._eq(h, "indicatorOfUnitForTimeRange", 1),
            )  # Hours
            self._check(
                'get(h,"lengthOfTimeRange") + get(h,"startStep") == get(h,"endStep")',
                self._get(h, "lengthOfTimeRange") + self._get(h, "startStep")
                == self._get(h, "endStep"),
            )

    def __has_bitmap(self, h, p, min_value, max_value):
        # print('bitMapIndicator %ld' % self._get(h,"bitMapIndicator"))
        self._check('eq(h,"bitMapIndicator",0)', self._eq(h, "bitMapIndicator", 0))

    def __has_soil_level(self, h, p, min_value, max_value):
        self._check(
            'get(h,"topLevel") == get(h,"bottomLevel")',
            self._get(h, "topLevel") == self._get(h, "bottomLevel"),
        )
        self._check('le(h,"level",14)', self._le(h, "level", 14))  # max in UERRA

    def __has_soil_layer(self, h, p, min_value, max_value):
        self._check(
            'get(h,"topLevel") == get(h,"bottomLevel") - 1',
            self._get(h, "topLevel") == self._get(h, "bottomLevel") - 1,
        )
        self._check('le(h,"level",14)', self._le(h, "level", 14))  # max in UERRA

    def __resolution_s2s(self, h, p, min_value, max_value):
        self._check(
            'eq(h,"iDirectionIncrement",1500000)',
            self._eq(h, "iDirectionIncrement", 1500000),
        )
        self._check(
            'eq(h,"jDirectionIncrement",1500000)',
            self._eq(h, "jDirectionIncrement", 1500000),
        )

    def __resolution_s2s_ocean(self, h, p, min_value, max_value):
        self._check(
            'eq(h,"iDirectionIncrement",1000000)',
            self._eq(h, "iDirectionIncrement", 1000000),
        )
        self._check(
            'eq(h,"jDirectionIncrement",1000000)',
            self._eq(h, "jDirectionIncrement", 1000000),
        )

    def __six_hourly(self, h, p, min_value, max_value):
        self.__statistical_process(h, p, min_value, max_value)
        if self._get(h, "indicatorOfUnitForTimeRange") == 11:
            self._check(
                'eq(h,"lengthOfTimeRange",1)', self._eq(h, "lengthOfTimeRange", 1)
            )
        else:
            self._check(
                'eq(h,"lengthOfTimeRange",6)', self._eq(h, "lengthOfTimeRange", 6)
            )

        self._check(
            'get(h,"endStep") == get(h,"startStep") + 6',
            self._get(h, "endStep") == self._get(h, "startStep") + 6,
        )
        self.__check_range(h, p, min_value, max_value)

    def __since_prev_pp(self, h, p, min_value, max_value):
        self.__statistical_process(h, p, min_value, max_value)
        self._check(
            'eq(h,"indicatorOfUnitForTimeRange",1)',
            self._eq(h, "indicatorOfUnitForTimeRange", 1),
        )
        self._check(
            'get(h,"endStep") == get(h,"startStep") + get(h,"lengthOfTimeRange")',
            self._get(h, "endStep")
            == self._get(h, "startStep") + self._get(h, "lengthOfTimeRange"),
        )
        self.__check_range(h, p, min_value, max_value)

    def __three_hourly(self, h, p, min_value, max_value):
        self.__statistical_process(h, p, min_value, max_value)

        if self._get(h, "indicatorOfUnitForTimeRange") == 11:
            self._check(
                'eq(h,"lengthOfTimeRange",1)', self._eq(h, "lengthOfTimeRange", 1)
            )
        else:
            self._check(
                'eq(h,"lengthOfTimeRange",3)', self._eq(h, "lengthOfTimeRange", 3)
            )

        self._check(
            'get(h,"endStep") == get(h,"startStep") + 3',
            self._get(h, "endStep") == self._get(h, "startStep") + 3,
        )
        self.__check_range(h, p, min_value, max_value)

    def __from_start(self, h, p, min_value, max_value):
        step = self._get(h, "endStep")
        self.__statistical_process(h, p, min_value, max_value)
        self._check('eq(h,"startStep",0)', self._eq(h, "startStep", 0))

        if step == 0:
            if not self.__is_uerra:
                self._check(
                    "min_value == 0 and max_value == 0",
                    min_value == 0 and max_value == 0,
                )  # ??? xxx
        else:
            self.__check_range(h, p, min_value / step, max_value / step)

    def __daily_average(self, h, p, min_value, max_value):
        step = self._get(h, "endStep")
        self._check(
            'get(h,"startStep") == get(h,"endStep") - 24',
            self._get(h, "startStep") == self._get(h, "endStep") - 24,
        )
        self.__statistical_process(h, p, min_value, max_value)

        if step == 0:
            self._check(
                "min_value == 0 && max_value == 0", min_value == 0 and max_value == 0
            )
        else:
            self.__check_range(h, p, min_value, max_value)

    def __given_level(self, h, p, min_value, max_value):
        self._check(
            'ne(h,"typeOfFirstFixedSurface",255)',
            self._ne(h, "typeOfFirstFixedSurface", 255),
        )
        self._check(
            '!missing(h,"scaleFactorOfFirstFixedSurface")',
            not self._missing(h, "scaleFactorOfFirstFixedSurface"),
        )
        self._check(
            '!missing(h,"scaledValueOfFirstFixedSurface")',
            not self._missing(h, "scaledValueOfFirstFixedSurface"),
        )

        self._check(
            'eq(h,"typeOfSecondFixedSurface",255)',
            self._eq(h, "typeOfSecondFixedSurface", 255),
        )
        self._check(
            'missing(h,"scaleFactorOfSecondFixedSurface")',
            self._missing(h, "scaleFactorOfSecondFixedSurface"),
        )
        self._check(
            'missing(h,"scaledValueOfSecondFixedSurface")',
            self._missing(h, "scaledValueOfSecondFixedSurface"),
        )

    def __predefined_level(self, h, p, min_value, max_value):
        self._check(
            'ne(h,"typeOfFirstFixedSurface",255)',
            self._ne(h, "typeOfFirstFixedSurface", 255),
        )
        self._check(
            'missing(h,"scaleFactorOfFirstFixedSurface")',
            self._missing(h, "scaleFactorOfFirstFixedSurface"),
        )
        self._check(
            'missing(h,"scaledValueOfFirstFixedSurface")',
            self._missing(h, "scaledValueOfFirstFixedSurface"),
        )

        self._check(
            'eq(h,"typeOfSecondFixedSurface",255)',
            self._eq(h, "typeOfSecondFixedSurface", 255),
        )
        self._check(
            'missing(h,"scaleFactorOfSecondFixedSurface")',
            self._missing(h, "scaleFactorOfSecondFixedSurface"),
        )
        self._check(
            'missing(h,"scaledValueOfSecondFixedSurface")',
            self._missing(h, "scaledValueOfSecondFixedSurface"),
        )

    def __predefined_thickness(self, h, p, min_value, max_value):
        self._check(
            'ne(h,"typeOfFirstFixedSurface",255)',
            self._ne(h, "typeOfFirstFixedSurface", 255),
        )
        self._check(
            'missing(h,"scaleFactorOfFirstFixedSurface")',
            self._missing(h, "scaleFactorOfFirstFixedSurface"),
        )
        self._check(
            'missing(h,"scaledValueOfFirstFixedSurface")',
            self._missing(h, "scaledValueOfFirstFixedSurface"),
        )

        self._check(
            'ne(h,"typeOfSecondFixedSurface",255)',
            self._ne(h, "typeOfSecondFixedSurface", 255),
        )
        self._check(
            'missing(h,"scaleFactorOfSecondFixedSurface")',
            self._missing(h, "scaleFactorOfSecondFixedSurface"),
        )
        self._check(
            'missing(h,"scaledValueOfSecondFixedSurface")',
            self._missing(h, "scaledValueOfSecondFixedSurface"),
        )

    def __given_thickness(self, h, p, min_value, max_value):
        self._check(
            'ne(h,"typeOfFirstFixedSurface",255)',
            self._ne(h, "typeOfFirstFixedSurface", 255),
        )
        self._check(
            '!missing(h,"scaleFactorOfFirstFixedSurface")',
            not self._missing(h, "scaleFactorOfFirstFixedSurface"),
        )
        self._check(
            '!missing(h,"scaledValueOfFirstFixedSurface")',
            not self._missing(h, "scaledValueOfFirstFixedSurface"),
        )

        self._check(
            'ne(h,"typeOfSecondFixedSurface",255)',
            self._ne(h, "typeOfSecondFixedSurface", 255),
        )
        self._check(
            '!missing(h,"scaleFactorOfSecondFixedSurface")',
            not self._missing(h, "scaleFactorOfSecondFixedSurface"),
        )
        self._check(
            '!missing(h,"scaledValueOfSecondFixedSurface")',
            not self._missing(h, "scaledValueOfSecondFixedSurface"),
        )

    def __latlon_grid(self, h):
        tolerance = 1.0 / 1000000.0  # angular tolerance for grib2: micro degrees
        data_points = self._get(h, "numberOfDataPoints")
        meridian = self._get(h, "numberOfPointsAlongAMeridian")
        parallel = self._get(h, "numberOfPointsAlongAParallel")

        north = self._get(h, "latitudeOfFirstGridPoint")
        south = self._get(h, "latitudeOfLastGridPoint")
        west = self._get(h, "longitudeOfFirstGridPoint")
        east = self._get(h, "longitudeOfLastGridPoint")

        ns = self._get(h, "jDirectionIncrement")
        we = self._get(h, "iDirectionIncrement")

        dnorth = self._dget(h, "latitudeOfFirstGridPointInDegrees")
        dsouth = self._dget(h, "latitudeOfLastGridPointInDegrees")
        dwest = self._dget(h, "longitudeOfFirstGridPointInDegrees")
        deast = self._dget(h, "longitudeOfLastGridPointInDegrees")

        dns = self._dget(h, "jDirectionIncrementInDegrees")
        dwe = self._dget(h, "iDirectionIncrementInDegrees")

        if self._eq(h, "basicAngleOfTheInitialProductionDomain", 0):
            self._check(
                'missing(h,"subdivisionsOfBasicAngle")',
                self._missing(h, "subdivisionsOfBasicAngle"),
            )
        else:
            # long basic    = self._get(h, 'basicAngleOfTheInitialProductionDomain')
            # long division = self._get(h, 'subdivisionsOfBasicAngle')
            self._check(
                '!missing(h,"subdivisionsOfBasicAngle")',
                not self._missing(h, "subdivisionsOfBasicAngle"),
            )
            self._check(
                '!eq(h,"subdivisionsOfBasicAngle",0)',
                not self._eq(h, "subdivisionsOfBasicAngle", 0),
            )

        if self._missing(h, "subdivisionsOfBasicAngle"):
            self._check(
                'eq(h,"basicAngleOfTheInitialProductionDomain",0)',
                self._eq(h, "basicAngleOfTheInitialProductionDomain", 0),
            )

        self._check(
            "meridian*parallel == data_points", meridian * parallel == data_points
        )

        self._check(
            'eq(h,"resolutionAndComponentFlags1",0)',
            self._eq(h, "resolutionAndComponentFlags1", 0),
        )
        self._check(
            'eq(h,"resolutionAndComponentFlags2",0)',
            self._eq(h, "resolutionAndComponentFlags2", 0),
        )
        self._check(
            'eq(h,"resolutionAndComponentFlags6",0)',
            self._eq(h, "resolutionAndComponentFlags6", 0),
        )
        self._check(
            'eq(h,"resolutionAndComponentFlags7",0)',
            self._eq(h, "resolutionAndComponentFlags7", 0),
        )
        self._check(
            'eq(h,"resolutionAndComponentFlags8",0)',
            self._eq(h, "resolutionAndComponentFlags8", 0),
        )

        self._check(
            'eq(h,"iDirectionIncrementGiven",1)',
            self._eq(h, "iDirectionIncrementGiven", 1),
        )
        self._check(
            'eq(h,"jDirectionIncrementGiven",1)',
            self._eq(h, "jDirectionIncrementGiven", 1),
        )

        self._check(
            'eq(h,"numberOfOctectsForNumberOfPoints",0)',
            self._eq(h, "numberOfOctectsForNumberOfPoints", 0),
        )
        self._check(
            'eq(h,"interpretationOfNumberOfPoints",0)',
            self._eq(h, "interpretationOfNumberOfPoints", 0),
        )

        if self._get(h, "iScansNegatively") != 0:
            tmp = east
            dtmp = deast

            east = west
            west = tmp

            deast = dwest
            dwest = dtmp

        if self._get(h, "jScansPositively") != 0:
            tmp = north
            dtmp = dnorth

            north = south
            south = tmp

            dnorth = dsouth
            dsouth = dtmp

        if not (self.__is_lam or self.__is_uerra):
            self._check("north > south", north > south)
            self._check("east > west", east > west)

            # Check that the grid is symmetrical */
            self._check("north == -south", north == -south)
            self._check(
                "DBL_EQUAL(dnorth, -dsouth, tolerance)",
                self._dbl_equal(dnorth, -dsouth, tolerance),
            )
            self._check(
                "parallel == (east-west)/we + 1", parallel == (east - west) / we + 1
            )
            self._check(
                "fabs((deast-dwest)/dwe + 1 - parallel) < 1e-10",
                math.fabs((deast - dwest) / dwe + 1 - parallel) < 1e-10,
            )
            self._check(
                "meridian == (north-south)/ns + 1", meridian == (north - south) / ns + 1
            )
            self._check(
                "fabs((dnorth-dsouth)/dns + 1 - meridian) < 1e-10",
                math.fabs((dnorth - dsouth) / dns + 1 - meridian) < 1e-10,
            )

            # Check that the field is global */
            area = (dnorth - dsouth) * (deast - dwest)
            globe = 360.0 * 180.0
            self._check("area <= globe", area <= globe)
            self._check("area >= globe*0.95", area >= globe * 0.95)

        # GRIB2 requires longitudes are always positive */
        self._check("east >= 0", east >= 0)
        self._check("west >= 0", west >= 0)

        # print('meridian=%ld north=%ld south=%ld ns=%ld', (meridian, north, south, ns))
        # print('meridian=%ld north=%f south=%f ns=%f', (meridian, dnorth, dsouth, dns))
        # print('parallel=%ld east=%ld west=%ld we=%ld', (parallel, east, west, we))
        # print('parallel=%ld east=%f west=%f we=%f', (parallel, deast, dwest, dwe))

    def __x(self, h, name):
        print("%s=%ld " % (name, self._get(h, name)), end="")

    # def __check_parameter(self, h, min_value, max_value):
    #     best = -1
    #     match = -1
    #     i = 0
    #
    #     for parameter in parameters:
    #         j = 0
    #         matches = 0
    #         for pair in parameter["pairs"]:
    #             val = -1
    #             if pair["key_type"] == "int":
    #                 try:
    #                     val = codes_get_long(h, pair["key"])
    #                     if pair["value_long"] == val:
    #                         matches += 1
    #                 except:
    #                     pass
    #             elif pair["key_type"] == "str":
    #                 if self.__is_uerra and pair["key"].lower() == "model":
    #                     # print("Skipping model keyword for UERRA class")
    #                     matches += 1  # xxx hack to pretend that model key was matched.
    #                 else:
    #                     if pair["value_string"].lower() == "MISSING".lower():
    #                         is_miss = codes_is_missing(h, pair["key"])
    #                         if is_miss != 0:
    #                             matches += 1
    #                     # elif codes_get_string(h, pair['key']):
    #                     else:
    #                         try:
    #                             strval = codes_get_string(h, pair["key"])
    #                             if pair["value_string"] == strval:
    #                                 matches += 1
    #                         except:
    #                             pass
    #             else:
    #                 assert "Unknown key type"
    #                 sys.exit(1)
    #
    #             j += 1
    #             # if 0
    #             #     print("%s %s %ld val -> %d %d %d" % (
    #             #             pair.key,
    #             #             pair.value_string,
    #             #             val,
    #             #             matches,
    #             #             j,
    #             #             best))
    #             # endif
    #
    #         if matches == j and matches > best:
    #             best = matches
    #             match = i
    #         i += 1
    #
    #     if match >= 0:
    #         self.__param = parameters[match]["name"]
    #         i = 0
    #         # j = 0
    #         for check_func in parameters[match]["checks"]:
    #             self._check_map[check_func](h, parameters[match], min_value, max_value)
    #             i += 1
    #             # print('=========================')
    #             # print('%s -> %d %d' , (self.__param, match, best))
    #             # for pair in  parameters[match].pairs:
    #             #     print('%s val -> %ld %d' % (pair['key'], pair['value'], j))
    #             #     j += 1
    #             # print('matched parameter: %s' % self.__param)
    #     else:
    #         print(
    #             "%s, field %d [%s]: cannot match parameter"
    #             % (self.__filename, self.__field, self.__param)
    #         )
    #         self.__x(h, "origin")
    #         self.__x(h, "discipline")
    #         self.__x(h, "parameterCategory")
    #         self.__x(h, "parameterNumber")
    #         self.__x(h, "typeOfFirstFixedSurface")
    #         self.__x(h, "scaleFactorOfFirstFixedSurface")
    #         self.__x(h, "scaledValueOfFirstFixedSurface")
    #         self.__x(h, "typeOfSecondFixedSurface")
    #         self.__x(h, "scaleFactorOfSecondFixedSurface")
    #         self.__x(h, "scaledValueOfSecondFixedSurface")
    #         print("")
    #         self.__error += 1

    def __check_packing(self, h):
        # ECC-1009: Warn if not using simple packing
        expected_packingType = "grid_simple"
        packingType = codes_get_string(h, "packingType")

        if packingType != expected_packingType:
            print(
                "warning: %s, field %d [%s]: invalid packingType %s (Should be %s)"
                % (
                    self.__filename,
                    self.__field,
                    self.__param,
                    packingType,
                    expected_packingType,
                )
            )
            self.__warning += 1

    def __verify(self, h):
        min_value = 0
        max_value = 0

        self._check('eq(h,"editionNumber",2)', self._eq(h, "editionNumber", 2))
        # self._check('missing(h,"reserved")||eq(h,"reserved",0)',
        # self.__missing(h, 'reserved') or self.__eq(h, 'reserved', 0))

        if self.__valueflg:
            count = 0
            try:
                count = codes_get_size(h, "values")
            except Exception as e:
                print(
                    "%s, field %d [%s]: cannot get number of values: %s"
                    % (self.__filename, self.__field, self.__param, str(e))
                )
                self.__error += 1
                return

            bitmap = not self._eq(h, "bitMapIndicator", 255)
            self._check(
                'eq(h,"numberOfDataPoints",count)',
                self._eq(h, "numberOfDataPoints", count),
            )
            n = count

            try:
                self.__values = codes_get_double_array(h, "values")
            except Exception as e:
                print(
                    "%s, field %d [%s]: cannot get values: %s"
                    % (self.__filename, self.__field, self.__param, str(e))
                )
                self.__error += 1
                return

            if n != count:
                print(
                    "%s, field %d [%s]: value count changed %ld -> %ld"
                    % (self.__filename, self.__field, self.__param, count, n)
                )
                self.__error += 1
                return

            if bitmap:
                missing = self._dget(h, "missingValue")
                min_value = max_value = missing
                for value in self.__values:
                    if (min_value == missing) or (
                        (value != missing) and (min_value > value)
                    ):
                        min_value = value
                    if (max_value == missing) or (
                        (value != missing) and (max_value < value)
                    ):
                        max_value = value
            else:
                min_value = max_value = self.__values[0]
                for value in self.__values:
                    if min_value > value:
                        min_value = value
                    if max_value < value:
                        max_value = value

        self._check_parameter(h, min_value, max_value)
        self.__check_packing(h)
        # Section 1

        self._check(
            'ge(h,"gribMasterTablesVersionNumber",4)',
            self._ge(h, "gribMasterTablesVersionNumber", 4),
        )
        self._check(
            'eq(h,"versionNumberOfGribLocalTables",0)',
            self._eq(h, "versionNumberOfGribLocalTables", 0),
        )  # Local tables not used

        self._check(
            'eq(h,"significanceOfReferenceTime",1)',
            self._eq(h, "significanceOfReferenceTime", 1),
        )  # Start of forecast

        if not self.__is_s2s:
            # todo check for how many years back the reforecast is done? Is it coded in the grib???
            # Check if the date is OK
            date = self._get(h, "date")
            # self._check(date > 20060101);
            self._check(
                '(date / 10000) == get(h,"year")',
                int(date / 10000) == self._get(h, "year"),
            )
            self._check(
                '((date % 10000) / 100) == get(h,"month")',
                int((date % 10000) / 100) == self._get(h, "month"),
            )
            self._check(
                '((date % 100)) == get(h,"day")',
                (int(date % 100)) == self._get(h, "day"),
            )

        if self.__is_uerra:
            self._check('le(h,"hour",24)', self._le(h, "hour", 24))
        elif self.__is_lam:
            self._check(
                'eq(h,"hour",0)||eq(h,"hour",3)||eq(h,"hour",6)||eq(h,"hour",9)||eq(h,"hour",12)||eq(h,"hour",15)||eq(h,"hour",18)||eq(h,"hour",21))',
                self._eq(h, "hour", 0)
                or self._eq(h, "hour", 3)
                or self._eq(h, "hour", 6)
                or self._eq(h, "hour", 9)
                or self._eq(h, "hour", 12)
                or self._eq(h, "hour", 15)
                or self._eq(h, "hour", 18)
                or self._eq(h, "hour", 21),
            )
        else:
            # Only 00, 06 12 and 18 Cycle OK
            self._check(
                'eq(h,"hour",0)||eq(h,"hour",6)||eq(h,"hour",12)||eq(h,"hour",18)',
                self._eq(h, "hour", 0)
                or self._eq(h, "hour", 6)
                or self._eq(h, "hour", 12)
                or self._eq(h, "hour", 18),
            )

        self._check('eq(h,"minute",0)', self._eq(h, "minute", 0))
        self._check('eq(h,"second",0)', self._eq(h, "second", 0))
        self._check('ge(h,"startStep",0)', self._ge(h, "startStep", 0))

        if self.__is_s2s:
            self._check(
                'eq(h,"productionStatusOfProcessedData",6)||eq(h,"productionStatusOfProcessedData",7)',
                self._eq(h, "productionStatusOfProcessedData", 6)
                or self._eq(h, "productionStatusOfProcessedData", 7),
            )  # S2S prod or test
            self._check('le(h,"endStep",100*24)', self._le(h, "endStep", 100 * 24))
        elif not self.__is_uerra:
            self._check(
                'eq(h,"productionStatusOfProcessedData",4)||eq(h,"productionStatusOfProcessedData",5)',
                self._eq(h, "productionStatusOfProcessedData", 4)
                or self._eq(h, "productionStatusOfProcessedData", 5),
            )  # TIGGE prod or test
            self._check('le(h,"endStep",30*24)', self._le(h, "endStep", 30 * 24))

        if self.__is_uerra:
            self._check(
                '(eq(h,"step",1)||eq(h,"step",2)||eq(h,"step",4)||eq(h,"step",5))||(get(h,"step") % 3) == 0)',
                (
                    self._eq(h, "step", 1)
                    or self._eq(h, "step", 2)
                    or self._eq(h, "step", 4)
                    or self._eq(h, "step", 5)
                )
                or (self._get(h, "step") % 3) == 0,
            )
        elif self.__is_lam:
            self._check('(get(h,"step") % 3) == 0', (self._get(h, "step") % 3) == 0)
        else:
            self._check('(get(h,"step") % 6) == 0', (self._get(h, "step") % 6) == 0)

        if self.__is_uerra:
            if self.__is_crra:
                self._check(
                    'eq(h,"productionStatusOfProcessedData",10)||eq(h,"productionStatusOfProcessedData",11)',
                    self._eq(h, "productionStatusOfProcessedData", 10)
                    or self._eq(h, "productionStatusOfProcessedData", 11),
                )  # CRRA prodortest
            else:
                self._check(
                    'eq(h,"productionStatusOfProcessedData",8)||eq(h,"productionStatusOfProcessedData",9)',
                    self._eq(h, "productionStatusOfProcessedData", 8)
                    or self._eq(h, "productionStatusOfProcessedData", 9),
                )  #  UERRA prodortest
            self._check('le(h,"endStep",30)', self._le(h, "endStep", 30))
            # 0 = analysis , 1 = forecast
            self._check(
                'eq(h,"typeOfProcessedData",0)||eq(h,"typeOfProcessedData",1)',
                self._eq(h, "typeOfProcessedData", 0)
                or self._eq(h, "typeOfProcessedData", 1),
            )
            if self._get(h, "typeOfProcessedData") == 0:
                self._check('eq(h,"step",0)', self._eq(h, "step", 0))
            else:
                self._check(
                    '(eq(h,"step",1)||eq(h,"step",2)||eq(h,"step",4)||eq(h,"step",5))||(get(h,"step") % 3) == 0)',
                    (
                        self._eq(h, "step", 1)
                        or self._eq(h, "step", 2)
                        or self._eq(h, "step", 4)
                        or self._eq(h, "step", 5)
                    )
                    or (self._get(h, "step") % 3) == 0,
                )
        else:
            # 2 = analysis or forecast , 3 = control forecast, 4 = perturbed forecast
            self._check(
                'eq(h,"typeOfProcessedData",2)||eq(h,"typeOfProcessedData",3)||eq(h,"typeOfProcessedData",4)',
                self._eq(h, "typeOfProcessedData", 2)
                or self._eq(h, "typeOfProcessedData", 3)
                or self._eq(h, "typeOfProcessedData", 4),
            )

        # TODO: validate local usage. Empty for now xxx
        # self._check('eq(h,"section2.sectionLength",5)', self.__eq(h,"section2.sectionLength",5))

        # Section 3

        self._check(
            'eq(h,"sourceOfGridDefinition",0)',
            self._eq(h, "sourceOfGridDefinition", 0),
        )  # Specified in Code table 3.1

        dtn = self._get(h, "gridDefinitionTemplateNumber")

        if dtn in [0, 1]:
            # gridDefinitionTemplateNumber == 1: rotated latlon
            self.__latlon_grid(h)
        elif dtn == 30:  # Lambert conformal
            # lambert_grid(h); # TODO xxx
            # print('warning: Lambert grid - geometry checking not implemented yet!')
            # self._check('eq(h,"scanningMode",64)', self.__eq(h, 'scanningMode', 64)) /* M-F data used to have it wrong.. but it might depends on other projection set up as well!
            pass
        elif dtn == 40:  # gaussian grid (regular or reduced)
            version_string = codes_get_version_info()
            version = [int(v) for v in version_string["bindings"].split(".")]
            if version[0] >= 1 and version[1] >= 5:
                self.__gaussian_grid(h)
            else:
                # raise(Exception('Require eccodes-python 1.5.0 or higher'))
                print(
                    "WARNING: Require eccodes-python 1.5.0 or higher for checking gaussian grids"
                )
        else:
            print(
                "%s, field %d [%s]: Unsupported gridDefinitionTemplateNumber %ld"
                % (
                    self.__filename,
                    self.__field,
                    self.__param,
                    self._get(h, "gridDefinitionTemplateNumber"),
                )
            )
            self.__error += 1
            return

        # If there is no bitmap, this should be true
        # self._check('eq(h,"bitMapIndicator",255)', self.__eq(h,"bitMapIndicator",255))

        if self._eq(h, "bitMapIndicator", 255):
            self._check(
                'get(h,"numberOfValues") == get(h,"numberOfDataPoints")',
                self._get(h, "numberOfValues") == self._get(h, "numberOfDataPoints"),
            )
        else:
            self._check(
                'get(h,"numberOfValues") <= get(h,"numberOfDataPoints")',
                self._get(h, "numberOfValues") <= self._get(h, "numberOfDataPoints"),
            )

        # Check values
        self._check(
            'eq(h,"typeOfOriginalFieldValues",0)',
            self._eq(h, "typeOfOriginalFieldValues", 0),
        )  # Floating point

        self.__check_validity_datetime(h)

        # do not store empty values e.g. fluxes at step 0
        #    todo ?? now it's allowed in the code here!
        #    if not self.__missing(h, 'typeOfStatisticalProcessing'):
        #      self._check('ne(h,"stepRange",0)', self.__ne(h,"stepRange",0))

    # def validate(self, path):
    #     count = 0
    #     self.__filename = path
    #     self.__field = 0
    #     try:
    #         f = open(path, "rb")
    #     except Exception as e:
    #         print("%s: %s" % (path, str(e)))
    #         self.__error += 1
    #         return
    #
    #     while 1:
    #         try:
    #             handle = codes_grib_new_from_file(f)
    #         except Exception as e:
    #             print("%s: grib_handle_new_from_file: %s" % (path, str(e)))
    #             self.__error += 1
    #             return
    #
    #         if handle is None:
    #             break
    #
    #         last_error = self.__error
    #         last_warning = self.__warning
    #         self.__field += 1
    #         self.__verify(handle)
    #         if (last_error != self.__error) or (
    #             (self.__warnflg != 0) and (last_warning != self.__warning)
    #         ):
    #             self.__save(handle, self.__bad, self.__fbad)
    #         else:
    #             self.__save(handle, self.__good, self.__fgood)
    #
    #         codes_release(handle)
    #         count = count + 1
    #         self.__param = "unknown"
    #
    #     if count == 0:
    #         print("%s does not contain any GRIBs" % path)
    #         self.__error += 1
    #         return
    #
    # def get_error_counter(self):
    #     return self.__error
    #
    # def get_warning_counter(self):
    #     return self.__warning
