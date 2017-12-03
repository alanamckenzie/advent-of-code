"""--- Day 10: Balance Bots ---

You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips,
and once it does, it gives each one to a different bot or puts it in a marked "output" bin.
Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number;
the bots must use some logic to decide what to do with each chip.
You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot;
the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2

    Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
    Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
    Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
    Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.

In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip,
and output bin 2 contains a value-3 microchip. In this configuration,
bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing
value-61 microchips with value-17 microchips?

What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?
"""

import re
from collections import defaultdict

import utils


class ChipRecipient:
    def __init__(self, number=None):
        self._chips = []
        self.number = number

    @property
    def num_chips(self):
        return len(self._chips)

    @property
    def chips(self):
        return list(self._chips)

    def add(self, value):
        raise NotImplementedError


class Output(ChipRecipient):
    def add(self, value):
        self._chips.append(value)


class Bot(ChipRecipient):

    chip_alert = [17, 61]

    def __init__(self, number=None, low_recipient=None, high_recipient=None):

        super().__init__(number)
        self._low_recipient = low_recipient
        self._high_recipient = high_recipient

    def update_recipients(self, low_recipient, high_recipient):
        self._low_recipient = low_recipient
        self._high_recipient = high_recipient

        if self.num_chips == 2 and self._low_recipient and self._high_recipient:
            self._distribute_chips()

    def add(self, value):
        if self.num_chips == 2:
            raise Exception(f'BOT {self.number} ALREADY HAS 2 MICROCHIPS')

        self._chips.append(value)

        if self.num_chips == 2 and self._low_recipient and self._high_recipient:
            self._distribute_chips()

    def _distribute_chips(self):
        chips = sorted(self._chips)

        # if chips == self.chip_alert:
        #    print(f'CHIPS {self.chip_alert} COMPARED BY BOT {self.number}')

        self._low_recipient.add(chips[0])
        self._high_recipient.add(chips[1])

        self._chips = []


def parse_instruction(instruction):
    re_value = r'(?P<type>value) (?P<value_num>\d+) goes to (?P<recipient_type>\w+) (?P<recipient_num>\d+)'
    re_bot = r'(?P<type>bot) (?P<value_num>\d+) gives low to (?P<low_recipient_type>\w+) (?P<low_recipient_num>\d+)' \
             r' and high to (?P<high_recipient_type>\w+) (?P<high_recipient_num>\d+)'

    m_value = re.match(re_value, instruction)
    if m_value:
        return m_value.groupdict()

    m_bot = re.match(re_bot, instruction)
    if m_bot:
        return m_bot.groupdict()

    raise Exception(f'Instruction did not match bot or value: {instruction}')


def run(instructions):

    recipients = {
        'bot': defaultdict(Bot),
        'output': defaultdict(Output)
    }

    for instruction in instructions:
        task = parse_instruction(instruction)
        if task['type'] == 'value':

            recipient_num = int(task['recipient_num'])
            value_num = int(task['value_num'])

            recipients[task['recipient_type']][recipient_num].number = recipient_num
            recipients[task['recipient_type']][recipient_num].add(value_num)

        elif task['type'] == 'bot':
            l_recipient_num = int(task['low_recipient_num'])
            h_recipient_num = int(task['high_recipient_num'])
            value_num = int(task['value_num'])

            recipients['bot'][value_num].number = value_num
            recipients['bot'][value_num].update_recipients(
                low_recipient=recipients[task['low_recipient_type']][l_recipient_num],
                high_recipient=recipients[task['high_recipient_type']][h_recipient_num]
            )

    results = [recipients['output'][i].chips[0] for i in range(3)]
    print(results)
    print(results[0]*results[1]*results[2])

if __name__ == '__main__':

    filename = 'dec10_input.txt'
    instructions = utils.read_file(filename)

    run(instructions)