"""
This module implements the aligned-spin TaylorT3 equations.

Some references:

 - [arXiv:0802.1249](https://arxiv.org/abs/0802.1249)
 - [arXiv:0901.2437](https://arxiv.org/abs/0901.2437)
 - [arXiv:0610122](https://arxiv.org/abs/gr-qc/0610122)
 - [arXiv:0907.0700](https://arxiv.org/abs/0907.0700)
 - [arXiv:0406012](https://arxiv.org/abs/gr-qc/0406012)
 - [arXiv:1210.2339](https://arxiv.org/abs/1210.2339)
 - [arXiv:1210.2339](https://arxiv.org/abs/1210.2339)
 - [arXiv:2004.08302](http://arxiv.org/abs/2004.08302)
 - [arXiv:2012.11923](http://arxiv.org/abs/2012.11923)
 - [LALSimInspiralTaylorT3.c](https://git.ligo.org/lscsoft/lalsuite/blob/master/lalsimulation/lib/LALSimInspiralTaylorT3.c)
 - [LALSimInspiralPNCoefficients.c](https://git.ligo.org/lscsoft/lalsuite/blob/master/lalsimulation/lib/LALSimInspiralPNCoefficients.c)
"""

import numpy as np
from lal import GAMMA, MTSUN_SI


def Msun_to_sec(M: float | int) -> float:
    """
    Geometric units convertion.
    convert mass (in units of solar masses)
    into seconds.

    The equation is M * MSUN_SI * G_SI / C_SI**3.

    Parameters
    ----------
    M : float | int
        Total mass in solar masses

    Returns
    -------
    float | int
        Mass converted into units of seconds.
    """
    #     return
    return M * MTSUN_SI


def TaylorT3_Omega_GW_Newt(t, tc: float | int, eta: float, M: float | int):
    """
    Newtonian pre factor for GW angular frequency

    Parameters
    ----------
    t : number or array
        The time coordinate
    tc : float | int
        The TaylorT3 coalescence time
    eta : float
        The symmetric mass ratio
    M : float | int
        Total mass in solar masses

    Returns
    -------
    float or array
        Newtonian pre factor for GW angular frequency
    """
    theta = TaylorT3_theta(t, tc, eta, M)
    return theta**3 / (8.0 * M)


def TaylorT3_theta(t, tc, eta, M):
    """
    Taylor3 parameter
    """
    theta = eta * (tc - t) / (5 * M)
    theta = theta ** (-1 / 8.0)
    return theta


def TaylorT3_t(theta, tc, eta, M):
    """
    Inverse of TaylorT3_theta
    """
    return -5 * M / eta / theta**8 + tc


def TaylorT3_Omega_GW(t, tc, eta, M, chi1, chi2):
    """
    22 mode angular GW frequency
    equation 7 in 0901.2437

    3.5PN term from https://arxiv.org/pdf/gr-qc/0610122.pdf and https://arxiv.org/pdf/0907.0700.pdf
    and this too apparently https://arxiv.org/pdf/gr-qc/0406012.pdf?

    https://git.ligo.org/lscsoft/lalsuite/blob/master/lalsimulation/lib/LALSimInspiralTaylorT3.c

    https://git.ligo.org/lscsoft/lalsuite/blob/master/lalsimulation/lib/LALSimInspiralPNCoefficients.c

    spinning terms from: http://arxiv.org/abs/2004.08302

    actually spinning terms were derived by me in https://gitlab.com/SpaceTimeKhantinuum/taylort3-paper/-/tree/main/derivation
    but I chose to only include spinning terms upto and including 2.5PN and this doesn't include
    horizon absorption terms.


    Parameters
    ----------
    t:
        time
    tc:
        coalescence time
    eta:
        symmetric mass ratio
    M:
        total mass (Msun)
    chi1:
        dimensionless spin of the primary (larger) black hole
    chi2:
        dimensionless spin of the secondary (smaller) black hole

    Returns
    -------
    """

    chi_a = (chi1 - chi2) / 2
    chi_s = (chi1 + chi2) / 2
    delta = np.sqrt(1 - 4 * eta)

    pi = np.pi

    theta = TaylorT3_theta(t, tc, eta, M)

    theta2 = theta * theta
    theta3 = theta2 * theta
    theta4 = theta3 * theta
    theta5 = theta4 * theta
    theta6 = theta5 * theta
    theta7 = theta6 * theta

    # pre factor
    ftaN = 1.0 / (8.0 * M)
    # 0PN
    fts1 = 1.0
    # 0.5PN = 0 in GR
    # 1PN
    fta2 = 11 * eta / 32 + 743 / 2688
    # 1.5PN
    fta3_nonspin = -3 * pi / 10
    fta3_spin = 113 * chi_a * delta / 160 + chi_s * (113 / 160 - 19 * eta / 40)
    fta3 = fta3_nonspin + fta3_spin
    # 2PN
    fta4_nonspin = 371 * eta**2 / 2048 + 56975 * eta / 258048 + 1855099 / 14450688
    fta4_spin = (
        chi_a**2 * (15 * eta / 16 + -243 / 1024)
        - 243 * chi_a * chi_s * delta / 512
        + chi_s**2 * (3 * eta / 256 + -243 / 1024)
    )
    fta4 = fta4_nonspin + fta4_spin
    # 2.5PN
    fta5_nonspin = 13 * pi * eta / 256 - 7729 * pi / 21504
    fta5_spin = chi_a * delta * (7 * eta / 64 + 146597 / 64512) + chi_s * (
        -17 * eta**2 / 64 - 1213 * eta / 576 + 146597 / 64512
    )
    fta5 = fta5_nonspin + fta5_spin
    # 3PN
    fta6_nonspin = (
        235925 * eta**3 / 1769472
        - 30913 * eta**2 / 1835008
        - 451 * pi**2 * eta / 2048
        + 25302017977 * eta / 4161798144
        + 107 * GAMMA / 280
        + -720817631400877 / 288412611379200
        + 53 * pi**2 / 200
    )
    fta6_spin = 0
    fta6 = fta6_nonspin + fta6_spin

    # 3.5PN
    fta7_nonspin = (
        141769 * pi * eta**2 / 1290240 - 97765 * pi * eta / 258048 - 188516689 * pi / 433520640
    )
    fta7_spin = 0
    fta7 = fta7_nonspin + fta7_spin

    # 3PN log term
    ftal6 = 107 / 280

    omega_orb = (
        theta3
        * ftaN
        * (
            fts1
            + fta2 * theta2
            + fta3 * theta3
            + fta4 * theta4
            + fta5 * theta5
            + (fta6 + ftal6 * np.log(2.0 * theta)) * theta6
            + fta7 * theta7
        )
    )

    # convert from orb to 22 GW
    return 2 * omega_orb


