mCider
======

mCider is markdown converter for slideshow.

* [Google I/O 2012](http://ogom.github.com/python-mcider/examples/io2012/slide.html)
* [Google I/O 2011](http://ogom.github.com/python-mcider/examples/io2011/slide.html)

![mcider](http://ogom.github.io/python-mcider/assets/img/mcider.png)

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

`-x` option to extend the markdown. [(Available Extensions)](http://freewisdom.org/projects/python-markdown/Available_Extensions)

```
$ mcider ./slide.md -x fenced_code tables
```

`--presenter` option is displayed in Presenter mode. Only theme `io2012`.

```
$ mcider ./slide.md -b --presenter
```

See also `mcider --help`.

## How to use
### Output Hints

Separates the slide is `----` or `____` or `****` be returned to hr tab at markdown.

io2012 or io2011 of the theme to change the class of article in the horizon.

| horizon | article class |
|:-------:|:--------------|
|  ----   |  none         |
|  ____   |  smaller      |
|  ****   |  fill         |

### I/O 2012

#### Presenter note

converted to the presenter note from markdown comment tag.

```markdown
<!--
  write a note here.
-->
```

```html
<aside class="note">
  write a note here.
</aside>
```

![presenter](http://ogom.github.com/python-mcider/assets/img/presenter.png)

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

* MIT
