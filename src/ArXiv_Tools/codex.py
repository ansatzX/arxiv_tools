replace_characters = {'[[' : '$[[',
                      ']]' : ']]$',
                      }

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

hep_ex = {'advanced': '',
                    'terms-0-term': '',
                    'terms-0-operator': 'AND',
                    'terms-0-field': 'title',
                    'classification-physics': 'y',
                    'classification-physics_archives': 'hep-ex',
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

query_args = {
    'quant-ph': quant_ph,
    'hep-ex': hep_ex,
}