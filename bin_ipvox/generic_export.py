import xlwt
import pyodbc
import sys
import re
from  os import path
#sys.path.insert ( 0,path.join (
# path.dirname (path.abspath(__file__)), '..','..'))
sys.path.append('../../')
from canal.connection import get_connection


# generic_export.py est un fichier python permettant de generer
# n'importe lequel des segment de Canal Plus
# Juste deux choses a verfier
# 1 . Verfier que on tulise le bon fichier sql
# 2 . Lui passer un bon nom de fichier


import sys
_re   = re.compile ('\?')
_re2  = re.compile ('&')

class Base(object):
    cursor  =  get_connection().cursor()
    def __init__ (self, header, sql):
      self.header=header
      self.sql   =sql
      self.data  =[]
      
    def export(self, main_seg, tmp_tab, *args, **kwargs):
      '''Il sagit ici d'exporter les donnees sachant que
      data n'est pas vide'''
      print  '-'*40
      print main_seg, tmp_tab
      self.prepare_export (
            main_seg,
            tmp_tab,
            *args,
            **kwargs)
      assert  len(self.data) > 0 , 'Les donnees sont vides'
      assert  len(self.header)> 0, 'L entete des colonnes est vide'
      # Va creer l'export 
      book = xlwt.Workbook(encoding='latin-1')
      sheet = book.add_sheet('Sheet1')
      for id,  h in enumerate (self.header):
        sheet.write(0, id , str (h))
      for id, list in enumerate(self.data[0]):
        for id_val,  val in enumerate(list):
            sheet.write(id +1, id_val, str(val))
      book.save('C:\pcci-scripts\zips\%s.xls'%main_seg) 
      self.clean_data()

    def clean_data (self):
       ''''''
       self.data  = []
       
    def _bulk_export (main_seg_list, tmp_tab_list):
     '''
     permet un export groupes , il sagit d'alimenter data en donnees
     et de proceder a l'export des donnees
     '''
     
     for id, (main_seg, tmp_tab) in enumerate(
              zip(main_seg_list, tmp_tab_list)):
         self.export (main_seg, tmp_tab)

    def prepare_export(self, *args , **kwargs):
      '''File to be implemented in the  child classes '''
      raise NotImplementedError
      
class CAM1M(Base):
    '''Exporting data  for CAMEROUN 1M '''
    def  __init__(self):
       '''Initializing data for CAMEROUN 1Mois'''

       
##       header  =list(open('query/SEN1M_header_NEW.sql')\
##               .read().split('#'))
##       sql     =open('query/SEN1M_NEW.sql')\
##               .read()


       
       #header  =list(open('query/CHADEC_header_NEW.sql')\
       #       .read().split('#'))
       #sql     =open('query/CHADEC_NEW.sql')\
       #       .read()

##       header  =list(open('query/CAM1M_header_NEW_WELCOM_CALL.sql')\
##               .read()\
##               .split('#'))
##       
##       sql     =open('query/CAM1M_NEW_WELCOM_CALL.sql')\
##             .read()
           
       header  =list(open('query/CAM1M_header_NEW.sql')\
                .read()\
               .split('#'))

       
       sql     =open('query/CAM1M_NEW.sql')\
              .read()

       
       super(CAM1M , self).__init__(header,sql)

    def prepare_export(self, main_seg, tmp_tab, *args, **kwargs):
      '''Prepare l'export pour CAMEROUN , argument est le nom du segment
      suivit de la table tmporaraire'''
      bits  = self.sql.split('#')
      qs_one , qs_two , qs_three = bits[0] , bits[1] ,bits[2]
      # Donnees a prendre dans la table Main
      qs_one, qs_two ,qs_two  =_re.sub (main_seg , qs_one),\
                                _re.sub(tmp_tab , qs_two),\
                                _re2.sub(main_seg , qs_two)
      
      qs_three=_re.sub(tmp_tab , qs_three)
      qs_three=_re2.sub(main_seg , qs_three)

      
      print   '-'*40
      print   qs_one
      print   '-'*40
      print   qs_two
      print   '-'*40
      print   qs_three
      self.data += [self.cursor.execute(qs_one ).fetchall()
                    #+\
                    #self.cursor.execute(qs_two ).fetchall() +\
                    #self.cursor.execute(qs_three ).fetchall()
                    ]
      assert len(self.data)> 0,(
            'Les donnees de la table main , temporaire sont vides')
                  
    class SEN1M(Base):
        '''
        Export des donnees pour le SENEGAL 1 MOIS ET Classique
        Je te laisse le definir
        '''
        pass

class GENERIC(CAM1M):
    def test(self):
      self.export(
        'CANAL_OA_ARRIVANT_A_ECHEANCE_CAMEROUN_1M_20110731',
        'AAE_CAMEROUN_20110731')

          
