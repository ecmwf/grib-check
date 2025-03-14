from Assert import Le, Ne, Eq, Fail, AssertTrue, DBL_EQUAL, IsIn
from Report import Report
from checker.TiggeBasicChecks import TiggeBasicChecks
import math


class S2SRefcst(TiggeBasicChecks):
    def __init__(self, param_file=None, valueflg=False):
        super().__init__(param_file, valueflg=valueflg)


    def _basic_checks(self, message, p):
        reports = super()._basic_checks(message, p)
        report = Report(f"{__class__.__name__}._basic_checks")
        # Only 00, 06 12 and 18 Cycle OK 
        report.add(IsIn(message, "hour", [0, 6, 12, 18]))
        report.add(IsIn(message, "productionStatusOfProcessedData", [4, 5]))
        report.add(Le(message, "endStep", 30*24))
        report.add(AssertTrue(message.get("step") % 6 == 0, "step % 6 == 0"))
        return reports + [report]

    def _latlon_grid(self, message):
        report = Report(f"{__class__.__name__}.latlon_grid")

        tolerance = 1.0/1000000.0; # angular tolerance for grib2: micro degrees
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


        report.add(AssertTrue(north > south, "north > south"))
        report.add(AssertTrue(east > west, "east > west"))

        # Check that the grid is symmetrical */
        report.add(AssertTrue(north == -south, "north == -south"))
        report.add(AssertTrue(DBL_EQUAL(dnorth, -dsouth, tolerance), "DBL_EQUAL(dnorth, -dsouth, tolerance) "))
        report.add(AssertTrue(parallel == (east-west)/we + 1, "parallel == (east-west)/we + 1"))
        report.add(AssertTrue(math.fabs((deast-dwest)/dwe + 1 - parallel) < 1e-10, "math.fabs((deast-dwest)/dwe + 1 - parallel) < 1e-10"))
        report.add(AssertTrue(meridian == (north-south)/ns + 1, "meridian == (north-south)/ns + 1"))
        report.add(AssertTrue(math.fabs((dnorth-dsouth)/dns + 1 - meridian) < 1e-10, "math.fabs((dnorth-dsouth)/dns + 1 - meridian) < 1e-10 "))

        # Check that the field is global */
        area = (dnorth-dsouth) * (deast-dwest)
        globe = 360.0*180.0
        report.add(AssertTrue(area <= globe, "area <= globe"))
        report.add(AssertTrue(area >= globe*0.95, "area >= globe*0.95"))

        reports = super()._latlon_grid(message)
        return reports + [report]

    # not registered in the lookup table
    def _statistical_process(self, message, p):
        report = Report(f"{__class__.__name__}.statistical_process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1, 2]: # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]: # Control forecast products, Perturbed forecast products
            report.add(Eq(message, "productDefinitionTemplateNumber", 61))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return [report]

        if message.get("indicatorOfUnitOfTimeRange") == 11: # six hours
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message, "indicatorOfUnitOfTimeRange", 1))
            report.add(AssertTrue(message.get("forecastTime") % 6 == 0, "forecastTime % 6 == 0"))

        report.add(Eq(message, "timeIncrementBetweenSuccessiveFields", 0))
        report.add(AssertTrue(message.get("endStep") % 6 == 0, "endStep % 6 == 0")) # Every six hours

        reports = super()._statistical_process(message, p)
        return reports + [report]

    def _from_start(self, message, p):
        reports = super()._from_start(message, p)
        if message.get("endStep") != 0:
            reports += self._check_range(message, p)
        return reports

    def _point_in_time(self, message, p):
        reports = super()._point_in_time(message, p)

        checks = Report()
        topd = message.get("typeOfProcessedData")
        if topd in [0, 1]: # Analysis, Forecast
            if message.get("productDefinitionTemplateNumber") == 1:
                checks.add(Ne(message, "numberOfForecastsInEnsemble", 0))
                checks.add(Le(message, "perturbationNumber", message.get("numberOfForecastsInEnsemble")))
        elif topd == 2: # Analysis and forecast products
            pass
        elif topd == 3: # Control forecast products 
            checks.add(Eq(message, "productDefinitionTemplateNumber", 60))
        elif topd == 4: # Perturbed forecast products
            checks.add(Eq(message, "productDefinitionTemplateNumber", 60))
            pn = message.get("perturbationNumber")
            nofe = message.get("numberOfForecastsInEnsemble")
            checks.add(AssertTrue(pn < nofe, "perturbationNumber < numberOfForecastsInEnsemble"))
        else:
            checks.add(Fail("Unsupported typeOfProcessedData %ld" % message.get("typeOfProcessedData")))

        if message.get("indicatorOfUnitOfTimeRange") == 11:
            # Six hourly is OK
            pass
        else:
            checks.add(Eq(message, "indicatorOfUnitOfTimeRange", 1))
            checks.add(AssertTrue(message.get("forecastTime") % 6 == 0, "forecastTime % 6 == 0"))

        return reports + [checks]
