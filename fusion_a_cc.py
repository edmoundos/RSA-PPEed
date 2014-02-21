# # RSA
# from __future__ import division
# from numpy import (floor, maximum as max_, where,
#                    logical_not as not_, logical_and as and_,
#                    logical_or as or_)
# from .data import QUIFAM, QUIFOY
# from .pfam import nb_enf, age_en_mois_benjamin


# PPE Modifiee
from numpy import (maximum as max_, minimum as min_, where,
                   logical_xor as xor_,
                   logical_not as not_, 
                   logical_and as and_,
                   logical_or as or_, round)

import collections

from openfisca_core.columns import IntCol, EnumCol, BoolCol, AgesCol, FloatCol
from openfisca_core.enumerations import Enum

from openfisca_france.model.data import QUIFOY, QUIFAM

from openfisca_france.model.pfam import nb_enf, age_en_mois_benjamin

import logging

log = logging.getLogger(__name__)

# zetrf = zeros(taille)
# jveuf = zeros(taille, dtype = bool)
# Reprise du credit d'impot en faveur des jeunes, des accomptes et des versements mensues de prime pour l'emploi
# reprise = zeros(taille) # TODO : reprise=J80
# Pcredit = P.credits_impots
# if hasattr(P.reductions_impots,'saldom'): Pcredit.saldom =  P.reductions_impots.saldom
# credits_impot = Credits(Pcredit, table)
# Reduction d'impot
# reductions = Reductions(IPnet, P.reductions_impots)

# def mcirra():
#    # impot sur le revenu
#    mcirra = -((IMP<=-8)*IMP)
#    mciria = max_(0,(IMP>=0)*IMP)
# #        mciria = max_(0,(IMP>=0)*IMP - credimp_etranger - cont_rev_loc - ( f8to + f8tb + f8tc ))
#
#    # Dans l'ERFS, les prelevement liberatoire sur les montants non declares
#    # sont integres. Pas possible de le recalculer.
#
#    # impot sur le revenu du foyer (hors prelevement liberatoire, revenus au quotient)
#    irpp   = -(mciria + ppetot - mcirra )


