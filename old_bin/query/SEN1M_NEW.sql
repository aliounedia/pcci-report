Select Main_NumeroAbonne NUMABO,Main_NumeroCarte NUMDEC,case When Main_Civ='1' Then 'MR' 
     When Main_Civ='2' Then 'MM' 
     When Main_Civ='3' Then 'ML' 
     Else Main_Civ End CCIVIL ,Main_Nom NOM,Main_Prenom PRENOM, Main_Formule FORMULE,
Main_DateFinAbonnement FINABO,Main_Duree DUREE,--Right(Main_Tel,9),
 Coalesce(Main_GSM ,'') MOBILE1,
Coalesce(Main_Tel4 ,'')  MOBILE2, Coalesce(Main_TelDom,'') MOBILE3, Coalesce(Main_TelBur ,'')TELEPHONE1,Coalesce(Main_Tel5 ,'') TELEPHONE2,
Coalesce(Main_Email,'')  EMAIL,Coalesce(Main_Adr1,'')  Adr1,Coalesce(Main_Adr2,'')  Adr2,Coalesce(Main_Adr3,'')  Adr3,Coalesce(Main_Ville,'') VILLE,Main_Pays PAYS ,
Case When Coalesce(Main_Q4NSP,'')='' Then Main_Q4Avis Else Main_Q4NSP End As Avis,Main_Q6BouquetAbonnement [Formule Abonnée],Main_Q6DureeAbonnement [Durée Abonnée],Main_Q6DateRV + ' '+ Main_Q6HeureRV [Date RV],Main_Q6Option [Option Choisi],
Case When Coalesce(Main_Nom,'') <> Coalesce(Main_NouvNom,'') Then Coalesce(Main_NouvNom,'') Else '' End As NouvNom,
Case When Coalesce(Main_Prenom,'') <> Coalesce(Main_NouvPrenom,'') Then Coalesce(Main_NouvPrenom,'') Else '' End As NouvPrenom,
Case When Coalesce(Main_Ville,'') <> Coalesce(Main_NouvVille,'') Then Coalesce(Main_NouvVille,'') Else '' End As NouvVille,
Case When Coalesce(Main_Adr1,'') <> Coalesce(Main_NouvAdr1,'') Then Coalesce(Main_NouvAdr1,'') Else '' End As NouvAdresse,
--Case When Coalesce(Main_Adr1,'') <> Coalesce(Main_NouvAdr1,'') Then Coalesce(Main_NouvAdr1,'') Else '' End As NouvAdresse,
Case When (Main_Pays='SENEGAL' And Right(Main_Tel,9)<>Right(Main_NouvTel,9) And Coalesce(Main_NouvTel,'')<>'' ) Then '221'+ Right(Main_NouvTel,9) Else '' End As NouvTel,
Case When (Main_Pays='SENEGAL' And Right(Main_Tel,9)<>Right(Main_NouvGSM,9)And Coalesce(Main_NouvTel,'')<>'') Then '221'+Right(Main_NouvTel,9)
Else '' End As NouvGSM,
Coalesce(Main_NouvBP,'')BP, Case When Coalesce(Main_NouvEmail,'') Like '%@%' Then Main_NouvEmail Else '' End As NouvEmail,
Case When Main_Called in ('O', 'X') Then Convert(Varchar(10),Main_DateAppel,120) Else '' End DateAppel,Main_CodeFinAppel CodeFinAppel, Main_CodeRefus CodeRefus
,Case When Main_Called in ('O', 'X')  Then Main_UserID Else '' End Main_UserID---, Case When  Main_RecG='R' Then 'Réinjectée même tel' When  Main_RecG='O' Then 'Réinjectée avec GSM' Else '' End   
FROM  MAIN_20121201  With(nolock)
Where Main_fichier in  (
'CANAL_OA_ECHUS_FRAIS_SENEGAL_20130201',
'CANAL_OA_ECHUS_FRAIS_SENEGAL_20130301'

)

#

Select [Numero Abonné],Carte,Civilité 
,Coalesce(Nom,'') NOM,Coalesce(Prénom,'') PRENOM,Coalesce(Formule,'') FORMULE , 
Coalesce([Fin abonnement],'') FINABO,[Durée],
Coalesce([Portable 1],'')MOBILE1 ,Coalesce([Portable 2],'') MOBILE2,
Coalesce([Tel bureau],'') MOBILE3,Coalesce([Tel maison 1],'') TELEPHONE1,
Coalesce([Tel maison 2],'') TELEPHONE2,Coalesce(Email,'')Email,
Coalesce(Adresse1,'') Adr1,Coalesce(Adresse2,'') Adr2,
Coalesce(Adresse3,'')Adr3, VILLE,'SENEGAL'
,'','','','','','','','','','','','','', '' , 'DOUBLON'
/*
Select [NUMABO],NUMDEC,CCIVIL 
,Coalesce(Nom,'') NOM,Coalesce(PRENOM,'') PRENOM,Coalesce(BOUQUET,'') FORMULE , 
Coalesce([FINABO],'') FINABO,[DUREE],
Coalesce([MOBILE1],'')MOBILE1 ,Coalesce([MOBILE2],'') MOBILE2,
WORK1 MOBILE3,Coalesce([HOME1],'') TELEPHONE1,
Coalesce([HOME2],'') TELEPHONE2,Coalesce(Email,'')Email,
Coalesce(ADRES1,'') Adr1,Coalesce(ADRES2,'') Adr2,
Coalesce(ADRES3,'')Adr3, COMMUNE,'SENEGAL'
,'','','','','','','','','','','','','', '' , 'DOUBLON'*/
FROM ?
wHERE coalesce (DOUBLON,'') !='' And coalesce (MAIn_Bloquer , '') ='' 

#

Select [Numero Abonné],Carte,Civilité 
,Coalesce(Nom,'') NOM,Coalesce(Prénom,'') PRENOM,Coalesce(Formule,'') FORMULE , 
Coalesce([Fin abonnement],'') FINABO,[Durée],
Coalesce([Portable 1],'')MOBILE1 ,Coalesce([Portable 2],'') MOBILE2,
Coalesce([Tel bureau],'') MOBILE3,Coalesce([Tel maison 1],'') TELEPHONE1,
Coalesce([Tel maison 2],'') TELEPHONE2,Coalesce(Email,'')Email,
Coalesce(Adresse1,'') Adr1,Coalesce(Adresse2,'') Adr2,
Coalesce(Adresse3,'')Adr3, VILLE,'SENEGAL'
,'','','','','','','','','','','','','', '' , 'DOUBLON'
/*
Select [NUMABO],NUMDEC,CCIVIL 
,Coalesce(Nom,'') NOM,Coalesce(PRENOM,'') PRENOM,Coalesce(BOUQUET,'') FORMULE , 
Coalesce([FINABO],'') FINABO,[DUREE],
Coalesce([MOBILE1],'')MOBILE1 ,Coalesce([MOBILE2],'') MOBILE2,
WORK1 MOBILE3,Coalesce([HOME1],'') TELEPHONE1,
Coalesce([HOME2],'') TELEPHONE2,Coalesce(Email,'')Email,
Coalesce(ADRES1,'') Adr1,Coalesce(ADRES2,'') Adr2,
Coalesce(ADRES3,'')Adr3, COMMUNE,'SENEGAL'
,'','','','','','','','','','','','','', '' , 'DOUBLON'*/
FROM ?
wHERE coalesce (MAIn_Bloquer , '') ='B' AND  coalesce (DOUBLON,'') =''
