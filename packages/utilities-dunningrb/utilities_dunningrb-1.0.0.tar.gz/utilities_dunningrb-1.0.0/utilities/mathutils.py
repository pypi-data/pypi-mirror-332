"""Define methods for mathematical operations.
"""
from __future__ import annotations

import math
import os
import random
import statistics
from typing import Any, Dict, List, Optional

import numpy

from utilities import dictutils


def correct_the_angle(
    angle: float, *, as_radians: bool = True, full_circle: bool = True
) -> float:
    """Return the given angle, rotated to the correct quadrant. If optional "as_radians" is True
    (default), assume the given angle is measured in radians, and if False, assume it is measured
    in degrees.

    :param angle: an angle, possibly in the wrong quadrant
    :param as_radians: True for radians, False for degrees
    :param full_circle: if True (default) return the corrected angle in the range [0, 2*pi] or
        [0, 360]. If False, return the corrected angle in the range [0, pi] or [0, 180].
    :return: the angle
    """
    if as_radians:
        max_angle = 2 * numpy.pi if full_circle else numpy.pi
    else:
        max_angle = 360.0 if full_circle else 180.0

    if 0 <= angle <= max_angle:
        return angle

    while angle < 0:
        angle += max_angle

    while angle > max_angle:
        angle -= max_angle

    return angle


def divide(a: int | float, b: int | float, r: int | float = None) -> float:
    """Return <a>/<b> if <b> is not zero otherwise return <r>.
    """
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return 0.0 if r is None else r


def get_bradley_results(*, runs: int, r0: int, r1: int) -> dict:
    """Return a dictionary of results for Bradley's runs tests. This method is called by methods
    that apply Bradley's runs tests for randomness in a list of elements.

        runs (int): total number of runs.
        r0 (int): number of runs above the median or of type A.
        r1 (int): number of runs below the median or of type B.

    See Bradley, (1968). Distribution-Free Statistical Tests, Chapter 12.
    """

    if r0 <= 10 or r1 <= 10:
        err_msg = (
            f"Parameters <r0> and <r1> must both be greater than or equal to 10. Received: "
            f"r0: {r0} and r1: {r1}."
        )
        raise ValueError(err_msg)

    expected_runs = 1 + int(divide((2 * r0 * r1), (r0 + r1), 0))
    numerator = 2 * r0 * r1 * (2 * r0 * r1 - r0 - r1)
    denominator = (r0 + r1) ** 2 * (r0 + r1 - 1)
    stddev = divide(numerator, denominator)
    zscore = divide(runs - expected_runs, stddev)

    return {
        "runs": runs,
        "runs-value-A": r0,
        "runs-value-B": r1,
        "expected-runs": expected_runs,
        "stddev": stddev,
        "z-score": zscore,
    }


def get_decimal_part(num: float) -> float:
    """Return the decimal part of the given num.
    """
    return abs(num) % 1


def get_percent_diff(*, accepted: int | float, measured: int | float) -> float:
    """Return the percent difference between the given values.
    """
    avg = 0.5 * (accepted + measured)
    return 100 * abs(accepted - measured) / avg


def get_percent_error(*, accepted: int | float, measured: int | float) -> float:
    """Return the percent error between the given values.
    """
    return 100 * abs((accepted - measured) / accepted)


def get_pvalue_from_zscore(zscore: float) -> float:
    """Given a z-score return the p-value.
    """
    return statistics.NormalDist().cdf(zscore) * 2 - 1


