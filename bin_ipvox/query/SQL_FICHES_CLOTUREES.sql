

DROP TABLE canal.main_temp3

$

CREATE TABLE canal.main_temp3(
-- select main_datechargment , main_fichier from main_temp 
SELECT  * FROM canal.main
WHERE 
CASE WHEN main_fichier LIKE '%ECHEANCE%1MC%2013%01%'  
	  THEN  STR_TO_DATE(main_datechargment,'%Y-%m-%d') 
 			<=STR_TO_DATE( ADDDATE( NOW(), -6) , '%Y-%m-%d')
    WHEN main_fichier LIKE '%FRAIS%2013%01%'  
	  THEN  STR_TO_DATE(main_datechargment,'%Y-%m-%d') 
			<=STR_TO_DATE( ADDDATE( NOW(), -7) , '%Y-%m-%d')
    WHEN main_fichier LIKE '%ECHEANCE%2013%01%' AND main_fichier NOT LIKE '%1MC%'  
          THEN  STR_TO_DATE(main_datechargment,'%Y-%m-%d')
			<=STR_TO_DATE( ADDDATE( NOW(), -15) , '%Y-%m-%d')
    WHEN main_fichier IN ('CANAL_PA_ECHUS_FRAIS_OFFREREABO_20130618', 
	'CANAL_PA_MAJ_DECEMBRE_20130723') 
	  THEN main_fichier IN ('CANAL_PA_ECHUS_FRAIS_OFFREREABO_20130618', 
	'CANAL_PA_MAJ_DECEMBRE_20130723') 
   END
-- order by main_datechargment , main_fichier
) 


$

DROP TABLE archives_appel_new_format_archive_temp

$

CREATE TABLE archives_appel_new_format_archive_temp (
	SELECT MAX(call_time) AS call_time ,main_id
	FROM archives_appel_new_format_archive
	WHERE COALESCE(STATUS, '')<> ''
	GROUP BY   main_id
)  

$

ALTER TABLE archives_appel_new_format_archive_temp ADD STATUS VARCHAR(50)
$
ALTER TABLE canal.main_temp3 ADD STATUS VARCHAR(50)


$
ALTER TABLE `archives_appel_new_format_archive_temp` ADD INDEX `main_id` (`main_id`)

$
ALTER TABLE canal.main_temp3  ADD INDEX `main_id` (`main_id`)
$

UPDATE archives_appel_new_format_archive_temp a2 ,
archives_appel_new_format_archive   a1
SET a2.status =a1.status 
WHERE a1.main_id = a2.main_id 
AND  a1.call_time = a2.call_time


$


UPDATE archives_appel_new_format_archive_temp a2 ,
canal.main_temp3   m
SET m.status =a2.status 
WHERE m.main_id = a2.main_id  

$

UPDATE canal.main_temp3
SET STATUS ='HUMAN'
WHERE  main_codefinappel IN 
 ('CPLUS', 'REFUS', 'CAS PARTICULIER')  
 
 
$

UPDATE canal.main_temp3
SET STATUS ='MACHIN'
 WHERE  main_codefinappel  NOT IN 
 ('CPLUS', 'REFUS', 'CAS PARTICULIER')
AND COALESCE(STATUS, '')=''
AND main_fichier LIKE '%20130%01%' 

 
$

 
 SELECT main_id, main_fichier, main_datechargment , main_codefinappel, main_coderefus, 
	main_called, main_called_old, main_dateappel, status
 FROM canal.main_temp3
 WHERE  COALESCE(main_called, '')<> 'B'  