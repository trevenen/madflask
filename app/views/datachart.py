import plotly
import plotly.graph_objects as go 
from flask import Flask, render_template
import json

def create_graph():
    data=[go.Pie(
        values=[50, 10, 10, 10, 10, 10],
        labels=["Log Level", "Debug", "Info", "Warn", "Error", "Fatal"],
        domain={"x": [0, .48]},
        marker_colors=[
                'rgb(255, 255, 255)',
                'rgb(232,226,202)',
                'rgb(226,210,172)',
                'rgb(223,189,139)',
                'rgb(223,162,103)',
                'rgb(226,126,64)'
            ],
        name="Gauge",
        hole=.3,
        direction="clockwise",
        rotation=90,
        showlegend=False,
        hoverinfo="none",
        textinfo="label",
        textposition="inside"
    )]
    fig = go.Figure(data)
    fig.add_trace(go.Pie(
    values=[40, 10, 10, 10, 10, 10, 10],
    labels=["-", "0", "20", "40", "60", "80", "100"],
    domain={"x": [0, .48]},
    marker_colors=['rgba(255, 255, 255, 0)']*7,
    hole=.4,
    direction="clockwise",
    rotation=108,
    showlegend=False,
    hoverinfo="none",
    textinfo="label",
    textposition="outside"
    ))
    fig.update_layout(
    xaxis=dict(
        showticklabels=True,
        showgrid=True,
        zeroline=False,
    ),
    yaxis=dict(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    ),
    shapes=[dict(
                type='path',
                path='M 0.235 0.5 L 0.24 0.65 L 0.245 0.5 Z',
                fillcolor='rgba(44, 160, 101, 0.5)',
                line_width=0.5,
                xref='paper',
                yref='paper')
    ],
    annotations=[
        dict(xref='paper',
             yref='paper',
             x=0.23,
             y=0.45,
            text='50',
            showarrow=False
        )
    ]
    )


    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON