select  Main_tel, Main_Nom, Main_Prenom, 
Main_NumeroAbonne, 
Main_FichierClient, Main_Datechargment
from main_bloquer
where main_datechargment = convert(varchar(10), getdate(), 120)
and  main_pays  ='CAMEROUN'
