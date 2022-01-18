# XSLT-like transformations over python lists

## Installation

Select a zip on the [releases page](https://github.com/olpa/python-lxslt/releases), give the path to `pip` directly or through `requirements.txt`.

```
pip install https://github.com/olpa/python-lxslt/archive/refs/tags/v0.1.0.zip
```

## Sample XPath-like

```
$ cat sample-xpath.py
import lxslt

tree = ['tree',
        ['child1', 'a'],
        ['child2', 'b'],
        ['child1', 'c'],
        ['child2',
            ['sub-child2', 'd']], ['child2']]

back = lxslt.select(
        tree,
        [lxslt.SelectStep(lxslt.MatchName('child1'))])

print(back)

$ python sample-xpath.py
[['child1', 'a'], ['child1', 'c']]
```

## Sample XSLT-like

```
$ cat ./sample-xslt.py
import lxslt

tree = ['root',
        ['child', 'anything here', '234234'],
        ['sub',
            ['child', 'ignored']]]

templates = [
        lxslt.Rule(lxslt.MatchName('child'), lxslt.Replace([['new-child']]))
        ]

back = lxslt.apply_templates(templates, tree)
print(back)

$ python sample-xslt.py
[['root', ['new-child'], ['sub', ['new-child']]]]
```

# Documentation

TODO
