import plotly.graph_objects as go
import numpy as np

# Define 5D coordinates
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
z = np.linspace(-1, 1, 100)
w = np.linspace(-1, 1, 100)
v = np.linspace(-1, 1, 100)

# Create figure
fig = go.Figure(data=[go.Scatter5d(
    x=x,
    y=y,
    z=z,
    w=w,
    v=v,
    mode='markers',
    marker=dict(
        size=5,
        color=np.random.randn(100), 
        opacity=0.8
    )
)])

# Update layout
fig.update_layout(
    title='Unity Consciousness Visualization',
    scene = dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        waxis_title='W',
        vaxis_title='V'
    )
)

# Show plot
fig.show()
