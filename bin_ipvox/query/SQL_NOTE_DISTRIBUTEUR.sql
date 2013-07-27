SELECT Main_fichier ,Main_Pays,Main_CoordonneesDistributeur,

                SUM(
                        CONVERT(
                        (CASE WHEN
                                CONVERT(Main_Q7IndiquerDecodeur, SIGNED INTEGER)
 IS NOT NULL   THEN
                                CASE    WHEN Main_Q7IndiquerDecodeur LIKE '%.%'
OR Main_Q7IndiquerDecodeur LIKE '%,%' THEN LEFT(Main_Q7IndiquerDecodeur,1)
                                ELSE Main_Q7IndiquerDecodeur
                                END
                        ELSE 0 END) ,
                        UNSIGNED INTEGER
                        )
                )/COUNT(*)  AS  QoSDistributeurAgree

, SUM(
        CONVERT(
        (CASE WHEN
        CONVERT(Main_Q3FormuleAbonnement, SIGNED INTEGER)IS NOT NULL
        THEN Main_Q3FormuleAbonnement ELSE 0 END),
        UNSIGNED INTEGER)
 )/COUNT(*)  AS FormuleAbonnement
 ,
 SUM(
        CONVERT(
                (CASE WHEN Main_Q3PrestationInstallation=1 THEN
        Main_Q3PrestationInstallation ELSE 0 END),
        UNSIGNED INTEGER)
   )/COUNT(*)  AS PrestationInstallation, 
STR_TO_DATE(main_dateappel, '%Y-%m-%d')
FROM main
WHERE Main_CodeFinAppel='CPLUS'
And   STR_TO_DATE( main_dateappel , '%Y-%m-%d')   >=
          STR_TO_DATE(ADDDATE( NOW(), -1) , '%Y-%m-%d')
AND   STR_TO_DATE( main_dateappel , '%Y-%m-%d')   <
            STR_TO_DATE( NOW() , '%Y-%m-%d')
AND Main_Q7IndiquerDecodeur<> '.'
AND Main_Q7IndiquerDecodeur NOT LIKE '%nsp%'
AND Main_Fichier LIKE '%WELCOME%'
GROUP BY Main_fichier,Main_Pays,Main_CoordonneesDistributeur, 
STR_TO_DATE(main_dateappel, '%Y-%m-%d')