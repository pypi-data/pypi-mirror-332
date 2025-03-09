import marimo

__generated_with = "0.11.17"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from svg import SVG, Circle, G, Rect
    import random
    return Circle, G, Rect, SVG, mo, random


@app.cell
def _(random):
    datapoints = []
    for _i in range(3):
        datapoints.append({
            'x': random.randint(20,180),
            'y': random.randint(20,180),
            'z': random.randint(20,180),
            'id': _i
        })
    return (datapoints,)


@app.cell
def _(Circle, datapoints):
    circles1 = []
    for datapoint in datapoints:
        circles1.append(Circle(
                        cx=datapoint['x'],
                        cy=datapoint['y'],
                        r=10,
                        fill="steelblue",
                        fill_opacity=0.5,
                        stroke_width=1,
                        stroke="white",
                        class_="jfsi2 brushable plot1",
                        id=datapoint['id']))

    circles2 = []
    for datapoint in datapoints:
        circles2.append(Circle(
                        cx=datapoint['x'],
                        cy=datapoint['z'],
                        r=10,
                        fill="steelblue",
                        fill_opacity=0.5,
                        stroke_width=1,
                        stroke="white",
                        class_="jfsi2 brushable plot2",
                        id=datapoint['id']))
    return circles1, circles2, datapoint


@app.cell
def _(SVG, circles1, circles2):
    svg1 = SVG(
        class_="notebook plot1",
        width=200,
        height=200,
        elements=[circles1]
    )
    svg2 = SVG(
        class_="notebook plot2",
        width=200,
        height=200,
        elements=[circles2]
    )
    return svg1, svg2


@app.cell
def _():
    from brushable_widget import BrushableWidget
    return (BrushableWidget,)


@app.cell
def _(mo):
    get_selected, set_selected = mo.state([])
    return get_selected, set_selected


@app.cell
def _(BrushableWidget, get_selected, svg1, svg2):
    brushable_1 = BrushableWidget(svg=svg1.as_str(), selected_ids = get_selected())
    brushable_2 = BrushableWidget(svg=svg2.as_str(), selected_ids = get_selected())
    return brushable_1, brushable_2


@app.cell
def _():
    msg = "test"
    return (msg,)


@app.cell
def _():
    def set_msg(x):
        msg = x["new"]
    return (set_msg,)


@app.cell
def _(brushable_1, brushable_2, set_msg):
    # brushable_1.observe(lambda x: set_selected(x["new"]), names="selected_ids")
    # brushable_2.observe(lambda x: set_selected(x["new"]), names="selected_ids")
    brushable_1.observe(lambda x: set_msg(x), names="selected_ids")
    brushable_2.observe(lambda x: set_msg(x), names="selected_ids")
    return


@app.cell
def _(mo, msg):
    mo.ui.text(msg)
    return


@app.cell
def _(brushable_1, brushable_2, mo):
    [mo.ui.anywidget(brushable_1), mo.ui.anywidget(brushable_2)]
    return


@app.cell
def _():
    print("hi")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
