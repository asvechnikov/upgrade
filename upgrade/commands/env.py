# -*- coding: utf-8 -*-

#    Copyright 2015 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cliff import command as cmd

from octane.commands import upgrade_env

def clone_env(env_id):
    upgrade_env.upgrade_env(env_id)
    # TODO add work with plugins


class CloneEnvCommand(cmd.Command):
    """ Clone Env and set specific settings for plugins. """

    def get_parser(self, prog_name):
        parser = super(CloneEnvCommand, self).get_parser(prog_name)
        parser.add_argument(
            "env",
            type=int,
            metavar='ENV_ID',
            help='ID of environment to be upgraded')
        return parser

    def take_action(self, parsed_args):
        clone_env(parsed_args.env)
