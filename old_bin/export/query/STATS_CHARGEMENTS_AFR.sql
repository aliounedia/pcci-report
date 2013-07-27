select main_fichier, Main_Pays,main_datechargment,
sum(case when (main_coderefus ='Répondeur' and main_called ='B') 
 Then 1 else 0 end ) as Repondeur_Bloques,
avg(
 right(left(ltrim(rtrim(Main_tempscom)),5),2)*60 +
 right(ltrim(rtrim(Main_tempscom)),2)
) DMT,  avg(

 right(left(ltrim(rtrim(Main_tempscom_reel)),5),2)*60 +
 right(ltrim(rtrim(Main_tempscom_reel)),2)
) DMC, count(*)  V
from main with(nolock)
where  convert(varchar(10),main_datechargment, 120)= '#'
group by  main_fichier, Main_Pays, main_datechargment

