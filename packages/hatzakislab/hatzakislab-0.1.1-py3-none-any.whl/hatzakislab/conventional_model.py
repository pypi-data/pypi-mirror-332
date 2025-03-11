import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit


def intensity_drop_df(t, I, t0, duration, half_life, drop_ratio):
    k_bleach = np.log(2) / half_life
    if t < t0:
        return -k_bleach * I
    elif t0 <= t <= t0 + duration:
        k_drop = -np.log(drop_ratio) / duration
        return -k_drop * I - k_bleach * I
    elif t > t0 + duration:
        return -k_bleach * I


def intensity_drop(t, amp, t0, duration, half_life, drop_ratio):
    sol = solve_ivp(
        lambda t_temp, I: intensity_drop_df(
            t_temp, I, t0, duration, half_life, drop_ratio
        ),
        [t[0], t[-1]],
        [amp],
        max_step=1,
        t_eval=t,
    )
    return sol.y[0]


def fit_intensity_drop(y, t=None, p0=None, bounds=None, maxfev=10000):
    y_len = len(y)
    if t is None:
        t = np.arange(y_len)
    if p0 is None:
        p0 = [
            y.max(),
            y_len / 2,
            2,
            y_len * 2,
            0.5,
        ]
    if bounds is None:
        bounds = (
            [y.min(), 0, 0, y_len, 0],
            [y.max() * 2, y_len, 10, np.inf, 1],
        )

    popt, pcov = curve_fit(intensity_drop, t, y, p0=p0, bounds=bounds, maxfev=maxfev)
    return_func = lambda t: intensity_drop(t, *popt)
    return return_func, popt, pcov


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    t = np.arange(40, step=1)
    base_line = 300
    amp = 100
    t0 = 10
    duration = 5
    half_life = 20
    drop_ratio = 0.5
    I = intensity_drop(t, amp, t0, duration, half_life, drop_ratio) + base_line
    I_poisson = np.random.poisson(I)

    plt.axvline(t0, color="r", linestyle="--")
    plt.axvline(t0 + duration, color="r", linestyle="--")
    plt.plot(t, I - base_line)
    plt.plot(t, I_poisson - base_line)
    plt.ylim(0, amp * 1.4)
    plt.show()
