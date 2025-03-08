#!/usr/bin/python
"""
@Author  :  Lijiawei
@Date    :  2022/3/22 5:45 下午
@Desc    :  toolbox line.
"""
import ast
import datetime
import getpass
import json
import os
import platform
import time
import traceback
import urllib.parse
from pathlib import Path
from loguru import logger

import jmespath
try:
    from airtest.core.api import assert_equal
    from airtest.core.api import log
    import requests
except ImportError:
    logger.warning("airtest not installed, please install airtest first.")

from deepdiff import DeepDiff

from garbevents.settings import Settings as ST


def diff(expect, actual, complete=True, exclude_paths=None, view="text") -> dict:
    """
    analysis diff result
    old new
    :param view: tree or text or _delta
    :param expect: expect
    :param actual: actual
    :param complete: match type, match complete or include, default complete.
    :param exclude_paths: parameter whitelist is empty by default.
    :return: {'result': True, 'data': {}}
    :Example:
        >>> {'result': True, 'data': {'dictionary_item_added': [root['data']]}}
    """
    exclude_paths = {f"root['{path}']" for path in str(exclude_paths).split(",")}
    if len(exclude_paths) == 0:
        exclude_paths = None

    if not isinstance(expect, dict):
        expect = ast.literal_eval(expect)
    if not isinstance(actual, dict):
        actual = ast.literal_eval(actual)

    log(arg=expect, desc="Expect")
    log(arg=actual, desc="Actual")

    compare_results = DeepDiff(
        expect, actual, view=view, ignore_order=True, exclude_paths=exclude_paths
    ).to_dict()
    if not complete:
        if compare_results.get("values_changed"):
            result = False
        else:
            result = True
    else:
        if (
            compare_results.get("dictionary_item_added")
            or compare_results.get("dictionary_item_removed")
            or compare_results.get("values_changed")
            or compare_results.get("iterable_item_added")
            or compare_results.get("iterable_item_removed")
        ):
            result = False
        else:
            result = True

    return {"result": result, "data": compare_results}


def extract(expressions, data):
    """
    extract the value you want！
    help documentation >>> https://jmespath.org/tutorial.html
    :param expressions: jsonpath expressions
    :param data: data dict
    :return: the value you want
    :Example:
        >>> test_dict = {"a": {"b": {"c": {"d": "value"}}}}
        >>> result = extract(expressions='a.b.c.d', data = test_dict)
        >>> print(result)
        >>> # value
    """
    _data = jmespath.search(expressions, data)
    return _data


def timestamp():
    """
    timestamp tool
    :return:
    """
    return int(round(time.time() * 1000))


