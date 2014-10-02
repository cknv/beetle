Beetle
======

Installation
------------

```shell
pip install beetle
```

Plugins
-------
Just installing Beetle will only get you so far though, there is no support of any markup language, nor is there a local server so you can see what the site will look like. It is basic, and intended so.

However...

Beetle is made to be extensible, this means that instead of being forced to use a certain markup language, you can instead find (or write) a plugin that enabled you to use your favorite markup language, install it, tell Beetle about it and off you go!

About
-----
Beetle is a simple static site generator, mostly driven by NIH thinking and a desire to have very little dictated from the engine.

So far, it works for me (TM), and I think I can guarantee that you will find it clunky and hard to work with. Especially from the lack of documentation.

I should give credit where credit is due, so:

* [Armin Ronacher](http://lucumr.pocoo.org/) for his [rstblog](https://github.com/mitsuhiko/rstblog) that really got me interested in making a static blog engine.
* [Mike Cooper](http://mythmon.com/) for [wok](https://github.com/mythmon/wok), and showing me there is a simple way to make a static blog - I could easily have ended up using wok or a patched version thereof.
* [Jeff Knupp](http://www.jeffknupp.com/) for pointing out that it's ok to make your own static blog engine, since it's so simple.
* [Kasper Jacobsen](http://mackwerk.dk/) for being the first guinea pig and giving much needed feedback.
* [Jeppe Toustrup](http://tenzer.dk) for also giving valuable feedback.

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

Name
----

When I started writing beetle, I needed to call it something. I figured that something starting with B would be appropriate because it makes a blog. I picked beetle in honour of the [dung beetle](http://en.wikipedia.org/wiki/Dung_beetle), because at times it felt like I was pushing a large ball of dung in front of me, due to how I wanted it to work. Luckily it turned out good enough for me to actually use it.
