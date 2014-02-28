# PPE Modifiee
def fusion_a(div_ms, ra_rsa, br_rmi_i, br_rmi_ms, br_rmi_pf, br_rmi, rmi_nbp, forf_log, rsa_socle, rmi, rsa, rsa_act, rsa_act_i, crds_mini, ppe_coef, ppe_base, ppe_coef_tp, ppe_elig, ppe_elig_i, ppe_rev, ppe_brute, ppe):
    """
    J'ajoute tous les variables qui composent le RSA et la PPE pour pouvoir
    créer des booleans et des boucles si nous en avons besoin ainsi que changer
    les bases des composants de la PPE et du RSA sans changer les fichiers.
    """ 
#     Pour calculer le rmi/RSA des le premier euro
    rmi = max_(1, rsa_socle - forf_log - br_rmi)
    return rmi

    P = _P.minim.rmi
    RSA = max_(1, rsa_socle + P.pente * (ra_rsa[CHEF] + ra_rsa[PART]) - forf_log - br_rmi)
    rsa = RSA * (RSA >= 12 * P.rsa_nv)
    return rsa
    
    res = max_(rsa - rmi, 1)
    return res

#     TODO: - Ajoute la PPE
#           - Changer l'age de 25 à 18 ans
#           - Créer une pente jusqu'à 0,7 du SMIC et décroit jusqu'au point de sortie
#           - Changer le point de sortie (1,1 du SMIC)
#           
#
    
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