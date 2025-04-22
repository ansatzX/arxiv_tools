from copy import deepcopy

replace_characters = {'[[' : '$[[',
                      ']]' : ']]$',
                      }
# phy 
quant_ph = {'advanced': '',
                    'terms-0-term': '',
                    'terms-0-operator': 'AND',
                    'terms-0-field': 'title',
                    'classification-physics': 'y',
                    'classification-physics_archives': 'quant-ph',
                    'classification-include_cross_list': 'include',
                    'date-filter_by': 'date_range',
                    'date-year': '',
                    'date-from_date': '2025-02-01',
                    'date-to_date': '2025-02-02',
                    'date-date_type': 'submitted_date_first', # first Submission 
                    'abstracts': 'show',
                    'size': '200',
                    'order': 'submitted_date'
                    }

hep_ex = deepcopy(quant_ph)
hep_ex['classification-physics_archives']= 'hep-ex'


hep_lat = deepcopy(quant_ph)
hep_lat['classification-physics_archives']= 'hep-lat'

hep_ph = deepcopy(quant_ph)
hep_ph['classification-physics_archives']= 'hep-ph'


hep_th = deepcopy(quant_ph)
hep_th['classification-physics_archives']= 'hep-th'

chem_ph = deepcopy(quant_ph)
chem_ph['classification-physics_archives']= 'physics'
chem_ph['terms-1-operator'] = 'AND'
chem_ph['terms-1-term'] = 'physics.chem-ph'
chem_ph['terms-1-field'] = 'all'

query_args = {
    'quant-ph': quant_ph,
    'hep-ex': hep_ex,
    'hep-lat': hep_lat,
    'hep-ph': hep_ph,
    'hep-th': hep_th,
    'chem-ph': chem_ph,
}