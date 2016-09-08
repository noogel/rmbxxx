#! /usr/bin/python
"""
RMB number representation and Chinese literal notation translation
"""
import sys
import logging

import execjs

JS_FUNC_NAME = "convertCurrency"

with open(JS_FUNC_NAME, "r") as f:
    JS_CODE = "\n".join(f.readlines()).decode("utf-8")

RMBXXX = execjs.compile(JS_CODE)


def rmbxxx(rmb):
    """
    RMB number representation to Chinese literal notation
    :param rmb:
    :return:
    """
    return RMBXXX.call(JS_FUNC_NAME, rmb)

if __name__ == "__main__":
    rmb_number = sys.argv[-1]
    try:
        rmb_number = round(float(rmb_number), 2)
    except ValueError:
        logging.error("You need input a number, not others.", exc_info=True)
    else:
        rmb_literal = rmbxxx(rmb_number)
        print "RMB:%s -> %s" % (rmb_number, rmb_literal)
