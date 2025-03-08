class BMW:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        self.engine_started = False

    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            print(f"L moteur de la BMW {self.model} est démarré.")
        else:
            print(f"La BMW {self.model} a déjà démarré.")

    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            print(f"L moteur de la BMW {self.model} est éteint.")
        else:
            print(f"La BMW {self.model} est déjà à l'arrêt.")

    def display_info(self):
        print(f"BMW {self.model} ({self.year}) - Couleur: {self.color}")


# Création d'une instance de BMW
my_bmw = BMW('X5', 'Noir', 2023)

# Affichage des informations de la voiture
my_bmw.display_info()

# Démarrer et arrêter le moteur
my_bmw.start_engine()
my_bmw.stop_engine()
