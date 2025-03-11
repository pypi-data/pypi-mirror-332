# %%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde, pearsonr


def collect_multi_csv(
    path_list: list,
    id_col: str,
    identification_func: callable = lambda x: os.path.basename(x),
    pandas_read_kwargs: dict = {},
):
    final_df = pd.DataFrame()
    for path in path_list:
        data = pd.read_csv(path, **pandas_read_kwargs)
        identification = identification_func(path)
        data["file_id"] = identification
        final_df = pd.concat([final_df, data])
    final_df.reset_index(drop=True, inplace=True)
    final_df["uID"] = final_df[id_col].astype(str) + "_" + final_df["file_id"]
    return final_df

def get_frame_plots(
    data: pd.DataFrame,
    frame_col: str,
    id_col: str,
    intensity_col: str = "intensity",
    length_filter: int = 20,
    hist_kwargs: dict = (),
    filter_frame_df_by_tracks: bool = True,
):
    
    print(data.head())
    print()
    track_grp = (
        data.groupby(id_col).filter(lambda x: len(x) > length_filter).groupby(id_col)
    )
    if filter_frame_df_by_tracks:
        filtered_data = data[data[id_col].isin(track_grp.groups.keys())]
    else:
        filtered_data = data
    frame_group = filtered_data.groupby(frame_col)

    first_frame = data[frame_col].min()
    last_frame = data[frame_col].max()

    first_frame_intensity = frame_group.get_group(first_frame)[intensity_col]
    last_frame_intensity = frame_group.last(last_frame)[intensity_col]

    track_first_frame = track_grp[frame_col].first()

    track_lengths = track_grp[intensity_col].count()
    first_intensity = track_grp[intensity_col].first()
    last_intensity = track_grp[intensity_col].last()
    diff_intensity = last_intensity - first_intensity

    frame_df = pd.concat(
        [first_frame_intensity, last_frame_intensity], axis=1, ignore_index=True
    )
    frame_df.columns = ["first_frame", "last_frame"]
    frame_df.reset_index(inplace=True, drop=True)

    track_df = pd.concat(
        [track_lengths, first_intensity, last_intensity, diff_intensity], axis=1
    )
    track_df.columns = ["length", "first_frame", "last_frame", "difference"]

    fig = plt.figure(figsize=(22, 12))
    ax = []
    ax.append(fig.add_subplot(231))
    ax.append(fig.add_subplot(232))
    ax.append(fig.add_subplot(233))
    ax.append(fig.add_subplot(234))
    ax.append(fig.add_subplot(235))
    ax.append(fig.add_subplot(236))

    ax[0].hist(
        first_frame_intensity,
        bins=50,
        alpha=0.5,
        label="First frame [{:.0f}] | N=".format(first_frame)
        + str(len(first_frame_intensity)),
        **hist_kwargs,
    )
    ax[0].set(
        xlabel="Intensity",
        ylabel="Frequency",
        title="Intensity distribution of first frame of data",
    )
    ax[1].hist(
        last_frame_intensity,
        bins=50,
        alpha=0.5,
        label="Last frame [{:.0f}] | N=".format(last_frame)
        + str(len(last_frame_intensity)),
        **hist_kwargs,
    )
    ax[1].set(
        xlabel="Intensity",
        ylabel="Frequency",
        title="Intensity distribution of last frame of data",
    )

    ax[2].hist(
        track_first_frame,
        bins=50,
        alpha=0.5,
        label="First Frame of track | N=" + str(len(track_first_frame)),
        **hist_kwargs,
    )
    ax[2].set(
        xlabel="Frame",
        ylabel="Frequency",
        title="First frame of tracks",
    )

    ax[3].hist(
        first_intensity,
        bins=100,
        alpha=0.5,
        label="First frame | N=" + str(len(first_intensity)),
        **hist_kwargs,
    )
    ax[3].set(
        xlabel="Intensity",
        ylabel="Frequency",
        title="Intensity distribution of first frame of tracks",
    )

    ax[4].hist(
        last_intensity,
        bins=100,
        alpha=0.5,
        label="Last frame | N=" + str(len(last_intensity)),
        **hist_kwargs,
    )
    ax[4].set(
        xlabel="Intensity",
        ylabel="Frequency",
        title="Intensity distribution of last frame of tracks",
    )

    ax[5].hist(
        diff_intensity,
        bins=100,
        alpha=0.5,
        label="Difference | N=" + str(len(diff_intensity)),
        **hist_kwargs,
    )
    ax[5].set(
        xlabel="Intensity",
        ylabel="Frequency",
        title="Track intensity difference last-first",
    )

    for a in ax:
        a.legend()
    fig.tight_layout()

    return (fig, frame_df, track_df)


