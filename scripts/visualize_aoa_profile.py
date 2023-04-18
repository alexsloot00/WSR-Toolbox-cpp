# '''
# (c) REACT LAB, Harvard University
# Author: Ninad Jadhav
# '''

# #!/usr/bin/env python3

import argparse
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


"""
Visualization modified by: Alex Sloot 18-05-2023
In this directory:
~/WSR_Project/WSR-Toolbox-cpp/scripts
run the following line to visualize a file.
python3 visualize_aoa_profile.py --file ~/WSR_Project/WSR-Toolbox-cpp/debug/tx1_aoa_profile_10cm_1.csv --nphi 180 --ntheta 90
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="AOA profile csv file")
    parser.add_argument("--nphi", type=int, help="Resolution of azimuth angle")
    parser.add_argument("--ntheta", type=int, help="Resolution of elevation angle")
    args = parser.parse_args()

    # Obtain x, y, z values
    x_range = 2 * args.nphi
    x_val, y_val = np.linspace(-args.nphi, args.nphi, x_range), np.linspace(
        0, args.ntheta, args.ntheta
    )
    z_data = pd.read_csv(args.file).T

    # Create figure
    fig = make_subplots(
        rows=1, cols=2, specs=[[{"type": "surface"}, {"type": "heatmap"}]]
    )
    fig.add_trace(go.Surface(z=z_data.values, x=x_val, y=y_val), row=1, col=1)
    fig.add_trace(go.Heatmap(z=z_data.values, x=x_val, y=y_val), row=1, col=2)

    # Modify different axis fonts for better visibility
    fig.update_layout(
        title="AOA profile",
        scene_camera_eye=dict(x=-0.8, y=-2, z=0.6),
        scene=dict(
            xaxis_title="Azimuth angle (degrees)",
            yaxis_title="Elevation angle (degrees)",
            zaxis_title="Estimated spectrum",
        ),
        font=dict(size=50),
        title_font=dict(size=50),
    )

    # Figure on the left (surface)
    fig.update_scenes(
        xaxis=dict(tickfont=dict(size=20), titlefont=dict(size=35)),
        yaxis=dict(tickfont=dict(size=20), titlefont=dict(size=35)),
        zaxis=dict(tickfont=dict(size=20), titlefont=dict(size=35)),
    )

    # Figure on the right (heatmap)
    fig.update_xaxes(
        title_text="Azimuth angle(degrees)",
        row=1,
        col=2,
    )
    fig.update_yaxes(
        title_text="Elevation angle (degrees)",
        row=1,
        col=2,
    )

    fig.show()


if __name__ == "__main__":
    main()
