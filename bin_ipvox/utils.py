import sys
from datetime import datetime
import traceback
def _pprint(lock_out, msg):
    # Pour le moment ces modules sont tres sales et un peu disperses
    #, mais je ne desespere pas de pouvoir trouver un moyen plus 
    # elegant  de reecrire le code , si je toruve le temps necessaire


    # L'approche est basique pour l'instant, chaque module doit en plus 
    # de ce qu'il est sense faire (exemple: un export) , definit 
    # un fonction appelee <target> qui especifie aux module
    # <job_thread_runner.py> a quelle heure de le journee il
    # doit executer ce module


    # Dans cette partie
    # <_pprint> est appele pour ecrire sur la cosole par tous les
    # module avec un lock pour permettre aux autres d'entendre
    # lorsque un module est entrain d'ecrire
    with lock_out:
        print '-'*40
        print >>sys.stdout, datetime.now()
        print >>sys.stdout, msg
        traceback.print_exc()
        print '-'*40
