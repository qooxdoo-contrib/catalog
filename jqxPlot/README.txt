==== jqxPlot ====

A demo of using the jqPlot charting library with qooxdoo.

This is an example how the jQuery (http://jquery.com) based plotting
library jqPlot (http://www.jqplot.com) can be used with qooxdoo.

This is NOT a proper qooxdoo class with a nice qooxdoo style
interface. Feel free to improve until I get around to it.


=== Notes ===

- You need to include the jQuery and jqPlot libraries (for example in
  your source/index.html file).

- The jqPlot libraries are actually split into several modules. You
  only need to include those actually used in your code.

- For support of Internet Explorer you also need ExplorerCanvas
  (http://excanvas.sourceforge.net). Please note: Since this component is 
  provided under the Apache License, this is not compatible to LGPL. 

- The required libraries for this demo are included in this package in
  source/plot/. 

  You might want to upgrade to the most current versions.

- I implemented a clear() method for jqPlot that is currently not
  included in the original jqPlot libraries. See the patch file
  source/plot/jqplot/jqplot.core.js.patch

  This method is currently not used in the demo application.

- Please refer to the documentation of jqPlot for details on the
  various graph types, options, etc.

- So far I did not find any incompatibilities with the qooxdoo
  libraries. However, before reporting problems with qooxdoo to the
  mailing list or filing bugs, please test your code WITHOUT the
  jQuery/ExCanvas/jqPlot libraries.


=== Licensing ===

- The jqxPlot package includes copies of ExplorerCanvas, jQuery and jqPlot. 
  Please refer to the licensing instructions of these libraries if you
  intend to use them in your applications.

- The jqxPlot package as a whole is distributed under the EPL license, due
  to the incompatibility of the Apache license covering ExplorerCanvas and
  and the LGPL license.

- The code in Application.js is distributed under LGPL and EPL, as it can be
  used without ExplorerCanvas (at least with some browsers).


Cheers,
Fritz
