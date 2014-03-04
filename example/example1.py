

# -*- coding: utf-8 -*-
from datetime import datetime
from openfisca_core import model
import openfisca_france
openfisca_france.init_country()
from openfisca_core.simulations import ScenarioSimulation

def case_study(year = 2013):
    
    simulation = ScenarioSimulation()
    simulation.set_config(year = year,
                          nmen = 101, 
                          maxrev = 20000,
                          x_axis = 'sali')
    scenario = simulation.scenario
    scenario.declar[0]['ppe_tp_sa']=True
    simulation.set_param() #legislation#
    df = simulation.get_results_dataframe(index_by_code=True)
    
    
 #   print df.info()
    rsa_ppe = df.loc[['rsa','ppe','sal']]
    print rsa_ppe.to_string()
    rsa_ppe.to_excel('rsa.xls') 

#     print df.to_string()                 

if __name__ == '__main__':
    case_study()
    
