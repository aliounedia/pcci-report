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
sys.path.insert(0,path.join(
    path.dirname(path.abspath(__file__)), '..'))
from smtp import send
# Only for test
from time import gmtime,strftime
import config  
from utils import _pprint
import time

class BarometreQuality(base_csv_export.BaseExport):
    # Pour le moment ces modules sont tres sales et un peu disperses
    #, mais je ne desespere pas de pouvoir trouver un moyen plus 
    # elegant  de reecrire le code , si je toruve le temps necessaire
    
    # <job_thread_runner.py> a quelle heure de le journee il
    # doit executer ce module
    def __init__(self):
        base_csv_export.BaseExport.__init__(self)
        
              
    def do_query(self, qs, with_date=False):
        self.execute(qs)
        
    def va_exporter(self, dict , *args, **kwargs):
        now = datetime.now().date()
        dir =  'EXPORT_QUOTIDIEN'
        try:
            if not os.path.exists(dir):
                os.mkdir(dir)
        except:
            pass
        #create the dir
           
        query  = dict['query']
        file   = dict['file']
        header = dict['header']

        # Create repository where to save file after
        # generation
        td    = date.today()
        fdst  = '%s/export_welcome_call_%s%s%s.csv'%(dir, td.year,
                                            td.month, td.day)      

        # The is extremly important, The file will bes
        # sent only if it contain exactly 333 lignes
            
        self.do_query(query, with_date =False)
        self.export(fdst, None, header)
        # All is ok , now send mail
        send_mail(dir = fdst)
           

# send mail to alioune
def  send_mail(dir):
    body  ="""
    Bonjoura tous <br/>
    Veuillez trouver ci-joint l'export du fichier welcome call du
    %s.<br/>
    Cordialement Informatique<br/> """%(datetime.now())
    to = [                 'eyfaye@pcci.sn',
                           'smgning@pcci.sn',
                           'magoudiaby@pcci.sn',
                           'andoye@pcci.sn',
                           'tsenghor@pcci.sn',
                           'adia@pcci.sn',
                           'kmbaye@pcci.sn',
                           'rlaoualy@pcci.sn',
                           'agano@pcci.sn',
                           'sdial@pcci.sn',
                           'asambou@pcci.sn']
    """
    to = [
        'adia@pcci.sn',
        'dia.aliounes@gmail.com']
    
    """
    subject="export welcome call %s" %( datetime.now() )    
    send.send(att_file= str(dir), body =body,to = to ,
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
        try:
            _s= BarometreQuality()
            _s.va_exporter(config.CONFIG_EXPORT_WELCOME_CALL) 
        except Exception, e:
            #_pprint(lock, 'Error into bar_qual')
            raise
            time.sleep(200)
        else:
            #_pprint(lock, 'Finished to excecute bar_qual')
            time.sleep(24*3600)

if __name__ == "__main__":
    target()
    
