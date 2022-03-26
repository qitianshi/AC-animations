"""Travelling sine wave with its corresponding phasor."""

# Copyright 2022 Qi Tianshi.
# Licensed under GNU GPL v3.0.


from matplotlib.animation import FuncAnimation
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt
import numpy as np

import arrows


X_MAX = 4

# Default fig size is 6.4 x 4.8. This ratio keeps the aspect ratio of
# the sinusoid the same as travelling_sine

fig, (ax_phasor, ax_sine) = plt.subplots(
    1, 2, figsize=(11.2, 4.8), gridspec_kw={'width_ratios': [3, 4]})

line, = ax_sine.plot([], [])

# Limits
ax_sine.set_xlim((0, X_MAX))
ax_sine.set_ylim((-1.5, 1.5))

# Ticks
ax_sine.set_xticks([])
ax_sine.set_yticks(ticks=[-1, 0, 1],
              labels=[r'V\textsubscript{min}', '0', r'V\textsubscript{max}'])

# Labels next to arrowheads
ax_sine.set_ylabel(r'V(t)', loc='top', rotation=0)
ax_sine.set_xlabel('t', loc='right')

# Vertical left and horizontal center axes with arrowheads.
ax_sine.spines['right'].set_visible(False)
ax_sine.spines['top'].set_visible(False)
ax_sine.spines['bottom'].set_position('zero')
ax_sine.plot(1, 0, ls='', marker=5, ms=5, color='k',
             transform=ax_sine.get_yaxis_transform(), clip_on=False)
ax_sine.plot(0, 1, ls='', marker=6, ms=5, color='k',
             transform=ax_sine.get_xaxis_transform(), clip_on=False)

# Axes for phasor
ax_phasor.set_ylim((-1.5, 1.5))
ax_phasor.set_xlim((-1.1, 1.1))
ax_phasor.spines['right'].set_visible(False)
ax_phasor.spines['top'].set_visible(False)
ax_phasor.spines['left'].set_position('zero')
ax_phasor.spines['bottom'].set_position('zero')
ax_phasor.plot(1, 0, ls='', marker=5, ms=5, color='k',
               transform=ax_phasor.get_yaxis_transform(), clip_on=False)
ax_phasor.plot(0, 1, ls='', marker=6, ms=5, color='k',
               transform=ax_phasor.get_xaxis_transform(), clip_on=False)
ax_phasor.set_aspect('equal')

# Ticks
ax_phasor.set_xticks([])
ax_phasor.set_yticks([])

# Unit circle
ax_phasor.add_patch(plt.Circle(
    (0, 0), radius=1, facecolor='white', edgecolor='darkgray', ls='--'))

# Lines and arrows
phasor = ax_phasor.arrow(0, 0, 0, 0)
horiz_connector = ConnectionPatch(
    xyA=(-1, 0), xyB=(0, 0),
    coordsA='data', coordsB='data', axesA=ax_phasor, axesB=ax_sine,
    ls='--', edgecolor='darkgray'
)
ax_sine.add_artist(horiz_connector)
phasor_x_resolve = ax_phasor.arrow(0, 0, 0, 0)
phasor_y_resolve = ax_phasor.arrow(0, 0, 0, 0)


def _init():
    line.set_data([], [])
    return (line,)


def _anim(i):

    x = np.linspace(0, X_MAX, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)

    phasor_coordinates = arrows.rotate_tail(
        0, 0, 1, -1 * (i / 100) * 360 - 90
    )
    phasor_tail = (
        phasor_coordinates[0] + phasor_coordinates[2],      # x
        phasor_coordinates[1] + phasor_coordinates[3]       # y
    )

    global phasor                                          #pylint: disable=all
    phasor.remove()
    phasor = ax_phasor.arrow(
        *phasor_coordinates,
        fc='k', ec='k',
        head_width=0.05, head_length=0.1, length_includes_head=True
    )

    global horiz_connector
    horiz_connector.remove()
    horiz_connector = ConnectionPatch(
        xyA=(phasor_tail[0], phasor_tail[1]), xyB=(0, phasor_tail[1]),
        coordsA='data', coordsB='data', axesA=ax_phasor, axesB=ax_sine,
        ls='--', edgecolor='darkgray'
    )
    ax_sine.add_patch(horiz_connector)

    global phasor_x_resolve
    phasor_x_resolve.remove()
    phasor_x_resolve = ax_phasor.arrow(
        0, 0, phasor_tail[0], 0,
        fc='darkgray', ec='darkgray', ls=':',
        head_width=0.05, head_length=0.1, length_includes_head=True
    )

    global phasor_y_resolve
    phasor_y_resolve.remove()
    phasor_y_resolve = ax_phasor.arrow(
        phasor_tail[0], 0, 0, phasor_tail[1],
        fc='darkgray', ec='darkgray', ls=':',
        head_width=0.05, head_length=0.1, length_includes_head=True
    )

    return (line, phasor, horiz_connector, phasor_x_resolve, phasor_y_resolve)


# Animate
anim = FuncAnimation(fig, _anim, init_func=_init, frames=100, interval=16,
                     blit=True)
anim.save('videos/ac/phasor_and_sine_resolved.gif', writer='imagemagick')

# plt.show()
