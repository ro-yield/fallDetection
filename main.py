from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import gyroscope

class GyroApp(App):
    def build(self):
        self.label = Label(text="Gyroscope data will appear here", font_size='20sp')
        Clock.schedule_interval(self.update, 1.0 / 10.0)  # Update every 0.1 seconds
        return self.label

    def update(self, dt):
        try:
            gyro_data = gyroscope.orientation
            if gyro_data:
                self.label.text = f"Gyroscope data:\nX: {gyro_data[0]}\nY: {gyro_data[1]}\nZ: {gyro_data[2]}"
            else:
                self.label.text = "No gyroscope data available"
        except NotImplementedError:
            self.label.text = "Gyroscope not implemented on this platform"

if __name__ == '__main__':
    GyroApp().run()
