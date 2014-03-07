from datetime import datetime
from openfisca_core import model
import openfisca_france
openfisca_france.init_country()
from openfisca_core.simulations import ScenarioSimulation

# PPE Modifiee
def fusion_a(div_ms, ra_rsa, br_rmi_i, br_rmi_ms, br_rmi_pf, br_rmi, rmi_nbp, forf_log, rsa_socle, rmi, rsa, rsa_act, rsa_act_i, crds_mini, ppe_coef, ppe_base, ppe_coef_tp, ppe_elig, ppe_elig_i, ppe_rev, ppe_brute, ppe):
    """
    Pour quelqu'un qui a l'age de 18 ou plus peut toucher la fusion. La premiere
    si est la partie croissante. Elif dsigne la partie decroissante. Et else
    designe que si le salaire ne tombe pas dans ces deux cas la personne touche
    rien. La boucle 'For' fait des iterations pour chaque individu dans QUIFOY. La
    commande 'break' arrete la boucle pour le chef comme nous sommes concernes 
    uniquement par le chef.
    """
    while age >= 18:
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

          

#     TODO: 
#           - Corrige les fautes et fait tourner la code
