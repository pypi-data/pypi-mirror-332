"""sopel-itcrowd

A Sopel plugin for IT Crowd jokes.
"""
from __future__ import annotations

import time

from sopel import plugin


PLUGIN_PREFIX = '[IT Crowd] '


@plugin.command('itnes', 'newnumber')
@plugin.output_prefix(PLUGIN_PREFIX)
@plugin.rate_channel(
    60 * 10,
    "This command can only be used once per 10 minutes in a given channel.",
)
def new_emergency_services(bot, trigger):
    numbers = ['0118', '999', '881 99', '9 119 725']
    for number in numbers:
        bot.say(number)
        time.sleep(1)
    time.sleep(2)
    bot.say('3')
