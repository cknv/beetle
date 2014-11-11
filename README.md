Beetle
======

Installation
------------

```shell
$ pip install beetle
```

Plugins
-------
Just installing Beetle will only get you so far though, there is no support of any markup language, nor is there a local server so you can see what the site will look like. It is basic, and intended so.

However...

Beetle is made to be extensible, this means that instead of being forced to use a certain markup language, you can instead find (or write) a plugin that enabled you to use your favorite markup language, install it, tell Beetle about it and off you go!

I have written a few plugins to get me started:

* [Beetle-Markdown](https://github.com/cknv/beetle-markdown), for rendering Markdown.
* [Beetle-Preview](https://github.com/cknv/beetle-preview), for local previewing.
* [Beetle-Image-Compressor](https://github.com/cknv/beetle-image-compressor), for compressing images.
* [Beetle-S3Uploader](https://github.com/cknv/beetle-s3uploader), for uploading to S3 where my site is hosted.

Furthermore, other plugins have been contributed:

* [Beetle-Sass](https://github.com/Tenzer/beetle-sass), for making SASS to CSS.

If you have written a plugin, just drop me a line, and I can add it here.

About
-----
Beetle is a simple static site generator, mostly driven by NIH thinking and a desire to have very little dictated from the engine.

So far, it works for me (TM), and I think I can guarantee that you will find it clunky and hard to work with. Especially from the lack of documentation.

I should give credit where credit is due, so:

* [Jeppe Toustrup](http://tenzer.dk) for early adopting and complaining whenever I got things wrong.
* [Armin Ronacher](http://lucumr.pocoo.org/) for his [rstblog](https://github.com/mitsuhiko/rstblog) that really got me interested in making a static blog engine.
* [Mike Cooper](http://mythmon.com/) for [wok](https://github.com/mythmon/wok), and showing me there is a simple way to make a static blog - I could easily have ended up using wok or a patched version thereof.
* [Jeff Knupp](http://www.jeffknupp.com/) for pointing out that it's ok to make your own static blog engine, since it's so simple.

Current State
-------------

Beetle already works, but since there is no documentation, be prepared to get your hands dirty and look at example sites and possibly the code, to get a working site up and running.

Gaps and missing stuff
-----------------------
There are some areas that I know I want to work on and improve, these are (in no particular order):

* Documentation.
* Tests.
* Page defaults by category.
* Multipages - pages that render into several pages, useful for some tag pages/feeds.
* Pagination of subpages.

Example Sites
-------------

* The site for which beetle was made: [cknv.dk](http://cknv.dk) and it's repo [github.com/cknv/cknv.dk](https://github.com/cknv/cknv.dk).
* Very basic example at [github.com/Tenzer/beetle-example](https://github.com/Tenzer/beetle-example).

If you have made a site, and want your site listed here, just let me know. Then I will add it.

Name
----

When I started writing beetle, I needed to call it something. I figured that something starting with B would be appropriate because it makes a blog. I picked beetle in honour of the [dung beetle](http://en.wikipedia.org/wiki/Dung_beetle), because at times it felt like I was pushing a large ball of dung in front of me, due to how I wanted it to work. Luckily it turned out good enough for me to actually use it.
