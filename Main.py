import pygame
import sys
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, K_SPACE

from Gyroscope import Gyroscope
from Simulation import Simulation


class Main:
    def __init__(self):
        # Initialize the gyroscope
        self.clock = pygame.time.Clock()
        self.gyro = Gyroscope()
        # Initialize the simulation
        self.simulation = Simulation()

    def run(self):
        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # delay
            self.clock.tick(500)
            # Get sensor data
            sensor_data = self.gyro.get_sensor_data()
            # Send sensor data over the network (optional)
            self.gyro.send_data(sensor_data)
            # Update the simulation with new sensor data
            self.simulation.update(sensor_data)
            # Delay to limit the update rate
            pygame.time.delay(10)

if __name__ == "__main__":
    main = Main()
    main.run()