SELECT Main_NumeroAbonne ,Main_NumeroContrat ,Main_NumeroCarte ,
CASE WHEN Main_Civ='1' THEN 'MR'
     WHEN Main_Civ='2' THEN 'MM'
     WHEN Main_Civ='3' THEN 'ML'
     ELSE Main_Civ END CivilitÚ ,
Main_Nom,Main_Prenom,Main_Formule,Main_Options,Main_DebutAbonnement,Main_DateFinAbonnement,
Main_Duree,
Main_TelDom,Main_Tel5, Main_TelBur,'', Main_GSM,Main_Tel4,Main_Email,
Main_Adr1,Main_Adr2,Main_Adr3,Main_Ville,Main_Pays,
Main_Distributeur,Main_TelDistributeur,Main_CoordonneesDistributeur,
Main_Q5PayerDecodeur  AS Ancien_abonnÚ_DSTV ,
Main_Q5BisPayerParabole AS RÚorientation_parabole_offerte ,
Main_Q6InstallerMateriel AS Nouvelle_parabole_offerte ,
Main_Q6BisBeneficierParabole Bonne_reception_images ,
Main_Q7IndiquerDecodeur   AS Note_qualitÚ_de_service_distributeur,
Main_Q5BisPayerCombien    AS prix_Decodeur,
Main_Q2VerbatimEtreSatisfaitDeCanal,
Main_Q1VerbatimDistributeur,
main_Q8AccederImage,
Main_CodeFinappel AS Code_Fin_Appel,
Main_CodeRefus Code_Refus,
main_dateappel AS Date_Appel ,
Main_userid AS LOG 
FROM main
WHERE
Main_Fichier LIKE '%CANAL_PA_WELCOME_CALL%'
And   STR_TO_DATE( main_dateappel , '%Y-%m-%d')   >=
          STR_TO_DATE(ADDDATE( NOW(), -1) , '%Y-%m-%d')
AND   STR_TO_DATE( main_dateappel , '%Y-%m-%d')   <
            STR_TO_DATE( NOW() , '%Y-%m-%d')