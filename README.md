
AUTHEUR
===========

Alioune Dia , Derniere modification : 2013-07-26-16:30


DESCRIPTION
===========

ce programme contient l'ensemble des modules qui sont utilises par
moi (Informatique) dans le cadre de la campagne PCCI - CANAL et 
permettant de traiter l'ensemble des exports dont le departement de 
reporting a besion pour traiter avec le client , il inclut des besions
couvrants des exports quotidients , des exports de fin d'exploitation, 
mais egalement des exports mensuels en vu de la facturation .
Je ne le vois pas etre utilse par un autre employe que PCCI , mais je 
prefere le mettre ici au cas ou j'aurai des problemes sur mes 
differentes machine , en vu d'une restauration ou pour un autre 
employer qui serait amener a travailler sur le compte.


EXTENSION
=========

Je l'ai programme de facon a etre generique et que elle puisse servir 
dans le cadre d'autres operations comme TIGO etc, mais pour le moment il ne 
gere que les exports pour CANAL plus pour le departement de reporting 
si quelqu'un souhaite l'utiliser , alors voici comment il devra proceder 


UTILISATION
===========

- Creer une classe heritant de ``BaseExport`` , deux bases exports sont 
disponibles , un pour les formats de Type ``CSV`` , et un autre pour les 
formats de Type ```XLS``.

ie, pour par exemple creer un programme devant exporter un ``CSV`` , il 
devra etre comme suivant:




class MyExport(base_csv_export.BaseExport):

    def __init__(self):

        base_csv_export.BaseExport.__init__(self)

    def chech_export(self):

         pass

    def blabla(self):

        pass

    def va_exporter(self):
        pass


Pour avoir une idee de quelques classes ,vous pouvez par exemple voir des 
classes que j'ai cree dans le dossier ``bin_ipvox``



- Un fois la classe cree , vous devez ensuite cree une petite fonction juste
a la fin de la definition de votre classe , cette fonction porte le nom 
de ``target`` , c'est dans cette que vous devez specifier l'heure , la date 
, et l'intervalle d'execution pour votre classe cree ``MyExport``.
la fonction `target` pourrait par exemple ressembler a ca .


 def target(lock =None , *args):

    from datetime import date

    while True :

        dt =datetime.now()

        if not dt.hour in (5, 6, 7, 4):

            time.sleep(60)

            continue
        try:
            my= MyExport()

            my.va_exporter(config.CONFIG_EXPORT_MyExport)
                    
        except Exception, e:

            time.sleep(3600)



- Enfin une fois que vous avez fin , il ne vous reste qu'a ajouter la 
fonction``target`` dans la liste des modules en execution, pour se faire , 
rien de plus simple, juste ouvir le module  ```job_thread_runner.py ``
qui contient une pile d'execution des differents modules et ajouter votre 
``target`` .par exemple pour ajouter la classe permettant d'exporter
des ``Fiches cloturees`` que vous avez cree dans un fichier appele 
``fiches_clotures.py``  ajouter ces lignes dans ```job_thread_runner.py ``.



from  bin_ipvox.export.fiches_clotures import target \

      as  fiches_clotures_target

targets =[

       (fiches_clotures, fiches_clotures.__name__)
]


- Enfin arreter l'execution de ```job_thread_runner.py `` avec Ctrl + x
puis redemarrer le avec ``python job_thread_runner.py ``


--Ad
        
              

