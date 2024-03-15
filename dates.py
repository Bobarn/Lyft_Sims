from dateutil.relativedelta import relativedelta


def add_years(date, modifier):

    new_date = date + relativedelta(years=modifier)
    return new_date
