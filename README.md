Beetle
======

Beetle is a simple static site generator, mostly driven by NIH thinking and a desire to have very little dictated from the engine.

So far, it works for me (TM), and I think I can guarantee that you will find it clunky and hard to work with. Especially from the lack of documentation. There is an example of a very basic site at [beetle-example](https://github.com/Tenzer/beetle-example) which can be a help for now.

I should give credit where credit is due, so:

* [Armin Ronacher](http://lucumr.pocoo.org/) for his [rstblog](https://github.com/mitsuhiko/rstblog) that really got me interested in making a static blog engine.
* [Mike Cooper](http://mythmon.com/) for [wok](https://github.com/mythmon/wok), and showing me there is a simple way to make a static blog - I could easily have ended up using wok or a patched version thereof.
* [Jeff Knupp](http://www.jeffknupp.com/) for pointing out that it's ok to make your own static blog engine, since it's so simple.
* [Kasper Jacobsen](http://mackwerk.dk/) for being the first guinea pig and giving much needed feedback.
* [Jeppe Toustrup](http://tenzer.dk) for also giving valuable feedback.

Gaps and missing stuff:
-----------------------
There are some areas that I know I want to work on and improve, these are (in no particular order):

* Tests!
* Page defaults by category.
* ~~Content rendering by file extensions.~~ Support more markup languages.
* Multipages - pages that render into several pages, useful for some tag pages/feeds.
* ~~Better subpage handling.~~
* Pagination of subpages.
* Actual pypi distribution.
* Better development server.

Name
----

Right now, this code is not published at pypi. Currently the name beetle is not taken (as far as I can see on pypi), but that may change. So I may have to rename the project if that happens, who knows?
