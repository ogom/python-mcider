---
layout: default
title:  Documentation
---

## Options

### Help

```
mcider --help
```

### Browser

`-b` option is displayed in the web browser.

```
$ mcider ./slide.md -b
```

### Output

`-o` option to change the location to save the file.

```
$ mcider ./slide.md -o /tmp/my.html
```

### Theme

`-t` option to change the theme of the slide.

```
$ mcider ./slide.md -t io2011
```

### Extensions

`-x` option to extend the markdown. [(Available Extensions)](https://pythonhosted.org/Markdown/extensions/index.html)

```
$ mcider ./slide.md -x fenced_code tables
```

### Presenter

`--presenter` option is displayed in Presenter mode. Only theme `io2012`.

```
$ mcider ./slide.md -b --presenter
```

### Themes

`--themes` option to change the custom themes to the path.

```
$ mcider ./slide.md --themes ./themes
```

[The theme here](https://github.com/ogom/mcider-themes).

## Horizon

Separates the slide is `----` or `____` or `****` be returned to hr tab at markdown.

io2012 or io2011 of the theme to change the class of article in the horizon.

| horizon | article class |
|:-------:|:--------------|
|  ----   |  none         |
|  ____   |  smaller      |
|  ****   |  fill         |

## Examples

* [Google I/O 2012](../docs/examples/io2012.html) ([Slide](../examples/io2012/slide.html))
* [Google I/O 2011](../docs/examples/io2011.html) ([Slide](../examples/io2011/slide.html))
