# -*- coding: latin-1 -*-

# Pour le moment ces modules sont tres sales et un peu disperses
#, mais je ne desespere pas de pouvoir trouver un moyen plus 
# elegant  de reecrire le code , si je toruve le temps necessaire

# Dans ce module
# Un fichier de configuration permettant
# aux module de trouver les requetes et entetes d'export

CONFIG_EXPORT_WELCOME_CALL= {
   'query': open('query/SQL_EXPORT_WELCOME_CALL.sql').read(),
   'file': 'canal_pa_export_welcome_call_',
   'header': ["Abonne",
      "Contrat","Carte", "Civilite", "Nom", "Prenom" , "Formule",
      "Options", "Debut_abo",
      "Fin abo", "Duree",
      "Tel. domicile 1",
      "Tel. domicile 2",
      "Tel. bureau 1" ,
      "Tel. bureau 2",
      "Tel. mobile 1",
      "Tél. mobile 2",
      "Email",
      "Adresse 1",
      "Adresse 2" ,
      "Adresse 3",
      "Ville",
      "Pays",
      "Num distrib",
      "Nom distrib",
      "Tél distrib",
      "[Ancien abonne DSTV]",
      "[R?orientation parabole offerte]",
      "[Nouvelle parabole offerte]",
      "[Bonne reception images]",
      "[Note qualite de service distributeur]",
      "[prix Decodeur]",
      "[Vous avez opte pour la formule LES CHAINES CANAL+ seules,\
              Pourquoi ce choix]",
      "[Quel prix avez-vous paye pour votre formule]",
      "[Qualite de l image]",
      "[Code Fin Appel]",
      "[Code Refus]",
      "[Date Appel]",
      "[Log]"
     ]
}

CONFIG_EXPORT_BAROMETRE_QUALITE= {
   'query': open('query/SQL_BAROMETRE_QUALITE.sql').read(),
   'file': 'canal_pa_export_barometre_qualite_',
   'header': [
       "NUM ABO",
       "NOM",
       "PRENOM",
       "TEL MOBILES",
       "TEL DOMICILE",
       "TEL BUREAU",
       "FORMULE EN COURS",
       "DUREE ABO",
       "MOTIF APPEL SORTANT",
       "ANCIENNETE",
       "VILLE DE RESIDENCE",
       "AYS DE RESIDENCE"
    ]
}

CONFIG_EXPORT_NOTE_DISTRIBUTEUR= {
   'query': open('query/SQL_NOTE_DISTRIBUTEUR.sql').read(),
   'file': 'canal_pa_export_note_distributeur_',
   'header': [
       "Fichier",
       "Pays",
       "Distributeur",
       "QoSDistributeurAgree",
       "FormuleAbonnement",
       "PrestationInstallation"

    ]
}

CONFIG_EXPORT_REPONDEURS_BLOQUES= {
   'query': open('query/SQL_REPONDEURS_BLOQUES.sql').read(),
   'file': 'canal_pa_export_repondeurs_bloques',
   'header': [
       "main_fichier",
       "main_numeroabonne",
       "main_numerocarte",
       "main_tel",
       "main_coderefus"	,
       "main_fichierclient",
       "main_codefinappel",
       "main_coderefus",
       "dateappel"

    ]
}


CONFIG_EXPORT_DEJA_REABONNES= {
   'query': open('query/SQL_DEJA_REABONNES.sql').read(),
   'file': 'canal_pa_export_deja_reabonnes',
   'header': [
       "main_fichier",
       "main_numeroabonne",
       "main_numerocarte",
       "main_tel",
       "main_coderefus"	,
       "main_fichierclient",
       "main_codefinappel",
       "main_coderefus",
       "dateappel"

    ]
}


CONFIG_EXPORT_FX_NUMBERS_AFRIQUE= {
   'query': open('query/SQL_FX_NUMBERS_AFRIQUE.sql').read(),
   'file': 'canal_pa_export_faux_numeros_afrique',
   'header': [
      "num abo"	,"num carte", "num tel"	,"statut",  "fichier"
    ]
}


CONFIG_EXPORT_FX_NUMBERS_SENEGAL= {
   'query': open('query/SQL_FX_NUMBERS_SENEGAL.sql').read(),
   'file': 'canal_pa_export_faux_numeros_senegal',
   'header': [
      "num abo"	,"num carte", "num tel"	,"statut",  "fichier"
    ]
}


CONFIG_EXPORT_APPELS_SUR_AFRIQUE= {
   'query': open('query/SQL_APPELS_SUR_AFRIQUE.sql').read(),
   'file': 'canal_pa_export_appels_sur_afrique',
   'header': [
      "main_fichier",
      "Main_Pays",
      "Main_CodeFinappel",
      "Main_CodeRefus",
      "main_dateappel",
      "Main_TempsCom",
      "Main_TempsCom_Reel",
      "date"

    ]
}

CONFIG_EXPORT_FICHES_CLOTUREES= {
   'query': open('query/SQL_FICHES_CLOTUREES.sql').read(),
   'file': 'canal_pa_export_fiches_cloturees',
   'header': [
    "main_id",
    "main_fichier",
    "main_datechargment",
    "main_codefinappel",
    "main_coderefus",
    "main_called",
    "main_called_old",
    "main_dateappel",
    "STATUS"										

    ]
}
