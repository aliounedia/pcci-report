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
        print 'The query'
        print qs
        self.cursor.execute(qs)

    def va_exporter(self, config=None, *args, **kwargs):
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
        #td    = date.today()
        td   = date.today()-timedelta(days = 1)
        fdst  = '%s/ORANGE_QUALIF_remerciement_%s_%s_%s.csv'%(
                dir, td.year,
                td.month, td.day)
        #
        self.do_query(query, with_date =False)
        # self.export(fdst, None, header)
        list = map( lambda x: 'gsm='+ x[0], self.cursor.fetchall())
        print list 
        send_mail(dir = '',list =list)
         

# send mail to alioune
def  send_mail(dir , list  = []):
    body  ="""[sms]\n%s\ntxt=Nous vous confirmons votre inscription.
    Vous recevrez bientôt gratuitement des bons plans et des promos.
    A bientôt sur www.mobilegagnant.fr
    """ % "\n".join(list)
    to = [
    'connaitre.orange@pcci.sn', 'alba@pcci.sn','adia@pcci.sn' ,
    'smgning@pcci.sn' , 'andoye@pcci.sn' ]
    """

    to = [
    'adia@pcci.sn']
    """
    print  dir
    subject="SMS de confirmation d'inscription à mobile gagnant"     
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
                config.CONFIG_ORANGE_QUALIF_confirmation)
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
