import struct
from typing import BinaryIO

import crcmod
import logging

logger = logging.getLogger(__name__)

divider = (
    "--------------------------------------------------------------------------------"
)

# speed of light
sol = 299792.458 / 1.0e6  # = 0.299792458 km/usec

def get_string(fh: bytes) -> str:
    """
    Get string from the file handle. decode as utf-8
    """
    mystr = b""
    byte = fh.read(1)
    while byte != "":
        tt = struct.unpack("c", byte)[0]
        if tt == b"\x00":
            break
        mystr += tt
        byte = fh.read(1)

    return mystr.decode("utf-8")


def get_float(fh: "FH", nbytes: int) -> float:
    """get floating point; fh is the file handle"""
    tmp = fh.read(nbytes)
    if nbytes == 4:
        return struct.unpack("<f", tmp)[0]
    elif nbytes == 8:
        return struct.unpack("<d", tmp)[0]
    else:
        logger.error("parts.get_float(): Invalid number of bytes {}".format(nbytes))
        raise ValueError("Trying to get float of size > 8bytes")


def get_uint(fh: "FH", nbytes: int = 2) -> int:
    """
    get unsigned int (little endian), 2 bytes by default
    (assume nbytes is positive)
    """

    word = fh.read(nbytes)
    if nbytes == 2:
        # unsigned short
        return struct.unpack("<H", word)[0]
    elif nbytes == 4:
        # unsigned int
        return struct.unpack("<I", word)[0]
    elif nbytes == 8:
        # unsigned long long
        return struct.unpack("<Q", word)[0]
    else:
        logger.error("parts.get_uint(): Invalid number of bytes {}".format(nbytes))
        raise ValueError("Trying to get uint of size > 8bytes")


def get_signed(fh: "FH", nbytes: int = 2) -> int:
    """
    get signed int (little endian), 2 bytes by default
    (assume nbytes is positive)
    """

    word = fh.read(nbytes)
    if nbytes == 2:
        # unsigned short
        val = struct.unpack("<h", word)[0]
    elif nbytes == 4:
        # unsigned int
        val = struct.unpack("<i", word)[0]
    elif nbytes == 8:
        # unsigned long long
        val = struct.unpack("<q", word)[0]
    else:
        logger.error("parts.get_signed(): Invalid number of bytes {}".format(nbytes))
        raise ValueError("Trying to get int of size > 8bytes")

    return val


def get_hex(fh: "FH", nbytes: int = 1) -> str:
    """
    get nbyte bytes (1 by default)
    and display as hexidecimal
    """
    hstr = ""
    for i in range(nbytes):
        b = "%02X " % ord(fh.read(1))
        hstr += b
    return hstr


def slurp(fh: "FH", bname: str, results: dict) -> str:
    """
    fh: file handle;
    results: dict for results;

    just read this block without processing
    """
    status = "nok"

    try:
        ref = results["blocks"][bname]
        startpos = ref["pos"]
        fh.seek(startpos)
    except:
        # TODO this should raise
        logger.error("{} block starting position unknown".format(bname))
        return status

    nn = ref["size"]

    fh.read(nn)

    status = "ok"
    return status
