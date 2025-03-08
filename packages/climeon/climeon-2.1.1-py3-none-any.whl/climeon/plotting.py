"""Climeon plotting utilities."""

# External modules
import pandas as pd
from plotly.graph_objects import Scattergl
from plotly.subplots import make_subplots
from plotly_resampler import FigureResampler, FigureWidgetResampler, \
    EveryNthPoint

DEFAULT_HEIGHT = 900

STATES = [
    "INIT",
    "IDLE",
    "READY",
    "START",
    "RUNNING",
    "STOP",
    "MANUAL",
    "",
    "NOT_AVAILABLE",
    "TIMEOUT",
    "PREHEATING"
]

START_STATES = [
    "INIT",
    "AWAIT_COLD_WATER",
    "START_DT",
    "START_MAIN_PUMP",
    "AWAIT_HOT_WATER",
    "PHT_FLUSH_COOLING",
    "PHT_HEAT_UP_GAS",
    "PHT_HEAT_UP_COILS",
    "PHT_HEAT_UP_TURBINE",
    "PHT_DEC_BOOSTER",
    "COND_BEAR",
    "START_TURBINE",
    "PRE_COND_TURBINE",
    "AWAIT_TURBINE_SPEED",
    "START_BOOSTER_PUMP",
    "RAMP_UP_TURBINE",
    "AWAIT_START_SPEED"
]

STATUS_WORD = [
    "READY",
    "IDLE",
    "STARTING",
    "RUNNING",
    "STOPPING",
    "PLANNED_STOP",
    "UNPLANNED_STOP",
    "TIMEOUT",
    "LIMPMODE",
    "", # VACANT
    "", # VACANT
    "", # ALARM
    "", # CRITICAL_ALARM
    "", # EMERGENCY_ALARM
    "", # WARNING
    "", # VACANT
    "", # TURBINE_RUN
    "", # MAIN_PUMP_RUN
    "", # BOOSTER_PUMP_RUN
    "", # BOOSTER_VALVE_OPEN
    "", # COOLING_VALVE_OPEN
    "", # VACANT
    "", # ATU_EVACUATING
    "", # VACANT
    "", # DRAIN_VALVE_OPEN
    "", # SPRAY_VALVE_OPEN
    "", # GAS_VALVE_OPEN
    "", # EXHAUST_VALVE_OPEN
    "", # VACANT
    "", # VACANT
    "", # VACANT
    "", # REMOTE_CONTROL
]

CONTROL_MASTER = [
    "",
    "POWER PID",
    "GEN TEMP PID",
    "PROCESS PID",
    "ANTICAV PID",
    "RETURN TEMP PID",
    "DEIF PID",
]

STATE_MAP = {
    "State [-]": STATES,
    "StartState [-]": START_STATES,
    "StatusWord [-]": STATUS_WORD,
    "ControlMaster [-]": CONTROL_MASTER,
}

STATE_VARIABLES = [
    "State [-]",
    "StatusWord [-]",
    "SecondaryStatusWord [-]",
    "ControlMaster [-]",
    "AlarmCode [-]",
]

# Silent Pandas future warnings
try:
    pd.set_option("future.no_silent_downcasting", True)
except Exception: # pylint: disable=broad-exception-caught
    # Older pandas version, nothing to silence
    pass

def add_transition(fig, data, variable, color="blue", template="%s", pos=1,
                   include_first=False):
    """Add status transitions for a specific variable in a plotly figure."""
    # pylint: disable=too-many-arguments,too-many-positional-arguments
    if variable not in data:
        return
    states = STATE_MAP[variable] if variable in STATE_MAP else None
    edges = data[data[variable].diff() != 0][variable].dropna()
    for idx, (timestamp, state) in enumerate(zip(edges.index, edges)):
        if idx == 0 and not include_first:
            continue
        if states and int(state) != state:
            continue
        if variable in ["StatusWord [-]", "SecondaryStatusWord [-]"]:
            bit = int(int(state) ^ int(edges[idx-1])).bit_length() - 1
            if not (int(state) >> bit) & 1 or not states[bit]:
                continue
            text = "%s" % states[bit]
        elif states and not states[int(state)]:
            continue
        elif states:
            text = template % states[int(state)]
        elif "%" in template:
            text = template % state
        else:
            text = template
        fig.add_vline(x=timestamp, line_width=1, line_dash="dash", line_color=color)
        fig.add_annotation(x=timestamp, y=pos, text=text, yref="paper")

