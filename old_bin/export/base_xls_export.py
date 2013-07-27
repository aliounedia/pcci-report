#!/usr/bin/python
# -*- coding: Utf-8 -*-
import xlwt
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

    def export(self, file, qs, header, encoding ='latin-1', *args, **kwargs):       
        data = self.cursor.fetchall()
        nb_rows = len(data)
        self.mydoc = xlwt.Workbook(encoding=  encoding )
        mysheet=self.mydoc.add_sheet("classique")
        for index, h in enumerate(header) :
            mysheet.write(0, int(index), h)
        if nb_rows > 0:
            nb_cols  = len(data[0])
        if nb_rows > 0:
         for nb_row  in range(nb_rows):
             for nb_col in range(nb_cols):
                 mysheet.write(
                     nb_row + 1,
                     int(nb_col),data[nb_row][nb_col]
                     if data[nb_row][nb_col]
                     else '')
        return file

       
