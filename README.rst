.. -*- rst -*-
.. vim:ft=rst

Overview
========

A Reportlab/Platypus table that can resize itself automatically.

The Reportlab PDF generation library and its high level wrapper Platypus are
all manners of fantastic. One area where they fall short, however, is tables,
and in particular, wide tables that don't fit the page.

This module implements a drop in replacement for the default Platypus table,
that automatically resizes itself and its textual contents to try and fit the
page it has been placed in.
