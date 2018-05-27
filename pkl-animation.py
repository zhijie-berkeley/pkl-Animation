# python animate_pkl.py *.pkl (--save)
from pathlib import Path
import mplcursors
from qtlib.types import OpenFilesType
from tweezers import api as tz, get_option
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def pklAnimation(time, dist, name, save):
    fig = plt.figure()
    ax = plt.axes(xlim=(0, max(time) + 50))
    ax.set(xlabel = "Time (s)", ylabel = "Transcribed distance (bp)", title = f"{name}.pkl")
    # ax.xaxis.label.set_fontsize(14)
    # ax.yaxis.label.set_fontsize(14)
    time_text = ax.text(0.95, 0.05,'',horizontalalignment='right',
        verticalalignment='bottom',
        transform=ax.transAxes,
        fontsize=12,
        bbox=dict(facecolor='yellow'))
    line, = ax.plot([], [], lw=2, color = 'red')
    xdata, ydata = [], []
    print(len(time))
    npss = 888.5, 961.5, 1035.5

    def init():
        line.set_data([], [])
        time_text.set_text('Start')
        return line, time_text

    def animate(i):
        x = time[i]
        y = dist[i]
        xdata.append(x)
        ydata.append(y)
        line.set_data(xdata, ydata)
        for pos in npss:
            if (y > pos):
                ax.axhline(pos, ls="--", color="k")
        ax.relim()
        ax.autoscale_view()
        time_text.set_text('Time: %.2fs' % x)
        return line, time_text

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=1, blit=True, repeat=False)
    # save animation
    if save:
        anim.save(f"{name}.mp4", writer="ffmpeg", fps=15, metadata={'title':'Animation of ploting ' + name +'.pkl'})
    else:
        plt.show()

def pklNpsAnimation(time, dist, name, save):
    fig = plt.figure()
    ax = plt.axes(xlim=(min(time) - 50, max(time) + 130), ylim=(min(dist) - 50, max(dist) + 50))
    ax.set(xlabel = "Time (s)", ylabel = "Transcribed distance (bp)", title = f"{name}.pkl")
    # ax.xaxis.label.set_fontsize(14)
    # ax.yaxis.label.set_fontsize(14)
    time_text = ax.text(0.01, 0.98,'',horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        fontsize=12,
        bbox=dict(facecolor='yellow'))
    line, = ax.plot([], [], lw=2, color = 'red')
    xdata, ydata = [], []
    print(len(time))
    npss = 888.5, 961.5, 1035.5
    for pos in npss:
        ax.axhline(pos, ls="--", color="k")
    ax.text(533, 876, 'NPS Entry')
    ax.text(533, 948, 'dyad')
    ax.text(533, 1022, 'NPS Exit')

    def init():
        line.set_data([], [])
        time_text.set_text('Start')
        return line, time_text

    def animate(i):
        x = time[i]
        y = dist[i]
        xdata.append(x)
        ydata.append(y)
        line.set_data(xdata, ydata)
        time_text.set_text('Time: %.2fs' % x)
        return line, time_text

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=1, blit=True, repeat=False)
    # save animation
    if save:
        anim.save(f"{name}-NPS.mp4", writer="ffmpeg", fps=15, metadata={'title':'Animation of ploting ' + name +'.pkl'})
    else:
        plt.show()

def main(filePath: Path, *,
         save: bool = False):
    print("reading...", filePath)
    name = str(filePath)[:-4]
    tr = tz.trace(filePath).get_downsampled_to(1)
    time = tr.time.tolist()
    dist = tr.dist.tolist()

    startIndex = next(n for n, i in enumerate(dist) if i > 850)
    endIndex = next(n for n, i in enumerate(dist) if i > 1050)
    print(startIndex, endIndex)

    font = {'family':'sans-serif', 'size': 12}
    plt.rc('font', **font)
# creat animation for full trace or zoom in animation on NPS region
    pklAnimation(time, dist, name, save)
    pklNpsAnimation(time[startIndex:endIndex], dist[startIndex:endIndex], name, save)

if __name__ == "__main__":
    import defopt
    defopt.run(main)