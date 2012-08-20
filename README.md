Mcider
======

Mcider is to convert markdown into slideshow.

![mcider](https://github.com/ogom/python-mcider/raw/master/mcider.png)

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

If you wanted to display the WEB browser with the option of `-b`.

    $ mcider ./slide.md -b

The output destination can be changed in the options `-o`.

    $ mcider ./slide.md -o /tmp/my.html

Theme is provided  io2012 and io2011. Select the option `-t`.

    $ mcider ./slide.md -t io2011

[Extensions](http://freewisdom.org/projects/python-markdown/Available_Extensions) of markdown is the options `-x`.

    $ mcider ./slide.md -x fenced_code tables


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
