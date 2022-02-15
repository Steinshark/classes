#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example implementation of the SHA-256 algorithm with the
TensorFlow API.

Pseudo-code for the SHA-256 algorithm taken from:
- https://en.wikipedia.org/wiki/SHA-2#Pseudocode
- https://github.com/delqn/py-sha256/blob/master/sha256.py
"""

from __future__ import absolute_import, division, print_function

try:
    bytes
except NameError:
    # older Python 2.x
    bytes = str

import hashlib
from struct import pack, unpack

# as "main" we just run tests for the `sha256()` function
import pytest

import numpy as np
import tensorflow as tf

from tensorflow import (
    constant as C_,
    #Variable as V_,
)
V_ = tf.Variable
from tensorflow.bitwise import (
    bitwise_and as and_,
    bitwise_or as or_,
    bitwise_xor as xor_,
    invert as not_,
    left_shift as lsl_,
    right_shift as lsr_,
)


def pad_with_zeroes(m, q=448, p=512):
    """
    Right-pad byte string `m` with null bytes so that its length in
    bits is congruent to `q` modulo `p`.

    (Assumes that a byte is 8 bits wide, which should be true for
    basically any hardware that Python runs on.)
    """
    assert 0 == (q % 8)
    assert q < p
    l = (len(m) * 8) % p
    if l > q:
        l -= p
    return (m + ('\x00' * ((q - l) // 8)))


def prepare(m):
    """
    Format byte string `m` into a message block suitable for
    processing by the SHA-2 algorithm.

    (Assumes that a byte is 8 bits wide, which should be true for
    basically any hardware that Python runs on.)
    """
    assert type(m) is bytes
    # begin with the original message of length L bits
    L = len(m) * 8
    # append a single '1' bit
    m += b'\x80'
    # append K '0' bits, where K is the minimum number >= 0 such that L + 1 + K + 64 is a multiple of 512
    m = pad_with_zeroes(m)
    # append L as a 64-bit big-endian integer, making the total post-processed length a multiple of 512 bits
    m += pack('>Q', L)
    return m


def chunked(m):
    """
    Iterate over byte string `m` in 512-bit chunks.
    """
    assert 0 == ((len(m) * 8) % 512), ('len(m)=%d not multiple of 64' % len(m))
    for i in range(0, len(m), 64):
        yield m[i:i+64]


#
# auxiliary bit manipulation functions -- mainly for better readability
#

def ror(n, b, w=32):
    """
    Rotate `w`-bit wide unsigned integer `n` by `b` bits to the right.

    Examples::

      >>> ror(2**8, 4)
      16

      >>> ror(1, 17)
      32768

      >>> ror(0, 3)
      0

      >>> ror(2**32-1, 13) == 2**32-1
      True
    """
    assert b < w
    lo_mask = (1<<b)-1
    hi_mask = ((1<<(w-b))-1)<<b
    hi = n & hi_mask
    lo = n & lo_mask
    return ((hi >> b) | (lo << (w-b)))

def ror_(n, b, w=32):
    """
    Rotate 32-bit unsigned integer `n` by `b` bits to the right.
    (Like `ror` but implemented using TF operations.)
    """
    n_ = tf.cast(n, tf.int64)
    lo_mask = (1<<b)-1
    hi_mask = ((1<<(w-b))-1)<<b
    hi = and_(n_, hi_mask)
    lo = and_(n_, lo_mask)
    return tf.cast(or_(lsr_(hi, b), lsl_(lo, w-b)), tf.int32)

def shr(n, b, w=32):
    """
    Shift `w`-bit wide unsigned integer `n` by `b` bits to the right.

    Examples::

      >>> shr(2**8, 4)
      16

      >>> shr(1, 17)
      0
    """
    assert b < w
    w_mask = (1<<w) - 1
    return ((n & w_mask) >> b)



#
# SHA-256 uses six logical functions, where each function operates on 64-bit words,
# which are represented as x, y, and z. The result of each function is a new 64-bit word.
#

def choose_(x, y, z):
    """
    The x input chooses if the output is from y or z:

      Ch(x,y,z)=(x∧y)⊕(¬x∧z)
    """
    return xor_(z, and_(x, xor_(y, z)))


def gamma0(x):
    """ROTR 7(x) ⊕ ROTR 18(x) ⊕ SHR 3(x)"""
    return ror(x, 7) ^ ror(x, 18) ^ shr(x, 3)


def gamma1(x):
    """ROTR 17(x) ⊕ ROTR 19(x) ⊕ SHR 10(x)"""
    return ror(x, 17) ^ ror(x, 19) ^ shr(x, 10)


def majority_(x, y, z):
    """
    The result is set according to the majority of the 3 inputs:

      Maj(x, y,z) = (x ∧ y) ⊕ (x ∧ z) ⊕ ( y ∧ z)
    """
    return or_(and_(or_(x, y), z), and_(x, y))


def sigma0_(x):
    """ROTR 2(x) ⊕ ROTR 13(x) ⊕ ROTR 22(x)"""
    return xor_(ror_(x, 2), xor_(ror_(x, 13), ror_(x, 22)))


def sigma1_(x):
    """ROTR 6(x) ⊕ ROTR 11(x) ⊕ ROTR 25(x)"""
    return xor_(ror_(x, 6), xor_(ror_(x, 11), ror_(x, 25)))


def sha256(msg):
    """
    Return the SHA-256 hex digest of byte string `msg`.
    """
    np.seterr(over='ignore')

    # Pre-processing (Padding):
    m = prepare(msg)

    # Initialize hash values:
    # (first 32 bits of the fractional parts of the square roots of the first 8 primes 2..19):
    h0 = np.array([
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
    ], dtype=np.int32)

    # Initialize array of round constants:
    # (first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311):
    k = np.array([
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
    ], dtype=np.int32)

    # Initialize hash (init by copying `h0`)
    h = np.array(h0, dtype=np.int32)

    state = np.array(h0, dtype=np.int32)
    a_ = V_(state[0], tf.int32, name='a')
    b_ = V_(state[1], tf.int32, name='b')
    c_ = V_(state[2], tf.int32, name='c')
    d_ = V_(state[3], tf.int32, name='d')
    e_ = V_(state[4], tf.int32, name='e')
    f_ = V_(state[5], tf.int32, name='f')
    g_ = V_(state[6], tf.int32, name='g')
    h_ = V_(state[7], tf.int32, name='h')

    with tf.Session().as_default():
        #writer = tf.summary.FileWriter('.')
        #writer.add_graph(tf.get_default_graph())

        # Process the message in successive 512-bit chunks:
        for c in chunked(m):
            # create a 64-entry message schedule array w[0..63] of 32-bit words:
            # - copy chunk into first 16 words w[0..15] of the message schedule array
            w = np.zeros(64, dtype=np.int32)
            w[:16] = unpack(('>' + (16 * 'i')), c)
            # - extend the first 16 words into the remaining 48 words
            #   w[16..63] of the message schedule array:
            for i in range(16, 64):
                w[i] = 0xffffffff & (gamma1(w[i-2]) + w[i-7] + gamma0(w[i-15]) + w[i-16])

            a_.load(h[0])
            b_.load(h[1])
            c_.load(h[2])
            d_.load(h[3])
            e_.load(h[4])
            f_.load(h[5])
            g_.load(h[6])
            h_.load(h[7])

            # Compression function main loop:
            for i in range(64):
                t1_ = h_ + sigma1_(e_) + choose_(e_, f_, g_) + k[i] + w[i]
                t2_ = sigma0_(a_) + majority_(a_, b_, c_)
                h_.assign(g_)
                g_.assign(f_)
                f_.assign(e_)
                e_.assign(d_ + t1_)
                d_.assign(c_)
                c_.assign(b_)
                b_.assign(a_)
                a_.assign(t1_ + t2_)

            # Add the compressed chunk to the current hash value:
            h[0] += a_.numpy()
            h[1] += b_.numpy()
            h[2] += c_.numpy()
            h[3] += d_.numpy()
            h[4] += e_.numpy()
            h[5] += f_.numpy()
            h[6] += g_.numpy()
            h[7] += h_.numpy()


    # Produce the final hash value (big-endian):
    digest = pack('>' + (8 * 'i'), *h)
    # hexdigest is easier to compare in ASCII test output
    return ''.join(('%02x' % ord(ch)) for ch in digest)


#
# main: check that results agree with stdlib implementation
# on a few test cases
#

def sha256_stdlib(m):
    """
    Return the SHA-256 hex digest of byte string `m`.

    Uses Python's stdlib `hashlib.sha256` for doing the computations.
    """
    return hashlib.sha256(m).hexdigest()

@pytest.mark.parametrize("msg", [
    '',
    'Nobody expects the spammy repetition!',
    'The quick brown fox jumped over the lazy dog',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
])
def test_sha256_tfe(msg):
    assert sha256(msg) == sha256_stdlib(msg)

if __name__ == '__main__':
    pytest.main(['-v', '--doctest-modules', '--forked', __file__])
