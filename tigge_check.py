#!/usr/bin/env python3

from eccodes import *
import sys
from pathlib import Path
import math
import os
import argparse
from tigge_check_parameters import parameters
import numpy as np
from shared import *

# static
last_n = 0
values = None

# global
class Config:
    def __init__(self):
        self.filename = ''
        self.error = 0
        self.warning = 0
        self.field = 0
        self.param = "unknown"
        self.valueflg = False
        self.warnflg = False
        self.zeroflg = False
        self.is_lam = False
        self.is_s2s = False
        self.is_s2s_refcst= False
        self.is_uerra = False
        self.is_crra = False
        self.good = ''
        self.bad = ''
        self.fgood = None
        self.fbad = None

cfg = Config()

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def CHECK(name, a):
    check(name, a)

def check(name, a):
    global cfg
    if not a:
        print("%s, field %d [%s]: %s failed" % (cfg.filename, cfg.field, cfg.param, name))
        cfg.error += 1

#/*
#def warn(const char* name,int a)
#{
    #if(!a) {
        #printf("%s, field %d [%s]: %s failed",filename,field,param,name);
        #warning++;
    #}
#}
#*/

def save(h, name, f):
    if f == None:
        return
    try:
        buffer = codes_get_message(h)
    except Exception as e:
        print("%s, field %d [%s]: cannot get message: %s\n" % (cfg.filename, cfg.field, cfg.param, str(e)))
        sys.exit(1)
    try:
        f.write(bytearray(buffer))
    except Exception as e:
        print(str(e))
        sys.exit(1)

def get(h, what) -> int:
    try:
        val = codes_get_long(h, what)
    except Exception as e:
        print("%s, field %d [%s]: cannot get %s: %s" % (cfg.filename, cfg.field, cfg.param, what, str(e)))
        cfg.error += 1;
        val = -1;
    return val;

def dget(h, what) -> float:
    try:
        val = codes_get_double(h, what)
    except Exception as e:
        print("%s, field %d [%s]: cannot get %s: %s" % (cfg.filename, cfg.field, cfg.param, what, str(e)))
        cfg.error += 1;
        val = -1;
    return val;

def missing(h, what) -> int:
    try:
        return codes_is_missing(h, what)
    except KeyValueNotFoundError as e:
        return 1

def eq(h, what, value) -> int:
    return get(h, what) == value

def ne(h, what, value) -> int:
    return get(h,what) != value

def ge(h, what, value) -> int:
    return get(h, what) >= value

def le(h, what, value) -> int:
    return get(h, what) <= value

def DBL_EQUAL(d1, d2, tolerance) -> int:
    return math.fabs(d1 - d2) <= tolerance

def gaussian_grid(h):
    global last_n
    global values

    tolerance = 1.0/1000000.0; # angular tolerance for grib2: micro degrees
    n = get(h,"numberOfParallelsBetweenAPoleAndTheEquator"); # This is the key N

    north = dget(h,"latitudeOfFirstGridPointInDegrees")
    south = dget(h,"latitudeOfLastGridPointInDegrees")

    west = dget(h,"longitudeOfFirstGridPointInDegrees")
    east = dget(h,"longitudeOfLastGridPointInDegrees")

    if n != last_n:
        try:
            values = codes_get_gaussian_latitudes(n)
        except:
            print("%s, field %d [%s]: cannot get gaussian latitudes for N%ld: %s" % (cfg.filename, cfg.field, cfg.param,n, str(e)))
            cfg.error += 1
            last_n = 0
            return
        last_n = n;

    # TODO
    if values == None:
        assert(0)
        return

    if values != None:
        values[0] = np.rint(values[0] * 1e6) / 1e6;

    if not DBL_EQUAL(north, values[0], tolerance) or not DBL_EQUAL(south, -values[0], tolerance):
        print("N=%ld north=%f south=%f v(=gauss_lat[0])=%f north-v=%0.30f south-v=%0.30f" % (n, north, south, values[0], north-values[0], south+values[0]))

    CHECK('DBL_EQUAL(north, values[0], tolerance)', DBL_EQUAL(north, values[0], tolerance))
    CHECK('DBL_EQUAL(south, -values[0], tolerance)', DBL_EQUAL(south, -values[0], tolerance))

    if(missing(h,"numberOfPointsAlongAParallel")): # same as key Ni 
        # If missing, this is a REDUCED gaussian grid 
        MAXIMUM_RESOLUTION = 640;
        CHECK('get(h,"PLPresent")', get(h,"PLPresent"))
        CHECK('DBL_EQUAL(west, 0.0, tolerance)', DBL_EQUAL(west, 0.0, tolerance))
        if n > MAXIMUM_RESOLUTION:
            print("Gaussian number N (=%ld) cannot exceed %ld" % (n, MAXIMUM_RESOLUTION))
            CHECK('n <= MAXIMUM_RESOLUTION', n <= MAXIMUM_RESOLUTION)
    else:
        # REGULAR gaussian grid 
        l_west = get(h,"longitudeOfFirstGridPoint")
        l_east = get(h,"longitudeOfLastGridPoint")
        parallel = get(h,"numberOfPointsAlongAParallel")
        we = get(h,"iDirectionIncrement")
        dwest = dget(h,"longitudeOfFirstGridPointInDegrees")
        deast = dget(h,"longitudeOfLastGridPointInDegrees")
        dwe = dget(h,"iDirectionIncrementInDegrees")
        # printf("parallel=%ld east=%ld west=%ld we=%ld",parallel,east,west,we)

        CHECK('parallel == (l_east-l_west)/we + 1', parallel == (l_east-l_west)/we + 1)
        CHECK('abs((deast-dwest)/dwe + 1 - parallel) < 1e-10', abs((deast-dwest)/dwe + 1 - parallel) < 1e-10)
        CHECK('not get(h,"PLPresent")', not get(h,"PLPresent"))

    CHECK('ne(h,"Nj",0)', ne(h,"Nj",0))

    get(h,"PLPresent")

    i = 0
    count = codes_get_size(h,"pl")
    expected_lon2 = 0
    total = 0
    max_pl = 0
    numberOfValues = get(h,"numberOfValues")
    numberOfDataPoints = get(h,"numberOfDataPoints")


    pl = codes_get_double_array(h,"pl")

    if len(pl) != count:
        print("len(pl)=%ld count=%ld" % (len(pl), count))

    CHECK('len(pl) == count', len(pl) == count)
    CHECK('len(pl) == 2*n', len(pl) == 2*n)

    total = 0;
    max_pl = pl[0]; #  max elem of pl array = num points at equator

    for p in pl:
        total = total + p
        if p > max_pl:
            max_pl = p


    # Do not assume maximum of pl array is 4N! not true for octahedral

    expected_lon2 = 360.0 - 360.0/max_pl;
    if not DBL_EQUAL(expected_lon2, east, tolerance):
        print("east actual=%g expected=%g diff=%g",east, expected_lon2, expected_lon2-east)

    CHECK('DBL_EQUAL(expected_lon2, east, tolerance)', DBL_EQUAL(expected_lon2, east, tolerance))

    if numberOfDataPoints != total:
        print("GAUSS numberOfValues=%ld numberOfDataPoints=%ld sum(pl)=%ld" % (
                numberOfValues,
                numberOfDataPoints,
                total))

    CHECK('numberOfDataPoints == total', numberOfDataPoints == total)

    CHECK('missing(h,"iDirectionIncrement")', missing(h,"iDirectionIncrement"))
    CHECK('missing(h,"iDirectionIncrementInDegrees")', missing(h,"iDirectionIncrementInDegrees"))

    CHECK('eq(h,"iDirectionIncrementGiven",0)', eq(h,"iDirectionIncrementGiven",0))
    CHECK('eq(h,"jDirectionIncrementGiven",1)', eq(h,"jDirectionIncrementGiven",1))

    CHECK('eq(h,"resolutionAndComponentFlags1",0)', eq(h,"resolutionAndComponentFlags1",0))
    CHECK('eq(h,"resolutionAndComponentFlags2",0)', eq(h,"resolutionAndComponentFlags2",0))
    CHECK('eq(h,"resolutionAndComponentFlags6",0)', eq(h,"resolutionAndComponentFlags6",0))
    CHECK('eq(h,"resolutionAndComponentFlags7",0)', eq(h,"resolutionAndComponentFlags7",0))
    CHECK('eq(h,"resolutionAndComponentFlags8",0)', eq(h,"resolutionAndComponentFlags8",0))

