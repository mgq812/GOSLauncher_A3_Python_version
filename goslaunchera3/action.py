#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# Module Interface Action

import os
import stat
import sys
import subprocess
from . import vars
from . import language
from . import priority
from . import gos_rsync
from PyQt5.QtCore import Qt

#
#  Action Interface : Liste MODS
#

def selection_tous_mods(self, liste_widget_mods):
    for index in range(liste_widget_mods.count()):
        liste_widget_mods.item(index).setCheckState(Qt.Checked)


def inv_selection_tous_mods(self, liste_widget_mods):
    for index in range(liste_widget_mods.count()):
        if liste_widget_mods.item(index).checkState() == Qt.Checked:
            liste_widget_mods.item(index).setCheckState(Qt.Unchecked)
        else:
            liste_widget_mods.item(index).setCheckState(Qt.Checked)

#
#  Action Interface : OPTIONS
#

def optionModifLangue(self, langue):
    language.change_language(self, langue)

#
# Action Widget Priority
#

def initPriorityTabWidget(self):
    priority.init_priority_tabwidget(self)


#
#  Action Interface : GENERAL
#




def launch_arma3(self):
    newLine = '\n'
    # Linux version
    if vars.OSName() == "linux":
        fichier = open("runArma3", "w")
        fichier.write('cd "' + self.var_Arma3Path + '" ' + newLine)
        fichier.write('./arma3' + ' "-MOD=' + vars.createListeModsLaunch(self) + '" ' + vars.createListeOptions(self))
        fichier.close()
        os.chmod('runArma3', stat.S_IRWXU)
        # TODO: change os.system Obsolete
        os.system('./runArma3')

    # Windows version
    if vars.OSName() == "windows":
        commandLine = '"' + self.var_Arma3Path + '/arma3.exe" "-MOD=' + vars.createListeModsLaunch(
            self) + '" ' + vars.createListeOptions(self)
        #
        print("execution : " + commandLine)
        subprocess.Popen(commandLine)
        
#
#  Action Interface : RSYNC
#
def rsyncTaille(self):
    
    # @TEMPLATE 
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@TEMPLATE","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@TEMPLATE"]
    self.process_TEMPLATE_Taille = gos_rsync.GosRsync(self, "@TEMPLATE",self.label_synchro_template_state, self.progressBar_synchro_template_fichier,self.progressBar_synchro_template_global,self.label_synchro_template_debit,self.pushButton_synchro_template_launch, arguments)
    self.process_TEMPLATE_Taille.getsize()
    # @ISLANDS
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@ISLANDS","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@ISLANDS"]
    self.process_ISLANDS_Taille = gos_rsync.GosRsync(self, "@ISLANDS",self.label_synchro_islands_state, self.progressBar_synchro_islands_fichier,self.progressBar_synchro_islands_global,self.label_synchro_islands_debit,self.pushButton_synchro_islands_launch, arguments)
    self.process_ISLANDS_Taille.getsize()
    # @MATERIEL
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@MATERIEL","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@MATERIEL"]
    self.process_MATERIEL_Taille = gos_rsync.GosRsync(self, "@MATERIEL",self.label_synchro_materiel_state, self.progressBar_synchro_materiel_fichier,self.progressBar_synchro_materiel_global,self.label_synchro_materiel_debit,self.pushButton_synchro_materiel_launch, arguments)
    self.process_MATERIEL_Taille.getsize()
    # @UNITS
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@UNITS","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@UNITS"]
    self.process_UNITS_Taille = gos_rsync.GosRsync(self, "@UNITS",self.label_synchro_units_state, self.progressBar_synchro_units_fichier,self.progressBar_synchro_units_global,self.label_synchro_units_debit,self.pushButton_synchro_units_launch, arguments)
    self.process_UNITS_Taille.getsize()
    # @FRAMEWORK
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@FRAMEWORK","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@FRAMEWORK"]
    self.process_FRAMEWORK_Taille = gos_rsync.GosRsync(self, "@FRAMEWORK",self.label_synchro_framework_state, self.progressBar_synchro_framework_fichier,self.progressBar_synchro_framework_global,self.label_synchro_framework_debit,self.pushButton_synchro_framework_launch, arguments)
    self.process_FRAMEWORK_Taille.getsize()
    # @CLIENT
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@CLIENT","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@CLIENT"]
    self.process_CLIENT_Taille = gos_rsync.GosRsync(self, "@CLIENT",self.label_synchro_client_state, self.progressBar_synchro_client_fichier,self.progressBar_synchro_client_global,self.label_synchro_client_debit,self.pushButton_synchro_client_launch, arguments)
    self.process_CLIENT_Taille.getsize()
    # @TEST
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@TEST","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@TEST"]
    self.process_TEST_Taille = gos_rsync.GosRsync(self, "@TEST",self.label_synchro_test_state, self.progressBar_synchro_test_fichier,self.progressBar_synchro_test_global,self.label_synchro_test_debit,self.pushButton_synchro_test_launch, arguments)
    self.process_TEST_Taille.getsize()
    # @INTERCLAN
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@INTERCLAN","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@INTERCLAN"]
    self.process_INTERCLAN_Taille = gos_rsync.GosRsync(self, "@INTERCLAN",self.label_synchro_interclan_state, self.progressBar_synchro_interclan_fichier,self.progressBar_synchro_interclan_global,self.label_synchro_interclan_debit,self.pushButton_synchro_interclan_launch, arguments)
    self.process_INTERCLAN_Taille.getsize()
    # @GENERAL
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@GOS","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS"]
    self.process_GENERAL_Taille = gos_rsync.GosRsync(self, "@GOS",self.label_info_synchro_taille, None,None,None,None, arguments)
    self.process_GENERAL_Taille.getsize()

     
