# -*- coding: latin-1 -*-
import pyodbc
import base_csv_export
from datetime import datetime, timedelta, date
import traceback
import time
import os
import shutil

import sys
from os import path
sys.path.insert(0,path.join(
    path.dirname(path.abspath(__file__)), '..','..','..'))
from smtp import send
# Only for test
from time import gmtime,strftime
import config 
from ..utils import _pprint
import time
import pyodbc

class BarometreQuality(base_csv_export.BaseExport):
    # Pour le moment ces modules sont tres sales et un peu disperses
    #, mais je ne desespere pas de pouvoir trouver un moyen plus 
    # elegant  de reecrire le code , si je toruve le temps necessaire


    # L'approche est basique pour l'instant, chaque module doit en plus 
    # de ce qu'il est sense faire (exemple: un export) , definit 
    # un fonction appelee <target> qui especifie aux module
    # <job_thread_runner.py> a quelle heure de le journee il
    # doit executer ce module
    def __init__(self):
        try:
            self.connection = pyodbc.connect(
            '''
            DRIVER={SQL Server};
            SERVER=xxx;
            DATABASE=xxx;
            UID=xxx;
            PWD=xxx''',
            autocommit =True
            )
            self.cursor = self.connection.cursor()
            self.close  = self.cursor.close
            self.data   = []
        except pyodbc.OperationalError:
               raise
              
    def do_query(self, qs, with_date=False):
        
        def query_with_date(qs):
            return  qs.replace('#', self._jourdy_fy )
        if  with_date:
            qs = query_with_date(qs)


        print 'The query'
        print qs
        self.cursor.execute(qs)

            
    @property
    def _jourdy_fy(self):
        dt   = date.today()-timedelta(days = 1)
        #dt   = date.today()-timedelta(days = 3)
        year = dt.year
        month= dt.month
        day  = dt.day
        if month < 10:
            month = '0%s'%str(month)
        if day < 10:
            day = '0%s'%str(day)
        return '%s-%s-%s'%(
            year, month, day)

    def va_exporter(self, config=None, *args, **kwargs):
        now = datetime.now().date()
        dir =  'EXPORT_QUOTIDIEN'
        try:
             if not os.path.exists(dir):
                 os.mkdir(dir)
        except:
            pass
    
        query  = config['query']
        file   = config['file']
        header = config['header']

        # Create repository where to save file after
        # generation
        td    = date.today()
        #td   = date.today()-timedelta(days = 3)
        fdst  = '%s/stats_chargements_afr_%s_%s_%s.csv'%(
                dir, td.year,
                td.month, td.day)

        #
        self.do_query(query, with_date =True)
        self.export(fdst, None, header)
        send_mail(dir = fdst)
         

# send mail to alioune
def  send_mail(dir):
    body  ="""
    Bonjour Yatma, tu trouveras en piece jointe l'export des
    chargements sur afrique.</br>
    Informatique.
    """
    to = [ 'eyfaye@pcci.sn',
                           'smgning@pcci.sn',
                           'magoudiaby@pcci.sn',
                           'andoye@pcci.sn',
                           'tsenghor@pcci.sn',
                           'adia@pcci.sn',
                           'kmbaye@pcci.sn',
                           'rlaoualy@pcci.sn',
                           'cmbacke@pcci.sn',
                           'sdial@pcci.sn']
    """
    to = [
    'adia@pcci.sn', 'eyfaye@pcci.sn']
    """
    
    print  dir
    subject="[Canal+]export statistiques des chargements\
        afr sur afrique"     
    send.send(att_file =dir,
              body =body,
              to = to ,
              subject =subject)


def target(lock =None , *args):
    from datetime import date
    while True :
        dt =datetime.now()
        #if False:
        if not dt.hour in (5, 6, 7, 4):
            _pprint(lock, 'Waiting into bar_qual')
            time.sleep(60)
            continue
        _pprint(lock, 'Starting to excecute bar_qual')
        try:
            _s= BarometreQuality()
            _s.va_exporter(
                config.CONFIG_STATS_CHARGEMENTS_AFR)
            _s.connection.close()
        except pyodbc.Error, e:
             _pprint(lock, 'Error into dialy_jobs')
             time.sleep(100) 
        except Exception, e:
            _pprint(lock, 'Error into bar_qual')
            time.sleep(200)
        else:
            _pprint(lock, 'Finished to excecute bar_qual')
            time.sleep(24*3600)


if __name__ =="__main__":
    target()
