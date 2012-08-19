Mcider
======

Mcider is to convert markdown into slideshow.

[![Build Status](https://secure.travis-ci.org/ogom/python-mcider.png?branch=master)](http://travis-ci.org/ogom/python-mcider)

![mcider](https://github.com/ogom/python-mcider/raw/master/mcider.png)


## Installation

    $ pip install mcider

or

    $ easy_install mcider

from source

    $ git clone https://github.com/ogom/python-mcider.git
    $ cd python-mcider
    $ make install


## Usage

Simple, the file is output to the same directory as the markdown.

    $ mcider ./slide.md

If you wanted to display the WEB browser with the option of `-b`.

    $ mcider ./slide.md -b

The output destination can be changed in the options `-o`.

    $ mcider ./slide.md -o /tmp/my.html

Theme is provided  io2012 and io2011. Select the option `-t`.

    $ mcider ./slide.md -t io2011

See also `mcider --help`.


## Examples

  TODO: io2012 and io2011.


## Tests
  make test


## Uses
* [Python-Markdown](https://github.com/waylan/Python-Markdown)
* [HTML5 slide template for Google I/O 2012](http://code.google.com/p/io-2012-slides/)
* [HTML5 slide template for Google I/O 2011](http://code.google.com/p/html5slides/)


## Licence
* [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