def check_validity_datetime(h):
    global cfg
    # If we just set the stepRange (for non-instantaneous fields) to its
    # current value, then this causes the validity date and validity time
    # keys to be correctly computed.
    # Then we can compare the previous (possibly wrongly coded) value with
    # the newly computed one

    stepType = codes_get_string(h, "stepType")

    if stepType != "instant": # not instantaneous
        # Check only applies to accumulated, max etc.
        stepRange = codes_get_string(h, "stepRange")

        saved_validityDate = get(h, "validityDate")
        saved_validityTime = get(h, "validityTime")

        codes_set_string(h, "stepRange", stepRange);

        validityDate = get(h, "validityDate");
        validityTime = get(h, "validityTime");
        if validityDate!=saved_validityDate or validityTime!=saved_validityTime:
            print("warning: %s, field %d [%s]: invalid validity Date/Time (Should be %ld and %ld)" % (cfg.filename, cfg.field, cfg.param, validityDate, validityTime))
            cfg.warning += 1

def check_range(h, p, min_value, max_value):
    global cfg
    missing = 0;
    if cfg.valueflg != 0:
        return

    missing = dget(h,"missingValue")

    # See ECC-437
    if not get(h,"bitMapIndicator") == 0 and min_value == missing and max_value == missing:
        if min_value < p['min1'] or min_value > p['min2']: 
            print("warning: %s, field %d [%s]: %s minimum value %g is not in [%g,%g]" % (cfg.filename, cfg.field, cfg.param, p['name'], min_value, p['min1'], p['min2']))
            print("  => [%g,%g]" % (min_value if min_value < p['min1'] else p['min1'], min_value if min_value > p['min2'] else p['min2']))
            cfg.warning += 1

        if max_value < p['max1'] or max_value > p['max2']:
            print("warning: %s, field %d [%s]: %s maximum value %g is not in [%g,%g]" % (cfg.filename, cfg.field, cfg.param, p['name'], max_value, p['max1'], p['max2']))
            print("  => [%g,%g]" % (max_value if max_value < p['max1'] else p['max1'], max_value if max_value > p['max2'] else p['max2']))
            cfg.warning += 1