def datetime_strife(fmt="%Y-%m-%d_%H-%M-%S"):
    """
    format datetime tool
    :param fmt: %Y-%m-%d_%H-%M-%S
    :return:
    """
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    sleep time
    :param seconds:
    :return:
    """
    time.sleep(seconds)


def target(target_url, sign="stag=", index=1) -> dict:
    """
    the value you want！
    :param index: default 1
    :param sign: split flag
    :param target_url: encoded string
    :return: the value you want！
    """
    stag = ast.literal_eval(
        str(urllib.parse.unquote(target_url).split(sign)[index].split("&")[0])
    )

    return stag


def assert_diff(result: dict, equal: bool = True):
    """
    Assert two values are equal
    :param equal: verify True or False, default True
    :param result: toolbox.diff() return value
    :raise AssertionError: if assertion
    :return: None
    """
    # Report step
    log(
        arg=str(result["data"])
        .replace("old_value", "expect_value")
        .replace("new_value", "actual_value"),
        desc="Diff Details",
    )

    # Assertion
    try:
        assert_equal(first=equal, second=result["result"], msg="Diff Result")
    except AssertionError:
        pass


def search(start_time, end_time, api, types, latest=False):
    """

    :param latest: latest data limit 1
    :param types: request or response
    :param start_time: 13-bit, millisecond timestamp, 1648545731537.
    :param end_time: default current timestamp, 1648645731537
    :param api: interface name.
    :return: interface information list.
    :Example:
        >>> search_data = search(start_time=1648545731537, end_time=1648645731537, api='/api/test', types='request')
        >>> print(search_data)
        >>> # [{'invokedBy': 'open'}]
    """
    from garbevents.db import proxy_data

    if latest:
        sql = f"select {types} from proxy where timestamps between {start_time} and {end_time} and api == '{api}' order by id desc limit 1;"
    else:
        sql = f"select {types} from proxy where api == '{api}' order by id desc limit 1;"

    data_collection = proxy_data.query(sql)
    # todo 去掉ip校验
    #  and client_ip == '{device().get_ip_address()}'

    res = []
    for data in data_collection:
        for d in data:
            res.append(ast.literal_eval(d))
    return res


def str_to_bool(value):
    """
    str convert bool
    :param value:
    :return:
    """
    return True if value.lower() == "true" else False


def match(cases: list, sign="stag=", index=1, equal: bool = True):
    """

    :param cases:
    :param sign:
    :param index:
    :param equal:
    :raise AssertionError: if assertion
    :return: None
    """
    for info in cases:
        if not isinstance(info, dict):
            info = ast.literal_eval(info)
        try:
            excepts = info["excepts"]

            search_data = search(
                start_time=info["search"]["start_time"],
                end_time=info["search"]["end_time"],
                api=info["api"],
                types=info["types"],
            )
            detail = []
            for _data in search_data:
                actual = extract(expressions=info["extract"], data=_data)

                if str_to_bool(info["target"]):
                    actual = target(target_url=actual, sign=sign, index=index)

                result = diff(
                    expect=excepts,
                    actual=actual,
                    complete=str_to_bool(info["diff"]["complete"]),
                    exclude_paths=info["diff"]["exclude_paths"],
                )
                detail.append(result)

            if len(detail) > 1:
                flag = True
                for res in detail:
                    if res["result"]:
                        assert_diff(result=res, equal=equal)
                        flag = False
                        break
                if flag:
                    log(
                        arg=str(detail)
                        .replace("old_value", "expect_value")
                        .replace("new_value", "actual_value"),
                        desc="No Results Were Matched",
                    )
                    assert_equal(first=True, second=False, msg="Multiple Diff Result")
            else:
                try:
                    assert_diff(result=detail[0], equal=equal)
                except IndexError:
                    logger.error(traceback.format_exc())
        except AssertionError:
            logger.error(traceback.format_exc())


def mock(options: list, events=ST.options):
    """
    mock api
    :param events: options command: map_remotes, map_locals, modify_bodys, modify_headers
    :param options: [{"api": url-regex, "content": {}}, {"api": url-regex, "content": {}},...]
    :return: {"map_locals": ["|flow-filter|url-regex|file-or-directory-path"]}
    """
    mock_opt = []
    for option in options:
        try:
            url_regex = option["api"]
            replacement = option["content"]
        except (TypeError, KeyError) as e:
            log(e)
            url_regex = ""
            replacement = ""

        if events == "map_locals":
            replacement_name = str(url_regex).replace("/", "_") + ".json"
            if platform.system() == "Darwin":
                path = f"/Users/{getpass.getuser()}/Documents/map_local/{replacement_name}"
            else:
                path = os.path.join(Path().expanduser().resolve(strict=True), replacement_name)
            with open(path, "w") as f:
                json.dump(replacement, f, ensure_ascii=False)
            replacement = replacement_name

        mock_opt.append(f"|{url_regex}|{replacement}")

    url_put = f"http://{ST.web_host}:{ST.web_port}/options"
    param = {events: mock_opt}
    try:
        requests.put(url_put, json=param, headers={"Content-Type": "application/json"})
        log(arg=param, desc="Mock Details")
    except Exception as e:
        logger.error(f"ConnectionRefusedError or ConnectionError: {e}")

