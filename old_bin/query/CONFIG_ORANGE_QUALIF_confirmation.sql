--SMS de remerciement tous a ceux qui ont repondu a OUI  a 'E12'et et qui ont un  Mobile.
select case when isnumeric(main_NouvGSM )<> 1 Then main_tel 
else main_NouvGSM end ,Main_EMail , Main_RepModeEnvoiAccepteOffres
from main with(nolock)
where 
(
coalesce(Main_EMail, '') not like '%@%'
and coalesce(Main_RepModeEnvoiAccepteOffres,'') <>''
and main_codefinappel ='CPLUS' 
)
and main_dateappel>=dateadd(day,-1 ,getdate())
and main_dateappel<  getdate()


--and main_dateappel>=dateadd(day,-2 ,getdate())
--and main_dateappel< dateadd(day,-1 ,getdate())
