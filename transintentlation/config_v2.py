#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the MIT license.
# pylint: disable=useless-super-delegation
"""
Enhancing the 'Config' class done in diffios projet
with some functions and trying to resolve some bugs (such as the
treatment of a banner or some changes not collected)
since the diffios project is not being supported anymore.
"""

from diffios import Config


class Configuring(Config):
    """ Child of diffios.Config class """
    def __init__(self, config, ignore_lines=None):
        super().__init__(config, ignore_lines)

    @staticmethod
    def _banner_case(line):
        """ Unfortunately we have to patch
        the banner case awfully """
        if line.startswith('banner'):
            return line[-1]
        return None

    @staticmethod
    def _valid_line(line):
        line = line.strip()
        return len(line) > 0 and not line.startswith(
            "!")

    def _group_config(self):
        banner = None
        current_group, groups = [], []
        for line in super()._valid_config():
            if banner:
                if not line.startswith(banner):
                    if len(current_group) > 1:
                        current_group[1] = '{}\n{}'.format(current_group[1], line)
                    else:
                        current_group.append(line)
                else:
                    groups.append(current_group)
                    current_group = []
                    banner = None
            elif not line.startswith(' ') and current_group:
                banner = self._banner_case(line)
                groups.append(current_group)
                current_group = [line]
            else:
                current_group.append(line)
        if current_group:
            groups.append(current_group)
        return sorted(groups)
