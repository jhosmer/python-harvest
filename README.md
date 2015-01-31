#Python Harvest API Client

###How to use:
    >>> import harvest
    >>> harvest.status()
    {u'description': u'All Systems Operational', u'indicator': u'none'}
    >>> h = harvest.Harvest('https://COMPANYNAME.harvestapp.com', 'EMAIL', 'PASSWORD')
    >>> data = {'notes': 'test note', 'project_id': 'PROJECT_ID', 'hours':'1.0', 'task_id': 'TASK_ID'}
    >>> h.add(data)
    >>> data['notes'] = 'another test'
    >>> data['hours'] = '6.5'
    >>> harvest.update('ENTRY_ID', data)
    >>> h.today
    {u'day_entries': [],
     u'for_day': u'2015-01-31',
     u'projects': [{u'billable': True,
       u'client': u'XXXclientXXX',
       u'client_currency': u'United States Dollars - USD',
       u'client_currency_symbol': u'$',
       u'client_id': 123456789,
       u'code': u'',
       u'id': 123456789,
       u'name': u'XXXXXnameXXXXX',
       u'tasks': [{u'billable': False, u'id': 123123123, u'name': u'Foo'},
        {u'billable': True, u'id': 123123124, u'name': u'Bar'}]}]}


