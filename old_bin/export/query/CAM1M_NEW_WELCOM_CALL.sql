select Main_NumeroAbonne ,Main_NumeroContrat ,Main_NumeroCarte ,
Case When Main_Civ='1' Then 'MR' 
     When Main_Civ='2' Then 'MM' 
     When Main_Civ='3' Then 'ML' 
     Else Main_Civ End Civilité ,
Main_Nom,Main_Prenom,Main_Formule,Main_Options,Main_DebutAbonnement,Main_DateFinAbonnement,Main_Duree,
Main_TelDom,Main_Tel5, Main_TelBur,'', Main_GSM,Main_Tel4,Main_Email,
Main_Adr1,Main_Adr2,Main_Adr3,Main_Ville,Main_Pays,
Main_Distributeur,Main_TelDistributeur,Main_CoordonneesDistributeur,
Main_Q5PayerDecodeur [Ancien abonné DSTV], 
--Main_Q5BisPayerCombien [Réorientation parabole offerte] , 
Main_Q5BisPayerParabole [Réorientation parabole offerte] ,  
Main_Q6InstallerMateriel [Nouvelle parabole offerte] ,
Main_Q6BisBeneficierParabole [Bonne reception images] ,
Main_Q7IndiquerDecodeur  [Note qualité de service distributeur],
Main_Q5BisPayerCombien    [prix Decodeur],
Main_Q2VerbatimEtreSatisfaitDeCanal,
Main_Q1VerbatimDistributeur,
main_Q8AccederImage,
Main_CodeFinappel [Code Fin Appel],
Main_CodeRefus [Code Refus], 
convert(varchar(10),main_dateappel,120) [Date Appel] , Main_userid [Log]
from MAIN_20121201
where main_fichier in
(

'CANAL_PA_WELCOME_CALL_20130301',
'CANAL_PA_WELCOME_CALL_20130401'
)


#

Select Abonné,Carte,Civilité,
Coalesce(NOM,'') NOM,Coalesce(PRENOM,'') PRENOM,Coalesce(FORMULE,'') FORMULE,
Coalesce([Fin abo.],'')FIN_ABONNEMENT,
Durée,Coalesce([Tél. domicile 1],'')TEL_MAISON ,Coalesce([Tél. bureau 1],'')TEL_BUREAU,Coalesce([Tél. mobile 1],'')PORTABLE,
Coalesce(EMAIL,'')EMAIL,Coalesce ([Adresse 1],'')ADRES1,Coalesce([Adresse 2],'')ADRES2,Coalesce([Adresse 3],'')ADRES3,
Coalesce(VILLE,'') VILLE,PAYS,
/*
select NUMABO,NUMCARTE,	CCIVIL,	NOM,	PRENOM,	FORMULE,	FINABO,	
DUREE,TELEPHONE1,TELEPHONE2 ,	MOBILE1 ,
EMAIL , ADR1,ADR2, ADR3, VILLE, PAYS,*/
'','','','','','','','','','','','','', '' , 'DOUBLON'
FROM ?
wHERE coalesce (DOUBLON,'') !='' And coalesce (MAIn_Bloquer , '') =''
AND main_fichier ='&'
#


Select Abonné,Carte,Civilité,
Coalesce(NOM,'') NOM,Coalesce(PRENOM,'') PRENOM,Coalesce(FORMULE,'') FORMULE,
Coalesce([Fin abo.],'')FIN_ABONNEMENT,
Durée,Coalesce([Tél. domicile 1],'') TEL_MAISON ,Coalesce([Tél. bureau 1],'')TEL_BUREAU,Coalesce([Tél. mobile 1],'')PORTABLE,
Coalesce(EMAIL,'')EMAIL,Coalesce ([Adresse 1],'')ADRES1,Coalesce([Adresse 2],'')ADRES2,Coalesce([Adresse 3],'')ADRES3,
Coalesce(VILLE,'') VILLE,PAYS,
/*
select NUMABO,NUMCARTE,	CCIVIL,	NOM,	PRENOM,	FORMULE,	FINABO,	
DUREE,TELEPHONE1,TELEPHONE2 ,	MOBILE1 ,
EMAIL , ADR1,ADR2, ADR3, VILLE, PAYS,*/
'','','','','','','','','','','','','', '' , 'INVALIDE'
FROM ?
wHERE coalesce (MAIn_Bloquer , '') ='B' AND  coalesce (DOUBLON,'') =''
AND main_fichier ='&'
