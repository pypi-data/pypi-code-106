# recast - python bit recaster
# Copyright (C) 2021 Phil Dreizen and Miccah Castorina
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

import sys
import struct
from functools import partial


def unpack(fmt, b):
    return struct.unpack(fmt, b)[0]


bytes2short = partial(unpack, 'h')
bytes2ushort = partial(unpack, 'H')
bytes2int = partial(unpack, 'i')
bytes2uint = partial(unpack, 'I')
bytes2long = partial(unpack, 'l')
bytes2ulong = partial(unpack, 'L')
bytes2longlong = partial(unpack, 'q')
bytes2ulonglong = partial(unpack, 'Q')
bytes2ssize_t = partial(unpack, 'n')
bytes2size_t = partial(unpack, 'N')
bytes2half = partial(unpack, 'e')  # half float
bytes2float = partial(unpack, 'f')
bytes2double = partial(unpack, 'd')
bytes2voidptr = partial(unpack, 'P')  # ???


def endian(order):
    return '<' if order == 'little' else '>'


def int2uint(i, byteorder=sys.byteorder):
    return bytes2uint(i.to_bytes(4, byteorder, signed=True))


def int2float(i, byteorder=sys.byteorder):
    return bytes2float(i.to_bytes(4, byteorder, signed=True))


def uint2int(ui, byteorder=sys.byteorder):
    return bytes2int(ui.to_bytes(4, byteorder))


def uint2float(ui, byteorder=sys.byteorder):
    return bytes2float(ui.to_bytes(4, byteorder))


def float2bytes(f, byteorder=sys.byteorder):
    return struct.pack(endian(byteorder) + 'f', f)


def float2int(f, byteorder=sys.byteorder):
    return bytes2int(float2bytes(f, byteorder))


def float2uint(f, byteorder=sys.byteorder):
    return bytes2uint(float2bytes(f, byteorder))


def double2bytes(d, byteorder=sys.byteorder):
    return struct.pack(endian(byteorder) + 'd', d)


def double2long(d, byteorder=sys.byteorder):
    return bytes2long(double2bytes(d, byteorder))


def double2ulong(d, byteorder=sys.byteorder):
    return bytes2ulong(double2bytes(d, byteorder))
