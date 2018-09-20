#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the MIT license.
"""
Translate the diffs into actual commands to apply
in an IOS-like environment.
"""
from transintentlation.compare_v2 import Comparing


class Translate():
    """ Translation of missing/additional commands to actual config"""
    def __init__(self, baseline, comparison, ignore_lines=None):
        self.comparing = Comparing(baseline, comparison, ignore_lines)
        self.missing = self.comparing.missing()
        self.additional = self.comparing.additional()
        self.diff = self.comparing.delta()
        self.cmd_to_apply = self.comparing.pprint_missing()
        self.cmd_to_delete = self.comparing.pprint_additional()

    # Utils :
    def _banner_case(self, group, add_del='add'):
        """ Specific handle for banners... """
        if 'add' in add_del:
            # We have to append the special char at the end
            group.append(group[0][-1])
        else:
            # We keep only the parent without the special char
            group = [group[0][:-1]]
        return group

    def _is_also_missing(self, parent):
        """ Verifies if the additional parent of a group of commands
        is also a missing parent """
        for group in self.missing:
            if group[0] == parent:
                return True
        return False

    def _get_missing_equivalent(self, additional_group):
        """ If a group of cmd is missing & additional (a modification of an
        interface IP for example) we return the group of cmd from the missing 
        group list equivalent to the group passed in parameters """
        for group in self.missing:
            if group[0] == additional_group[0]:
                return group

    def _get_additional_equivalent(self, missing_group):
        """ If a group of cmd is missing & additional (a modification of an
        interface IP for example) we return the group of cmd from the
        additional group list equivalent to the group passed in parameters """
        for group in self.additional:
            if group[0] == missing_group[0]:
                return group

    def _print_cmds(self, group, deletion=False):
        """ Simple method to print easily a list of commands """
        negation = ' no ' if deletion else ''

        print(group[0])
        if len(group) > 1:
            for cmd in group[1:]:
                print(negation + cmd)

    # Methods :
    def to_apply(self, and_del=False):
        """ Show the cmds to apply to match the intended config """
        for group in self.missing:
            if 'banner' in group[0]:
                group = self._banner_case(group)
                self._print_cmds(group)
            elif and_del:
                if self._get_additional_equivalent(group):
                    pass
                else:
                    self._print_cmds(group)
            else:
                self._print_cmds(group)

    def to_delete(self, and_add=False):
        """ Show the cmd to delete to match the intended config """
        for group in self.additional:
            if 'banner' in group[0]:
                group = self._banner_case(group, 'del')
            if self._is_also_missing(group[0]):
                self._print_cmds(group, deletion=True)
                if and_add:
                    missing_group = self._get_missing_equivalent(group)[1:]
                    self._print_cmds(missing_group)
            else:
                print('no ' + group[0])

    def apply_all_configs(self):
        """ Combines the configs to add/delete """

        print('!'+'#'*99)
        print('!'+'#'*36+'CLEANINGS AND MODIFICATIONS'+'#'*36)
        print('!'+'#'*99)
        self.to_delete(and_add=True)
        print('!'+'#'*99)
        print('!'+'#'*40+'APPLYING NEW CONFIGS'+'#'*39)
        print('!'+'#'*99)
        self.to_apply(and_del=True)
