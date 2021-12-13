import fileinput
from collections import namedtuple


Target = namedtuple("Target", "val,offset")


def solve(input_file):
    timestamp = int(input_file.readline())

    entries = []
    for i, line in enumerate(input_file.readline().split(",")):
        if line != "x":
            entries.append(Target(int(line), i))

    g = entries[0].val
    new_offset = 0

    sync_time = 0
    for entry in entries[1:]:
        phase, period = _departure_time(g, entry.val, entry.offset - new_offset)
        sync_time = (phase % period) - entry.offset

        g = period
        new_offset = -phase + entry.offset

    return sync_time


# Adapted from Eric Langlois' answer to https://math.stackexchange.com/questions/2218763


def _departure_time(line1_period, line2_period, offset):
    """Where the departure times first align, line1 starts shifted by offset"""
    period, phase = _combine_phased_rotations(
        line2_period, 0, line1_period, -offset % line1_period
    )
    return -phase, period


def _combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = _extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def _extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))
