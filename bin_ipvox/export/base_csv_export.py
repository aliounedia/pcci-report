#!/usr/bin/python
# -*- coding: latin-1 -*-
import csv
import MySQLdb
class BaseExport(object):
    # Pour le moment ces modules sont tres sales et un peu disperses
    #, mais je ne desespere pas de pouvoir trouver un moyen plus 
    # elegant  de reecrire le code , si je toruve le temps necessaire

    # Dans ce module
    # <BaseExport> une classe de base pour l'export xls et csv 
    def __init__ (self, *args, **kwargs):
            pass

    def execute_file(self, query):
        """
        The query are read from a File and the file
        contain many request separed by  $
        """
        self.db = MySQLdb.connect("10.2.3.2", "ipvoxdb2",
                         "ipvoxdb2", "canal")
        sqls    = out.split("$")
        for s in sqls:
            try:
                cursor = self.db.cursor()
                lines  = cursor.execute(s)   
                self.data  = cursor.fetchall()
            except : pass 
        db.close()
        print self.data
        return self.data

    def execute(self, query):
        """
        Execute a single query from  canal database
        """
        self.db = MySQLdb.connect("10.2.3.2", "ipvoxdb2",
                         "ipvoxdb2", "canal")
        cursor  = self.db.cursor()
        lines   = cursor.execute(query)   
        self.data  = cursor.fetchall()
        #print self.data
        self.db.close()
        return self.data

    def execute_execute_file_from_outband(self, query):
        """
        The query are read from a File and the file
        contain many request separed by  $
        """
        self.db = MySQLdb.connect("10.2.3.2", "ipvoxdb2",
                         "ipvoxdb2", "ipvox_outband")
        sqls    = query.split("$")
        for s in sqls:
            try:
                cursor = self.db.cursor()
                lines  = cursor.execute(s)   
                self.data  = cursor.fetchall()
            except : pass 
        self.db.close()
        #print self.data
        return self.data

    def execute_from_outband(self, query):
        """
        Execute a single query  from ipvox_outband database
        """
        self.db = MySQLdb.connect("10.2.3.2", "ipvoxdb2",
                         "ipvoxdb2", "ipvox_outband")
        cursor  = self.db.cursor()
        lines   = cursor.execute(query)   
        self.data   = cursor.fetchall()
        print self.data
        self.db.close()
        return self.data

    def export(self, file, qs, header, delimiter =';', *args, **kwargs):
      """
      Generate the csv file and save it  with  the given name
      """
      try:
         file =  open(file, 'wb')
         
      except IOError, e:
           raise e
      w = csv.writer(file, dialect = csv.excel,
                         delimiter = delimiter)
      if header:
            w.writerow(header)
      ln  =len(self.data)
      if ln >0:
         for j  in range(ln):              
            print (self.data[j], type(self.data[j]),
                    len(self.data[j]))
            w.writerow(self.data[j])
      file.close()
      return file
   
if __name__ == '__main__':
      test()
