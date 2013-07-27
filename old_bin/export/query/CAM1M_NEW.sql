select Main_NumeroAbonne ,Main_NumeroContrat ,Main_NumeroCarte ,
Case When Main_Civ='1' Then 'MR' 
     When Main_Civ='2' Then 'MM' 
     When Main_Civ='3' Then 'ML' 
     Else Main_Civ End Civilité ,
Main_Nom,Main_Prenom,Main_Formule,Main_Options,Main_DebutAbonnement,Main_DateFinAbonnement,Main_Duree,
Main_TelDom,Main_Tel5, Main_TelBur,'', Main_GSM,Main_Tel4,Main_Email,
Main_Adr1,Main_Adr2,Main_Adr3,Main_Ville,Main_Pays,
Main_Distributeur,Main_TelDistributeur,Main_CoordonneesDistributeur,
Case When Coalesce(Main_Q4NSP,'')='' Then Main_Q4Avis Else Main_Q4NSP End As Avis,Main_Q6BouquetAbonnement [Formule Abonnée],Main_Q6DureeAbonnement [Durée Abonnée],Main_Q6DateRV + ' '+ Main_Q6HeureRV [Date RV],Main_Q6Option [Option Choisi],
Case When Coalesce(Main_Nom,'') <> Coalesce(Main_NouvNom,'') Then Coalesce(Main_NouvNom,'') Else '' End As NouvNom,
Case When Coalesce(Main_Prenom,'') <> Coalesce(Main_NouvPrenom,'') Then Coalesce(Main_NouvPrenom,'') Else '' End As NouvPrenom,
Case When Coalesce(Main_Ville,'') <> Coalesce(Main_NouvVille,'') Then Coalesce(Main_NouvVille,'') Else '' End As NouvVille,
Case When Coalesce(Main_Adr1,'') <> Coalesce(Main_NouvAdr1,'') Then Coalesce(Main_NouvAdr1,'') Else '' End As NouvAdresse,
Case When (Right(Main_Tel,8)<>Right(Main_NouvTel,8)And Coalesce(Main_NouvTel,'')<>'' ) Then '237'+Right(Main_NouvTel,8) Else '' End As NouvTel,
Case When (Right(Main_GSM,8)<>Right(Main_NouvGSM,8)And Coalesce(Main_NouvGSM,'')<>'') Then '237'+Right(Main_NouvGSM,8) Else '' End As NouvGSM,
Coalesce(Main_NouvBP,'')BP, Case When Coalesce(Main_NouvEmail,'') Like '%@%' Then Main_NouvEmail Else '' End As NouvEmail,Main_Q3SolutionPourRegarderTele,
Case When Main_Called IN ('O','X') Then Convert(Varchar(10),Main_DateAppel,120) Else '' End DateAppel,Main_CodeFinAppel CodeFinAppel, Main_CodeRefus CodeRefus
,Case When Main_Called IN ('O','X') Then Main_UserID Else '' End Main_UserID--,Coalesce(Main_Traite1,'') Traite1 ,Coalesce(Main_Traite2,'') Traite2  ,Coalesce(Main_Traite3,'') Traite3 
FROM  MAIN_20121201  With(nolock)
FROM  Main  With(nolock)
Where Main_fichier in  ( 
'CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA_20130301',
'CANAL_OA_ARRIVANT_A_ECHEANCE_BURKINA__20130401'
)

