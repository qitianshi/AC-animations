"""Travelling AC wave with galvanometer."""

# Copyright 2022 Qi Tianshi.
# Licensed under GNU GPL v3.0.


from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

import arrows


X_MAX = 4

# Default fig size is 6.4 x 4.8. This ratio keeps the aspect ratio of
# the sinusoid the same as travelling_sine

fig, (ax_img, ax_sine) = plt.subplots(
    1, 2, figsize=(8.53, 4.8), gridspec_kw={'width_ratios': [1, 3]})

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


# Circuit diagram
image = mpimg.imread('resources/ac_galvanometer.png')
im = ax_img.imshow(image)
ax_img.axis('off')
arrow = ax_img.arrow(0, 0, 0, 0)


def _init():
    line.set_data([], [])
    return (line,)


def _anim(i):

    x = np.linspace(0, X_MAX, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)

    global arrow                                           #pylint: disable=all
    arrow.remove()
    arrow = ax_img.arrow(
        *arrows.rotate_center(
            414, 1050, 160, -1 * (np.sin((i / 100) * 2 * np.pi) * 60 + 180)
        ),
        fc='k', ec='k',
        head_width=30, head_length=60, length_includes_head=True)

    return (line, arrow)


# Animate
anim = FuncAnimation(fig, _anim, init_func=_init, frames=100, interval=16,
                     blit=True)
anim.save('videos/ac/ac_galvanometer.gif', writer='imagemagick')

# plt.show()
