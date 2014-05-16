---
layout: default
title:  Overview
---

mCider is markdown converter for slideshow.

* [Examples of Google I/O 2012]({{ site.baseurl }}/examples/io2012/slide.html).
* [Examples of Google I/O 2011]({{ site.baseurl }}/examples/io2011/slide.html).

<style>img[alt=mcider] { margin-left: 60px;}</style>
![mcider]({{ site.baseurl }}/assets/img/mcider.png)

## Installation

```
$ pip install mcider
```

or

```
$ easy_install mcider
```

from source

```
$ git clone https://github.com/ogom/python-mcider.git
$ cd python-mcider
$ make install
```

## Usage

Simple, the file is output to the same directory as the markdown.

```
$ mcider ./slide.md
```

`-b` option is displayed in the web browser.

```
$ mcider ./slide.md -b
```

`-o` option to change the location to save the file.

```
$ mcider ./slide.md -o /tmp/my.html
```

`-t` option to change the theme of the slide.

```
$ mcider ./slide.md -t io2011
```

`-x` option to extend the markdown. [(Available Extensions)](https://pythonhosted.org/Markdown/extensions/index.html)

```
$ mcider ./slide.md -x fenced_code tables
```

`--presenter` option is displayed in Presenter mode. Only theme `io2012`.

```
$ mcider ./slide.md -b --presenter
```

See also `mcider --help`.

## Tests

```
$ make test
```

[![Build Status](https://secure.travis-ci.org/ogom/python-mcider.png?branch=master)](http://travis-ci.org/ogom/python-mcider)

## Uses

* [Python-Markdown](https://github.com/waylan/Python-Markdown)
* [HTML5 slide template for Google I/O 2012](http://code.google.com/p/io-2012-slides/)
* [HTML5 slide template for Google I/O 2011](http://code.google.com/p/html5slides/)

## Licence

* [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
