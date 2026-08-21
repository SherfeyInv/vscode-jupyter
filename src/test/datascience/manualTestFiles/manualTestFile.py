# To run this file either conda or pip install the following: jupyter, torch, numpy, matplotlib, pandas, tqdm, bokeh, vega_datasets, altair, vega, plotly
# When installing torch please visit https://pytorch.org to identify the install instructions for your OS

# %% Basic Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch

# %% Matplotlib Plot
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

#%% Test exception
def raiser():
    raise Exception("<This is bracketed>")

#%% Call exception
# The test previously called raiser() unconditionally which will always raise.
# Keep the function for manual testing, but do NOT call it automatically.
# If you want to exercise it during an interactive/manual run, set call_raiser = True.
call_raiser = False
if call_raiser:
    try:
        raiser()
    except Exception as e:
        # Print or handle the exception during manual testing
        print("raiser() raised:", e)

# %% Bokeh Plot
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
# Only call output_notebook() if running in an environment that supports notebook output.
try:
    output_notebook()
except Exception:
    # Non-notebook environment; skip notebook-specific setup.
    pass

p = figure(plot_width=400, plot_height=400)
p.circle([1,2,3,4,5], [6,7,2,4,5], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)
# show(p)  # show() may or may not render depending on the environment; leave commented for automated runs.

# %% Progress bar
from tqdm import trange
import time
for i in trange(100):
    time.sleep(0.01)

# %% [markdown]
# # Heading
# ## Sub-heading
# *bold*,_italic_,`monospace`
# Horizontal rule
# ---
# Bullet List
# * Apples
# * Pears
# Numbered List
# 1. ???
# 2. Profit
#
# [Link](http://www.microsoft.com)
print('post markdown cell')

# %% Magics
# Replace the bare %whos magic with a guard so it runs only if IPython is available.
try:
    ip = get_ipython()  # type: ignore(NameError)
    if ip is not None:
        ip.run_line_magic('whos', '')
except Exception:
    # Not in IPython environment: skip
    pass

# %% Some extra variable types for the variable explorer
myNparray = np.array([['Bob', 1, 2, np.inf], ['Alice', 4, np.nan, 6], ['Gina', -np.inf, 8, 9]])
myDataFrame = pd.DataFrame(myNparray, columns=['name', 'b', 'c', 'd'])
mySeries = myDataFrame['name']
myList = [x ** 2 for x in range(0, 100000)]
myString = 'testing testing testing'
myTensor = torch.LongTensor([[[1, 2, 3], [4, 5, 6]]])

# %% Latex
# Convert the %%latex cell magic into an IPython-safe display call. If IPython is not present, skip.
latex_content = r"""
\begin{align}
\nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} & = 0
\end{align}
"""
try:
    from IPython.display import Latex, display  # type: ignore
    display(Latex(latex_content))
except Exception:
    # Not in IPython: skip latex rendering
    pass

# %% Altair (vega)
import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalLength',
    y='petalWidth',
    color='species'
)

# %% Plotly
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1, 5]))
# For automated runs, avoid opening interactive viewers; comment out in non-interactive contexts.
# fig.show()

#%% [markdown]
# ## Test split cell (code below should run -- see issue https://github.com/microsoft/vscode-jupyter/issues/8543)
print("hi")
