"""
Fichier principal du jeu Scattergories

Tous droits réservés

Adaption par Arnaud Lapierre
Pour utilisation personnelle seulement
"""

import sys
import json
from app_window import Ui_Scattergories
from PyQt6 import QtCore, QtGui, QtWidgets
from jeu_scattergories import coup_de_dé


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_Scattergories()
        self.ui.setupUi(self)

        # Customization de la fenêtre
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # liste question
        # Settings pour l'affichage des cartes. Carte #1 affichée par défaut à lorsque le script est lancé.
        self.ui.questions_suiv.clicked.connect(self.carte_suivante_bouton)
        self.ui.questions_prec.clicked.connect(self.carte_precedente_bouton)
        self.num_carte = 1
        self.afficher_questions()

        # timer
        self.timer = QtCore.QTimer()
        self.timer.start(1000)

        # la commande «afficher_temps» permet de contrôler l'état des boutons à t=0
        self.timer.timeout.connect(self.afficher_temps)
        self.ui.pushButton_start.clicked.connect(self.lancer_de)
        self.ui.pushButton_stop.clicked.connect(self.stop_bouton)
        self.ui.pushButton_pause.clicked.connect(self.pause_bouton)

        self.minutes_restantes = 0
        self.secondes_restantes = 0
        self.lettre_finale = "A"
        self.pause = False


    def afficher_questions(self):

        with open("Questions_Scattergories.json", ) as fich:
            data = json.load(fich)

        # convertir le numéro de la carte où on est rendu en str
        num_carte_str = str(self.num_carte)

        # ajout du numéro de la carte en bold centré
        numero_de_la_carte = QtWidgets.QLabel(f"{num_carte_str}")
        self.ui.formLayout.addWidget(numero_de_la_carte)
        myFont = QtGui.QFont("Times", 25)
        myFont.setBold(True)
        numero_de_la_carte.setFont(myFont)
        numero_de_la_carte.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # ajout des questions
        for i, j in enumerate(data[num_carte_str]):
            numero = QtWidgets.QLabel(f"{i + 1}. {j}")
            self.ui.formLayout.addWidget(numero)
            numero.setFont(QtGui.QFont("Times", 19))

    def carte_suivante(self):
        if self.num_carte == 12:
            self.num_carte = 1
        else:
            self.num_carte += 1

    def carte_precedente(self):
        if self.num_carte == 1:
            self.num_carte = 12
        else:
            self.num_carte = self.num_carte - 1

    def carte_suivante_bouton(self):
        for i in reversed(range(self.ui.formLayout.count())):
            widgetToRemove = self.ui.formLayout.itemAt(i).widget()
            # remove it from the layout list
            self.ui.formLayout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

        self.carte_suivante()
        self.afficher_questions()

    def carte_precedente_bouton(self):
        for i in reversed(range(self.ui.formLayout.count())):
            widgetToRemove = self.ui.formLayout.itemAt(i).widget()
            # remove it from the layout list
            self.ui.formLayout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

        self.carte_precedente()
        self.afficher_questions()

    # Timer
    def start_countdown(self):

        # initialisation des variables secondes (int), minutes (int), temps (datetime)
        self.minutes_restantes = self.ui.timer.time().minute()
        self.secondes_restantes = self.ui.timer.time().second()

        # État des boutons au Temps 0
        self.ui.pushButton_start.setEnabled(False)
        self.ui.pushButton_pause.setEnabled(True)
        self.ui.pushButton_stop.setEnabled(True)
        self.ui.questions_suiv.setEnabled(False)
        self.ui.questions_prec.setEnabled(False)

    def afficher_temps(self):

        if self.minutes_restantes == 0 and self.secondes_restantes == 0:
            self.partie_terminee()

        else:
            if self.secondes_restantes == 0 and self.minutes_restantes != 0:
                self.minutes_restantes -= 1
                self.secondes_restantes = 59
                temps = QtCore.QTime(0, self.minutes_restantes, self.secondes_restantes)
                time_string = temps.toPyTime().strftime("%M:%S")
                self.ui.label_2.setText(time_string)
            else:
                self.secondes_restantes -= 1
                temps = QtCore.QTime(0, self.minutes_restantes, self.secondes_restantes)
                time_string = temps.toPyTime().strftime("%M:%S")
                self.ui.label_2.setText(time_string)

    def partie_terminee(self):
        self.ui.label_2.setText("00:00")
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_pause.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.questions_suiv.setEnabled(True)
        self.ui.questions_prec.setEnabled(True)

    def stop_bouton(self):
        self.minutes_restantes = 0
        self.secondes_restantes = 0
        self.partie_terminee()

    def pause_bouton(self):
        if self.pause is True:
            self.timer.start(1000)
            self.ui.pushButton_pause.setText("Pause")
            self.pause = False
        else:
            self.pause = True
            self.ui.pushButton_pause.setText("Continuer")
            self.timer.stop()

    # Lancement du dé
    def lancer_de(self):
        self.timer_de = QtCore.QTimer()
        self.timer_de_singleshot = QtCore.QTimer()
        self.timer_de.start(100)
        self.timer_de_singleshot.singleShot(2000, self.commencer_partie)
        self.timer_de.timeout.connect(self.choix_lettre)

    def choix_lettre(self):
        self.ui.lettre.setText(coup_de_dé())

    def choix_lettre_finale(self):
        self.lettre_finale = coup_de_dé()
        self.ui.lettre.setText(self.lettre_finale)

    def commencer_partie(self):
        self.timer_dé.stop()
        self.start_countdown()
        self.choix_lettre_finale()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("windowsvista")
    w = MyWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
