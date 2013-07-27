SELECT main_fichier, 
main_numeroabonne,
main_numerocarte , 
main_tel   , 
main_coderefus    , 
main_fichierclient ,
main_codefinappel,
main_coderefus ,
STR_TO_DATE(main_dateappel , '%Y-%m-%d') AS dateappel
FROM main  
-- WHERE  main_codefinappel IN ('CNADEF', 'CPLUS', 'REFUS','CAS PARTICULIER')
WHERE  main_fichier LIKE '%2013%07%01%'
AND Main_called ='B'