def add_transitions(fig, data):
    """Add all possible state transitions.

    Parameters:
        fig (figure):       A plotly figure.
        data (DataFrame):   A pandas dataframe with data.
    """
    # pylint: disable=too-many-arguments
    add_transition(fig, data, "State [-]", pos=0.96)
    add_transition(fig, data, "AlarmCode [-]", "red", "AlarmCode %d", 1.04)
    add_transition(fig, data, "ControlMaster [-]", "green", include_first=True)
    add_transition(fig, data, "NoOfGreasingCyclesFrontBearing [-]", template="Front greasing")
    add_transition(fig, data, "NoOfGreasingCyclesRearBearing [-]", template="Rear greasing")
    add_transition(fig, data, "NoOfAtuCycles [-]", "green", "ATU", 1.02)
    if "State [-]" not in data:
        add_transition(fig, data, "StatusWord [-]", pos=0.96)
    return fig

def color_code(fig, state, colors, text=""):
    """Color code the background of a plot based on state."""
    state_notnull = state.fillna(False).infer_objects(copy=False)
    state_changes = state_notnull[state_notnull.diff() != 0]
    for idx, timestamp in enumerate(state_changes.index):
        if idx == len(state_changes) - 1:
            end_idx = state.index[-1]
        else:
            end_idx = state_changes.index[idx + 1]
        color = colors[int(state_changes[timestamp])]
        if color is not None:
            fig.add_vrect(timestamp, end_idx, annotation_text=text,
                          fillcolor=color, opacity=0.2, line_width=0)
    return fig

def get_figure(rows=1, cols=1, secondary_y=True, resampler=False, height=DEFAULT_HEIGHT):
    """Convenience function for creating a plotly figure.

    Parameters:
        rows (int): Amount of plot rows to include (subplots).
        secondary_y (bool): Indicates if secondary y-axis should be enabled.
        resampler (bool): Indicates if resampling should be done dynamically
                          to improve loading times.
        height (int): Figure height.
    """
    specs = [[{"secondary_y": secondary_y} for _ in range(cols)] for _ in range(rows)]
    fig = make_subplots(rows, cols, shared_xaxes=True, specs=specs,
                        vertical_spacing=0.02, horizontal_spacing=0.02)
    if resampler:
        if is_notebook():
            fig = FigureWidgetResampler(fig)
        else:
            fig = FigureResampler(fig)
    fig.update_layout(hovermode="x", height=height, hoversubplots="axis")
    return fig

def plot(data, resampler=False, height=DEFAULT_HEIGHT):
    """Plot a dataframe with variables of different units on different axes."""
    units = []
    for column in data.columns:
        if "[" in column:
            unit = column[column.index("["):]
        else:
            unit = "[-]"
        if column not in STATE_VARIABLES and unit not in units:
            units.append(unit)
    fig = get_figure((len(units)+1)//2, resampler=resampler, height=height)
    row = 1
    secondary_y = False
    for i, unit in enumerate(units):
        for column in data.columns:
            if column in STATE_VARIABLES:
                continue
            if (unit in column or (unit == "[-]" and "[" not in column)):
                add_trace(fig, data, column, row, secondary_y=secondary_y)
        axis_name = "yaxis%s" % ("" if i == 0 else i + 1)
        fig["layout"][axis_name]["title"] = unit
        if secondary_y:
            fig["layout"][axis_name]["showgrid"] = False
            fig["layout"][axis_name]["zeroline"] = False
        row += (1 if secondary_y else 0)
        secondary_y = not secondary_y
    add_transitions(fig, data)
    return fig

def add_trace(fig, data, variable, row=1, col=1, visible=None, secondary_y=False):
    """Add a trace to a resampled plotly figure."""
    # pylint: disable=too-many-arguments,too-many-positional-arguments
    if not variable in data:
        return fig
    if isinstance(fig, (FigureWidgetResampler, FigureResampler)):
        trace = Scattergl(name=variable, visible=visible)
        fig.add_trace(trace, row=row, col=col, secondary_y=secondary_y,
                      hf_x=data.index, hf_y=data[variable].values,
                      downsampler=EveryNthPoint(interleave_gaps=False))
    else:
        trace = Scattergl(x=data.index, y=data[variable].values, name=variable,
                          visible=visible)
        fig.add_trace(trace, row=row, col=col, secondary_y=secondary_y)
    return fig

def is_notebook():
    """Check if code is running in a notebook."""
    try:
        get_ipython() # type: ignore
        return True
    except NameError:
        return False
