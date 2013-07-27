#!/usr/bin/python
# -*- coding: Utf-8 -*-
import xlwt
import MySQLdb
class BaseExport(object):
    # Pour le moment ces modules sont tres sales et un peu disperses
    #, mais je ne desespere pas de pouvoir trouver un moyen plus 
    # elegant  de reecrire le code , si je toruve le temps necessaire
    # Dans ce module
    # <BaseExport> une classe de base pour l'export xls 
    def __init__ (self, *args, **kwargs):
        pass

    def execute_file(self, query):
        """
        The query are read from a File and the file
        contain sql lines separated by #
        """
        self.db = MySQLdb.connect("10.2.3.2", "ipvoxdb2",
                         "ipvoxdb2", "canal")
        sqls    = query.split("$")
        for s in sqls:
            try:
                cursor = self.db.cursor()
                lines  = cursor.execute(s)   
                self.data = cursor.fetchall()
            except : pass 
        db.close()
        print self.data
        return self.data
    
    def execute(self, query):
        """
        Execute a single query 
        """
        self.db = MySQLdb.connect("10.2.3.2", "ipvoxdb2",
                         "ipvoxdb2", "canal")
        cursor  = self.db.cursor()
        lines   = cursor.execute(query)   
        self.data  = cursor.fetchall()
        print self.data
        self.db.close()
        return self.data

    def execute_execute_file_from_outband(self, query):
        """
        The query are read from a File and the file
        contain many request separed by  $
        """
        self.db = MySQLdb.connect("10.2.3.2", "ipvoxdb2",
                         "ipvoxdb2", "ipvox_outband")
        sqls    = out.split("$")
        for s in sqls:
            try:
                cursor = self.db.cursor()
                lines  = cursor.execute(s)   
                self.data  = cursor.fetchall()
            except : pass 
        self.db.close()
        print self.data
        return self.data
    
    def execute_from_outband(self, query):
        """
        Execute a single query  from canal database
        """
        self.db = MySQLdb.connect("10.2.3.2", "ipvoxdb2",
                         "ipvoxdb2", "ipvox_outband")
        cursor  = self.db.cursor()
        lines   = cursor.execute(query)   
        self.data  = cursor.fetchall()
        print self.data
        self.db.close()
        return self.data

    def export(self, file, qs, header, encoding ='latin-1', *args, **kwargs):       
        """
        Generate the csv file and save it  with  the given name
        """
        print   'self.data', self.data
        nb_rows  = len(self.data)
        self.mydoc = xlwt.Workbook(encoding=  encoding )
        mysheet    = self.mydoc.add_sheet("classique")
        for index, h in enumerate(header) :
            mysheet.write(0, int(index), h)
        if nb_rows > 0:
            nb_cols  = len(self.data[0])
        if nb_rows > 0:
         for nb_row  in range(nb_rows):
             for nb_col in range(nb_cols):
                 mysheet.write(
                     nb_row + 1,
                     int(nb_col),self.data[nb_row][nb_col]
                     if self.data[nb_row][nb_col]
                     else '')
        print "file" , file
        return file

       
