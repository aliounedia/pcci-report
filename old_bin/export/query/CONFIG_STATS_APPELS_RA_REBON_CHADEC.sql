select dem_id , dem_msisdn, dem_motifdemande, dem_naturedemande
, dem_rebon as  rebon, dem_rebonchadec as chadec from tab_demandes where 
dem_dateappel>='2013-03-01'
and  dem_dateappel < '2013-04-01'
and not ( coalesce(dem_rebon, '') ='' 
and  coalesce(dem_rebonchadec, '') ='')
