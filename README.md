# Pytex tutorial

Pytex is a language which allows easily script your LaTeX files with Python. 
It supperts good style of code, for example by forcing indents like in Python.
Thus Pytex is easy to learn, easy to read and easy to code in!

## Python and LateX

Every line which starts from # is LaTeX line. Other lines are Python lines. 
```
include("standard")
document.class = "article"

# First line of text.
new_line()
# Second line of text.
````

You can access Python in LaTeX lines by writing `#your code here#`.

```
include("standard")
document.class = "article"
a = 10

# Variable a is equal to #a#
```

Line `# some code` is equivalent to `tex("some code")`.

You don't need to care about `\begin{document}`!

# Indent

LaTeX lines indentation rules are the same as Python lines.
```
for i in range(10):
    # This is line number # i #
    new_line()
```

# Basic commands

* `include("module_name")` – equivalent to `\include{module_name}` in LaTeX. 
* `new_page()` – equivalent to `\newpage'

# Basic properties

* `document` object is main object of a document
  ** `document.class` – class of a documemnt – f. e. article, beamer
  ** `document.title` – title of a document – equivalent to `\title{}`
  ** `document.author` – author of a document – equivalent to `\author{}`
  ** `document.date` – date of a document – equivalent to `\date{}`
