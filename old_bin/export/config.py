# -*- coding: latin-1 -*-

CONFIG_EXPORT_DOUBLONS= {
             "query":open('query/EXPORT_DOUBLONS.sql','r').read(),
             "file": "DOUBLONS_CAMEROUN",
             "header": [ 'tel' ,'Nom', 'Prenom', 'NumeroAbonne', 'FichierClient', 'Datechargment']
        }


CONFIG_STATS_CHARGEMENTS_AFR= {
             "query":open('query/STATS_CHARGEMENTS_AFR.sql','r').read(),
             "file": "ESTATS_CHARGEMENTS_AFR",
             "header": ['main_fichier', 'Main_Pays', 'main_datechargment', 'Repondeur_Bloques' , 'DMT',	'DMC'	,'V']
             #"header": ['main_fichier', 'Main_Pays', 'V']
        }


CONFIG_ORANGE_QUALIF_confirmation= {
             "query":open('query/CONFIG_ORANGE_QUALIF_confirmation.sql','r').read(),
             "file": "CONFIG_ORANGE_QUALIF_confirmation",
             "header": ['']
        }

CONFIG_ORANGE_QUALIF_remerciement= {
             "query":open('query/CONFIG_ORANGE_QUALIF_remerciement.sql','r').read(),
             "file": "CONFIG_ORANGE_QUALIF_remerciement",
             "header": ['']
        }
