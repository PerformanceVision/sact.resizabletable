.. -*- rst -*-
.. vim:ft=rst

OVERVIEW
========

A Reportlab/Platypus table that can resize itself automatically.

The Reportlab PDF generation library and its high level wrapper Platypus are
all manners of fantastic. One area where they fall short, however, is tables,
and in particular, wide tables that don't fit the page.

This module implements a drop in replacement for the default Platypus table,
that automatically resizes itself and its textual contents to try and fit the
page it has been placed in.


USAGE
=====

Anywhere you would use the Table class from Reportlab/Platypus, use the
ResizableTable class instead:

>>> from sact.resizabletable import ResizableTable
>>> table = ResizableTable(your_data)

The API is identical to that of the Table class as described here:
http://www.reportlab.com/apis/reportlab/dev/platypus.html#module-reportlab.platypus.tables

Mind that ResizableTable does not work properly with images or complex
flowables in its cells.
