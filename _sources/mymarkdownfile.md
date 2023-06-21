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

# Here's my sample title

This is some sample text.

(section-label)=
## Here's my first section

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


