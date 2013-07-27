select  distinct main_id , main_numeroabonne, main_tel, main_fichier, main_codefinappel,
case when  main_codefinappel ='CPLUS' Then
     Main_coderefus 
     else
     Main_Q5PresentationOffre 
end 
from main_appeles  with(nolock) 
where main_dateappel >='2013-03-01'
and  main_dateappel < '2013-04-01'
and
case when  main_codefinappel ='CPLUS' Then
     Main_coderefus 
     else
     Main_Q5PresentationOffre 
end   not in ('Cas Particulier' , 'Entretien abouti' , 'Entretien aboutis' , 'Entretien abouti' ,'Entretiens aboutis', 'Refus', '')
and main_codefinappel in ('CPLUS', 'REFUS')
