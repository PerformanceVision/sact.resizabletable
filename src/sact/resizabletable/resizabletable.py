## -*- coding: utf-8 -*-

from reportlab.platypus import Table

import copy


class ResizableTable(Table):
    """Auto-resizing replacement for the default Platypus table.

    This class is meant to be used as a drop-in replacement for the default
    Platypus Table. When the Reportlab engine computes the page layout,
    the ResizableTable determines if it would fit inside the requested width,
    and if not, scales down the padding and font size of its cells in
    proportion.

    It doesn't work with cell contents other than text.

    """

    def __init__(self, *args, **kwargs):

        self.init_args = args, kwargs
        Table.__init__(self, *args, **kwargs)

        self._cached_cell_styles = None


    def wrap(self, availWidth, availHeight):
        """Reimplementation of Table.wrap().

        It works by mimicking the width calculation on a dummy Table, and if
        the result warrant it, by scaling down the text and padding of each
        cell.

        """

        ## Create a standard Table with the same contents and style as ours.
        ## Use it to determine if it fits inside our available width.

        args, kwargs = self.init_args
        std_table = Table(*args, **kwargs)
        std_table._calc(availWidth, availHeight)

        ## Cache the cell metrics. The Platypus layout algorithm may call this
        ## any number of times, and we only want to compute new metrics based
        ## on the original cell metrics.

        if not self._cached_cell_styles:
            self._cached_cell_styles = copy.deepcopy(self._cellStyles)

        if availWidth < std_table._width and len(self._cellStyles) > 0:

            ## If a standard table wouldn't fit, attempt to resize the current
            ## table's contents.

            ratio = availWidth / float(std_table._width)

            for current_line, cached_line in zip(self._cellStyles, self._cached_cell_styles):
                for current_cell, cached_cell in zip(current_line, cached_line):
                    current_cell.fontsize      = ratio * cached_cell.fontsize
                    current_cell.leftPadding   = ratio * cached_cell.leftPadding
                    current_cell.rightPadding  = ratio * cached_cell.rightPadding
                    current_cell.topPadding    = ratio * cached_cell.topPadding
                    current_cell.bottomPadding = ratio * cached_cell.bottomPadding

        return Table.wrap(self, availWidth, availHeight)