def point_in_time(h, p, min_value, max_value):
    global cfg
    topd = get(h,"typeOfProcessedData")

    if topd == 0: # Analysis
        if cfg.is_uerra:
            CHECK('eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1))
        if get(h,"productDefinitionTemplateNumber") == 1:
            CHECK('ne(h,"numberOfForecastsInEnsemble",0)', ne(h,"numberOfForecastsInEnsemble",0))
            CHECK('le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble"))', le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")))

    elif topd == 1: # Forecast
        if cfg.is_uerra:
            CHECK('eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1))
        if get(h,"productDefinitionTemplateNumber") == 1:
            CHECK('ne(h,"numberOfForecastsInEnsemble",0)', ne(h,"numberOfForecastsInEnsemble",0))
            CHECK('le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble"))', le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")))

    elif topd == 2: # Analysis and forecast products
        CHECK('eq(h,"productDefinitionTemplateNumber",0)', eq(h,"productDefinitionTemplateNumber",0))

    elif topd == 3: # Control forecast products 
        CHECK('eq(h,"perturbationNumber",0)', eq(h,"perturbationNumber",0))
        CHECK('ne(h,"numberOfForecastsInEnsemble",0)', ne(h,"numberOfForecastsInEnsemble",0))
        if cfg.is_s2s_refcst:
            CHECK('eq(h,"productDefinitionTemplateNumber",60)', eq(h,"productDefinitionTemplateNumber",60))
        elif cfg.is_s2s:
            # CHECK('eq(h,"productDefinitionTemplateNumber",60) or eq(h,"productDefinitionTemplateNumber",11) or eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",60) or eq(h,"productDefinitionTemplateNumber",11) or eq(h,"productDefinitionTemplateNumber",1))
            CHECK('eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",1))
        else:
            CHECK('eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",1))

    elif topd == 4: # Perturbed forecast products
        CHECK('ne(h,"perturbationNumber",0)', ne(h,"perturbationNumber",0))
        CHECK('ne(h,"numberOfForecastsInEnsemble",0)', ne(h,"numberOfForecastsInEnsemble",0))
        if cfg.is_s2s_refcst:
            CHECK('eq(h,"productDefinitionTemplateNumber",60)', eq(h,"productDefinitionTemplateNumber",60))
        elif cfg.is_s2s:
            # CHECK('eq(h,"productDefinitionTemplateNumber",60) or eq(h,"productDefinitionTemplateNumber",11) or eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",60) or eq(h,"productDefinitionTemplateNumber",11) or eq(h,"productDefinitionTemplateNumber",1))
            CHECK('eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",1))
        else:
            CHECK('eq(h,"productDefinitionTemplateNumber",1)', eq(h,"productDefinitionTemplateNumber",1));
        if cfg.is_lam:
            CHECK('le(h,"perturbationNumber", get(h,"numberOfForecastsInEnsemble"))', le(h,"perturbationNumber", get(h,"numberOfForecastsInEnsemble")))
        else:
            # Is there always cf in tigge global datasets??
            CHECK('le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")-1)', le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")-1))

    else:
        print("Unsupported typeOfProcessedData %ld" % get(h,"typeOfProcessedData"))
        CHECK('0', 0)

    if cfg.is_lam:
        if get(h,"indicatorOfUnitOfTimeRange") == 10: # three hours
            # Three hourly is OK 
            pass
        else:
            CHECK('eq(h,"indicatorOfUnitOfTimeRange",1)', eq(h,"indicatorOfUnitOfTimeRange",1)) # Hours
            CHECK('(get(h,"forecastTime) % 3) == 0"', (get(h,"forecastTime") % 3) == 0) # Every three hours
    elif cfg.is_uerra:
        if(get(h,"indicatorOfUnitOfTimeRange") == 1): #hourly
            CHECK(
                '(eq(h,"forecastTime",1) or eq(h,"forecastTime",2) or eq(h,"forecastTime",4) or eq(h,"forecastTime",5)) or (get(h,"forecastTime") % 3) == 0',
                 (eq(h,"forecastTime",1) or eq(h,"forecastTime",2) or eq(h,"forecastTime",4) or eq(h,"forecastTime",5)) or (get(h,"forecastTime") % 3) == 0)
    else:
        if get(h,"indicatorOfUnitOfTimeRange") == 11: #six hour
            # Six hourly is OK
            pass
        else:
            CHECK('eq(h,"indicatorOfUnitOfTimeRange",1)', eq(h,"indicatorOfUnitOfTimeRange",1)) # Hours
            CHECK('(get(h,"forecastTime) % 6) == 0"', (get(h,"forecastTime") % 6) == 0) # Every six hours

    check_range(h, p, min_value, max_value)

def height_level(h, p, min_value, max_value):
    global cfg
    level = get(h, "level");
    levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500]
    if cfg.is_uerra:
        if level in levels:
            pass
        else:
            print("%s, field %d [%s]: invalid height level %ld" % (cfg.filename, cfg.field, cfg.param, level))
            cfg.error += 1

def pressure_level(h, p, min_value, max_value):
    global cfg
    level = get(h,"level");

    if cfg.is_uerra and not cfg.is_crra:
        if level in [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10]:
            pass
        else:
            print("%s, field %d [%s]: invalid pressure level %ld" % (cfg.filename, cfg.field, cfg.param, level))
            cfg.error += 1
    elif cfg.is_uerra and cfg.is_crra:
        if level in [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1]:
            pass
        else:
            print("%s, field %d [%s]: invalid pressure level %ld" % (cfg.filename, cfg.field, cfg.param, level))
            cfg.error += 1
    elif cfg.is_s2s:
        if level in [1000, 925, 850, 700, 500, 300, 200, 100, 50, 10]:
            pass
        else:
            print("%s, field %d [%s]: invalid pressure level %ld" % (cfg.filename, cfg.field, cfg.param, level))
            cfg.error += 1
    else:
        if level in [1000, 200, 250, 300, 500, 700, 850, 925, 50]:
            pass
        else:
            print("%s, field %d [%s]: invalid pressure level %ld" % (cfg.filename, cfg.field, cfg.param, level))
            cfg.error += 1

def potential_vorticity_level(h, p, min_value, max_value):
    global cfg
    level = get(h, "level")
    if level == 2:
        pass
    else:
        print("%s, field %d [%s]: invalid potential vorticity level %ld" % (cfg.filename, cfg.field, cfg.param, level))
        cfg.error += 1

def potential_temperature_level(h, p, min_value, max_value):
    global cfg
    level = get(h, "level")
    if level == 320:
        pass
    else:
        print("%s, field %d [%s]: invalid potential temperature level %ld" % (cfg.filename, cfg.field, cfg.param, level))
        cfg.error += 1

def statistical_process(h, p, min_value, max_value):
    global cfg
    topd = get(h, "typeOfProcessedData")

    if topd ==  0: # Analysis
        if cfg.is_uerra:
            CHECK('eq(h,"productDefinitionTemplateNumber",8) or eq(h,"productDefinitionTemplateNumber",11)', eq(h,"productDefinitionTemplateNumber",8) or eq(h,"productDefinitionTemplateNumber",11))
    elif topd == 1: # Forecast
        if cfg.is_uerra:
            CHECK('eq(h,"productDefinitionTemplateNumber",8) or eq(h,"productDefinitionTemplateNumber",11)', eq(h,"productDefinitionTemplateNumber",8) or eq(h,"productDefinitionTemplateNumber",11))
    elif topd == 2: # Analysis and forecast products
        CHECK('eq(h,"productDefinitionTemplateNumber",8)', eq(h,"productDefinitionTemplateNumber",8))
    elif topd == 3: # Control forecast products
        if not cfg.is_s2s_refcst:
            CHECK('eq(h,"productDefinitionTemplateNumber",11)', eq(h,"productDefinitionTemplateNumber",11))
        else:
            CHECK('eq(h,"productDefinitionTemplateNumber",61)', eq(h,"productDefinitionTemplateNumber",61))
    elif topd == 4: # Perturbed forecast products
        if not cfg.is_s2s_refcst:
            CHECK('eq(h,"productDefinitionTemplateNumber",11)', eq(h,"productDefinitionTemplateNumber",11))
        else:
            CHECK('eq(h,"productDefinitionTemplateNumber",61)', eq(h,"productDefinitionTemplateNumber",61))
    else:
        print("Unsupported typeOfProcessedData %ld" % (get(h,"typeOfProcessedData")))
        cfg.error += 1
        return;

    if cfg.is_lam:
        if get(h,"indicatorOfUnitOfTimeRange") == 10: # three hours
            # Three hourly is OK
            pass
        else:
            CHECK('eq(h,"indicatorOfUnitOfTimeRange",1)', eq(h,"indicatorOfUnitOfTimeRange",1)) # Hours
            CHECK('(get(h,"forecastTime"', (get(h,"forecastTime") % 3) == 0); # Every three hours
    elif cfg.is_uerra:
#  forecastTime for uerra might be all steps decreased by 1 i.e 0,1,2,3,4,5,8,11...29 too many... */
        if get(h,"indicatorOfUnitOfTimeRange") == 1:
            CHECK('le(h,"forecastTime",30)', le(h,"forecastTime",30))
    else:
        if get(h,"indicatorOfUnitOfTimeRange") == 11: # six hours
            # Six hourly is OK
            pass
        else:
            CHECK('eq(h,"indicatorOfUnitOfTimeRange",1)', eq(h,"indicatorOfUnitOfTimeRange",1)); # Hours
            CHECK('(get(h,"forecastTime"', (get(h,"forecastTime") % 6) == 0); # Every six hours

    CHECK('eq(h,"numberOfTimeRange",1)', eq(h,"numberOfTimeRange",1))
    CHECK('eq(h,"numberOfMissingInStatisticalProcess",0)', eq(h,"numberOfMissingInStatisticalProcess",0))
    CHECK('eq(h,"typeOfTimeIncrement",2)', eq(h,"typeOfTimeIncrement",2))
    # CHECK('eq(h,"indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed",255)', eq(h,"indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed",255))

    if cfg.is_s2s:
        if get(h,"typeOfStatisticalProcessing") == 0:
            CHECK('eq(h,"timeIncrementBetweenSuccessiveFields",1) or eq(h,"timeIncrementBetweenSuccessiveFields",4)', eq(h,"timeIncrementBetweenSuccessiveFields",1) or eq(h,"timeIncrementBetweenSuccessiveFields",4))
        else:
            CHECK('eq(h,"timeIncrementBetweenSuccessiveFields",0)', eq(h,"timeIncrementBetweenSuccessiveFields",0))
    else:
        CHECK('eq(h,"timeIncrementBetweenSuccessiveFields",0)', eq(h,"timeIncrementBetweenSuccessiveFields",0))

    CHECK('eq(h,"minuteOfEndOfOverallTimeInterval",0)', eq(h,"minuteOfEndOfOverallTimeInterval",0))
    CHECK('eq(h,"secondOfEndOfOverallTimeInterval",0)', eq(h,"secondOfEndOfOverallTimeInterval",0))

    if cfg.is_uerra:
        CHECK('(eq(h,"endStep",1) or eq(h,"endStep",2) or eq(h,"endStep",4) or eq(h,"endStep",5)) or (get(h,"endStep"', (eq(h,"endStep",1) or eq(h,"endStep",2) or eq(h,"endStep",4) or eq(h,"endStep",5)) or (get(h,"endStep") % 3) == 0)
    elif cfg.is_lam:
        CHECK('(get(h,"endStep"', (get(h,"endStep") % 3) == 0);  # Every three hours
    else:
        CHECK('(get(h,"endStep"', (get(h,"endStep") % 6) == 0); # Every six hours

    if get(h,"indicatorOfUnitForTimeRange") == 11:
        # Six hourly is OK
        CHECK('get(h,"lengthOfTimeRange")*6 + get(h,"startStep") == get(h,"endStep")', get(h,"lengthOfTimeRange")*6 + get(h,"startStep") == get(h,"endStep"))
    elif get(h,"indicatorOfUnitForTimeRange") == 10:
        # Three hourly is OK
        CHECK('get(h,"lengthOfTimeRange")*3 + get(h,"startStep") == get(h,"endStep")', get(h,"lengthOfTimeRange")*3 + get(h,"startStep") == get(h,"endStep"))
    else:
        CHECK('eq(h,"indicatorOfUnitForTimeRange",1)', eq(h,"indicatorOfUnitForTimeRange",1)) # Hours
        CHECK('get(h,"lengthOfTimeRange") + get(h,"startStep") == get(h,"endStep")', get(h,"lengthOfTimeRange") + get(h,"startStep") == get(h,"endStep"))

def has_bitmap(h, p, min_value, max_value):
    # printf("bitMapIndicator %ld",get(h,"bitMapIndicator"))
    CHECK('eq(h,"bitMapIndicator",0)', eq(h,"bitMapIndicator",0))

def has_soil_level(h, p, min_value, max_value):
    CHECK('get(h,"topLevel") == get(h,"bottomLevel")', get(h,"topLevel") == get(h,"bottomLevel"))
    CHECK('le(h,"level",14)', le(h,"level",14)); # max in UERRA

def has_soil_layer(h, p, min_value, max_value):
    CHECK('get(h,"topLevel") == get(h,"bottomLevel") - 1', get(h,"topLevel") == get(h,"bottomLevel") - 1)
    CHECK('le(h,"level",14)', le(h,"level",14)); # max in UERRA

def resolution_s2s(h, p, min_value, max_value):
    CHECK('eq(h,"iDirectionIncrement",1500000)', eq(h,"iDirectionIncrement",1500000))
    CHECK('eq(h,"jDirectionIncrement",1500000)', eq(h,"jDirectionIncrement",1500000))

def resolution_s2s_ocean(h, p, min_value, max_value):
    CHECK('eq(h,"iDirectionIncrement",1000000)', eq(h,"iDirectionIncrement",1000000))
    CHECK('eq(h,"jDirectionIncrement",1000000)', eq(h,"jDirectionIncrement",1000000))

def six_hourly(h, p, min_value, max_value):
    statistical_process(h,p,min_value,max_value);

    if get(h,"indicatorOfUnitForTimeRange") == 11:
        CHECK('eq(h,"lengthOfTimeRange",1)', eq(h,"lengthOfTimeRange",1))
    else:
        CHECK('eq(h,"lengthOfTimeRange",6)', eq(h,"lengthOfTimeRange",6))

    CHECK('get(h,"endStep") == get(h,"startStep") + 6', get(h,"endStep") == get(h,"startStep") + 6)
    check_range(h,p,min_value,max_value)

def since_prev_pp(h, p, min_value, max_value):
    statistical_process(h,p,min_value,max_value)
    CHECK('eq(h,"indicatorOfUnitForTimeRange",1)', eq(h,"indicatorOfUnitForTimeRange",1))
    CHECK('get(h,"endStep") == get(h,"startStep") + get(h,"lengthOfTimeRange")', get(h,"endStep") == get(h,"startStep") + get(h,"lengthOfTimeRange"))
    check_range(h,p,min_value,max_value)

def three_hourly(h, p, min_value, max_value):
    statistical_process(h,p,min_value,max_value)

    if get(h,"indicatorOfUnitForTimeRange") == 11:
        CHECK('eq(h,"lengthOfTimeRange",1)', eq(h,"lengthOfTimeRange",1))
    else:
        CHECK('eq(h,"lengthOfTimeRange",3)', eq(h,"lengthOfTimeRange",3))

    CHECK('get(h,"endStep") == get(h,"startStep") + 3', get(h,"endStep") == get(h,"startStep") + 3)
    check_range(h,p,min_value,max_value)

def from_start(h, p, min_value, max_value):
    global cfg
    step = get(h,"endStep")
    statistical_process(h,p,min_value,max_value)
    CHECK('eq(h,"startStep",0)', eq(h,"startStep",0))

    if step == 0:
        if not cfg.is_uerra:
            CHECK('min_value == 0 and max_value == 0', min_value == 0 and max_value == 0); # ??? xxx
    else:
        check_range(h,p,min_value/step,max_value/step)

def daily_average(h, p, min_value, max_value):
    step = get(h,"endStep")
    CHECK('get(h,"startStep") == get(h,"endStep") - 24', get(h,"startStep") == get(h,"endStep") - 24)
    statistical_process(h,p,min_value,max_value)

    if step == 0:
        CHECK('min_value == 0 and max_value == 0', min_value == 0 and max_value == 0)
    else:
        check_range(h,p,min_value,max_value)

def given_level(h, p, min_value, max_value):
    CHECK('ne(h,"typeOfFirstFixedSurface",255)', ne(h,"typeOfFirstFixedSurface",255))
    CHECK('not missing(h,"scaleFactorOfFirstFixedSurface")', not missing(h,"scaleFactorOfFirstFixedSurface"))
    CHECK('not missing(h,"scaledValueOfFirstFixedSurface")', not missing(h,"scaledValueOfFirstFixedSurface"))

    CHECK('eq(h,"typeOfSecondFixedSurface",255)', eq(h,"typeOfSecondFixedSurface",255))
    CHECK('missing(h,"scaleFactorOfSecondFixedSurface")', missing(h,"scaleFactorOfSecondFixedSurface"))
    CHECK('missing(h,"scaledValueOfSecondFixedSurface")', missing(h,"scaledValueOfSecondFixedSurface"))

def predefined_level(h, p, min_value, max_value):
    CHECK('ne(h,"typeOfFirstFixedSurface",255)', ne(h,"typeOfFirstFixedSurface",255))
    CHECK('missing(h,"scaleFactorOfFirstFixedSurface")', missing(h,"scaleFactorOfFirstFixedSurface"))
    CHECK('missing(h,"scaledValueOfFirstFixedSurface")', missing(h,"scaledValueOfFirstFixedSurface"))

    CHECK('eq(h,"typeOfSecondFixedSurface",255)', eq(h,"typeOfSecondFixedSurface",255))
    CHECK('missing(h,"scaleFactorOfSecondFixedSurface")', missing(h,"scaleFactorOfSecondFixedSurface"))
    CHECK('missing(h,"scaledValueOfSecondFixedSurface")', missing(h,"scaledValueOfSecondFixedSurface"))

def predefined_thickness(h, p, min_value, max_value):
    CHECK('ne(h,"typeOfFirstFixedSurface",255)', ne(h,"typeOfFirstFixedSurface",255))
    CHECK('missing(h,"scaleFactorOfFirstFixedSurface")', missing(h,"scaleFactorOfFirstFixedSurface"))
    CHECK('missing(h,"scaledValueOfFirstFixedSurface")', missing(h,"scaledValueOfFirstFixedSurface"))

    CHECK('ne(h,"typeOfSecondFixedSurface",255)', ne(h,"typeOfSecondFixedSurface",255))
    CHECK('missing(h,"scaleFactorOfSecondFixedSurface")', missing(h,"scaleFactorOfSecondFixedSurface"))
    CHECK('missing(h,"scaledValueOfSecondFixedSurface")', missing(h,"scaledValueOfSecondFixedSurface"))

def given_thickness(h, p, min_value, max_value):
    CHECK('ne(h,"typeOfFirstFixedSurface",255)', ne(h,"typeOfFirstFixedSurface",255))
    CHECK('not missing(h,"scaleFactorOfFirstFixedSurface")', not missing(h,"scaleFactorOfFirstFixedSurface"))
    CHECK('not missing(h,"scaledValueOfFirstFixedSurface")', not missing(h,"scaledValueOfFirstFixedSurface"))

    CHECK('ne(h,"typeOfSecondFixedSurface",255)', ne(h,"typeOfSecondFixedSurface",255))
    CHECK('not missing(h,"scaleFactorOfSecondFixedSurface")', not missing(h,"scaleFactorOfSecondFixedSurface"))
    CHECK('not missing(h,"scaledValueOfSecondFixedSurface")', not missing(h,"scaledValueOfSecondFixedSurface"))

def latlon_grid(h):
    global cfg
    tolerance = 1.0/1000000.0; # angular tolerance for grib2: micro degrees
    data_points = get(h,"numberOfDataPoints")
    meridian = get(h,"numberOfPointsAlongAMeridian")
    parallel = get(h,"numberOfPointsAlongAParallel")

    north = get(h,"latitudeOfFirstGridPoint")
    south = get(h,"latitudeOfLastGridPoint")
    west = get(h,"longitudeOfFirstGridPoint")
    east = get(h,"longitudeOfLastGridPoint")

    ns= get(h,"jDirectionIncrement")
    we= get(h,"iDirectionIncrement")

    dnorth = dget(h,"latitudeOfFirstGridPointInDegrees")
    dsouth = dget(h,"latitudeOfLastGridPointInDegrees")
    dwest = dget(h,"longitudeOfFirstGridPointInDegrees")
    deast = dget(h,"longitudeOfLastGridPointInDegrees")

    dns = dget(h,"jDirectionIncrementInDegrees")
    dwe = dget(h,"iDirectionIncrementInDegrees")

    if eq(h,"basicAngleOfTheInitialProductionDomain",0):
        CHECK('missing(h,"subdivisionsOfBasicAngle")', missing(h,"subdivisionsOfBasicAngle"))
    else:
        # long basic    = get(h,"basicAngleOfTheInitialProductionDomain")
        # long division = get(h,"subdivisionsOfBasicAngle")
        CHECK('not missing(h,"subdivisionsOfBasicAngle")', not missing(h,"subdivisionsOfBasicAngle"))
        CHECK('not eq(h,"subdivisionsOfBasicAngle",0)', not eq(h,"subdivisionsOfBasicAngle",0))

    if missing(h,"subdivisionsOfBasicAngle"):
        CHECK('eq(h,"basicAngleOfTheInitialProductionDomain",0)', eq(h,"basicAngleOfTheInitialProductionDomain",0))

    CHECK('meridian*parallel == data_points', meridian*parallel == data_points)

    CHECK('eq(h,"resolutionAndComponentFlags1",0)', eq(h,"resolutionAndComponentFlags1",0))
    CHECK('eq(h,"resolutionAndComponentFlags2",0)', eq(h,"resolutionAndComponentFlags2",0))
    CHECK('eq(h,"resolutionAndComponentFlags6",0)', eq(h,"resolutionAndComponentFlags6",0))
    CHECK('eq(h,"resolutionAndComponentFlags7",0)', eq(h,"resolutionAndComponentFlags7",0))
    CHECK('eq(h,"resolutionAndComponentFlags8",0)', eq(h,"resolutionAndComponentFlags8",0))

    CHECK('eq(h,"iDirectionIncrementGiven",1)', eq(h,"iDirectionIncrementGiven",1))
    CHECK('eq(h,"jDirectionIncrementGiven",1)', eq(h,"jDirectionIncrementGiven",1))

    CHECK('eq(h,"numberOfOctectsForNumberOfPoints",0)', eq(h,"numberOfOctectsForNumberOfPoints",0))
    CHECK('eq(h,"interpretationOfNumberOfPoints",0)', eq(h,"interpretationOfNumberOfPoints",0))

    if get(h,"iScansNegatively") != 0:
        tmp = east
        dtmp = deast

        east = west
        west = tmp

        deast = dwest
        dwest = dtmp

    if get(h,"jScansPositively") != 0:
        tmp = north
        dtmp = dnorth

        north = south
        south = tmp

        dnorth = dsouth
        dsouth = dtmp

    if not (cfg.is_lam or cfg.is_uerra):
        CHECK('north > south', north > south)
        CHECK('east > west', east> west)

        # Check that the grid is symmetrical */
        CHECK('north == -south', north == -south)
        CHECK('DBL_EQUAL(dnorth, -dsouth, tolerance) ',  DBL_EQUAL(dnorth, -dsouth, tolerance) )
        CHECK('parallel == (east-west)/we + 1', parallel == (east-west)/we + 1)
        CHECK('math.fabs((deast-dwest)/dwe + 1 - parallel) < 1e-10', math.fabs((deast-dwest)/dwe + 1 - parallel) < 1e-10)
        CHECK('meridian == (north-south)/ns + 1', meridian == (north-south)/ns + 1)
        CHECK('math.fabs((dnorth-dsouth)/dns + 1 - meridian) < 1e-10 ', math.fabs((dnorth-dsouth)/dns + 1 - meridian) < 1e-10 )

        # Check that the field is global */
        area = (dnorth-dsouth) * (deast-dwest)
        globe = 360.0*180.0
        CHECK('area <= globe', area <= globe)
        CHECK('area >= globe*0.95', area >= globe*0.95)

    # GRIB2 requires longitudes are always positive */
    CHECK('east >= 0', east >= 0)
    CHECK('west >= 0', west >= 0)

      #printf("meridian=%ld north=%ld south=%ld ns=%ld ",meridian,north,south,ns)
      #printf("meridian=%ld north=%f south=%f ns=%f ",meridian,dnorth,dsouth,dns)
      #printf("parallel=%ld east=%ld west=%ld we=%ld ",parallel,east,west,we)
      #printf("parallel=%ld east=%f west=%f we=%f ",parallel,deast,dwest,dwe)

#define X(x) printf("%s=%ld ",#x,get(h,#x))
def X(h, name):
    print("%s=%ld " % (name, get(h, name)), end='')

def check_parameter(h, min_value, max_value):
    global cfg

    best = -1;
    match = -1;
    i = 0;

    #for (i = 0; i < NUMBER(parameters); i++):
    for parameter in parameters:
        j = 0;
        matches = 0;

        #while(parameter.pairs[j].key != NULL)
        for pair in parameter['pairs']:
            val = -1;
            ktype = pair['key_type']
            if ktype == int:
                try:
                    val = codes_get_long(h, pair['key'])
                    if pair['value_long'] == val:
                        matches += 1
                except:
                    pass
            elif ktype == str:
                if cfg.is_uerra and pair['key'].lower() == "model":
                    # print("Skipping model keyword for UERRA class")
                    matches += 1 # xxx hack to pretend that model key was matched.
                else:
                    if pair['value_string'].lower() == "MISSING".lower():
                        is_miss = codes_is_missing(h, pair['key'])
                        if is_miss != 0:
                            matches += 1
                    # elif codes_get_string(h, pair['key']):
                    else:
                        try:
                            strval = codes_get_string(h, pair['key'])
                            if pair['value_string'] == strval:
                                matches += 1
                        except:
                            pass
            else:
                assert("Unknown key type")
            j += 1
#if 0
            #print("%s %s %ld val -> %d %d %d" % (
                    #pair.key,
                    #pair.value_string,
                    #val,
                    #matches,
                    #j,
                    #best))
#endif

        if matches == j and matches > best:
            best = matches
            match = i
        i += 1

    if match >= 0:
        # int j = 0;
        cfg.param = parameters[match]['name']
        i = 0
        for check_func in parameters[match]['checks']:
            check_map[check_func](h, parameters[match], min_value, max_value)
            i += 1
                #printf("=========================");
                #printf("%s -> %d %d",param, match, best);
                #while(parameters[match].pairs[j].key != NULL)
                #{
                #     printf("%s val -> %ld %d",parameters[match].pairs[j].key,parameters[match].pairs[j].value,j);
                #     j++;
                #}
                #printf("matched parameter: %s", param);
    else:
        print("%s, field %d [%s]: cannot match parameter" % (cfg.filename, cfg.field, cfg.param))
        X(h, 'origin')
        X(h, "discipline")
        X(h, "parameterCategory")
        X(h, "parameterNumber")
        X(h, "typeOfFirstFixedSurface")
        X(h, "scaleFactorOfFirstFixedSurface")
        X(h, "scaledValueOfFirstFixedSurface")
        X(h, "typeOfSecondFixedSurface")
        X(h, "scaleFactorOfSecondFixedSurface")
        X(h, "scaledValueOfSecondFixedSurface")
        print("")
        cfg.error += 1

def check_packing(h):
    global cfg
    # ECC-1009: Warn if not using simple packing
    expected_packingType = "grid_simple";
    packingType = codes_get_string(h, "packingType")

    if packingType != expected_packingType:
        print("warning: %s, field %d [%s]: invalid packingType %s (Should be %s)" %(cfg.filename, cfg.field, cfg.param, packingType, expected_packingType))
        cfg.warning += 1

def verify(h):
    global cfg

    min_value = 0
    max_value = 0

    CHECK('eq(h,"editionNumber",2)', eq(h,"editionNumber",2))
    # CHECK('missing(h,"reserved") or eq(h,"reserved",0)', missing(h,"reserved") or eq(h,"reserved",0))


    if cfg.valueflg:
        count = 0
        try:
            count = codes_get_size(h,"values")
        except Exception as e:
            print("%s, field %d [%s]: cannot get number of values: %s" % (cfg.filename, cfg.field, cfg.param, str(e)))
            cfg.error += 1
            return;

        bitmap = not eq(h,"bitMapIndicator",255);

        CHECK('eq(h,"numberOfDataPoints",count)', eq(h,"numberOfDataPoints", count));

        n = count

        try:
            values = codes_get_double_array(h, "values")
        except Exception as e:
            print("%s, field %d [%s]: cannot get values: %s" % (cfg.filename, cfg.field, cfg.param, str(e)))
            cfg.error += 1
            return

        if n != count:
            print("%s, field %d [%s]: value count changed %ld -> %ld" % (cfg.filename, cfg.field, cfg.param, count, n))
            cfg.error += 1
            return

        if bitmap:
            missing = dget(h, "missingValue")
            min_value = max_value = missing;
            for value in values:
                if (min_value == missing) or ((value != missing) and (min_value > value)):
                    min_value = value
                if (max_value == missing) or ((value != missing) and (max_value < value)):
                    max_value = value
        else:
            min_value = max_value = values[0]
            for value in values:
                if min_value > value:
                    min_value = value
                if max_value < value:
                    max_value = value;

    check_parameter(h, min_value, max_value);
    check_packing(h);

    # Section 1

    CHECK('ge(h,"gribMasterTablesVersionNumber",4)', ge(h,"gribMasterTablesVersionNumber",4))
    CHECK('eq(h,"versionNumberOfGribLocalTables",0)', eq(h,"versionNumberOfGribLocalTables",0)) # Local tables not used

    CHECK('eq(h,"significanceOfReferenceTime",1)', eq(h,"significanceOfReferenceTime",1)); # Start of forecast

    if not cfg.is_s2s:
        # todo check for how many years back the reforecast is done? Is it coded in the grib???
        # Check if the date is OK
        date = get(h,"date");
        # CHECK(date > 20060101);
        CHECK('(date / 10000) == get(h,"year")', int(date / 10000) == get(h,"year"))
        CHECK('((date % 10000) / 100) == get(h,"month")', int((date % 10000) / 100) == get(h,"month"))
        CHECK('((date % 100)) == get(h,"day")', (int(date % 100)) == get(h,"day"))

    if cfg.is_uerra:
        CHECK('le(h,"hour",24)', le(h,"hour",24))
    elif cfg.is_lam:
        CHECK(
            'eq(h,"hour",0) or eq(h,"hour",3) or eq(h,"hour",6) or eq(h,"hour",9) or eq(h,"hour",12) or eq(h,"hour",15) or eq(h,"hour",18) or eq(h,"hour",21))',
             eq(h,"hour",0) or eq(h,"hour",3) or eq(h,"hour",6) or eq(h,"hour",9) or eq(h,"hour",12) or eq(h,"hour",15) or eq(h,"hour",18) or eq(h,"hour",21))
    else:
        # Only 00, 06 12 and 18 Cycle OK 
        CHECK('eq(h,"hour",0) or eq(h,"hour",6) or eq(h,"hour",12) or eq(h,"hour",18)', eq(h,"hour",0) or eq(h,"hour",6) or eq(h,"hour",12) or eq(h,"hour",18))

    CHECK('eq(h,"minute",0)', eq(h,"minute",0))
    CHECK('eq(h,"second",0)', eq(h,"second",0))
    CHECK('ge(h,"startStep",0)', ge(h,"startStep",0))

    if cfg.is_s2s:
        CHECK('eq(h,"productionStatusOfProcessedData",6) or eq(h,"productionStatusOfProcessedData",7)', eq(h,"productionStatusOfProcessedData",6) or eq(h,"productionStatusOfProcessedData",7)) #S2S prod or test
        CHECK('le(h,"endStep",100*24)', le(h,"endStep",100*24))
    elif not cfg.is_uerra:
        CHECK('eq(h,"productionStatusOfProcessedData",4) or eq(h,"productionStatusOfProcessedData",5)', eq(h,"productionStatusOfProcessedData",4) or eq(h,"productionStatusOfProcessedData",5)) # TIGGE prod or test
        CHECK('le(h,"endStep",30*24)', le(h,"endStep",30*24))

    if cfg.is_uerra:
        CHECK(
            '(eq(h,"step",1) or eq(h,"step",2) or eq(h,"step",4) or eq(h,"step",5)) or (get(h,"step") % 3) == 0)',
             (eq(h,"step",1) or eq(h,"step",2) or eq(h,"step",4) or eq(h,"step",5)) or (get(h,"step") % 3) == 0)
    elif cfg.is_lam:
        CHECK('(get(h,"step") % 3) == 0', (get(h,"step") % 3) == 0)
    else:
        CHECK('(get(h,"step") % 6) == 0', (get(h,"step") % 6) == 0)

    if cfg.is_uerra:
        if cfg.is_crra:
            CHECK('eq(h,"productionStatusOfProcessedData",10) or eq(h,"productionStatusOfProcessedData",11)', eq(h,"productionStatusOfProcessedData",10) or eq(h,"productionStatusOfProcessedData",11)) # CRRA prodortest
        else:
            CHECK('eq(h,"productionStatusOfProcessedData",8) or eq(h,"productionStatusOfProcessedData",9)', eq(h,"productionStatusOfProcessedData",8) or eq(h,"productionStatusOfProcessedData",9)); #  UERRA prodortest
        CHECK('le(h,"endStep",30)', le(h,"endStep",30))
        # 0 = analysis , 1 = forecast
        CHECK('eq(h,"typeOfProcessedData",0) or eq(h,"typeOfProcessedData",1)', eq(h,"typeOfProcessedData",0) or eq(h,"typeOfProcessedData",1))
        if get(h,"typeOfProcessedData") == 0:
            CHECK('eq(h,"step",0)', eq(h,"step",0))
        else:
            CHECK(
                '(eq(h,"step",1) or eq(h,"step",2) or eq(h,"step",4) or eq(h,"step",5)) or (get(h,"step") % 3) == 0)',
                 (eq(h,"step",1) or eq(h,"step",2) or eq(h,"step",4) or eq(h,"step",5)) or (get(h,"step") % 3) == 0)
    else:
        # 2 = analysis or forecast , 3 = control forecast, 4 = perturbed forecast
        CHECK('eq(h,"typeOfProcessedData",2) or eq(h,"typeOfProcessedData",3) or eq(h,"typeOfProcessedData",4)', eq(h,"typeOfProcessedData",2) or eq(h,"typeOfProcessedData",3) or eq(h,"typeOfProcessedData",4));

    # TODO: validate local usage. Empty for now xxx
    # CHECK('eq(h,"section2.sectionLength",5)', eq(h,"section2.sectionLength",5))

    # Section 3

    CHECK('eq(h,"sourceOfGridDefinition",0)', eq(h,"sourceOfGridDefinition",0)) # Specified in Code table 3.1 

    dtn = get(h,"gridDefinitionTemplateNumber")

    if dtn in [0, 1]:
        # dtn == 1: rotated latlon
        latlon_grid(h);
    elif dtn == 30: #Lambert conformal
        # lambert_grid(h); # TODO xxx
        # print("warning: Lambert grid - geometry checking not implemented yet!")
        # CHECK('eq(h,"scanningMode",64)', eq(h,"scanningMode",64));*/ /* M-F data used to have it wrong.. but it might depends on other projection set up as well!
        pass
    elif dtn == 40: # gaussian grid (regular or reduced)
        gaussian_grid(h)
    else:
        print("%s, field %d [%s]: Unsupported gridDefinitionTemplateNumber %ld" %
                (cfg.filename, cfg.field, cfg.param, get(h,"gridDefinitionTemplateNumber")))
        cfg.error += 1
        return;

    # If there is no bitmap, this should be true
    # CHECK('eq(h,"bitMapIndicator",255)', eq(h,"bitMapIndicator",255))

    if eq(h,"bitMapIndicator",255):
        CHECK('get(h,"numberOfValues") == get(h,"numberOfDataPoints")', get(h,"numberOfValues") == get(h,"numberOfDataPoints"))
    else:
        CHECK('get(h,"numberOfValues") <= get(h,"numberOfDataPoints")', get(h,"numberOfValues") <= get(h,"numberOfDataPoints"))

    # Check values 
    CHECK('eq(h,"typeOfOriginalFieldValues",0)', eq(h,"typeOfOriginalFieldValues",0)) # Floating point 

    check_validity_datetime(h)

    # do not store empty values e.g. fluxes at step 0
    #    todo ?? now it's allowed in the code here!
    #    if not missing(h,"typeOfStatisticalProcessing"):
    #      CHECK('ne(h,"stepRange",0)', ne(h,"stepRange",0))

def validate(path):
    global cfg

    count = 0;
    cfg.filename = path;
    cfg.field = 0;

    try:
        f = open(path, 'rb')
    except Exception as e:
        print("%s: %s" % (path, str(e)));
        cfg.error += 1;
        return;

    while 1:
        try:
            handle = codes_grib_new_from_file(f)
        except Exception as e:
            print("%s: grib_handle_new_from_file: %s" %(path, str(e)))
            cfg.error += 1
            return

        if handle == None:
            break

        last_error   = cfg.error;
        last_warning = cfg.warning;

        cfg.field += 1
        verify(handle);

        if (last_error != cfg.error) or ((cfg.warnflg != 0) and (last_warning != cfg.warning)):
            save(handle, cfg.bad, cfg.fbad)
        else:
            save(handle, cfg.good, cfg.fgood)

        codes_release(handle)
        count = count + 1
        cfg.param = "unknown"

    if count == 0:
        print("%s does not contain any GRIBs" % path)
        cfg.error += 1
        return

if __name__ == "__main__":
    check_map = dict()
    check_map['daily_average'] = daily_average
    check_map['from_start'] = from_start
    check_map['given_level'] = given_level
    check_map['given_thickness'] = given_thickness
    check_map['has_bitmap'] = has_bitmap
    check_map['has_soil_layer'] = has_soil_layer
    check_map['has_soil_level'] = has_soil_level
    check_map['height_level'] = height_level
    check_map['point_in_time'] = point_in_time
    check_map['potential_temperature_level'] = potential_temperature_level
    check_map['potential_vorticity_level'] = potential_vorticity_level
    check_map['predefined_level'] = predefined_level
    check_map['predefined_thickness'] = predefined_thickness
    check_map['pressure_level'] = pressure_level
    check_map['resolution_s2s'] = resolution_s2s
    check_map['resolution_s2s_ocean'] = resolution_s2s_ocean
    check_map['since_prev_pp'] = since_prev_pp
    check_map['six_hourly'] = six_hourly
    check_map['three_hourly'] = three_hourly

    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--warnflg', help='warnings are treated as errors', action='store_true')
    parser.add_argument('-z', '--zeroflg', help='return 0 to calling shell', action='store_true')
    parser.add_argument('-v', '--valueflg', help='check value ranges', action='store_true')
    parser.add_argument('-g', '--good', help='write good gribs', default=None)
    parser.add_argument('-b', '--bad', help='write bad gribs', default=None)
    parser.add_argument('file', nargs='+', help='Grib files', type=str)
    parser.add_argument('-l', '--lam', help='check local area model fields', action='store_true')
    parser.add_argument('-s', '--s2s', help='check s2s fields', action='store_true')
    parser.add_argument('-r', '--s2s_refcst', help='check s2s reforecast fields', action='store_true')
    parser.add_argument('-u', '--uerra', help='check uerra fields', action='store_true')
    parser.add_argument('-c', '--crra', help='check crra fields (-u must be also used in this case)', action='store_true')
    args = parser.parse_args()

    cfg.warnflg = args.warnflg
    cfg.zeroflg = args.zeroflg
    cfg.valueflg = args.valueflg
    cfg.is_lam = args.lam
    cfg.is_s2s = args.s2s
    cfg.is_s2s_refcst = args.s2s_refcst
    cfg.is_uerra = args.uerra
    cfg.is_crra = args.crra

    if args.good:
        good = args.good
        fgood = open(args.good,"w")
        if not fgood:
            print("Couldn't open %s" % good)
            sys.exit(1)

    if args.bad:
        bad = args.bad
        fbad = open(args.bad,"w")
        if not fbad:
            print("Couldn't open %s" % bad)
            sys.exit(1)

    err = 0
    for file in args.file:
        scan(file, validate)
        if cfg.error != 0:
            err = 1
        if cfg.warning and cfg.warnflg:
            err = 1

    if cfg.fgood != None and not cfg.fgood.closed:
        cfg.fgood.close()
    if cfg.fbad != None and not cfg.fbad.closed:
        cfg.fbad.close()

    sys.exit(0 if cfg.zeroflg else err)
