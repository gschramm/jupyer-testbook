---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# A chapter containing many things

This is some sample text.

(section-label)=
## A section containing code

Here is a [reference to the intro](intro.md). Here is a reference to [](section-label).

```{code-cell}
print(2 + 2)
```

```{code-cell}
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x**2

fig, ax = plt.subplots()
ax.plot(x,y)
```

## A section containing math

This is an important equation according to {cite}`holdgraf_evidence_2014`

```{math}
:label: eq-one
\int_0^\alpha f(x) dx = I_\alpha
```
See Equation [](eq-one)

\begin{gather*}
a_1=b_1+c_1\\
a_2=b_2+c_2-d_2+e_2
\end{gather*}

This works because of the amsmath MyST extension:

```{math}
:label: eq-two
\begin{align}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align}
```

See Equation [](eq-two)


## A section containg a table

Here is [My cool table](my-table-ref)

```{table} A table
:name: my-table-ref

| col 1 | col 2 |
|---|---|
| 3 | 4 |
| 1 | 2 |
| a | b |
```

## Bibliography

```{bibliography}
:style: unsrt
```