def rsyncGos(self, syncname, label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton):
    arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::"+syncname,"cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/"+syncname]
    if pushbutton.text()=="Lancer" or syncname=='@GENERALE':
        if syncname=='@TEMPLATE':
            self.process_TEMPLATE = gos_rsync.GosRsync(self, syncname, label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton, arguments)
            self.process_TEMPLATE.start()
        elif syncname=='@ISLANDS':
            self.process_ISLANDS = gos_rsync.GosRsync(self, syncname, label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton, arguments)
            self.process_ISLANDS.start()
        elif syncname=='@MATERIEL':
            self.process_MATERIEL = gos_rsync.GosRsync(self, syncname, label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton, arguments)
            self.process_MATERIEL.start()
        elif syncname=='@UNITS':
            self.process_UNITS = gos_rsync.GosRsync(self, syncname, label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton, arguments)
            self.process_UNITS.start()
        elif syncname=='@FRAMEWORK':
            self.process_FRAMEWORK = gos_rsync.GosRsync(self, syncname, label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton, arguments)
            self.process_FRAMEWORK.start()
        elif syncname=='@CLIENT':
            self.process_CLIENT = gos_rsync.GosRsync(self, syncname, label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton, arguments)
            self.process_CLIENT.start()
        elif syncname=='@TEST':
            self.process_TEST = gos_rsync.GosRsync(self, syncname, label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton, arguments)
            self.process_TEST.start()
        elif syncname=='@INTERCLAN':
            self.process_INTERCLAN = gos_rsync.GosRsync(self, syncname, label_state, progressbar_fichier,progressbar_global, label_debit, pushbutton, arguments)
            self.process_INTERCLAN.start() 
        elif syncname=='@GENERALE':
            # @TEMPLATE
            arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@TEMPLATE","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@TEMPLATE"]
            self.process_TEMPLATE = gos_rsync.GosRsync(self, "@TEMPLATE",self.label_synchro_template_state, self.progressBar_synchro_template_fichier,self.progressBar_synchro_template_global,self.label_synchro_template_debit,self.pushButton_synchro_template_launch, arguments)
            self.process_TEMPLATE.start() 
            # @ISLANDS
            arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@ISLANDS","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@ISLANDS"]
            self.process_ISLANDS = gos_rsync.GosRsync(self, "@ISLANDS",self.label_synchro_islands_state, self.progressBar_synchro_islands_fichier,self.progressBar_synchro_islands_global,self.label_synchro_islands_debit,self.pushButton_synchro_islands_launch, arguments)
            self.process_ISLANDS.start() 
            # @MATERIEL
            arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@MATERIEL","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@MATERIEL"]
            self.process_MATERIEL = gos_rsync.GosRsync(self, "@MATERIEL",self.label_synchro_materiel_state, self.progressBar_synchro_materiel_fichier,self.progressBar_synchro_materiel_global,self.label_synchro_materiel_debit,self.pushButton_synchro_materiel_launch, arguments)
            self.process_MATERIEL.start()
            # @UNITS
            arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@UNITS","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@UNITS"]
            self.process_UNITS = gos_rsync.GosRsync(self, "@UNITS",self.label_synchro_units_state, self.progressBar_synchro_units_fichier,self.progressBar_synchro_units_global,self.label_synchro_units_debit,self.pushButton_synchro_units_launch, arguments)
            self.process_UNITS.start()
            # @FRAMEWORK
            arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@FRAMEWORK","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@FRAMEWORK"]
            self.process_FRAMEWORK = gos_rsync.GosRsync(self, "@FRAMEWORK",self.label_synchro_framework_state, self.progressBar_synchro_framework_fichier,self.progressBar_synchro_framework_global,self.label_synchro_framework_debit,self.pushButton_synchro_framework_launch, arguments)
            self.process_FRAMEWORK.start()
            # @CLIENT
            arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@CLIENT","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@CLIENT"]
            self.process_CLIENT = gos_rsync.GosRsync(self, "@CLIENT",self.label_synchro_client_state, self.progressBar_synchro_client_fichier,self.progressBar_synchro_client_global,self.label_synchro_client_debit,self.pushButton_synchro_client_launch, arguments)
            self.process_CLIENT.start()
            # @TEST
            arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@TEST","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@TEST"]
            self.process_TEST = gos_rsync.GosRsync(self, "@TEST",self.label_synchro_test_state, self.progressBar_synchro_test_fichier,self.progressBar_synchro_test_global,self.label_synchro_test_debit,self.pushButton_synchro_test_launch, arguments)
            self.process_TEST.start()
            # @INTERCLAN
            arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@INTERCLAN","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS/@INTERCLAN"]
            self.process_INTERCLAN = gos_rsync.GosRsync(self, "@INTERCLAN",self.label_synchro_interclan_state, self.progressBar_synchro_interclan_fichier,self.progressBar_synchro_interclan_global,self.label_synchro_interclan_debit,self.pushButton_synchro_interclan_launch, arguments)
            self.process_INTERCLAN.start()
            # @GENERALE
            #arguments = ["--exclude '@TEST'"," --exclude '@CLIENT'","--exclude '@FRAMEWORK'","--exclude '@INTERCLAN'","--exclude '@ISLANDS'","--exclude '@MATERIEL'","--exclude '@TEMPLATE'","--exclude '@UNITS'","--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@GOS","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS"]
            arguments = ["--partial", "--inplace","--progress","--delete-after", "--bwlimit=0", "--chmod=ugo=rwX","www.clan-gos.fr::@GOS","cygdrive/G/JEUX/steamapps/common/Arma 3/@GOS"]
            self.process_GENERALE = gos_rsync.GosRsync(self, "@GOS",self.label_info_synchro_taille, None,None,None,None, arguments)
            self.process_GENERALE.start()
            
    else:
        if syncname=='@TEMPLATE':
            self.process_TEMPLATE.killProcess()
        elif syncname=='@ISLANDS':
            self.process_ISLANDS.killProcess()
        elif syncname=='@MATERIEL':
            self.process_MATERIEL.killProcess()
        elif syncname=='@UNITS':
            self.process_UNITS.killProcess()
        elif syncname=='@FRAMEWORK':
            self.process_FRAMEWORK.killProcess()
        elif syncname=='@CLIENT':
            self.process_CLIENT.killProcess()
        elif syncname=='@TEST':
            self.process_TEST.killProcess()
        elif syncname=='@INTERCLAN':
            self.process_INTERCLAN.killProcess()      
    
################################################################

if __name__ == "__main__":
    # execute when run directly, but not when called as a module.
    # therefore this section allows for testing this module!

    # print "running directly, not as a module!"

    sys.exit()
