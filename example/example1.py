

# -*- coding: utf-8 -*-
from datetime import datetime
from openfisca_core import model
import openfisca_france
openfisca_france.init_country()
from openfisca_core.simulations import ScenarioSimulation

def case_study(year = 2013):
    
    simulation = ScenarioSimulation()
    simulation.set_config(year = year,
                          nmen = 2, 
                          maxrev = 10000,
                          x_axis = 'sali')
    simulation.set_param() #legislation#
    df = simulation.get_results_dataframe()
    print df.to_string()                 

if __name__ == '__main__':
    print "toto"
    case_study()
  