# Hello, World.

:::{div} hero-lead
I'm **Clark James E. Tagalog**, a **Data Science Undergraduate** working where
technology, sustainability and social good come together.
:::

```{raw} html
<div class="terminal">
  <div class="terminal-bar">
    <span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
    <span class="terminal-title">profile.py</span>
  </div>
<pre class="terminal-body"><code><span class="t-k">class</span> <span class="t-f">Developer</span>:
    name    = <span class="t-s">"Clark James E. Tagalog"</span>
    program = <span class="t-s">"Data Science Undergraduate"</span>
    focus   = [<span class="t-s">"data analytics"</span>, <span class="t-s">"ICT"</span>,
               <span class="t-s">"sustainability"</span>, <span class="t-s">"social advocacy"</span>]
    mission = <span class="t-s">"technology + sustainability + social good"</span>

<span class="t-k">if</span> __name__ == <span class="t-s">"__main__"</span>:
    <span class="t-b">print</span>(Developer.mission)

<span class="t-p">$</span> python profile.py
<span class="t-o">technology + sustainability + social good</span><span class="cursor"></span></code></pre>
</div>
```

:::{div} hero-badges
{bdg-primary}`Python` {bdg-primary}`PyTorch` {bdg-primary}`NumPy` {bdg-primary}`scikit-learn` {bdg-primary}`pandas` {bdg-primary}`Matplotlib`
:::

## About me

I am deeply committed to environmental conservation and social advocacy,
working to promote sustainability, eco-friendly practices, and inclusive
communities. My passion lies in advancing equality and justice, using my voice
and actions to challenge discrimination and push for meaningful change.

With a background in data analytics and a strong interest in Information and
Communication Technology (ICT), I strive to integrate technology into my
advocacy work. I believe in harnessing data and innovation to design solutions
that not only address environmental challenges but also create opportunities
for marginalized communities.

> At the core of my work is the vision of building a future that is sustainable,
> inclusive, and resilient, where technology, sustainability, and social good
> come together to make lasting impact.

## Focus areas

::::{grid} 1 1 3 3
:gutter: 3
:class-container: lab-grid

:::{grid-item-card} {octicon}`globe;1.1em;sd-mr-1` Sustainability
:class-card: lab-card

Environmental conservation and eco-friendly practices, using data and
innovation to design solutions to environmental challenges.
:::

:::{grid-item-card} {octicon}`people;1.1em;sd-mr-1` Inclusion & Justice
:class-card: lab-card

Advancing equality, challenging discrimination, and creating opportunities for
marginalized communities.
:::

:::{grid-item-card} {octicon}`cpu;1.1em;sd-mr-1` Data & ICT
:class-card: lab-card

A background in data analytics and a strong interest in ICT, integrating
technology into advocacy work.
:::

::::

## Lab reports

<!-- ─────────────────────────────────────────────────────────────────────────
     ADDING A NEW LAB?  Copy one card below, paste it just before the closing
     "::::", then change: the title, the ":link:" (notebook filename WITHOUT
     .ipynb), the description, and the badges.
     ───────────────────────────────────────────────────────────────────────── -->

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

:::{grid-item-card} {octicon}`workflow;1.1em;sd-mr-1` Lab 6 · CNN Architecture
:link: Lab_Activity_6_CNN_Architecture
:link-type: doc
:class-card: lab-card

Turning a CNN architecture diagram into a PyTorch model: layer shapes derived
by hand, verified with a dummy forward pass, plus a correct Softmax + NLLLoss
training step.
+++
{bdg-secondary-line}`PyTorch` {bdg-secondary-line}`CNN`
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
