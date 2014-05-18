mCider
======

mCider is markdown converter for slideshow.

* `----` is separate of the slides.
* Adjust the slide to the size of the window.

![mcider](http://ogom.github.com/python-mcider/assets/img/mcider.png)

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

### Initializes

```
$ mcider ./slide.md
```

Other [options](http://ogom.github.com/python-mcider/docs/usage/options.html).

## Examples

* [Examples of Google I/O 2012](http://ogom.github.com/python-mcider/examples/io2012/slide.html)
* [Examples of Google I/O 2011](http://ogom.github.com/python-mcider/examples/io2011/slide.html)


### Base Markdown

```
I/O 2012 slide example
======================

----

### Simple slide with header and text
Here is the text of hgroup.

This is a slide with just text. This is a slide with just text.
```

### Converted HTML

```html
<slide>
  <hgroup>
    <h1>
      I/O 2012 slide example
    </h1>
  </hgroup>
</slide>

<slide>
  <hgroup>
    <h3>
      Simple slide with header and text
    </h3>
    <p>
      Here is the text of hgroup.
    </p>
  </hgroup>
  <article class="none">
    <p>
      This is a slide with just text. This is a slide with just text.<br />
    </p>
  </article>
</slide>
```

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
