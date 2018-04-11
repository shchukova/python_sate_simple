import datetime as dt

DATE_FORMAT = '%Y/%m/%d'


def get_date_object(date=None):
    """ takes an optional string date and returns a date object """
    if date is not None and not isinstance(date, str):
        raise ValueError('Parameter date is not String')

    if date is None:
        return dt.datetime.today().date()

    try:
        return dt.datetime.strptime(date, DATE_FORMAT).date()
    except ValueError as err:
        raise ValueError("Incorrect `date` format, should be {}. Message: {}".format(DATE_FORMAT, err))


def get_date_string(date_object=None):
    """ takes an optional date object and returns a formatted string """

    if date_object is not None and not isinstance(date_object, dt.date):
        raise TypeError('Parameter `date_object` is not datetime')

    if date_object is None:
        return dt.datetime.today().date().strftime(DATE_FORMAT)
    else:
        return date_object.strftime(DATE_FORMAT)


def valid_format(date_format):

    formats = ['%Y/%m/%d']
    if date_format in formats:
        return True
    else:
        return False


def get_date_string(date_object=None, date_format='%Y/%m/%d'):
    """ takes an optional date object and returns a formatted string """

    if date_object is not None and not isinstance(date_object, dt.date):
        raise TypeError('Parameter `date_object` is not datetime')

    if valid_format(date_format) == False:
        raise ValueError("Incorrect date format: {}.".format(date_format))

    if date_object is None:
        return dt.datetime.today().date().strftime(date_format)

    return date_object.strftime(date_format)


def main():
    """ the main event """

    d = get_date_string(date_format=DATE_FORMAT)
    print(d)
    print(type(d))


if __name__ == '__main__':
    main()
