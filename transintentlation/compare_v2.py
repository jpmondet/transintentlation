#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the MIT license.
"""
Enhancing the 'Compare' class done in diffios projet
with some functions and trying to resolve some bugs (such as the
treatment of a banner or some changes not collected)
since the diffios project is not being supported anymore.
"""

from collections import namedtuple
try:
    from queue import Queue
except ImportError:
    from Queue import Queue

from diffios import Compare, DELIMITER_START
from transintentlation.config_v2 import Configuring


class Comparing(Compare):
    def __init__(self, baseline, comparison, ignore_lines=None):
        self._baseline = baseline
        self._comparison = comparison
        self._ignore_lines = ignore_lines

        if isinstance(self._baseline, Configuring):
            self.baseline = self._baseline
        else:
            self.baseline = Configuring(self._baseline, self._ignore_lines)
        if isinstance(self._comparison, Configuring):
            self.comparison = self._comparison
        else:
            self.comparison = Configuring(self._comparison,
                                          self._ignore_lines)
        if self.baseline and self.comparison:
            self.ignore_lines = self.baseline.ignore_lines

    def _hash_lookup(self, baseline, comparison):
        missing, additional, with_vars = [], [], []
        while not baseline.empty():
            baseline_group = baseline.get()
            baseline_parent = baseline_group[0]
            baseline_children = baseline_group[1:]
            baseline_family = ' '.join(baseline_group)
            if DELIMITER_START in baseline_family:
                with_vars.append(baseline_group)
            else:
                try:
                    comparison_children = comparison.pop(baseline_parent)
                    child_lookup = self._child_lookup(baseline_parent,
                                                      baseline_children,
                                                      comparison_children)
                    if child_lookup.additional:
                        additional.append(child_lookup.additional)
                    if child_lookup.missing:
                        missing.append(child_lookup.missing)
                except KeyError:
                    missing.append(baseline_group)
        return (missing, additional, with_vars)
