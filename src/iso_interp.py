#
import numpy as np
from scipy.interpolate import interp1d, interp2d

ages = np.arange(600.0, 910.0, 50.0)*1.0e6

for age in ages:
    # load each isochrone
    isop00 = np.genfromtxt("../iso/p000/dmestar_{:07.1f}myr_z+0.00_a+0.00_phx.iso".format(age/1.0e6))
    isop10 = np.genfromtxt("../iso/p010/dmestar_{:07.1f}myr_z+0.10_a+0.00_phx.iso".format(age/1.0e6))
    isop20 = np.genfromtxt("../iso/p020/dmestar_{:07.1f}myr_z+0.20_a+0.00_phx.iso".format(age/1.0e6))

    # create an interpolation curve for each isochrone
    icurve00 = interp1d(isop00[:,0], isop00, kind="cubic", axis=0)
    icurve10 = interp1d(isop10[:,0], isop10, kind="cubic", axis=0)
    icurve20 = interp1d(isop20[:,0], isop20, kind="cubic", axis=0)

    # Metallicities for the isochrones
    FeHs = np.array([0.0, 0.1, 0.2])

    # desired mass range for interpolated isochrone
    masses = np.arange(0.12, 1.51, 0.01)

    # create new isochrones
    trim_iso00 = icurve00(masses)
    trim_iso10 = icurve10(masses)
    trim_iso20 = icurve20(masses)

    new_iso = np.empty_like(trim_iso00)
    # interpolate in Z
    for i in range(len(trim_iso00)):
        icurve = interp1d(FeHs, np.array([trim_iso00[i,:], trim_iso10[i,:], trim_iso20[i,:]]), kind='quadratic', axis=0)
        new_iso[i] = icurve(0.12)

    np.savetxt("dmestar_{:07.1f}myr_z+0.12_a+0.00_phx.iso".format(age/1.0e6), new_iso, fmt="%14.6e")
