#!/usr/bin/python
# -*- coding: latin-1 -*-
import pyodbc
import csv
class BaseExport(object):
    # Pour le moment ces modules sont tres sales et un peu disperses
    #, mais je ne desespere pas de pouvoir trouver un moyen plus 
    # elegant  de reecrire le code , si je toruve le temps necessaire


    # L'approche est basique pour l'instant, chaque module doit en plus 
    # de ce qu'il est sense faire (exemple: un export) , definit 
    # un fonction appelee <target> qui especifie aux module
    # <job_thread_runner.py> a quelle heure de le journee il
    # doit executer ce module


    # Dans ce module
    # <BaseExport> une classe de base pour l'export xls et csv 
    def __init__ (self, *args, **kwargs):
        pass
    
    def export(self, file, qs, header, delimiter =';', *args, **kwargs):        
      data = self.cursor.fetchall()
      try:
         file =  open(file, 'wb')
         
      except IOError ,e:
           raise e
      w = csv.writer(file, dialect = csv.excel,
                         delimiter = delimiter)
      if header:
            w.writerow(header)
      ln  =len(data)
      if ln >0:
         for j  in range(ln):              
            print data[j], type(data[j]), len(data[j])
            w.writerow(data[j])

      file.close()
      return file
      
def test():
    class TestBaseExport(BaseExport):
        def __init__(self ):
            try:
                self.connection = pyodbc.connect('''
                DRIVER={SQL Server};
                SERVER=xx;
                DATABASE=xxx;
                UID=xx;
                PWD=xx''')
                self.cursor = self.connection.cursor()
                self.close  = self.cursor.close
                self.data   = []

            except pyodbc.OperationalError:
                raise
          
        def do_query(self, qs, with_date=False):
            
            def query_with_date(qs):
                return  qs.replace('#', self._jourdy_fy)

                if with_date:
                    qs = query_with_date(qs) 
                self.cursor.execute(qs)


        @property
        def _jourdy_fy(self):
            from datetime import date, timedelta
            dt = date.today() - timedelta(days =1)
            year, month, day  = dt.year, dt.month, dt.day
            if month<10:
                 month = '0%s'%str(month)
            if day<10:
                 day   = '0%s'%str(day)
            return '%s-%s-%s'\
                  %(year, month, day)
          
    query =  open('../query/Copie de EXPORT_FAUX_NUMERAUX_JOURNALIER.sql')\
            .read()
    
    print  '-'*40
    print query
    print  '-'*40
    
    tt =  TestBaseExport()
    tt.do_query(query)
    file = tt.export('test_export.csv',
           header=['num abo', 'num carte', 'num tel' ,'statut', 'fichier'],
           qs=query)


if __name__ =='__main__':
      test()
      
      
