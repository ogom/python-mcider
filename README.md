Mcider
======

Mcider is to convert markdown into slideshow.

![mcider](https://ogom.github.com/python-mcider/images/mcider.png)

### Examples of themes

* [Google I/O 2012](http://ogom.github.com/python-mcider/examples/io2012/slide.html)
* [Google I/O 2011](http://ogom.github.com/python-mcider/examples/io2011/slide.html)


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

`-b` option is displayed in the web browser.

    $ mcider ./slide.md -b

`-o` option to change the location to save the file.

    $ mcider ./slide.md -o /tmp/my.html

`-t` option to change the theme of the slide.

    $ mcider ./slide.md -t io2011

`-x` option to extend the markdown. [(Available Extensions)](http://freewisdom.org/projects/python-markdown/Available_Extensions)

    $ mcider ./slide.md -x fenced_code tables

`--presenter` option is displayed in Presenter mode. Only theme `io2012`.

    $ mcider ./slide.md -b --presenter


See also `mcider --help`.


## How to use
### Output Hints

Separates the slide is `---` or `___` or `***` be returned to hr tab at markdown.  
io2012 or io2011 of the theme to change the class of article in the horizon. 

 horizon |  article class
-------- | --------------
  ---    |  none
  ___    |  smaller
  ***    |  fill


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

![presenter](https://ogom.github.com/python-mcider/images/presenter.png)


## Examples

### Theme of io2012

Markdown the original

```markdown
I/O 2012 slide example
======================

---

### Simple slide with header and text
Here is the text of hgroup.

This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  

There is more text just underneath.

___

### Simple slide with header and text (small font)
Here is the text of hgroup.

This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  

There is more text just underneath.

***

### Image filling the slide (with optional header)
Here is the text of hgroup.

![syaraku](images/syaraku_eye.jpg)

There is more text just underneath.
```

The converted html

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
      This is a slide with just text. This is a slide with just text.<br />
      This is a slide with just text. This is a slide with just text.<br />
    </p>
    <p>
      There is more text just underneath.
    </p>
  </article>
</slide>

<slide>
  <hgroup>
    <h3>
      Simple slide with header and text (small font)
    </h3>
    <p>
      Here is the text of hgroup.
    </p>
  </hgroup>
  <article class="smaller">
    <p>
      This is a slide with just text. This is a slide with just text.<br />
      This is a slide with just text. This is a slide with just text.<br />
      This is a slide with just text. This is a slide with just text.<br />
    </p>
    <p>
      There is more text just underneath.
    </p>
  </article>
</slide>

<slide>
  <hgroup>
    <h3>
      Image filling the slide (with optional header)
    </h3>
    <p>
      Here is the text of hgroup.
    </p>
  </hgroup>
  <article class="fill">
    <p>
      <img alt="syaraku" src="images/syaraku_eye.jpg" />
    </p>
    <p>
      There is more text just underneath.
    </p>
  </article>
</slide>
```

### Theme of io2011

Markdown the original

```markdown
I/O 2011 slide example
======================

---

### Simple slide with header and text

This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  

There is more text just underneath.

___

### Simple slide with header and text (small font)

This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  

There is more text just underneath.

***

### Image filling the slide (with optional header)

![syaraku](images/syaraku_eye.jpg)

There is more text just underneath.
```

The converted html

```html
<article class="none">
  <h1>
    I/O 2011 slide example
  </h1>
</article>

<article class="none">
  <h3>
    Simple slide with header and text
  </h3>
  <p>
    This is a slide with just text. This is a slide with just text.<br />
    This is a slide with just text. This is a slide with just text.<br />
    This is a slide with just text. This is a slide with just text.<br />
  </p>
  <p>
    There is more text just underneath.
  </p>
</article>

<article class="smaller">
  <h3>
    Simple slide with header and text (small font)
  </h3>
  <p>
    This is a slide with just text. This is a slide with just text.<br />
    This is a slide with just text. This is a slide with just text.<br />
    This is a slide with just text. This is a slide with just text.<br />
  </p>
  <p>
    There is more text just underneath.
  </p>
</article>

<article class="fill">
  <h3>
    Image filling the slide (with optional header)
  </h3>
  <p>
    <img alt="syaraku" src="images/syaraku_eye.jpg" />
  </p>
  <p>
    There is more text just underneath.
  </p>
</article>
```


## Tests

    $ make test

[![Build Status](https://secure.travis-ci.org/ogom/python-mcider.png?branch=master)](http://travis-ci.org/ogom/python-mcider)


## Uses
* [Python-Markdown](https://github.com/waylan/Python-Markdown)
* [HTML5 slide template for Google I/O 2012](http://code.google.com/p/io-2012-slides/)
* [HTML5 slide template for Google I/O 2011](http://code.google.com/p/html5slides/)


## Licence
* [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
