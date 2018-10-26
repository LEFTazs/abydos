# -*- coding: utf-8 -*-

# Copyright 2018 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.phonetic.test_phonetic_nrl.

This module contains unit tests for abydos.phonetic.nrl
"""

from __future__ import unicode_literals

import unittest

from abydos.phonetic.nrl import nrl


class NRLTestCases(unittest.TestCase):
    """Test Naval Research Laboratory phonetic encoding functions.

    test cases for abydos.phonetic.nrl.nrl
    """

    def test_nrl(self):
        """Test abydos.phonetic.nrl.nrl."""
        # Base case
        self.assertEqual(nrl(''), '')

        # common English words
        self.assertEqual(nrl('the'), 'DHAX')
        self.assertEqual(nrl('of'), 'AXv')
        self.assertEqual(nrl('and'), 'AEnd')
        self.assertEqual(nrl('a'), 'AX')
        self.assertEqual(nrl('to'), 'tUW')
        self.assertEqual(nrl('in'), 'IHn')
        self.assertEqual(nrl('is'), 'IHz')
        self.assertEqual(nrl('you'), 'yUW')
        self.assertEqual(nrl('that'), 'DHAEt')
        self.assertEqual(nrl('it'), 'IHt')
        self.assertEqual(nrl('he'), 'hIY')
        self.assertEqual(nrl('was'), 'wAAz')
        self.assertEqual(nrl('for'), 'fAOr')
        self.assertEqual(nrl('on'), 'AAn')
        self.assertEqual(nrl('are'), 'AAr')
        self.assertEqual(nrl('as'), 'AEz')
        self.assertEqual(nrl('with'), 'wIHTH')
        self.assertEqual(nrl('his'), 'hIHz')
        self.assertEqual(nrl('they'), 'DHEY')
        self.assertEqual(nrl('I'), 'AY')
        self.assertEqual(nrl('at'), 'AEt')
        self.assertEqual(nrl('be'), 'bIY')
        self.assertEqual(nrl('this'), 'DHIHs')
        self.assertEqual(nrl('have'), 'hAEv')
        self.assertEqual(nrl('from'), 'frAAm')
        self.assertEqual(nrl('or'), 'AOr')
        self.assertEqual(nrl('one'), 'wAHn')
        self.assertEqual(nrl('had'), 'hAEd')
        self.assertEqual(nrl('by'), 'bAY')
        self.assertEqual(nrl('word'), 'wERd')
        self.assertEqual(nrl('but'), 'bAHt')
        self.assertEqual(nrl('not'), 'nAAt')
        self.assertEqual(nrl('what'), 'WHAAt')
        self.assertEqual(nrl('all'), 'AOl')
        self.assertEqual(nrl('were'), 'wER')
        self.assertEqual(nrl('we'), 'wIY')
        self.assertEqual(nrl('when'), 'WHEHn')
        self.assertEqual(nrl('your'), 'yUWr')
        self.assertEqual(nrl('can'), 'kAEn')
        self.assertEqual(nrl('said'), 'sEHd')
        self.assertEqual(nrl('there'), 'DHEHr')
        self.assertEqual(nrl('use'), 'yUWz')
        self.assertEqual(nrl('an'), 'AEn')
        self.assertEqual(nrl('each'), 'IYCH')
        self.assertEqual(nrl('which'), 'WHIHCH')
        self.assertEqual(nrl('she'), 'SHIY')
        self.assertEqual(nrl('do'), 'dUW')
        self.assertEqual(nrl('how'), 'hAW')
        self.assertEqual(nrl('their'), 'DHEHr')
        self.assertEqual(nrl('if'), 'IHf')
        self.assertEqual(nrl('will'), 'wIHl')
        self.assertEqual(nrl('up'), 'AHp')
        self.assertEqual(nrl('other'), 'AHDHER')
        self.assertEqual(nrl('about'), 'AEbAWt')
        self.assertEqual(nrl('out'), 'AWt')
        self.assertEqual(nrl('many'), 'mEHnIY')
        self.assertEqual(nrl('then'), 'DHEHn')
        self.assertEqual(nrl('them'), 'DHEHm')
        self.assertEqual(nrl('these'), 'DHIYz')
        self.assertEqual(nrl('so'), 'sOW')
        self.assertEqual(nrl('some'), 'sAHm')
        self.assertEqual(nrl('her'), 'hER')
        self.assertEqual(nrl('would'), 'wUHd')
        self.assertEqual(nrl('make'), 'mEYk')
        self.assertEqual(nrl('like'), 'lAYk')
        self.assertEqual(nrl('him'), 'hIHm')
        self.assertEqual(nrl('into'), 'IHntUW')
        self.assertEqual(nrl('time'), 'tAYm')
        self.assertEqual(nrl('has'), 'hAEz')
        self.assertEqual(nrl('look'), 'lUHk')
        self.assertEqual(nrl('two'), 'tUW')
        self.assertEqual(nrl('more'), 'mAOr')
        self.assertEqual(nrl('write'), 'rAYt')
        self.assertEqual(nrl('go'), 'gOW')
        self.assertEqual(nrl('see'), 'sIY')
        self.assertEqual(nrl('number'), 'nAHmbER')
        self.assertEqual(nrl('no'), 'nOW')
        self.assertEqual(nrl('way'), 'wEY')
        self.assertEqual(nrl('could'), 'kUHd')
        self.assertEqual(nrl('people'), 'pIYpl')
        self.assertEqual(nrl('my'), 'mAY')
        self.assertEqual(nrl('than'), 'DHAEn')
        self.assertEqual(nrl('first'), 'fERst')
        self.assertEqual(nrl('water'), 'wAAtER')
        self.assertEqual(nrl('been'), 'bIYn')
        self.assertEqual(nrl('call'), 'kAOl')
        self.assertEqual(nrl('who'), 'hUW')
        self.assertEqual(nrl('oil'), 'OYl')
        self.assertEqual(nrl('its'), 'IHtz')
        self.assertEqual(nrl('now'), 'nAW')
        self.assertEqual(nrl('find'), 'fAYnd')
        self.assertEqual(nrl('long'), 'lAONG')
        self.assertEqual(nrl('down'), 'dAWn')
        self.assertEqual(nrl('day'), 'dEY')
        self.assertEqual(nrl('did'), 'dIHd')
        self.assertEqual(nrl('get'), 'gEHt')
        self.assertEqual(nrl('come'), 'kAHm')
        self.assertEqual(nrl('made'), 'mEYd')
        self.assertEqual(nrl('may'), 'mEY')
        self.assertEqual(nrl('part'), 'pAArt')
        self.assertEqual(nrl('supply'), 'sAHpplIH')
        self.assertEqual(nrl('corner'), 'kAOrnER')
        self.assertEqual(nrl('electric'), 'IYlEHktrIHk')
        self.assertEqual(nrl('insects'), 'IHnsEHktz')
        self.assertEqual(nrl('crops'), 'krAAps')
        self.assertEqual(nrl('tone'), 'tOWn')
        self.assertEqual(nrl('hit'), 'hIHt')
        self.assertEqual(nrl('sand'), 'sAEnd')
        self.assertEqual(nrl('doctor'), 'dAAktER')
        self.assertEqual(nrl('provide'), 'prAHvAYd')
        self.assertEqual(nrl('thus'), 'DHAHs')
        self.assertEqual(nrl('won\'t'), 'wOWnt')
        self.assertEqual(nrl('cook'), 'kUHk')
        self.assertEqual(nrl('bones'), 'bOWnz')
        self.assertEqual(nrl('tail'), 'tEYl')
        self.assertEqual(nrl('board'), 'bOWrd')
        self.assertEqual(nrl('modern'), 'mOWdERn')
        self.assertEqual(nrl('compound'), 'kAAmpAWnd')
        self.assertEqual(nrl('mine'), 'mAYn')
        self.assertEqual(nrl('wasn\'t'), 'wAAzAXnt')
        self.assertEqual(nrl('fit'), 'fIHt')
        self.assertEqual(nrl('addition'), 'AEddIHSHAXn')
        self.assertEqual(nrl('belong'), 'bIHlAONG')
        self.assertEqual(nrl('safe'), 'sEYf')
        self.assertEqual(nrl('soldiers'), 'sOWldIYERs')
        self.assertEqual(nrl('guess'), 'gEHs')
        self.assertEqual(nrl('silent'), 'sAYlEHnt')
        self.assertEqual(nrl('trade'), 'trEYd')
        self.assertEqual(nrl('rather'), 'rAEDHER')
        self.assertEqual(nrl('compare'), 'kAAmpEHr')
        self.assertEqual(nrl('crowd'), 'krOWd')
        self.assertEqual(nrl('poem'), 'pOWEHm')
        self.assertEqual(nrl('enjoy'), 'EHnjOY')
        self.assertEqual(nrl('elements'), 'IYlIYmEHntz')
        self.assertEqual(nrl('indicate'), 'IHndIHkEYt')
        self.assertEqual(nrl('except'), 'EHkssEHpt')
        self.assertEqual(nrl('expect'), 'EHkspEHkt')
        self.assertEqual(nrl('flat'), 'flAEt')
        self.assertEqual(nrl('seven'), 'sIYvEHn')
        self.assertEqual(nrl('interest'), 'IHntIYrEHst')
        self.assertEqual(nrl('sense'), 'sEHns')
        self.assertEqual(nrl('string'), 'strIHNG')
        self.assertEqual(nrl('blow'), 'blOW')
        self.assertEqual(nrl('famous'), 'fAEmAXs')
        self.assertEqual(nrl('value'), 'vAElUW')
        self.assertEqual(nrl('wings'), 'wIHNGz')
        self.assertEqual(nrl('movement'), 'mUWvIYmEHnt')
        self.assertEqual(nrl('pole'), 'pOWl')
        self.assertEqual(nrl('exciting'), 'EHkssAYtIHNG')
        self.assertEqual(nrl('branches'), 'brAEnCHIHz')
        self.assertEqual(nrl('thick'), 'THIHk')
        self.assertEqual(nrl('blood'), 'blUHd')
        self.assertEqual(nrl('lie'), 'lAY')
        self.assertEqual(nrl('spot'), 'spAAt')
        self.assertEqual(nrl('bell'), 'bEHl')
        self.assertEqual(nrl('fun'), 'fAHn')
        self.assertEqual(nrl('loud'), 'lAWd')
        self.assertEqual(nrl('consider'), 'kAAnsAYdER')
        self.assertEqual(nrl('suggested'), 'sAHgjEHstIHd')
        self.assertEqual(nrl('thin'), 'THIHn')
        self.assertEqual(nrl('position'), 'pAAzIHSHAXn')
        self.assertEqual(nrl('entered'), 'EHntIYrd')
        self.assertEqual(nrl('fruit'), 'frUWIHt')
        self.assertEqual(nrl('tied'), 'tAYd')
        self.assertEqual(nrl('rich'), 'rIHCH')
        self.assertEqual(nrl('dollars'), 'dAAlAArs')
        self.assertEqual(nrl('send'), 'sEHnd')
        self.assertEqual(nrl('sight'), 'sAYt')
        self.assertEqual(nrl('chief'), 'CHAYEHf')
        self.assertEqual(nrl('Japanese'), 'jAEpAEnIYz')
        self.assertEqual(nrl('stream'), 'strIYm')
        self.assertEqual(nrl('plants'), 'plAEntz')
        self.assertEqual(nrl('rhythm'), 'rIHTHm')
        self.assertEqual(nrl('eight'), 'EYt')
        self.assertEqual(nrl('science'), 'sAYEHns')
        self.assertEqual(nrl('major'), 'mAEjER')
        self.assertEqual(nrl('observe'), 'AAbsERv')
        self.assertEqual(nrl('tube'), 'tUWb')
        self.assertEqual(nrl('necessary'), 'nIYsEHsAArIH')
        self.assertEqual(nrl('weight'), 'wEYt')
        self.assertEqual(nrl('meat'), 'mIYt')
        self.assertEqual(nrl('lifted'), 'lIHftIHd')
        self.assertEqual(nrl('process'), 'prOWsEHs')
        self.assertEqual(nrl('army'), 'AArmIY')
        self.assertEqual(nrl('hat'), 'hAEt')
        self.assertEqual(nrl('property'), 'prOWpERtIH')
        self.assertEqual(nrl('particular'), 'pAArtIHkyUWlER')
        self.assertEqual(nrl('swim'), 'swIHm')
        self.assertEqual(nrl('terms'), 'tERmz')
        self.assertEqual(nrl('current'), 'kERrEHnt')
        self.assertEqual(nrl('park'), 'pAArk')
        self.assertEqual(nrl('sell'), 'sEHl')
        self.assertEqual(nrl('shoulder'), 'SHUHdER')
        self.assertEqual(nrl('industry'), 'IHndAHstrIH')
        self.assertEqual(nrl('wash'), 'wAASH')
        self.assertEqual(nrl('block'), 'blAAk')
        self.assertEqual(nrl('spread'), 'sprEHd')
        self.assertEqual(nrl('cattle'), 'kAEttl')
        self.assertEqual(nrl('wife'), 'wAYf')
        self.assertEqual(nrl('sharp'), 'SHAArp')
        self.assertEqual(nrl('company'), 'kAAmpAEnIH')
        self.assertEqual(nrl('radio'), 'rEYdIHOW')
        self.assertEqual(nrl('we\'ll'), 'wEHl')
        self.assertEqual(nrl('action'), 'AEkSHAXn')
        self.assertEqual(nrl('capital'), 'kAEpIHtAXl')
        self.assertEqual(nrl('factories'), 'fAEktAOrIYs')
        self.assertEqual(nrl('settled'), 'sEHttld')
        self.assertEqual(nrl('yellow'), 'yEHlOW')
        self.assertEqual(nrl('isn\'t'), 'IHzAXnt')
        self.assertEqual(nrl('southern'), 'sAWDHERn')
        self.assertEqual(nrl('truck'), 'trAHk')
        self.assertEqual(nrl('train'), 'trEYn')
        self.assertEqual(nrl('printed'), 'prIHntIHd')
        self.assertEqual(nrl('wouldn\'t'), 'wUHdnt')
        self.assertEqual(nrl('ahead'), 'EYhEHd')
        self.assertEqual(nrl('chance'), 'CHAEns')
        self.assertEqual(nrl('born'), 'bAOrn')
        self.assertEqual(nrl('level'), 'lIYvEHl')
        self.assertEqual(nrl('triangle'), 'trIHAENGgAXl')
        self.assertEqual(nrl('molecules'), 'mOWlEHkyUWlz')
        self.assertEqual(nrl('France'), 'frAEns')
        self.assertEqual(nrl('repeated'), 'rIYpIYtIHd')
        self.assertEqual(nrl('column'), 'kAAlAHmn')
        self.assertEqual(nrl('western'), 'wEHstERn')
        self.assertEqual(nrl('church'), 'CHERCH')
        self.assertEqual(nrl('sister'), 'sIHstER')
        self.assertEqual(nrl('oxygen'), 'AAksIHjEHn')
        self.assertEqual(nrl('plural'), 'plUHrAXl')
        self.assertEqual(nrl('various'), 'vEHrIHAXs')
        self.assertEqual(nrl('agreed'), 'AEgrIYd')
        self.assertEqual(nrl('opposite'), 'AAppAAzAYt')
        self.assertEqual(nrl('wrong'), 'rAONG')
        self.assertEqual(nrl('chart'), 'CHAArt')
        self.assertEqual(nrl('prepared'), 'prEHpEHrd')
        self.assertEqual(nrl('pretty'), 'prEHttIH')
        self.assertEqual(nrl('solution'), 'sAAlUWSHAXn')
        self.assertEqual(nrl('fresh'), 'frEHSH')
        self.assertEqual(nrl('shop'), 'SHAAp')
        self.assertEqual(nrl('suffix'), 'sAHffIHks')
        self.assertEqual(nrl('especially'), 'EHspEHSHAXlIY')
        self.assertEqual(nrl('shoes'), 'SHOWz')
        self.assertEqual(nrl('actually'), 'AEkCHUWAXlIY')
        self.assertEqual(nrl('nose'), 'nOWz')
        self.assertEqual(nrl('afraid'), 'AEfrEYd')
        self.assertEqual(nrl('dead'), 'dEHd')
        self.assertEqual(nrl('sugar'), 'sUWgER')
        self.assertEqual(nrl('adjective'), 'AEdjEHktAYv')
        self.assertEqual(nrl('fig'), 'fIHg')
        self.assertEqual(nrl('office'), 'AOffIHs')
        self.assertEqual(nrl('huge'), 'hyUWj')
        self.assertEqual(nrl('gun'), 'gAHn')
        self.assertEqual(nrl('similar'), 'sIHmIHlER')
        self.assertEqual(nrl('death'), 'dIYTH')
        self.assertEqual(nrl('score'), 'skAOr')
        self.assertEqual(nrl('forward'), 'fAOrwAOrd')
        self.assertEqual(nrl('stretched'), 'strEHtCHd')
        self.assertEqual(nrl('experience'), 'EHkspIYrIYEHns')
        self.assertEqual(nrl('rose'), 'rOWz')
        self.assertEqual(nrl('allow'), 'AOlOW')
        self.assertEqual(nrl('fear'), 'fIYr')
        self.assertEqual(nrl('workers'), 'wERkERs')
        self.assertEqual(nrl('Washington'), 'wAASHIHNGtAXn')
        self.assertEqual(nrl('Greek'), 'grIYk')
        self.assertEqual(nrl('women'), 'wOWmEHn')
        self.assertEqual(nrl('brought'), 'brAOt')
        self.assertEqual(nrl('led'), 'lEHd')
        self.assertEqual(nrl('march'), 'mAArCH')
        self.assertEqual(nrl('northern'), 'nAOrDHERn')
        self.assertEqual(nrl('create'), 'krIYt')
        self.assertEqual(nrl('British'), 'brAYtIHSH')
        self.assertEqual(nrl('difficult'), 'dIHffIHkAHlt')
        self.assertEqual(nrl('match'), 'mAEtCH')
        self.assertEqual(nrl('win'), 'wIHn')
        self.assertEqual(nrl('doesn\'t'), 'dAHznt')
        self.assertEqual(nrl('steel'), 'stIYl')
        self.assertEqual(nrl('total'), 'tAAtAXl')
        self.assertEqual(nrl('deal'), 'dIYl')
        self.assertEqual(nrl('determine'), 'dIHtERmAYn')
        self.assertEqual(nrl('evening'), 'IYvIYnIHNG')
        self.assertEqual(nrl('nor'), 'nAOr')
        self.assertEqual(nrl('rope'), 'rOWp')
        self.assertEqual(nrl('cotton'), 'kAAttAXn')
        self.assertEqual(nrl('apple'), 'AEppAXl')
        self.assertEqual(nrl('details'), 'dIHtEYlz')
        self.assertEqual(nrl('entire'), 'EHntAYr')
        self.assertEqual(nrl('corn'), 'kAOrn')
        self.assertEqual(nrl('substances'), 'sAHbstAEnsIHz')
        self.assertEqual(nrl('smell'), 'smEHl')
        self.assertEqual(nrl('tools'), 'tUWlz')
        self.assertEqual(nrl('conditions'), 'kAAndIHSHAXnz')
        self.assertEqual(nrl('cows'), 'kOWz')
        self.assertEqual(nrl('track'), 'trAEk')
        self.assertEqual(nrl('arrived'), 'AXrIHvd')
        self.assertEqual(nrl('located'), 'lOWkEYtIHd')
        self.assertEqual(nrl('sir'), 'sER')
        self.assertEqual(nrl('seat'), 'sIYt')
        self.assertEqual(nrl('division'), 'dIHvIHZHAXn')
        self.assertEqual(nrl('effect'), 'EHffEHkt')
        self.assertEqual(nrl('underline'), 'AHndERlAYn')
        self.assertEqual(nrl('view'), 'vyUW')

        # non-English words (with letters not used in English)
        self.assertEqual(nrl('garçon'), 'gAArÇAAn')
        self.assertEqual(nrl('ðæt'), 'ÐÆt')
        self.assertEqual(nrl('wünschen'), 'wÜnsCHEHn')
        self.assertEqual(nrl('øl'), 'Øl')


if __name__ == '__main__':
    unittest.main()