def Hhat22_pre_factor(x, eta):
    """
    https://arxiv.org/pdf/0802.1249.pdf
    eq. 9.3a and 9.3b
    """
    return np.sqrt(16.0 * np.pi / 5) * 2 * eta * x


def Hhat22_x(x, eta, chi1, chi2):
    """
    https://arxiv.org/pdf/0802.1249.pdf - eq. 9.4a

    3.5PN term: https://arxiv.org/pdf/1210.2339.pdf

    Spinning part from http://arxiv.org/abs/2004.08302 and http://arxiv.org/abs/2012.11923
    Here I implement the spinning terms from the 2nd paper (Equation A1) becuase I think
    the spinning terms from the 1st paper might have typos.
    Note that m1 = (1 + delta)/2 and m2 = (1 - delta)/2.

    here we leave the expression to depend on the post-newtonian
    parameter 'x' so that you can choose how to calculate it.
    e.g., from PN like TaylorT3 or from the model which
    is TaylorT3 + corrections

    return complex
    """
    delta_m = np.sqrt(1 - 4 * eta)

    xarr = np.zeros(8, dtype=np.complex128)

    xarr[0] = 1.0
    # 0.5 PN term is zero
    xarr[1] = 0
    xarr[2] = -107.0 / 42 + 55 * eta / 42
    x3_non_spin = 2.0 * np.pi

    x3_spin = 2.0 / 3.0 * (-delta_m * (chi1 - chi2) + eta * (chi1 + chi2) - (chi1 + chi2))

    xarr[3] = x3_non_spin + x3_spin
    x4_non_spin = -2173.0 / 1512 - 1069.0 * eta / 216 + 2047.0 * eta**2 / 1512

    chi1_2 = chi1**2
    chi2_2 = chi2**2
    x4_spin = (
        delta_m / 2 * (chi1_2 - chi2_2)
        - eta * (chi1_2 + chi2_2 - 2 * eta * chi1 * chi2)
        + (chi1_2 + chi2_2) / 2.0
    )

    xarr[4] = x4_non_spin + x4_spin
    xarr[5] = -107 * np.pi / 21 - 24.0 * 1.0j * eta + 34.0 * np.pi * eta / 21

    x6a = 27027409.0 / 646800 - 856.0 * GAMMA / 105 + 428 * 1.0j * np.pi / 105 + 2.0 * np.pi**2 / 3
    x6b = (
        (-278185.0 / 33264 + 41 * np.pi**2 / 96) * eta
        - 20261.0 * eta**2 / 2772
        + 114635.0 * eta**3 / 99792
    )

    x6log = -428.0 * np.log(16 * x) / 105

    xarr[6] = x6a + x6b

    xarr[7] = (
        -2173 * np.pi / 756
        + (-(2495 * np.pi / 378) + (14333 * 1.0j / 162)) * eta
        + ((40 * np.pi / 27) - (4066 * 1.0j / 945)) * eta**2
    )

    # pn = xarr[0] + x*xarr[2] + x**(3/2.)*xarr[3] + x**2*xarr[4] + x**(5/2.)*xarr[5] + x**3*(xarr[6] + x6log) + x**(7/2.)*xarr[7]
    pn = xarr[0]
    pn += x * xarr[2]
    pn += x ** (3 / 2.0) * xarr[3]
    pn += x**2 * xarr[4]
    pn += x ** (5 / 2.0) * xarr[5]
    pn += x**3 * (xarr[6] + x6log)
    pn += x ** (7 / 2.0) * xarr[7]

    pre = Hhat22_pre_factor(x, eta)

    return pre * pn


