from controller import Controller
from model import Model
from viewer import Viewer

class Main:
    def __init__(self):
        # Initialize the model and the controller
        self.model = Model()
        self.controller = Controller(self.model)

        # Initialize the viewer with the controller and the model
        self.viewer = Viewer(self.controller, self.model)

    def run(self):
        # Run the viewer
        self.viewer.run()

if __name__ == "__main__":
    # Create and run the main class
    main = Main()
    main.run()