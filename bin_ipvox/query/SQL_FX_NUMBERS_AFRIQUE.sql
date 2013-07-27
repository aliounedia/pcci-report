SELECT main_numeroabonne,
main_numerocarte , 
main_tel , 
main_coderefus    , 
main_fichierclient ,
STR_TO_DATE(main_dateappel , '%Y-%m-%d')
FROM main  
WHERE  main_codefinappel IN ('CNADEF', 'CPLUS', 'REFUS','CAS PARTICULIER')
And   STR_TO_DATE( main_dateappel , '%Y-%m-%d')   >=
          STR_TO_DATE(ADDDATE( NOW(), -1) , '%Y-%m-%d')
AND   STR_TO_DATE( main_dateappel , '%Y-%m-%d')   <
            STR_TO_DATE( NOW() , '%Y-%m-%d')
AND main_fichier<> ''
AND main_fichierclient<> ''
AND main_fichierclient LIKE '%AFR%'