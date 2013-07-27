SELECT main_fichier, Main_Pays, Main_CodeFinappel,  
Main_CodeRefus, main_dateappel, Main_TempsCom, Main_TempsCom_Reel
, STR_TO_DATE(main_dateappel, '%Y-%m-%d')
FROM main
WHERE STR_TO_DATE( main_dateappel , '%Y-%m-%d')   >=
          STR_TO_DATE(ADDDATE( NOW(), -1) , '%Y-%m-%d')
AND   STR_TO_DATE( main_dateappel , '%Y-%m-%d')   <
            STR_TO_DATE( NOW() , '%Y-%m-%d')
AND main_codeFinappel IN ('CPLUS', 'REFUS', 
'CAS PARTICULIER', 
'CNADEF', 
'CNANONDEF', 'Indisponible')
AND ( 
main_fichier LIKE '%2013%01%' 
OR main_fichier ='CANAL_OA_ARRIVANT_A_ECHEANCE_PRELEVEMENT_20130307'
OR ( main_fichier ='CANAL_PA_CHADEC_BENIN_20130312' AND  
	main_coderefus NOT IN ('Client en déplacement', 
	'Décés', 'Dialogue impossible (ni FR ni ANG)',
	'Doublon' , 'Injoignables Permanents', 
	'Refus - Pas intéressé', 
	'Refus de répondre- Pas par téléphone',
	'Stop contact téléphonique'))
OR main_fichier ='CANAL_OA_ARRIVANT_A_ECHEANCE_CIV_RELANCE_20130315' 
OR main_fichier ='CANAL_PA_ECHUS_FRAIS_OFFREREABO_20130315'
OR main_fichier ='CANAL_OA_ARRIVANT_A_ECHEANCE_EVOLUTION_20130315'
OR main_fichier ='CANAL_OA_ARRIVANT_A_ECHEANCE_EVOLUTION_20130419'
OR main_fichier ='CANAL_OA_ARRIVANT_A_ECHEANCE_EVOLUTION_20130606'
OR main_fichier ='CANAL_PA_ECHUS_FRAIS_OFFREREABO_20130618'
OR main_fichier ='CANAL_PA_ECHUS_FRAIS_OFFREREABO_20130618'
OR main_fichier ='CANAL_OA_ARRIVANT_A_ECHEANCE_CIV_RELANCE_20130716'
OR main_fichier ='CANAL_PA_MAJ_DECEMBRE_20130626'
OR main_fichier ='CANAL_PA_DSTV_ECHUS_AFR_20130715'
OR main_fichier ='CANAL_PA_MAJ_DECEMBRE_20130723'
)