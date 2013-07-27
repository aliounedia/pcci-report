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
from  old_bin.export.doublons import target as  doublons_target
from  old_bin.export.stats_chargements_afr import target as  stats_chargements_afr
from  old_bin.export.orange_qualif_transverse_confirmation import target as  orange_qualif_transverse_confirmation
from  old_bin.export.orange_qualif_transverse_remerciement import target as  orange_qualif_transverse_remerciement

import time
import threading
lock   =threading.RLock()
targets =[
          (stats_chargements_afr, stats_chargements_afr.__name__)
          ,(doublons_target ,doublons_target.__name__)
          ,(orange_qualif_transverse_remerciement, orange_qualif_transverse_remerciement.__name__)
          ,(orange_qualif_transverse_confirmation , orange_qualif_transverse_confirmation.__name__)
          ]

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

