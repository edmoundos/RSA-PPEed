from datetime import datetime
from openfisca_core import model
import openfisca_france
openfisca_france.init_country()
from openfisca_core.simulations import ScenarioSimulation
# PPE Modifiee
def fusion_a(div_ms, ra_rsa, br_rmi_i, br_rmi_ms, br_rmi_pf, br_rmi, rmi_nbp, forf_log, rsa_socle, rmi, rsa, rsa_act, rsa_act_i, crds_mini, ppe_coef, ppe_base, ppe_coef_tp, ppe_elig, ppe_elig_i, ppe_rev, ppe_brute, ppe):
    
    for agent in QUIFOY:
        if sal >=1 & sal <= 0.7*SMIC:
            total = min(sal, 0.7 * SMIC)
            fusion = min(12*total, 2000)

        elif sal >0.7 * SMIC & sal <=1.1 * SMIC:
            total = max((77/40)*SMIC - (7/4)*sal, 0)
            fusion = min(12*total, 2000)
      
        else:
            fusion = 0
        break

def case_study(year = 2013):
    
    simulation = ScenarioSimulation()
    simulation.set_config(year = year,
                          nmen = 20, 
                          maxrev = 20000,
                          x_axis = 'sali')
    scenario = simulation.scenario
    simulation.set_param() #legislation#
    scenario = simulation.scenario
    simulation.set_param()
    df = simulation.get_results_dataframe(index_by_code=True)

    print df.info()
    print df.to_string()


if __name__ == '__main__':
    case_study(fusion_a)

          

#     TODO: - Ajoute la PPE
#           - Changer l'age de 25 a 18 ans
#           - Creer une pente jusqu'a 0,7 du SMIC et decroit jusqu'au point de sortie
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