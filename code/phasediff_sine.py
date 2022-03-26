"""Two travelling sine waves, with a phase difference."""

# Copyright 2022 Qi Tianshi.
# Licensed under GNU GPL v3.0.


from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


X_MAX = 4

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line1, = ax.plot([], [])
line2, = ax.plot([], [])

# Limits
ax.set_xlim((0, X_MAX))
ax.set_ylim((-1.5, 1.5))

# Ticks
ax.set_xticks([])
ax.set_yticks(ticks=[-1, 0, 1],
              labels=[r'V\textsubscript{min}', '0', r'V\textsubscript{max}'])

# Labels next to arrowheads
ax.set_ylabel(r'V(t)', loc='top', rotation=0)
ax.set_xlabel('t', loc='right')

# Vertical left and horizontal center axes with arrowheads.
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.plot(1, 0, ls='', marker=5, ms=5, color='k',
        transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, ls='', marker=6, ms=5, color='k',
        transform=ax.get_xaxis_transform(), clip_on=False)


def _init():
    line1.set_data([], [])
    line2.set_data([], [])
    return (line1,)


def _anim(i):
    x = np.linspace(0, X_MAX, 1000)
    y1 = np.sin(2 * np.pi * (x - 0.01 * i))
    y2 = np.sin(2 * np.pi * (x - 0.01 * i) + 1)
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    return (line1, line2)


# Animate
anim = FuncAnimation(fig, _anim, init_func=_init, frames=100, interval=16,
                     blit=True)
anim.save('videos/ac/phasediff_sine.gif', writer='imagemagick')

# plt.show()
