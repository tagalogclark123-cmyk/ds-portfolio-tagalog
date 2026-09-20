# Welcome to my portfolio

:::{div} hero-lead
Hands-on lab reports on **neural networks** and **deep learning with PyTorch**.
Each one starts from the underlying math, builds it up in code, and then checks
the result against a library implementation.
:::

:::{div} hero-badges
{bdg-primary}`Python` {bdg-primary}`NumPy` {bdg-primary}`PyTorch` {bdg-primary}`scikit-learn` {bdg-primary}`pandas` {bdg-primary}`Matplotlib`
:::

## What's inside

::::{grid} 1 1 2 2
:gutter: 3
:class-container: lab-grid

:::{grid-item-card} {octicon}`arrow-right;1.1em;sd-mr-1` Lab 2 · Forward Pass & Error
:link: Lab_Task_2_Forward_Pass_and_Error
:link-type: doc
:class-card: lab-card

A single forward pass through a tiny 3 → 2 → 1 network with ReLU activations,
worked out step by step, then vectorised in NumPy and cross-checked in PyTorch.
+++
{bdg-secondary-line}`NumPy` {bdg-secondary-line}`PyTorch`
:::

:::{grid-item-card} {octicon}`sync;1.1em;sd-mr-1` Lab 3 · Forward & Backward Propagation
:link: Lab_Task_3_Forward_and_Backward_Propagation
:link-type: doc
:class-card: lab-card

Backpropagation by hand with the chain rule, verified with numerical gradient
checking and PyTorch autograd, plus a look at the "dying ReLU" effect.
+++
{bdg-secondary-line}`NumPy` {bdg-secondary-line}`PyTorch` {bdg-secondary-line}`Matplotlib`
:::

:::{grid-item-card} {octicon}`graph;1.1em;sd-mr-1` Lab 4 · PyTorch Regression
:link: Lab_Task_4_PyTorch_Regression
:link-type: doc
:class-card: lab-card

A two-layer network trained with SGD (batch size 8, 1000 epochs) on the
scikit-learn diabetes dataset, benchmarked against plain linear regression.
+++
{bdg-secondary-line}`PyTorch` {bdg-secondary-line}`scikit-learn` {bdg-secondary-line}`pandas`
:::

:::{grid-item-card} {octicon}`stack;1.1em;sd-mr-1` Lab 5 · Tensor Fundamentals
:link: Lab_Task_5_PyTorch_Tensor_Fundamentals
:link-type: doc
:class-card: lab-card

Creating, converting, reshaping, indexing and multiplying tensors, with
reproducible seeding across NumPy and PyTorch.
+++
{bdg-secondary-line}`PyTorch` {bdg-secondary-line}`NumPy`
:::

::::

## How each lab is laid out

Every report follows the same rhythm, so it is easy to skim:

1. **Task card**: the original instructions and given values.
2. **My Approach**: the reasoning and assumptions *before* any code.
3. **Numbered steps**: code, output and short explanations.
4. **Summary**: what the results show and what to carry into the next lab.

```{tip}
Use the {octicon}`download` button at the top of a page to grab the notebook,
the {octicon}`screen-full` button for a distraction-free reading view, and the
half-moon icon to switch between light and dark mode.
```

% Tip: add a short "About me" section here (a couple of sentences + links to
% GitHub / LinkedIn) to make the home page more personal.