def get_primes_up_to(limit: int) -> list[int]:
    """The sieve of Eratosthanes. Return a list of prime numbers up to and including the given
    limit.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [k for k in range(limit + 1) if sieve[k]]


def get_composites_up_to(limit: int, primes: Optional[list[int]] = None) -> list[int]:
    """Given an upper limit and optionally the list of prime numbers up to that limit, return a
    list of composite numbers up to and including the given limit. If the list of prime numbers
    is not given, we make a call get_primes_up_to.
    """
    if primes is None:
        primes = get_primes_up_to(limit)
    return [i for i in range(2, limit + 1) if i not in set(primes)]


def get_random_capture(a: int | float, b: int | float) -> bool:
    """Return True if an internally generated random number in the range [0, 1] is between the given
    <a> and <b>.
    """
    return a < b and a <= get_random_number() < b


def get_random_mask(*, size: int, cut: float = 0.5, one_if_above: bool = True) -> list:
    """Return a flat 1-d mask of length <size>, containing only 1s and 0s.

    If optional <one_if_above> is:

        True.... each element has a 1 - <cut> chance of being ONE and a <cut> chance of being ZERO.
        False... each element has a 1 - <cut> chance of being ZERO and a <cut> chance of being ONE.
    """
    above_val = {1: True, 0: False}[one_if_above]
    below_val = {1: True, 0: False}[not one_if_above]

    return [
        above_val if i >= cut else below_val for i in get_random_number_list(size=size)
    ]


def get_random_number() -> float:
    """Return a random number in the range [0, 1].
    """
    return int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)


def get_random_number_list(size: int) -> list[float]:
    """Return a list of random numbers each in the range [0, 1]. Makes a call to get_random_number,
    which see.
    """
    return [get_random_number() for _ in range(size)]


def get_smaller(z: float | int, thresh: float = 0.1, n: int = 0) -> tuple:
    """Return a tuple containing the first real number equal to or less than the given threshold
    (thresh, which defaults to 0.1) reached by successively dividing the given starting value (z)
    by 4, and the required number of integer steps to reach or pass threshold, starting from the
    given value (n, which defaults to 0).

    :param z: starting value
    :param thresh: threshold; defaults to 0.1
    :param n: counter; default starting value is 0
    :return: (s, n) where s is the first real number less or equal to thresh after dividing z by
        4 successively for n steps
    """
    if thresh < 0.0:
        raise ValueError(f"Parameter <<thresh>> must be >= 0. Received: {thresh}.")

    if z <= thresh:
        return z, 0

    i = 0
    while not z <= thresh:
        z /= 4
        i += 1

    return z, i


def get_transpose(m: list[list]) -> list[list]:
    """Return the transpose of the given matrix.
    """
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def get_zscore_from_pvalue(p: float) -> float:
    """Given a p-value return the z-score.
    """
    return statistics.NormalDist().inv_cdf((1 + p) / 2.0)


def is_normalized(table: dict, *, tol: float = 1e-5) -> bool:
    """Run a normalization tests against the give table.
    """
    return math.isclose(math.fsum(table.values()), 1, abs_tol=tol)


def is_random(
    r: list[int | float], *, zthresh: float = 1.960, sizethresh: int = 20
) -> dict:
    """Applies Bradly's run tests to the given list <r>, where len(set(r)) > 2, to determine if
    the values are randomized with significance level determined by the given z-score threshold.

    See:
        1. Bradley, (1968). Distribution-Free Statistical Tests, Chapter 12.
        2. https://www.itl.nist.gov/div898/handbook/eda/section3/eda35d.htm.
    """
    if len(set(r)) in [1, 2]:
        return is_random_binary_values(r=r, zthresh=zthresh, sizethresh=sizethresh)
    elif any([type(i) not in [float, int] for i in r]):
        err_msg = "All elements of the given list must be of type float or int."
        raise ValueError(err_msg)
    elif len(r) < sizethresh:
        err_msg = (
            f"The number of elements must exceed the size threshold: {sizethresh}. "
            f"Received: {len(r)} elements."
        )
        raise ValueError(err_msg)

    r_median = statistics.median(r)
    runs = r0 = r1 = 0  # r0 ascending, r1 descending

    for i in range(len(r)):
        if r[i] >= r_median and r[i - 1] < r_median:
            runs += 1
            r0 += 1
        elif r[i] < r_median and r[i - 1] >= r_median:
            runs += 1
            r1 += 1

    results = get_bradley_results(runs=runs, r0=r0, r1=r1)
    zscore = results["z-score"]

    results.update(
        {
            "len(r)": len(r),
            "z-score": zscore,
            "z-threshold": zthresh,
            "size-thresh": sizethresh,
            "num-distinct-values": len(set(r)),
            "runs": runs,
            "runs-value-A": r0,
            "runs-value-B": r1,
            "is-random": zscore > zthresh,
        }
    )

    return results


def is_random_binary_values(
    r: list[Any], *, zthresh: float = 1.960, sizethresh: int = 20
) -> dict:
    """Similar to is_random, which see. Intended for lists where each element is one of two
    possible values.

    See: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6422539/
    """
    if len(r) < sizethresh:
        err_msg = (
            f"The number of elements must exceed the size threshold: {sizethresh}. "
            f"Received: {len(r)} elements."
        )
        raise ValueError(err_msg)
    elif len(set(r)) > 2:
        err_msg = (
            f"The given list must contain not more than two distinct values. Received: "
            f"{len(set(r))} distinct values."
        )
        raise ValueError(err_msg)

    runs = r0 = 1

    for i in range(1, len(r)):
        if r[i] != r[i - 1]:  # we are starting a new run
            runs += 1
            if r[i] == r[0]:
                r0 += 1

    r1 = runs - r0
    results = get_bradley_results(runs=runs, r0=r0, r1=r1)
    zscore = results["z-score"]

    results.update(
        {
            "len(r)": len(r),
            "z-score": zscore,
            "z-threshold": zthresh,
            "size-thresh": sizethresh,
            "num-distinct-values": len(set(r)),
            "runs": runs,
            "runs-value-A": r0,
            "runs-value-B": r1,
            "is-random": zscore > zthresh,
        }
    )

    return results


def get_integers_with_random_step(*, start: int, stop: int, maxstep: int) -> list[int]:
    """Return a list of non-repeating random integers whose smallest-possible element is
    <start> and whose largest-possible element is <stop>, with the step between each element (
    when are they written in order from largest to smallest) being an integer randomly-selected
    from the range [1, maxstep].

    NOTES:
        1. The order of the elements in the returned list is not guaranteed.
        2. This method will raise ValueError if <<start>> is not less than <<stop>> or if
            <<maxstep>> < 2.
    """
    if start >= stop:
        err_msg = (
            f"Parameter <start> must be less than parameter <stop>. Received: start: "
            f"{start}; stop: {stop}."
        )
        raise ValueError(err_msg)

    if maxstep < 2:
        err_msg = f"Parameter <maxstep> must be greater than or equal to 2. Received: {maxstep}."
        raise ValueError(err_msg)

    n = start - 1  # makes it possible for <start> to be included in the list
    r = []  # result list

    while n < stop:
        step = random.randint(1, maxstep)
        next_n = n + step
        if next_n < stop:
            r.append(next_n)
            n = next_n
        else:
            r.append(stop)
            n = stop
    return r


def get_normalized_table(table: dict[Any:float]) -> dict[Any:float]:
    """Return a normalized table based on the given table, which is not modified.
    """
    z = math.fsum(table.values())
    return {k: v / z for k, v in table.items()}


def normalize_table(table: dict[Any:float]) -> None:
    """Normalize the given table in place.
    """
    t_new = get_normalized_table(table)
    for k in t_new:
        table[k] = t_new[k]


def select_from_table(table: dict) -> Any:
    """Return a randomly-selected key from the given table, for which it is assumed the keys are
    ordered such that the mapped values are in order from smallest to largest, with the smallest
    value being 0.0 and the largest being 1.0 (exact). Calls select_from_table_by_cut, which see.
    """
    return select_from_table_by_cut(table, cut=get_random_number())


def select_from_table_by_cut(table: dict, *, cut: int | float) -> Any:
    """Return a key from the given table, for which it is assumed the keys are
    ordered such that the mapped values are in order from smallest to largest, with the smallest
    value being greater than 0.0 and the largest being 1.0 (exact). Under this assumption,
    the first key for which <cut> is NOT greater than the mapped value is returned. If no such
    key is found, return None.
    """
    if cut > 1:
        err_msg = f"Parameter cut cannot be greater than 1. Received: {cut}."
        raise ValueError(err_msg)

    dictutils.reorder_by_value(table)

    for k, v in table.items():
        if cut <= v:
            return k


def sign(a: Any) -> float:
    """Return the sign (+1 or -1) of the given input.
    """
    return (lambda i: math.copysign(1, i))(a)


def xor(a: Any, b: Any) -> bool:
    """Return a xor b.
    """
    return bool(a) != bool(b)
