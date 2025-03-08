#!/usr/bin/env python3
# License: BSD-3-Clause

import gzip
import io
from base64 import b64decode

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy import units as u
from astropy import visualization
from astropy.io import fits
from astropy.time import Time
from matplotlib.colors import Normalize
from matplotlib.ticker import MultipleLocator
from ztfquery.utils.stamps import get_ps_stamp

from nuztf.ampel.ampel_cutout import create_empty_cutout
from nuztf.api import ensure_cutouts
from nuztf.cat_match import get_cross_match_info
from nuztf.paths import CUTOUT_CACHE_DIR
from nuztf.utils import cosmo


def alert_to_pandas(alert):
    candidate = alert[0]["candidate"]
    prv_candid = alert[0]["prv_candidates"]
    combined = [candidate]
    combined.extend(prv_candid)

    df_detections_list = []
    df_ulims_list = []

    for cand in combined:
        _df = pd.DataFrame().from_dict(cand, orient="index").transpose()
        _df["mjd"] = _df["jd"] - 2400000.5
        if "magpsf" in cand.keys() and "isdiffpos" in cand.keys():
            df_detections_list.append(_df)

        else:
            df_ulims_list.append(_df)

    df_detections = pd.concat(df_detections_list)
    if len(df_ulims_list) > 0:
        df_ulims = pd.concat(df_ulims_list)
    else:
        df_ulims = None

    return df_detections, df_ulims


