from bokeh.plotting import figure
from bokeh.models import HoverTool
from bokeh.models.widgets import Panel


# Bokeh tools in sidebar
TOOLS = "crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset," \
        "tap,save,box_select,poly_select,lasso_select"


def plot_network(x, y,
                 nodes, edges,
                 group_col, color_col, title=None):
    """Draw a network in 2d space using Bokeh
    Function from networkplots.py
    """

    hover = HoverTool(names=['cell'],
                      tooltips=[# ("Cell Barcode", "@{barcode}"),
                                (f"{group_col}", f"@{group_col}"),]
                     )

    fig = figure(plot_height=500, plot_width=750, title=title,
                 tools=[TOOLS, hover])

    # edges
    fig.multi_line(x, y, source=edges,
                   alpha='alphas', line_width=1.5, color='black')
    
    #nodes
    fig.circle(x, y, source=nodes,
               size=10, fill_alpha=0.5, muted_alpha=0.2, color=color_col,
               legend=group_col, hover_alpha=1, hover_fill_color=color_col,
               name='cell')

    fig.legend.click_policy = "mute"

    return fig
