import pytest
from datetime import date,timedelta
from seasons import validate

def test_errs():
    with pytest.raises(SystemExit):
        validate("18-08-2024")

    with pytest.raises(SystemExit):
        validate("2007-12-52")

    with pytest.raises(SystemExit):
        validate("2009-12 52")




    #assert (date.today()-timedelta(days=355))=="Five hundred twenty-five thousand, six hundred"
