---
layout: default
title:  Options
---

## Help

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
