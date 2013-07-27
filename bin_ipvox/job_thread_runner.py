"""
jobs thread, permet de bouffer tous le modules
dans des processus separes.Lorsque ca run ,un
travaille enorme se fait en background(des exports,
des archivages, des transferts entre db)
les modules gerent  leurs ''target'' et ce module manage tout
"""

__author__ ='Alioune Dia'
__version__ = "0.1"

from sys import path
from os.path import dirname, join
import sys
path.append(join(dirname(__file__),'..'))

from  bin_ipvox.export.barometre_qualite import target \
      as  barometre_qualite_target

from  bin_ipvox.export.welcome_call import target \
      as  welcome_call_target

from  bin_ipvox.export.appels_sur_afrique import target \
      as  appels_sur_afrique_target

from  bin_ipvox.export.note_distributeur import target \
      as  note_distributeur_target

from  bin_ipvox.export.fx_number_senegal import target \
      as  fx_number_senegal_target

from  bin_ipvox.export.fx_number_afrique import target \
      as  fx_number_afrique_target

from  bin_ipvox.export.deja_reabonnes import target \
      as  deja_reabonnes_target


from  bin_ipvox.export.repondeurs_bloques import target \
      as  repondeurs_bloques_target

from  bin_ipvox.export.fiches_clotures import target \
      as  fiches_clotures_target

import time
import threading
lock   =threading.RLock()
targets =[
       (welcome_call_target, welcome_call_target.__name__),
       (barometre_qualite_target, barometre_qualite_target.__name__),
       (appels_sur_afrique_target, appels_sur_afrique_target.__name__),
       (note_distributeur_target, note_distributeur_target.__name__),
       (fx_number_senegal_target, fx_number_senegal_target.__name__),
       (fx_number_afrique_target, fx_number_afrique_target.__name__),
       (deja_reabonnes_target, deja_reabonnes_target.__name__),
       (repondeurs_bloques_target, repondeurs_bloques_target.__name__),
       (fiches_clotures_target, fiches_clotures_target.__name__)
       
          ]
##targets = [
## (fiches_clotures_target, fiches_clotures_target.__name__)
##    ]
def run():
    ''' This script is executed from prompt and
    then all job will be run.I you need to add new job, you  need to define
    your module with a target loop and add them here.
    Ce script doit etre execute depuis la console pour demarrer tous
    les travaux en backround , si vous voulez ajouter un nouveau job,
    (par exeemple un script ftp copie) , vous definissez  votre module
    puis le target function a l'ajouter ici)'''

    # Ajouter tous les targets (loops)
    threads =[ (threading.Thread(
                    target =func,
                    name =str(name),
                    args =(lock,)
                ),name)
               for func, name in targets
             ]
    # chaque target est exectute de facon autonome
    # pour eviter les problemes sequenctiels
    for  _ , (t, name) in enumerate(threads):
        t.deamon =True
        #print >> sys.stdout, 'Starting %s Thread'%name
        time.sleep(10)
        t.start()


    while True:
        print >> sys.stdout, 'WAIT into Main '
        try:
            time.sleep(10)
        except KeyboardInterrupt, e:
            # Le script est arrete, il faut arreter tous les
            # threads qui sont entrain de tourner
            break

    for _, (t ,name) in enumerate(threads):
        print >> sys.stdout,'Stopped %s Thread'%name
        time.sleep(10)
        t._Thread__stopped=True

        print >> sys.stdout, 'All treads are stopped'


if __name__ =='__main__':
    print >> sys.stdout, '*'*40
    run()