def x_from_omega_22(GW22AngFreq, M=1):
    OrgAngFreq = GW22AngFreq / 2
    x = (M * OrgAngFreq) ** (2.0 / 3)
    return x


def TaylorT3_Hhat22(t, tc, eta, M, chi1, chi2):
    """
    https://arxiv.org/pdf/0802.1249.pdf - eq. 9.4a
    Post-Newtonian expression for (l,m)=(2,2) time domain
    amplitude assuming TaylorT3 frequency evolution
    """

    GW22AngFreq = TaylorT3_Omega_GW(t, tc, eta, M, chi1, chi2)
    x = x_from_omega_22(GW22AngFreq, M)
    return Hhat22_x(x, eta, chi1, chi2)


def TaylorT3_Phase_Orbital(t, tc, eta, M, chi1=0, chi2=0, phi_0=0):
    """
    TaylorT3 orbital phase
    equation 3.10a in http://arxiv.org/abs/0907.0700


    spinning terms were derived by me in https://gitlab.com/SpaceTimeKhantinuum/taylort3-paper/-/tree/main/derivation
    but I chose to only include spinning terms upto and including 2.5PN and this doesn't include
    horizon absorption terms.


    Parameters
    ----------
    t:
        time
    tc:
        coalescence time
    eta:
        symmetric mass ratio
    M:
        total mass (Msun)
    chi1:
        dimensionless spin of the primary (larger) black hole
    chi2:
        dimensionless spin of the secondary (smaller) black hole
    phi_0:
        reference orbital phase

    Returns
    -------
    """
    chi_a = (chi1 - chi2) / 2
    chi_s = (chi1 + chi2) / 2
    delta = np.sqrt(1 - 4 * eta)

    pi = np.pi

    theta = TaylorT3_theta(t, tc, eta, M)
    theta_m5 = theta**-5

    theta2 = theta * theta
    theta3 = theta2 * theta
    theta4 = theta3 * theta
    theta5 = theta4 * theta
    theta6 = theta5 * theta
    theta7 = theta6 * theta

    # pre factor
    ftaN = -1.0 / eta
    # 0PN
    fts1 = 1.0
    # 0.5PN = 0 in GR
    # 1PN
    fta2 = 3715 / 8064 + 55 / 96 * eta
    # 1.5PN
    fta3_nonspin = -3.0 / 4.0 * np.pi
    fta3_spin = 113 * chi_a * delta / 64 + chi_s * (113 / 64 - 19 * eta / 16)
    fta3 = fta3_nonspin + fta3_spin
    # 2PN
    fta4_nonspin = 9275495 / 14450688 + 284875 / 258048 * eta + 1855 / 2048 * eta**2
    fta4_spin = (
        chi_a**2 * (75 * eta / 16 + -1215 / 1024)
        - 1215 * chi_a * chi_s * delta / 512
        + chi_s**2 * (15 * eta / 256 + -1215 / 1024)
    )
    fta4 = fta4_nonspin + fta4_spin
    # 2.5PN (Proportional to log(theta)*theta**5)
    fta5_nonspin = -65 * pi * eta / 256 + 38645 * pi / 21504
    fta5_spin = chi_a * delta * (-35 * eta / 64 + -732985 / 64512) + chi_s * (
        85 * eta**2 / 64 + 6065 * eta / 576 + -732985 / 64512
    )
    fta5 = fta5_nonspin + fta5_spin
    # 3PN
    fta6_nonspin = (
        831032450749357 / 57682522275840
        - 53 / 40 * np.pi * np.pi
        + ((-126510089885 / 4161798144) + 2255 / 2048 * np.pi * np.pi) * eta
        - 107 / 56 * GAMMA
        + 154565 / 1835008 * eta**2
        - 1179625 / 1769472 * eta**3
    )
    fta6_spin = 0
    fta6 = fta6_nonspin + fta6_spin

    # 3.5PN
    fta7_nonspin = (
        188516689 / 173408256 + 488825 / 516096 * eta - 141769 / 516096 * eta**2
    ) * np.pi
    fta7_spin = 0
    fta7 = fta7_nonspin + fta7_spin

    # 3PN log term
    ftal6 = -107 / 56

    phase_orb = (
        theta_m5
        * ftaN
        * (
            fts1
            + fta2 * theta2
            + fta3 * theta3
            + fta4 * theta4
            + fta5 * np.log(theta) * theta5
            + (fta6 + ftal6 * np.log(2.0 * theta)) * theta6
            + fta7 * theta7
        )
    )

    return phase_orb + phi_0
