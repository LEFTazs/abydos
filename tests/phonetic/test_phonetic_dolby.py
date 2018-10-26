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

"""abydos.tests.phonetic.test_phonetic_dolby.

This module contains unit tests for abydos.phonetic._dolby
"""

from __future__ import unicode_literals

import unittest

from abydos.phonetic import dolby


class DolbyTestCases(unittest.TestCase):
    """Test Dolby functions.

    test cases for abydos.phonetic._dolby.dolby
    """

    def test_dolby(self):
        """Test abydos.phonetic._dolby.dolby."""
        # Base case
        self.assertEqual(dolby(''), '')

        # Tests from Dolby (1970) pp. 264--274
        # https://ejournals.bc.edu/ojs/index.php/ital/article/download/5259/4734
        # Checked against Cunningham, et al. (1969) pp. 127--136, as needed.
        # https://files.eric.ed.gov/fulltext/ED029679.pdf
        test_cases = (
            ('*BL', 'Abel', 'Abele', 'Abell', 'Able'),
            ('*BRMS', 'Abrahams', 'Abrams'),
            ('*BRMSN', 'Abrahamson', 'Abramson'),
            ('*D', 'Eddy', 'Eddie'),
            ('*DMNS', 'Edmonds', 'Edmunds'),
            ('*DMNSN', 'Edmondson', 'Edmundson'),
            ('*DMS', 'Adams', 'Addems'),
            ('*GN', 'Eagen', 'Egan', 'Eggen'),
            ('*GR', '!Jaeger', 'Yaeger', 'Yeager'),
            ('*KN', 'Aiken', 'Aikin', 'Aitken'),
            ('*KNS', 'Adkins', 'Akins'),
            ('*KR', 'Acker', 'Aker'),
            ('*KR', 'Eckard', 'Eckardt', 'Eckart', 'Eckert', 'Eckhardt'),
            ('*KS', 'Oakes', 'Oaks', 'Ochs'),
            ('*LBRD', 'Albright', 'Allbright'),
            ('*LD', 'Elliot', 'Elliott'),
            ('*LN', 'Allan', 'Allen', 'Allyn'),
            ('*LSN', 'Ohlsen', 'Olesen', 'Olsen', 'Olson', 'Olsson'),
            ('*LVR', 'Oliveira', 'Olivera', 'Olivero'),
            ('*MS', 'Ames', 'Eames'),
            ('*NGL', 'Engel', 'Engle', 'Ingle'),
            ('*NL', 'O\'Neal', 'O\'Neil', 'O\'Neill'),
            ('*NRS', 'Andrews', 'Andrus'),
            ('*NRSN', 'Andersen', 'Anderson', 'Andreasen'),
            ('*NS', 'Ennis', 'Enos'),
            # Corrected: 'Enrichsen' below was an error
            # (It's correct in Cunningham, et al. 1969.)
            (
                '*RKSN',
                'Erichsen',
                'Erickson',
                'Ericson',
                'Ericsson',
                'Eriksen',
            ),
            ('*RL', 'Earley', 'Early'),
            ('*RN', 'Erwin', 'Irwin'),
            (
                '*RNS',
                'Aarons',
                'Ahrends',
                'Ahrens',
                'Arens',
                'Arentz',
                'Arons',
            ),
            ('*RS', 'Ayers', 'Ayres'),
            ('*RVN', 'Ervin', 'Ervine', 'Irvin', 'Irvine'),
            ('*RVNG', 'Erving', 'Irving'),
            ('*SBRN', 'Osborn', 'Osborne', 'Osbourne', 'Osburn'),
            ('B*D', 'Beatie', 'Beattie', 'Beatty', 'Beaty', 'Beedie'),
            ('B*DS', 'Betts', 'Betz'),
            ('B*KMN', 'Bachman', 'Bachmann', 'Backman'),
            ('B*L', 'Bailey', 'Baillie', 'Bailly', 'Baily', 'Bayley'),
            ('B*L', 'Beal', 'Beale', 'Beall', 'Biehl'),
            ('B*L', 'Belew', 'Ballou', 'Bellew'),
            ('B*L', 'Buhl', 'Buell'),
            ('B*L', 'Belle', 'Bell'),
            # Corrected: No reason for D to disappear
            ('B*LDN', 'Bolton', 'Boulton'),
            ('B*M', 'Baum', 'Bohm', 'Bohme'),
            ('B*MN', 'Bauman', 'Bowman'),
            ('B*N', 'Bain', 'Bane', 'Bayne'),
            ('B*ND', 'Bennet', 'Bennett'),
            (
                'B*R',
                'Baer',
                'Bahr',
                'Baier',
                'Bair',
                'Bare',
                'Bear',
                'Beare',
                'Behr',
                'Beier',
                'Bier',
                '!Bryer',
            ),
            ('B*R', 'Barry', 'Beare', 'Beery', 'Berry'),
            ('B*R', 'Bauer', 'Baur', 'Bower'),
            ('B*R', 'Bird', 'Burd', 'Byrd'),
            ('B*RBR', 'Barbour', 'Barber'),
            ('B*RG', 'Berg', 'Bergh', 'Burge'),
            ('B*RGR', 'Berger', 'Burger'),
            ('B*RK', 'Boerke', 'Birk', 'Bourke', 'Burk', 'Burke'),
            ('B*RN', 'Burn', 'Byrne'),
            ('B*RNR', 'Bernard', 'Bernhard', 'Bernhardt', 'Bernhart'),
            ('B*RNS', 'Berns', 'Birns', 'Burns', 'Byrns', 'Byrnes'),
            ('B*RNSN', 'Bernstein', 'Bornstein'),
            # Corrected: 'RCH' -> 'RH' in rule 2
            ('B*RS', 'Bertsch', '!Birch', '!Burch'),
            ('BL*KBRN', 'Blackburn', '!Blagburn'),
            ('BL*M', 'Blom', 'Bloom', 'Bluhm', 'Blum', 'Blume'),
            ('BR*D', 'Brode', 'Brodie', 'Brody'),
            ('BR*N', 'Braun', 'Brown', 'Browne'),
            ('BR*N', 'Brand', 'Brandt', 'Brant'),
            # Corrected: 'Diezt' -> 'D*SD', so reversed zt -> tz
            # (Correct in Cunningham, et al. 1969.)
            ('D*DS', 'Dietz', 'Ditz'),
            ('D*F', 'Duffie', 'Duffy'),
            ('D*GN', 'Dougan', 'Dugan', 'Duggan'),
            ('D*K', 'Dickey', 'Dicke'),
            ('D*KNSN', 'Dickenson', '!Dickerson', 'Dickinson', '!Dickison'),
            ('D*KSN', 'Dickson', 'Dixon', 'Dixson'),
            ('D*L', 'Dailey', 'Daily', 'Daley', 'Daly'),
            ('D*L', 'Dahl', 'Dahle', 'Dall', 'Doll'),
            ('D*L', 'Deahl', 'Deal', 'Diehl'),
            ('D*MN', 'Diamond', 'Dimond', 'Dymond'),
            ('D*N', 'Dean', 'Deane', 'Deen'),
            ('D*N', 'Denney', 'Denny'),
            ('D*N', 'Donahoo', 'Donahue', 'Donoho', 'Donohoe', 'Donohoo,'),
            ('D*N', 'Donohue', 'Dunnahoo'),
            ('D*N', 'Downey', 'Downie'),
            ('D*N', 'Dunn', 'Dunne'),
            ('D*NL', 'Donley', 'Donnelley', 'Donnelly'),
            ('D*R', 'Daugherty', 'Doherty', 'Dougherty'),
            ('D*R', 'Dyar', 'Dyer'),
            ('D*RM', 'Derham', 'Durham'),
            ('D*VDSN', 'Davidsen', 'Davidson', '!Davison'),
            ('D*VS', 'Davies', 'Davis'),
            ('DR*SL', 'Driscoll', 'Driskell'),
            ('F*', 'Fay', 'Fahay', 'Fahey'),
            ('F*FR', 'Fifer', 'Pfeffer', 'Pfeiffer'),
            ('F*GN', 'Fagan', 'Feigan', 'Fegan'),
            ('F*L', 'Feil', 'Pfeil'),
            # Corrected: T -> D after LD -> D
            ('F*L', 'Feld', 'Feldt', '!Felt'),
            ('F*LKNR', 'Faulkner', 'Falconer'),
            ('F*LPS', 'Philips', 'Phillips'),
            ('F*NGN', 'Finnegan', 'Finnigan'),
            ('F*NL', 'Finlay', 'Finley'),
            ('F*RL', 'Farrell', 'Ferrell'),
            ('F*RR', 'Ferrara', 'Ferreira', 'Ferriera'),
            # Corrected: No reason for S to be eliminated
            ('F*RSR', 'Foerster', 'Forester', 'Forrester', 'Forster'),
            ('F*RS', 'Forrest', 'Forest'),
            ('F*RS', 'Faris', 'Farriss', 'Ferris', 'Ferriss'),
            ('F*RS', 'First', 'Fuerst', 'Furst'),
            ('F*SR', 'Fischer', 'Fisher'),
            ('FL*N', 'Flinn', 'Flynn'),
            ('FL*NGN', 'Flanagan', 'Flanigan', 'Flannigan'),
            ('FR*', 'Frei', 'Frey', 'Fry', 'Frye'),
            ('FR*DMN', 'Freedman', 'Friedman'),
            # Corrected: Fredickson -> Fredrickson
            # (Correct in Cunningham, et al. 1969.)
            (
                'FR*DRKSN',
                'Frederickson',
                'Frederiksen',
                'Fredrickson',
                'Fredriksson',
            ),
            # Corrected: NK would not reduce to K because of rule 4
            ('FR*NK', 'Franck', 'Frank'),
            ('FR*NS', 'France', 'Frantz', 'Franz'),
            # Corrected: vowel deletion happens after double
            # consonant deletion
            ('FR*NSS', 'Frances', 'Francis'),
            ('FR*S', 'Freeze', 'Freese', 'Fries'),
            ('FR*SR', 'Fraser', 'Frasier', 'Frazer', 'Frazier'),
            ('G*D', 'Good', 'Goode'),
            ('G*DS', 'Getz', 'Goetz', 'Goetze'),
            ('G*F', 'Goff', 'Gough'),
            ('G*L', 'Gold', 'Goold', 'Gould'),
            ('G*LMR', 'Gilmer', 'Gilmore', 'Gilmour'),
            ('G*LR', 'Gallagher', 'Gallaher', 'Galleher'),
            ('G*MS', 'Gomes', 'Gomez'),
            ('G*NR', 'Guenther', 'Gunther'),
            ('G*NSLS', 'Gonzales', 'Gonzalez'),
            # Corrected: 'Consalves' for the first case likely a typo
            # (Correct in Cunningham, et al. 1969.)
            ('G*NSLVS', 'Gonsalves', 'Gonzalves'),
            ('G*RD', 'Garratt', 'Garrett'),
            ('G*RD', 'Garrity', 'Geraghty', 'Geraty', 'Gerrity'),
            ('G*RN', 'Gorden', 'Gordohn', 'Gordon'),
            ('G*RNR', 'Gardiner', 'Gardner', 'Gartner'),
            ('G*RR', 'Garrard', 'Gerard', 'Gerrard', 'Girard'),
            ('G*S', 'Gauss', 'Goss'),
            ('GR*', 'Gray', 'Grey'),
            ('GR*FD', 'Griffeth', 'Griffith'),
            ('GR*N', 'Green', 'Greene'),
            ('GR*S', 'Gros', 'Grose', 'Gross'),
            ('H*D', 'Hyde', 'Heidt'),
            ('H*F', 'Hoff', 'Hough', 'Huff'),
            ('H*FMN', 'Hoffman', 'Hoffmann', 'Hofman', 'Hofmann', 'Huffman'),
            ('H*G', 'Hoag', 'Hoge', 'Hogue'),
            ('H*GN', 'Hagan', 'Hagen'),
            ('H*K', 'Hauch', 'Hauck', 'Hauk', 'Hauke'),
            ('H*KSN', 'Hutcheson', 'Hutchison'),
            ('H*L', 'Holley', 'Holly'),
            ('H*L', 'Holl', 'Hall'),
            ('H*L', 'Halley', 'Haley'),
            ('H*L', 'Haile', 'Hale'),
            ('H*LD', 'Holiday', 'Halliday', 'Holladay', 'Holliday'),
            ('H*LG', 'Helwig', 'Hellwig'),
            ('H*LM', 'Holm', '!Home'),
            ('H*LMS', 'Holmes', '!Homes'),
            ('H*LN', 'Highland', 'Hyland'),
            ('H*M', 'Ham', 'Hamm'),
            ('H*MR', 'Hammar', 'Hammer'),
            ('H*N', 'Hanna', 'Hannah'),
            ('H*N', 'Hahn', 'Hahne', 'Hann', 'Haun'),
            ('H*NN', 'Hanan', 'Hannan', 'Hannon'),
            ('H*NRKS', 'Hendricks', 'Hendrix', 'Henriques'),
            ('H*NRKSN', 'Hendrickson', 'Henriksen', 'Henrikson'),
            (
                'H*NS',
                'Heintz',
                'Heinz',
                'Heinze',
                'Hindes',
                'Hinds',
                'Hines',
                'Hinze',
            ),
            ('H*NS', 'Haines', 'Haynes'),
            (
                'H*NSN',
                'Henson',
                'Hansen',
                'Hanson',
                'Hanssen',
                'Hansson',
                'Hanszen',
            ),
            ('H*R', 'Herd', 'Heard', 'Hird', 'Hurd'),
            ('H*R', 'Hart', 'Hardt', 'Harte', 'Heart'),
            ('H*R', 'Hare', 'Hair'),
            ('H*R', 'Hardey', 'Hardie', 'Hardy'),
            ('H*RMN', 'Hartman', 'Hardmen', 'Hardman', 'Hartmann'),
            ('H*RMN', 'Herman', 'Hermann', 'Herrmann'),
            ('H*RMN', 'Harman', 'Harmon'),
            ('H*RN', 'Heron', 'Herrin', 'Herron'),
            ('H*RN', 'Hardin', 'Harden'),
            ('H*RN', 'Horn', 'Horne'),
            ('H*RNGDN', 'Herrington', 'Harrington'),
            ('H*S', 'Haas', 'Haase', 'Hasse'),
            ('H*S', 'Howes', 'House', 'Howse'),
            ('H*S', 'Hays', 'Hayes'),
            ('H*SN', 'Houston', 'Huston'),
            ('H*VR', 'Hoover', 'Hover'),
            ('J*', 'Jew', 'Jue'),
            ('J*FR', 'Jeffery', 'Jeffrey'),
            ('J*FRS', 'Jefferies', 'Jefferis', 'Jefferys', 'Jeffreys'),
            ('J*KB', 'Jacobi', 'Jacoby'),
            ('J*KBSN', 'Jacobsen', 'Jacobson', 'Jackobsen'),
            ('J*KS', 'Jacques', 'Jacks', 'Jaques'),
            ('J*L', 'Jewell', 'Juhl'),
            ('J*MS', 'Jaimes', 'James'),
            ('J*MSN', 'Jameson', 'Jamieson', 'Jamison'),
            (
                'J*NSN',
                'Jahnsen',
                'Jansen',
                'Jansohn',
                'Janssen',
                'Jansson,',
                'Janzen',
                'Jensen',
                'Jenson',
            ),
            ('J*S', 'Joice', 'Joyce'),
            ('K*', 'Kay', 'Kaye'),
            ('K*F', 'Coffee', 'Coffey'),
            ('K*FMN', 'Coffman', 'Kauffman', 'Kaufman', 'Kaufmann'),
            ('K*K', 'Cook', 'Cooke', 'Koch', 'Koche'),
            ('K*K', 'Cook', 'Cooke', 'Koch', 'Koche'),
            ('K*L', 'Cole', 'Kohl', 'Koll'),
            ('K*L', 'Cole', 'Kohl', 'Koll'),
            ('K*L', 'Kelley', 'Kelly'),
            ('K*LMN', 'Coleman', 'Colman'),
            ('K*LR', 'Koehler', 'Koeller', 'Kohler', 'Koller'),
            ('K*MBRLN', 'Chamberlain', 'Chamberlin'),
            ('K*MBS', 'Combs', 'Coombes', 'Coombs'),
            ('K*MP', 'Camp', 'Kampe', 'Kampf'),
            ('K*MPS', 'Campos', 'Campus'),
            ('K*N', 'Cahn', 'Conn', 'Kahn'),
            ('K*N', 'Cahen', 'Cain', 'Caine', 'Cane', 'Kain', 'Kane'),
            ('K*N', 'Chin', 'Chinn'),
            ('K*N', 'Chaney', 'Cheney'),
            ('K*N', 'Coen', 'Cohan', 'Cohen', 'Cohn', 'Cone', 'Koehn', 'Kahn'),
            ('K*N', 'Coon', 'Kuhn', 'Kuhne'),
            ('K*N', 'Kenney', 'Kenny', 'Kinney'),
            ('K*NL', 'Conley', 'Conly', 'Connelly', 'Connolly'),
            ('K*NR', 'Conner', 'Connor'),
            ('K*NS', 'Coons', 'Koontz', 'Kuhns', 'Kuns', 'Kuntz', 'Kunz'),
            ('K*P', 'Coop', 'Co-op', 'Coope', 'Coupe', 'Koop'),
            (
                'K*PL',
                'Chapel',
                'Chapell',
                'Chappel',
                'Chappell',
                'Chappelle',
                'Chapple',
            ),
            ('K*R', 'Carrie', 'Carey', 'Cary'),
            ('K*R', 'Corey', 'Cory'),
            ('K*R', 'Carr', 'Kar', 'Karr'),
            # Corrected: No reason to strip S
            ('K*RS', 'Kurtz', 'Kurz'),
            ('K*R', 'Kehr', 'Ker', 'Kerr'),
            ('K*RD', 'Cartwright', 'Cortright'),
            # Corrected: No reason to strip D
            ('K*RLDN', 'Carleton', 'Carlton'),
            # Corrected: CE -> SE
            ('K*RN', 'Carney', '!Cerney', 'Kearney'),
            # Corrected: RC -> R
            ('K*RSNR', 'Kirschner', '!Kirchner'),
            ('K*S', 'Chace', 'Chase'),
            ('K*S', 'Cass', 'Kass'),
            ('K*S', 'Kees', 'Keyes', 'Keys'),
            ('K*SL', 'Cassel', 'Cassell', 'Castle'),
            ('K*SLR', 'Kesler', 'Kessler', 'Kestler'),
            (
                'K*SR',
                'Kaiser',
                'Kayser',
                'Keizer',
                'Keyser',
                'Kieser',
                'Kiser',
                'Kizer',
            ),
            ('KL*N', 'Cline', 'Klein', 'Kleine', 'Kline'),
            ('KL*RK', 'Clark', 'Clarke'),
            ('KL*SN', 'Claussen', 'Clausen', 'Clawson', 'Closson'),
            ('KR*', 'Crow', 'Crowe'),
            ('KR*GR', 'Krieger', 'Kroeger', 'Krueger', 'Kruger'),
            ('KR*MR', 'Creamer', 'Cramer', 'Kraemer', 'Kramer', 'Kremer'),
            ('KR*N', 'Craine', 'Crane'),
            ('KR*S', 'Christie', 'Christy', 'Kristee'),
            ('KR*S', 'Crouss', 'Kraus', 'Krausch', 'Krause', 'Krouse'),
            ('KR*S', 'Cross', 'Krost'),
            ('KR*S', 'Crews', 'Cruz', 'Kruse'),
            ('KR*SNSN', 'Christensen', 'Christiansen', 'Christianson'),
            ('L*', 'Loe', 'Loewe', 'Low', 'Lowe'),
            ('L*', 'Lea', 'Lee', '!Leigh'),
            ('L*D', 'Lloyd', 'Loyd'),
            ('L*DL', 'Litle', 'Littell', 'Little', 'Lytle'),
            ('L*DRMN', 'Ledterman', 'Letterman'),
            ('L*K', 'Leach', 'Leech', 'Leitch'),
            ('L*KS', 'Lucas', 'Lukas'),
            ('L*LN', 'Laughlin', 'Loughlin'),
            ('L*LR', 'Lawler', 'Lawlor'),
            ('L*MB', 'Lamb', '!Lamm'),
            ('L*MN', 'Lemen', 'Lemmon', 'Lemon'),
            ('L*MN', 'Layman', 'Lehman', 'Lehmann'),
            ('L*N', 'Lind', 'Lynd', 'Lynde'),
            ('L*N', 'Lion', 'Lyon'),
            ('L*N', 'Lin', 'Linn', 'Lynn', 'Lynne'),
            # Corrected: NG -> NG (!N)
            ('L*N', 'Lain', 'Laine', '!Laing', 'Lane', 'Layne'),
            ('L*NG', 'Lang', 'Lange'),
            ('L*NN', 'London', 'Lundin'),
            ('L*NS', 'Lindsay', 'Lindsey', '!Lindsley', '!Linsley'),
            ('L*R', 'Lawry', 'Lowery', 'Lowrey', 'Lowry'),
            ('L*RNS', 'Lawrence', 'Lowrance'),
            ('L*RNS', 'Laurence', 'Lawrance', 'Lawrence', 'Lorence', 'Lorenz'),
            ('L*RSN', 'Larsen', 'Larson'),
            ('L*S', 'Lewis', 'Louis', 'Luis', 'Luiz'),
            ('L*S', 'Lacey', 'Lacy'),
            ('L*SR', '!Leicester', 'Lester'),
            ('L*V', 'Levey', 'Levi', 'Levy'),
            ('L*VD', 'Leavett', 'Leavitt', 'Levit'),
            ('L*VL', 'Lavell', 'Lavelle', 'Leavelle', 'Loveall', 'Lovell'),
            ('L*VN', 'Lavin', 'Levin', 'Levine'),
            ('M*D', 'Mead', 'Meade'),
            # Corrected: RT*N -> R*N -> RN
            ('M*RN', '!Moretton', 'Morton'),
            ('M*DS', 'Mathews', 'Matthews'),
            (
                'M*DSN',
                'Madison',
                'Madsen',
                'Matson',
                'Matteson',
                'Mattison',
                'Mattson',
            ),
            ('M*KL', 'Michael', 'Michel'),
            ('M*KM', 'Meacham', 'Mechem'),
            # Corrected: RQ*S -> RKS, not KS
            ('M*RKS', 'Marques', 'Marquez', 'Marquis', 'Marquiss'),
            # Corrected: RKS does not compress to KS
            ('M*RKS', 'Marcks', 'Marks', 'Marx'),
            ('M*LN', 'Maloney', 'Moloney', 'Molony'),
            ('M*LN', 'Mullan', 'Mullen', 'Mullin'),
            ('M*LR', 'Mallery', 'Mallory'),
            ('M*LR', 'Moeller', 'Moller', 'Mueller', 'Muller'),
            ('M*LR', 'Millar', 'Miller'),
            ('M*LS', 'Miles', 'Myles'),
            ('M*N', 'Mahan', 'Mann'),
            ('M*NR', 'Miner', 'Minor'),
            ('M*NR', 'Monroe', 'Munro'),
            ('M*NSN', 'Monson', 'Munson'),
            ('M*R', 'Murray', 'Murrey'),
            ('M*R', 'Maher', 'Maier', 'Mayer'),
            ('M*R', 'Mohr', 'Moor', 'Moore'),
            # Corrected: No reason to eliminate final S
            ('M*RS', 'Meyers', 'Myers'),
            ('M*R', 'Meier', 'Meyer', 'Mieir', 'Myhre'),
            ('M*RF', 'Murphey', 'Murphy'),
            ('M*RL', 'Merrell', 'Merrill'),
            ('M*RN', 'Marten', 'Martin', 'Martine', 'Martyn'),
            ('M*RS', 'Meyers', 'Myers'),
            ('M*RS', 'Maurice', 'Morris', 'Morse'),
            ('MK*', 'McCoy', 'McCaughey'),
            ('MK*', 'Magee', 'McGee', 'McGehee', 'McGhie'),
            ('MK*', 'Mackey', 'MacKay', 'Mackie', 'McKay'),
            ('MK*', 'McCue', '!McHugh'),
            ('MK*L', 'Magill', 'McGill'),
            ('MK*LF', 'McCollough', '!McCullah', 'McCullough'),
            ('MK*LM', 'McCallum', 'McCollum', 'McColm'),
            ('MK*N', 'McKenney', 'McKinney'),
            ('MK*NR', 'Macintyre', 'McEntire', 'Mcintire', 'Mcintyre'),
            ('MK*NS', 'MacKenzie', 'McKenzie'),
            (
                'MK*NS',
                'Maginnis',
                'McGinnis',
                'McGuinness',
                'Mcinnes',
                'Mcinnis',
            ),
            ('MK*R', 'Maguire', 'McGuire'),
            ('MK*R', 'McCarthy', 'McCarty'),
            ('MKD*NL', 'MacDonald', 'McDonald', 'McDonnell'),
            ('MKF*RLN', 'MacFarland', 'MacFarlane', 'McFarland', 'McFarlane'),
            ('MKF*RSN', 'MacPherson', 'McPherson'),
            ('MKL*D', 'MacLeod', 'McCloud', 'McLeod'),
            (
                'MKL*KLN',
                'MacLachlan',
                'Maclachlin',
                'McLachlan',
                '!McLaughlin,',
                '!McLoughlin',
            ),
            ('MKL*LN', 'McClellan', 'McClelland', 'McLellan'),
            ('MKL*N', 'McClain', 'McClaine', 'McLain', 'McLane'),
            ('MKL*N', 'MacLean', 'McClean', 'McLean'),
            ('MKL*S', 'McCloskey', 'McClosky', 'McCluskey'),
            ('MKM*LN', 'MacMillan', 'McMillan', 'McMillin'),
            ('MKN*L', 'MacNeal', 'McNeal', 'McNeil', 'McNeill'),
            ('MKR*D', 'Magrath', 'McGrath'),
            (
                'N*KL',
                'Nichol',
                'Nicholl',
                'Nickel',
                'Nickle',
                'Nicol',
                'Nicoll',
            ),
            ('N*KLS', 'Nicholls', 'Nichols', 'Nickels', 'Nickles', 'Nicols'),
            ('N*KLS', 'Nicholas', 'Nicolas'),
            ('N*KLSN', 'Nicholsen', 'Nicholson', 'Nicolaisen', 'Nicolson'),
            ('N*KSN', 'Nickson', 'Nixon'),
            ('N*L', 'Neal', 'Neale', 'Neall', 'Neel', 'Neil', 'Neill'),
            (
                'N*LSN',
                'Neilsen',
                'Neilson',
                'Nelsen',
                'Nelson',
                'Nielsen',
                'Nielson,',
                'Nilson',
                'Nilssen',
                'Nilsson',
            ),
            ('N*MN', 'Neumann', 'Newman'),
            ('N*RS', 'Norris', 'Nourse'),
            ('N*SBD', 'Nesbit', 'Nesbitt', 'Nisbet'),
            ('P*D', 'Pettee', 'Petty'),
            (
                'P*DRSN',
                'Peterson',
                'Pederson',
                'Pedersen',
                'Petersen',
                'Petterson',
            ),
            ('P*G', 'Page', 'Paige'),
            ('P*LK', 'Polak', 'Pollack', 'Pollak', 'Pollock'),
            ('P*LSN', 'Polson', 'Paulsen', 'Paulson', 'Poulsen', 'Poulsson'),
            ('P*N', 'Paine', 'Payn', 'Payne'),
            ('P*R', 'Parry', 'Perry'),
            ('P*R', 'Parr', 'Paar'),
            ('P*RK', 'Park', 'Parke'),
            ('P*RKS', 'Parks', 'Parkes'),
            # Corrected: RC -> R
            ('P*R', 'Pierce', 'Pearce', 'Peirce', '!Piers'),
            ('P*RS', 'Parish', 'Parrish'),
            ('P*RS', 'Paris', 'Parris'),
            ('P*RSN', 'Pierson', 'Pearson', 'Pehrson', 'Peirson'),
            ('PR*KR', 'Prichard', 'Pritchard'),
            ('PR*NS', 'Prince', 'Prinz'),
            ('PR*R', 'Prior', 'Pryor'),
            ('R*', 'Roe', 'Rowe'),
            ('R*', 'Rae', 'Ray', 'Raye', 'Rea', 'Rey', 'Wray'),
            ('R*BNSN', 'Robinson', '!Robison'),
            ('R*D', 'Rothe', 'Roth'),
            ('R*D', 'Rudd', 'Rood', 'Rude'),
            ('R*D', 'Reed', 'Read', 'Reade', 'Reid'),
            ('R*DR', 'Rider', 'Ryder'),
            ('R*DS', 'Rhoades', 'Rhoads', 'Rhodes'),
            ('R*GN', 'Regan', 'Ragon', 'Reagan'),
            # Corrected: No reason to drop final S
            ('R*GRS', 'Rodgers', 'Rogers'),
            ('R*K', 'Richey', 'Ritchey', 'Ritchie'),
            ('R*K', 'Reich', 'Reiche'),
            ('R*KR', 'Reichardt', 'Richert', 'Rickard'),
            ('R*L', 'Reilley', 'Reilly', 'Reilli', 'Riley'),
            # Corrected: T -> D
            ('R*MNGDN', 'Remington', 'Rimington'),
            ('R*MR', 'Reamer', 'Reimer', 'Riemer', 'Rimmer'),
            ('R*MS', 'Ramsay', 'Ramsey'),
            ('R*N', 'Rhein', 'Rhine', 'Ryan'),
            (
                'R*NR',
                'Reinhard',
                'Reinhardt',
                'Reinhart',
                'Rhinehart',
                'Rinehart',
            ),
            ('R*S', 'Reas', 'Reece', 'Rees', 'Reese', 'Reis', 'Reiss', 'Ries'),
            ('R*S', '!Rauch', 'Rausch', '!Roach', '!Roche', 'Roush'),
            ('R*S', 'Rush', 'Rusch'),
            ('R*S', 'Russ', 'Rus'),
            ('R*VS', 'Reaves', 'Reeves'),
            ('S*BR', 'Seibert', 'Siebert'),
            ('S*FL', 'Schofield', 'Scofield'),
            ('S*FN', 'Stefan', 'Steffan', 'Steffen', 'Stephan', 'Stephen'),
            ('S*FNS', 'Steffens', 'Stephens', '!Stevens'),
            ('S*FNSN', 'Steffensen', 'Steffenson', 'Stephenson', '!Stevenson'),
            (
                'S*FR',
                'Schaefer',
                'Schaeffer',
                'Schafer',
                'Schaffer',
                'Schafer,',
                'Shaffer',
                'Sheaffer',
            ),
            ('S*FR', 'Stauffer', 'Stouffer'),
            ('S*GL', 'Siegal', 'Sigal'),
            ('S*GLR', 'Sigler', 'Ziegler'),
            ('S*K', 'Schuck', 'Shuck'),
            ('S*KS', 'Sachs', 'Sacks', 'Saks', 'Sax', 'Saxe'),
            ('S*L', 'Seeley', 'Seely', 'Seley'),
            ('S*L', 'Schell', 'Shell'),
            ('S*LR', 'Schuler', 'Schuller'),
            # Corrected: LD -> L precedes T -> D
            (
                'S*LDS',
                'Schultz',
                'Schultze',
                '!Schulz',
                '!Schulze',
                'Shults',
                'Shultz',
            ),
            ('S*LV', 'Silva', 'Sylva'),
            ('S*LVR', 'Silveira', 'Silvera', 'Silveria'),
            (
                'S*MKR',
                'Schomaker',
                'Schumacher',
                'Schumaker',
                'Shoemaker,',
                'Shumaker',
            ),
            ('S*MN', 'Simon', 'Symon'),
            ('S*MN', 'Seaman', 'Seemann', 'Semon'),
            ('S*MRS', 'Somers', 'Sommars', 'Sommers', 'Summers'),
            ('S*MS', 'Simms', 'Sims'),
            ('S*N', 'Stein', 'Stine'),
            ('S*N', 'Sweeney', 'Sweeny', 'Sweney'),
            ('S*NR', 'Senter', 'Center'),
            ('S*NRS', 'Sanders', 'Saunders'),
            (
                'S*PR',
                'Shepard',
                '!Shephard',
                '!Shepheard',
                '!Shepherd',
                'Sheppard',
            ),
            ('S*R', 'Stahr', 'Star', 'Starr'),
            ('S*R', 'Stewart', 'Stuart'),
            ('S*R', 'Storey', 'Story'),
            ('S*R', 'Saier', 'Sayre'),
            # Corrected: No reason to strip final S
            ('S*RS', 'Schwartz', 'Schwarz', 'Schwarze', 'Swartz'),
            ('S*RL', 'Schirle', 'Shirley'),
            ('S*RLNG', 'Sterling', 'Stirling'),
            ('S*RMN', 'Scheuermann', 'Schurman', 'Sherman'),
            ('S*RN', 'Stearn', 'Stern'),
            ('S*RR', 'Scherer', 'Shearer', 'Sharer', 'Sherer', 'Sheerer'),
            ('S*S', 'Sousa', 'Souza'),
            ('SM*D', 'Smith', 'Smyth', 'Smythe'),
            ('SM*D', 'Schmid', 'Schmidt', 'Schmit', 'Schmitt', 'Smit'),
            ('SN*DR', 'Schneider', 'Schnieder', 'Snaider', 'Snider', 'Snyder'),
            ('SN*L', 'Schnell', 'Snell'),
            ('SP*LNG', 'Spalding', 'Spaulding'),
            ('SP*R', 'Spear', 'Speer', '!Speirer'),
            # Corrected: No reason to strip final S
            ('SP*RS', 'Spears', 'Speers'),
            ('SR*DR', 'Schroder', 'Schroeder', 'Schroeter'),
            ('SR*DR', 'Schrader', 'Shrader'),
            # Corrected: Everywhere else, rule 3 applies to char 1
            ('D*D', 'Tait', 'Tate'),
            ('D*MSN', 'Thomason', '!Thompson', 'Thomsen', 'Thomson', 'Tomson'),
            ('D*RL', 'Terrel', 'Terrell', 'Terrill'),
            ('DR*S', 'Tracey', 'Tracy'),
            ('V*L', 'Vail', 'Vaile', 'Vale'),
            ('V*L', 'Valley', 'Valle'),
            ('V*R', 'Vieira', 'Vierra'),
            ('W*D', 'White', 'Wight'),
            ('W*DKR', 'Whitacre', 'Whitaker', 'Whiteaker', 'Whittaker'),
            ('W*DL', 'Whiteley', 'Whitley'),
            ('W*DMN', 'Whitman', 'Wittman'),
            ('W*DR', 'Woodard', 'Woodward'),
            ('W*DRS', 'Waters', 'Watters'),
            (
                'W*GNR',
                'Wagener',
                'Waggener',
                'Wagoner',
                'Wagner',
                'Wegner,',
                'Waggoner',
            ),
            ('W*L', 'Willey', 'Willi'),
            ('W*L', 'Wiley', 'Wylie'),
            ('W*L', 'Wahl', 'Wall'),
            ('W*LBR', 'Wilber', 'Wilbur'),
            (
                'W*LF',
                'Wolf',
                'Wolfe',
                'Wolff',
                'Woolf',
                'Woulfe',
                'Wulf',
                'Wulff',
            ),
            ('W*LKNS', 'Wilkens', 'Wilkins'),
            ('W*LKS', 'Wilkes', 'Wilks'),
            ('W*LN', 'Whalen', 'Whelan'),
            # Corrected: LD -> L precedes T -> D
            ('W*LDR', 'Walter', 'Walther', 'Wolter'),
            ('W*LDRS', 'Walters', 'Walthers', 'Wolters'),
            ('W*LS', 'Wallace', 'Wallis'),
            ('W*LS', 'Welch', 'Welsh'),
            ('W*LS', 'Welles', 'Wells'),
            ('W*LSN', 'Willson', 'Wilson'),
            ('W*N', 'Winn', 'Wynn', 'Wynne'),
            ('W*R', 'Worth', 'Wirth'),
            ('W*R', 'Ware', 'Wear', 'Weir', 'Wier'),
            ('W*RL', 'Wehrle', 'Wehrlie', 'Werle', 'Worley'),
            ('W*RNR', 'Warner', 'Werner'),
            ('W*S', 'Weis', 'Weiss', 'Wiese', 'Wise', 'Wyss'),
            (
                'W*SMN',
                'Weismann',
                'Weissman',
                'Weseman',
                'Wiseman,',
                'Wismonn',
                'Wissman',
            ),
        )

        for tests in test_cases:
            result, names = tests[0], tests[1:]
            for name in names:
                if name[0] == '!':
                    self.assertNotEqual(result, dolby(name[1:]))
                else:
                    self.assertEqual(result, dolby(name))

        # Additional tests to improve coverage
        self.assertEqual(dolby('Rune'), 'R*N')
        self.assertEqual(dolby('Rune', keep_vowels=True), 'R*N*')
        self.assertEqual(dolby('Rune', vowel_char=''), 'RN')
        self.assertEqual(dolby('Rune', vowel_char='A'), 'RAN')
        self.assertEqual(dolby('Rune', max_length=2), 'R*')
        self.assertEqual(dolby('Rune', max_length=2), 'R*')
        self.assertEqual(dolby('Wassermann', max_length=4), 'W*SR')
        self.assertEqual(
            dolby('Wassermanns', max_length=4, keep_vowels=True), 'W*S*'
        )
        self.assertEqual(dolby('Wassermanns'), 'W*SRMNS')


if __name__ == '__main__':
    unittest.main()