def lightcurve_from_alert(
    alert: list,
    figsize: list = [8, 5],
    title: str = None,
    include_ulims: bool = True,
    include_cutouts: bool = True,
    include_ps1: bool = True,
    include_crossmatch: bool = True,
    mag_range: list = None,
    z: float = None,
    legend: bool = False,
    grid_interval: int = None,
    t_0_mjd: float = None,
    logger=None,
):
    """plot AMPEL alerts as lightcurve"""

    if logger is None:
        import logging

        logger = logging.getLogger(__name__)
    else:
        logger = logger

    if z is not None:
        if np.isnan(z):
            z = None
            logger.debug("Redshift is nan, will be ignored")

    # ZTF color and naming scheme
    BAND_NAMES = {1: "ZTF g", 2: "ZTF r", 3: "ZTF i"}
    BAND_COLORS = {1: "green", 2: "red", 3: "orange"}

    name = alert[0]["objectId"]
    candidate = alert[0]["candidate"]

    if include_cutouts:
        if "cutoutScience" in alert[0].keys():
            if "stampData" in alert[0]["cutoutScience"].keys():
                logger.debug(f"{name}: Cutouts are present.")
            else:
                logger.debug(f"{name}: Cutouts are missing data. Will obtain them")
                alert = ensure_cutouts(alert)
        else:
            logger.debug(
                "The alert dictionary does not contain cutouts. Will obtain them."
            )
            alert = ensure_cutouts(alert)

    logger.debug(f"Plotting {name}")

    df, df_ulims = alert_to_pandas(alert)

    fig = plt.figure(figsize=figsize)

    if include_cutouts:
        lc_ax1 = fig.add_subplot(5, 4, (9, 19))
        cutoutsci = fig.add_subplot(5, 4, (1, 5))
        cutouttemp = fig.add_subplot(5, 4, (2, 6))
        cutoutdiff = fig.add_subplot(5, 4, (3, 7))
        cutoutps1 = fig.add_subplot(5, 4, (4, 8))
    else:
        lc_ax1 = fig.add_subplot(1, 1, 1)
        fig.subplots_adjust(top=0.8, bottom=0.15)

    plt.subplots_adjust(wspace=0.4, hspace=1.8)

    if include_cutouts:
        for cutout_, ax_, type_ in zip(
            [alert[0], alert[0], alert[0]],
            [cutoutsci, cutouttemp, cutoutdiff],
            ["Science", "Template", "Difference"],
        ):
            create_stamp_plot(alert=cutout_, ax=ax_, cutout_type=type_)

        if include_ps1:
            img_cache = CUTOUT_CACHE_DIR.joinpath(f"{name}_PS1.png")

            if not img_cache.is_file():
                img = get_ps_stamp(
                    candidate["ra"], candidate["dec"], size=240, color=["y", "g", "i"]
                )
                img.save(img_cache)

            else:
                from PIL import Image

                img = Image.open(img_cache)

            cutoutps1.imshow(np.asarray(img))
            cutoutps1.set_title("PS1", fontdict={"fontsize": "small"})
            cutoutps1.set_xticks([])
            cutoutps1.set_yticks([])

    # If redshift is given, calculate absolute magnitude via luminosity distance
    # and plot as right axis
    if z is not None:
        dist_l = cosmo.luminosity_distance(z).to(u.pc).value

        def mag_to_absmag(mag):
            absmag = mag - 5 * (np.log10(dist_l) - 1)
            return absmag

        def absmag_to_mag(absmag):
            mag = absmag + 5 * (np.log10(dist_l) - 1)
            return mag

        lc_ax3 = lc_ax1.secondary_yaxis(
            "right", functions=(mag_to_absmag, absmag_to_mag)
        )

        if not include_cutouts:
            lc_ax3.set_ylabel(f"Absolute Magnitude [AB]")

    # Give the figure a title
    if not include_cutouts:
        if title is None:
            fig.suptitle(f"{name}", fontweight="bold")
        else:
            fig.suptitle(title, fontweight="bold")

    if grid_interval is not None:
        lc_ax1.xaxis.set_major_locator(MultipleLocator(grid_interval))

    lc_ax1.grid(visible=True, axis="both", alpha=0.5)
    lc_ax1.set_ylabel("Magnitude [AB]")

    if not include_cutouts:
        lc_ax1.set_xlabel("MJD")

    # Determine magnitude limits
    if mag_range is None:
        max_mag = np.max(df.magpsf.values) + 0.3
        min_mag = np.min(df.magpsf.values) - 0.3
        lc_ax1.set_ylim([max_mag, min_mag])
    else:
        lc_ax1.set_ylim([np.max(mag_range), np.min(mag_range)])

    for fid in BAND_NAMES.keys():
        # Plot older datapoints
        df_temp = df.iloc[1:].query("fid == @fid")
        lc_ax1.errorbar(
            df_temp["mjd"],
            df_temp["magpsf"],
            df_temp["sigmapsf"],
            color=BAND_COLORS[fid],
            fmt=".",
            label=BAND_NAMES[fid],
            mec="black",
            mew=0.5,
        )

        # Plot upper limits
        if df_ulims is not None:
            if include_ulims:
                df_temp2 = df_ulims.query("fid == @fid")
                lc_ax1.scatter(
                    df_temp2["mjd"],
                    df_temp2["diffmaglim"],
                    c=BAND_COLORS[fid],
                    marker="v",
                    s=1.3,
                    alpha=0.5,
                )

    # Plot datapoint from alert
    df_temp = df.iloc[0]
    fid = df_temp["fid"]
    lc_ax1.errorbar(
        df_temp["mjd"],
        df_temp["magpsf"],
        df_temp["sigmapsf"],
        color=BAND_COLORS[fid],
        fmt=".",
        label=BAND_NAMES[fid],
        mec="black",
        mew=0.5,
        markersize=12,
    )

    if legend:
        plt.legend()

    # Now we create an infobox
    if include_cutouts:
        info = []

        info.append(name)
        info.append("------------------------")
        info.append(f"RA: {candidate['ra']:.8f}")
        info.append(f"Dec: {candidate['dec']:.8f}")
        if "drb" in candidate.keys():
            info.append(f"drb: {candidate['drb']:.3f}")
        else:
            info.append(f"rb: {candidate['rb']:.3f}")
        info.append("------------------------")

        for entry in ["sgscore1", "distpsnr1", "srmag1"]:
            info.append(f"{entry[:-1]}: {candidate[entry]:.3f}")

        if alert[0].get("kilonova_eval") is not None:
            info.append(
                f"------------------------\nAMPEL KN score: {alert[0]['kilonova_eval']['kilonovaness']}"
            )

        if (redshift := alert[0].get("redshifts", {}).get("ampel_z")) is not None:
            if alert[0]["redshifts"]["group_z_nbr"] in [1, 2]:
                info.append(f"spec z: {redshift:.3f}")
            else:
                info.append(f"photo z: {redshift:.3f}")

        fig.text(0.77, 0.55, "\n".join(info), va="top", fontsize="medium", alpha=0.5)

    # Add annotations

    lc_ax1.annotate(
        "See On Fritz",
        xy=(0.5, 1),
        xytext=(0.78, 0.10),
        xycoords="figure fraction",
        verticalalignment="top",
        color="royalblue",
        url=f"https://fritz.science/source/{name}",
        fontsize=12,
        bbox=dict(boxstyle="round", fc="cornflowerblue", ec="royalblue", alpha=0.4),
    )

    if include_crossmatch:
        xmatch_info = get_cross_match_info(
            raw=alert[0],
        )
        if include_cutouts:
            ypos = 0.975
        else:
            ypos = 0.035

        if "[TNS NAME=" in xmatch_info:
            tns_name = (
                xmatch_info.split("[TNS NAME=")[1].split("]")[0].strip("AT").strip("SN")
            )
            lc_ax1.annotate(
                "See On TNS",
                xy=(0.5, 1),
                xytext=(0.78, 0.05),
                xycoords="figure fraction",
                verticalalignment="top",
                color="royalblue",
                url=f"https://www.wis-tns.org/object/{tns_name}",
                fontsize=12,
                bbox=dict(
                    boxstyle="round", fc="cornflowerblue", ec="royalblue", alpha=0.4
                ),
            )

        fig.text(
            0.5,
            ypos,
            xmatch_info,
            va="top",
            ha="center",
            fontsize="medium",
            alpha=0.5,
        )

    if t_0_mjd is not None:
        lc_ax1.axvline(t_0_mjd, linestyle=":")
    else:
        t_0_mjd = np.mean(df.mjd.values)

    # Ugly hack because secondary_axis does not work with astropy.time.Time datetime conversion
    mjd_min = min(np.min(df.mjd.values), t_0_mjd)
    mjd_max = max(np.max(df.mjd.values), t_0_mjd)
    length = mjd_max - mjd_min

    lc_ax1.set_xlim([mjd_min - (length / 20), mjd_max + (length / 20)])

    lc_ax2 = lc_ax1.twiny()

    datetimes = [Time(x, format="mjd").datetime for x in [mjd_min, mjd_max]]

    lc_ax2.scatter(
        [Time(x, format="mjd").datetime for x in [mjd_min, mjd_max]], [20, 20], alpha=0
    )
    lc_ax2.tick_params(axis="both", which="major", labelsize=6, rotation=45)
    lc_ax1.tick_params(axis="x", which="major", labelsize=6, rotation=45)
    lc_ax1.ticklabel_format(axis="x", style="plain")
    lc_ax1.tick_params(axis="y", which="major", labelsize=9)

    if z is not None:
        lc_ax3.tick_params(axis="both", which="major", labelsize=9)

    if z is not None:
        axes = [lc_ax1, lc_ax2, lc_ax3]
    else:
        axes = [lc_ax1, lc_ax2]

    return fig, axes


def create_stamp_plot(alert: dict, ax, cutout_type: str):
    """Helper function to create cutout subplot"""
    v3_cutout_names = {
        "Science": "Cutoutscience",
        "Template": "Cutouttemplate",
        "Difference": "Cutoutdifference",
    }

    if alert.get(f"cutout{cutout_type}") is None:
        v3_cutout_type = v3_cutout_names[cutout_type]
        _data = alert.get(f"cutout{v3_cutout_type}", {}).get("stampData", {})
        if _data is not None:
            data = _data.get("stampData")
        else:
            data = None
        if data is None:
            data = create_empty_cutout()
    else:
        data = alert[f"cutout{cutout_type}"]["stampData"]

    with gzip.open(io.BytesIO(b64decode(data)), "rb") as f:
        data = fits.open(io.BytesIO(f.read()), ignore_missing_simple=True)[0].data
    vmin, vmax = np.percentile(data[data == data], [0, 100])
    data_ = visualization.AsinhStretch()((data - vmin) / (vmax - vmin))
    ax.imshow(
        data_,
        norm=Normalize(*np.percentile(data_[data_ == data_], [0.5, 99.5])),
        aspect="auto",
    )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(cutout_type, fontdict={"fontsize": "small"})