if  __name__ =='__main__':
    '''
    --
    python  generic_export.py    CANAL_PA_WELCOME_CALL_GABON_20130401 CANAL_PA_WELCOME_CALL_GABON_20130401
    python  generic_export.py    CANAL_PA_WELCOME_CALL_20130301 CANAL_PA_WELCOME_CALL_20130301
    python  generic_export.py    CANAL_PA_ECHUS_FRAIS_RDC_20130301 CANAL_PA_ECHUS_FRAIS_RDC_20130301
    python  generic_export.py    CANAL_PA_ECHUS_FRAIS_GUINEE_20130301 CANAL_PA_ECHUS_FRAIS_GUINEE_20130301
    python  generic_export.py    CANAL_PA_ECHUS_FRAIS_GABON_20130301 CANAL_PA_ECHUS_FRAIS_GABON_20130301
    python  generic_export.py    CANAL_PA_ECHUS_FRAIS_CONGO_20130301 CANAL_PA_ECHUS_FRAIS_CONGO_20130301
    python  generic_export.py    CANAL_PA_ECHUS_FRAIS_CAMEROUN_20130301 CANAL_PA_ECHUS_FRAIS_CAMEROUN_20130301
    python  generic_export.py    CANAL_PA_ECHUS_FRAIS_BURKINA_20130301 CANAL_PA_ECHUS_FRAIS_BURKINA_20130301
    python  generic_export.py    CANAL_PA_ECHUS_FRAIS_AFR_20130301 CANAL_PA_ECHUS_FRAIS_AFR_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_1MC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_1MC_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_PresGABON_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_PresGABON_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_NIGERIA_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_NIGERIA_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_NIGERIA_1MC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_NIGERIA_1MC_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_GUINEE_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_GUINEE_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_GUINEE_1MC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_GUINEE_1MC_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_GABON_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_GABON_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_GABON_1MC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_GABON_1MC_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_CONGO_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_CONGO_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_CONGO_1MC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_CONGO_1MC_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_CAMEROUN_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_CAMEROUN_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_CAMEROUN_1MC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_CAMEROUN_1MC_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA_1MC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA_1MC_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_AFR_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_AFR_20130301
    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_AFR_1MC_20130301 CANAL_OA_ARRIVANT_A_ECHEANCE_AFR_1MC_20130301

    python  generic_export.py    CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_20130301 CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_20130301
    python  generic_export.py    CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_1M_20130301 CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_1M_20130301
    python  generic_export.py    CANAL_OA_ECHUS_FRAIS_SENEGAL_20130301 CANAL_OA_ECHUS_FRAIS_SENEGAL_20130301

    python  generic_export.py    CANAL_OA_ARRIVANT_A_ECHEANCE_CIV_RELANCE_20130315 CANAL_OA_ARRIVANT_A_ECHEANCE_CIV_RELANCE_20130315
    python  generic_export.py    CANAL_PA_ECHUS_FRAIS_OFFREREABO_20130315 CANAL_PA_ECHUS_FRAIS_OFFREREABO_20130315

    python  generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_EVOLUTION_20130315 CANAL_OA_ARRIVANT_A_ECHEANCE_EVOLUTION_20130315
    python  generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_EVOLUTION_20130315_Bloquer CANAL_OA_ARRIVANT_A_ECHEANCE_EVOLUTION_20130315_Bloquer

    ---

    python  generic_export.py  CANAL_PA_WELCOME_CALL_20130401 CANAL_PA_WELCOME_CALL_20130401
    python  generic_export.py  CANAL_PA_WELCOME_CALL_GABON_20130401 CANAL_PA_WELCOME_CALL_GABON_20130401
    python generic_export.py  CANAL_PA_ECHUS_FRAIS_RDC_20130401 CANAL_PA_ECHUS_FRAIS_RDC_20130401
    ppython generic_export.py  CANAL_PA_ECHUS_FRAIS_GUINEE_20130401 CANAL_PA_ECHUS_FRAIS_GUINEE_20130401
    python generic_export.py  CANAL_PA_ECHUS_FRAIS_GABON_20130401 CANAL_PA_ECHUS_FRAIS_GABON_20130401
    python generic_export.py  CANAL_PA_ECHUS_FRAIS_CONGO_20130401 CANAL_PA_ECHUS_FRAIS_CONGO_20130401
    python generic_export.py   CANAL_PA_ECHUS_FRAIS_CAMEROUN_20130401 CANAL_PA_ECHUS_FRAIS_CAMEROUN_20130401
    python generic_export.py   CANAL_PA_ECHUS_FRAIS_CAMEROUN_20130401 CANAL_PA_ECHUS_FRAIS_CAMEROUN_20130401
    python generic_export.py   CANAL_PA_ECHUS_FRAIS_BURKINA_20130401 CANAL_PA_ECHUS_FRAIS_BURKINA_20130401
    python generic_export.py   CANAL_PA_ECHUS_FRAIS_AFR_20130401 CANAL_PA_ECHUS_FRAIS_AFR_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_AFR_1MC_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_AFR_1MC_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_AFR_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_AFR_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA_1MC_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA_1MC_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_CAMEROUN_1MC_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_CAMEROUN_1MC_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_CAMEROUN_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_CAMEROUN_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_CONGO_1MC_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_CONGO_1MC_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_CONGO_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_CONGO_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_GABON_1MC_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_GABON_1MC_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_GABON_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_GABON_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_GUINEE_1MC_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_GUINEE_1MC_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_GUINEE_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_GUINEE_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_NIGERIA_1MC_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_NIGERIA_1MC_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_NIGERIA_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_NIGERIA_20130401
    python generic_export.py   CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_1MC_20130401 CANAL_OA_ARRIVANT_A_ECHEANCE_RDC_1MC_20130401
    python generic_export.py   CANAL_OA_ECHUS_FRAIS_SENEGAL_20130401 CANAL_OA_ECHUS_FRAIS_SENEGAL_20130401
    python generic_export.py   CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_1M_20130401 CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_1M_20130401
    python generic_export.py   CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_20130401 CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_20130401
    python generic_export.py   CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_20130401 CANAL_PA_ARRIVANT_A_ECHEANCE_SENEGAL_20130401


    python generic_export.py CANAL_PA_ECHUS_FRAIS_OFFREREABO_20130315 CANAL_PA_ECHUS_FRAIS_OFFREREABO_20130315
    python generic_export.py CANAL_OA_ARRIVANT_A_ECHEANCE_EVOLUTION_20130419 CANAL_OA_ARRIVANT_A_ECHEANCE_EVOLUTION_20130419

    '''

   
     
    args  = sys.argv[1:]
    CAM1M ().export(*args)
    
          
