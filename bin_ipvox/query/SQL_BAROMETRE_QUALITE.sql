SELECT    
main_numeroabonne , main_nom , main_prenom, 
Main_GSM 
, Main_TelDom  , Main_TelBur  ,
main_formule ,main_duree ,
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END ,
' ' , main_ville ,
 main_pays  
FROM main_temp
WHERE main_called ='O'
AND main_codefinappel IN ('CPLUS', 'REFUS')
AND COALESCE(main_formule,'')<>''
AND COALESCE(main_duree,'') <>''
AND NOT ( COALESCE(Main_TelDom,'') ='' AND COALESCE(Main_TelBur,'') ='' 
AND  COALESCE(Main_GSM,'') ='' )
AND  STR_TO_DATE( main_dateappel , '%Y-%m-%d')   >=
          STR_TO_DATE(ADDDATE( NOW(), -15) , '%Y-%m-%d')
AND main_pays 
IN ('TOGO')
AND COALESCE(
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END 
, '') <> ''
LIMIT  10 
UNION
SELECT    
main_numeroabonne , main_nom , main_prenom, 
Main_GSM 
, Main_TelDom  , Main_TelBur  ,
main_formule ,main_duree ,
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END ,
' ' , main_ville ,
 main_pays  
FROM main_temp
WHERE main_called ='O'
AND main_codefinappel IN ('CPLUS', 'REFUS')
AND COALESCE(main_formule,'')<>''
AND COALESCE(main_duree,'') <>''
AND NOT ( COALESCE(Main_TelDom,'') ='' AND COALESCE(Main_TelBur,'') ='' 
AND  COALESCE(Main_GSM,'') ='' )
AND  STR_TO_DATE( main_dateappel , '%Y-%m-%d')   >=
          STR_TO_DATE(ADDDATE( NOW(), -15) , '%Y-%m-%d')
AND main_pays 
IN ('MALI')
AND COALESCE(
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END 
, '') <> ''
LIMIT  10 
UNION
SELECT    
main_numeroabonne , main_nom , main_prenom, 
Main_GSM 
, Main_TelDom  , Main_TelBur  ,
main_formule ,main_duree ,
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END ,
' ' , main_ville ,
 main_pays  
FROM main_temp
WHERE main_called ='O'
AND main_codefinappel IN ('CPLUS', 'REFUS')
AND COALESCE(main_formule,'')<>''
AND COALESCE(main_duree,'') <>''
AND NOT ( COALESCE(Main_TelDom,'') ='' AND COALESCE(Main_TelBur,'') ='' 
AND  COALESCE(Main_GSM,'') ='' )
AND  STR_TO_DATE( main_dateappel , '%Y-%m-%d')   >=
          STR_TO_DATE(ADDDATE( NOW(), -15) , '%Y-%m-%d')
AND main_pays 
IN ('BURKINA FASO')
AND COALESCE(
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END 
, '') <> ''
LIMIT  10 
UNION
SELECT    
main_numeroabonne , main_nom , main_prenom, 
Main_GSM 
, Main_TelDom  , Main_TelBur  ,
main_formule ,main_duree ,
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END ,
' ' , main_ville ,
 main_pays  
FROM main_temp
WHERE main_called ='O'
AND main_codefinappel IN ('CPLUS', 'REFUS')
AND COALESCE(main_formule,'')<>''
AND COALESCE(main_duree,'') <>''
AND NOT ( COALESCE(Main_TelDom,'') ='' AND COALESCE(Main_TelBur,'') ='' 
AND  COALESCE(Main_GSM,'') ='' )
AND  STR_TO_DATE( main_dateappel , '%Y-%m-%d')   >=
          STR_TO_DATE(ADDDATE( NOW(), -15) , '%Y-%m-%d')
AND main_pays 
IN ('REP.DEMOCRATIQUE DU CONGO')
AND COALESCE(
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END 
, '') <> ''
LIMIT  10 
UNION

SELECT    
main_numeroabonne , main_nom , main_prenom, 
Main_GSM 
, Main_TelDom  , Main_TelBur  ,
main_formule ,main_duree ,
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END ,
' ' , main_ville ,
 main_pays  
FROM main_temp
WHERE main_called ='O'
AND main_codefinappel IN ('CPLUS', 'REFUS')
AND COALESCE(main_formule,'')<>''
AND COALESCE(main_duree,'') <>''
AND NOT ( COALESCE(Main_TelDom,'') ='' AND COALESCE(Main_TelBur,'') ='' 
AND  COALESCE(Main_GSM,'') ='' )
AND  STR_TO_DATE( main_dateappel , '%Y-%m-%d')   >=
          STR_TO_DATE(ADDDATE( NOW(), -15) , '%Y-%m-%d')
AND main_pays 
IN ('BENIN','BURKINA FASO','CAMEROUN','GHANA','GUINEE',
'GUINEE EQUATORIALE',
'MALI','MAURITANIE','NIGER',
'NIGERIA','REP.CENTRAFRICAINE','SENEGAL','TCHAD','TOGO','BAHREIN',
'CONGO','COTE D IVOIRE','GABON','GUINEE BISSAU',
'REP.DEMOCRATIQUE DU CONGO')
AND COALESCE(
CASE WHEN  main_fichier LIKE '%ECHEANCE%' THEN 'AAE'
     WHEN  main_fichier LIKE '%FRAIS%'   THEN  'EF' 
     WHEN  main_fichier LIKE '%LONGS%'   THEN  'EL' END 
, '') <> ''
LIMIT  333   