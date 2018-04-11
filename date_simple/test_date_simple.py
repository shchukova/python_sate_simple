#!/usr/bin/env python

import pytest
import datetime as dt
import date_simple as ds

DATE_STRING = '2018/10/10'
WRONG_DATE = 'gfgfgfgfgf'


def test_get_date_object():

    date_obj = ds.get_date_object(DATE_STRING)
    assert date_obj.strftime(ds.DATE_FORMAT) == DATE_STRING


def test_get_date_object_none():

    date_obj_res = ds.get_date_object()
    date_obj = dt.datetime.today().date()
    assert date_obj_res == date_obj


def test_get_date_object_error():

    with pytest.raises(ValueError):
      ds.get_date_object(WRONG_DATE)


def test_get_date_string_none():

    date_str_res = ds.get_date_string()
    date_str = dt.datetime.today().date().strftime(ds.DATE_FORMAT)
    assert date_str_res == date_str


def test_get_date_string():

    date_obj = dt.datetime.strptime(DATE_STRING, ds.DATE_FORMAT).date()
    date_str_res = ds.get_date_string(date_obj)
    assert date_str_res == DATE_STRING


def test_get_date_string_date_type_error():

    with pytest.raises(TypeError):
      ds.get_date_string(DATE_STRING)


def test_get_date_string_format_error():
    with pytest.raises(ValueError):
      ds.get_date_string(date_format='dsdfdfdfs')


def test_get_date_string_format():

    date_obj = dt.datetime.strptime(DATE_STRING, '%Y/%m/%d').date()
    date_str_res = ds.get_date_string(date_obj, ds.DATE_FORMAT)
    assert date_str_res == DATE_STRING




