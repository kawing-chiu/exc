import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path

def main():
    # Contour some regular (fake) data
    grid = np.arange(100).reshape((10,10))
    plt.contourf(grid)

    # "外圈"(axes边界)顺时针，"内圈"(图形)逆时针
    # Verticies of the clipping polygon in counter-clockwise order
    #  (A triange, in this case)
    poly_verts = [(2, 2), (5, 2.5), (6, 8), (2, 2)]

    mask_outside_polygon(poly_verts)

    plt.show()

num_to_command = {
    Path.MOVETO: 'move_to',
    Path.LINETO: 'line_to',
    Path.CLOSEPOLY: 'close',
}

def mask_outside_polygon(poly_verts, ax=None):
    """
    Plots a mask on the specified axis ("ax", defaults to plt.gca()) such that
    all areas outside of the polygon specified by "poly_verts" are masked.  

    "poly_verts" must be a list of tuples of the verticies in the polygon in
    counter-clockwise order.

    Returns the matplotlib.patches.PathPatch instance plotted on the figure.
    """
    import matplotlib.patches as mpatches
    import matplotlib.path as mpath

    if ax is None:
        ax = plt.gca()

    # Get current plot limits
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Verticies of the plot boundaries in clockwise order
    bound_verts = [(xlim[0], ylim[0]), (xlim[0], ylim[1]), 
                   (xlim[1], ylim[1]), (xlim[1], ylim[0]), 
                   (xlim[0], ylim[0])]

    # A series of codes (1 and 2) to tell matplotlib whether to draw a line or 
    # move the "pen" (So that there's no connecting line)
    bound_codes = [mpath.Path.MOVETO] + (len(bound_verts) - 1) * [mpath.Path.LINETO]
    poly_codes = [mpath.Path.MOVETO] + (len(poly_verts) - 1) * [mpath.Path.LINETO]

    print("bound_verts + poly_verts:",
          list(zip(bound_verts + poly_verts,
                   [num_to_command[code] for code in bound_codes + poly_codes])))

    # Plot the masking patch
    path = mpath.Path(bound_verts + poly_verts, bound_codes + poly_codes)
    patch = mpatches.PathPatch(path, facecolor='white', edgecolor='none', alpha=0.8)
    patch = ax.add_patch(patch)

    # Reset the plot limits to their original extents
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    return patch

if __name__ == '__main__':
    main()