def intesnity_decrease_plots(
    data: pd.DataFrame,
    percentile_mask: float = 1,
):

    mask = data["first_frame"] < data["first_frame"].quantile(percentile_mask)
    mask &= data["last_frame"] < data["last_frame"].quantile(percentile_mask)
    filtered_data = data[mask]

    kde_1 = gaussian_kde([filtered_data["first_frame"], filtered_data["last_frame"]])
    corr_1, _ = pearsonr(filtered_data["first_frame"], filtered_data["last_frame"])
    linear_fit_1 = np.polyfit(
        filtered_data["first_frame"], filtered_data["last_frame"], 1
    )

    kde_2 = gaussian_kde([filtered_data["length"], filtered_data["difference"]])
    corr_2, _ = pearsonr(filtered_data["length"], filtered_data["difference"])
    linear_fit_2 = np.polyfit(filtered_data["length"], filtered_data["difference"], 1)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax = ax.flatten()
    ax[0].scatter(
        filtered_data["first_frame"],
        filtered_data["last_frame"],
        s=10,
        alpha=0.6,
        edgecolor="k",
        linewidth=0.5,
    )
    x = np.linspace(0, ax[0].get_xlim()[1], 100)
    y = np.linspace(0, ax[0].get_ylim()[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = kde_1([X.ravel(), Y.ravel()]).reshape(X.shape)
    ax[0].contour(X, Y, Z, levels=10, cmap="inferno", alpha=1, zorder=0)
    ax[0].plot(
        x, np.polyval(linear_fit_1, x), color="red", linestyle="-", label="Linear fit"
    )
    ax[0].plot([0, 1], [0, 1], transform=ax[0].transAxes, color="black", linestyle="--")

    ax[0].set_xlabel("First frame intensity")
    ax[0].set_ylabel("Last frame intensity")
    ax[0].set(
        title="First vs last frame",
        xlim=(0, np.percentile(filtered_data["first_frame"], 99)),
        ylim=(0, np.percentile(filtered_data["last_frame"], 99)),
    )
    ax[0].text(
        0.75,
        0.2,
        f"Correlation: {corr_1:.2f}",
        horizontalalignment="center",
        verticalalignment="center",
        transform=ax[0].transAxes,
        bbox=dict(facecolor="white", alpha=0.5),
    )

    ax[1].scatter(
        filtered_data["length"],
        filtered_data["difference"],
        s=10,
        alpha=0.6,
        edgecolor="k",
        linewidth=0.5,
    )
    ax[1].axhline(0, color="black", linestyle="--")
    x = np.linspace(*ax[1].get_xlim(), 100)
    y = np.linspace(*ax[1].get_ylim(), 100)
    X, Y = np.meshgrid(x, y)
    Z = kde_2([X.ravel(), Y.ravel()]).reshape(X.shape)
    ax[1].contour(X, Y, Z, levels=10, cmap="inferno", alpha=1, zorder=0)
    ax[1].plot(
        x, np.polyval(linear_fit_2, x), color="red", linestyle="-", label="Linear fit"
    )
    ax[1].set_xlabel("Track length")
    ax[1].set_ylabel("Intensity difference")
    ax[1].set(title="Track length vs intensity difference")
    ax[1].text(
        0.5,
        0.1,
        f"Correlation: {corr_2:.2f}",
        horizontalalignment="center",
        verticalalignment="center",
        transform=ax[1].transAxes,
        bbox=dict(facecolor="white", alpha=0.5),
    )
    plt.tight_layout()
    [ax_.legend() for ax_ in ax]

    return (fig, corr_1, corr_2)

# %%
