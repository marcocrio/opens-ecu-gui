import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout



class DataWindow(GridLayout):
    pass

class OpensecuApp(App):
    def build(self):
        return DataWindow()


if __name__ == '__main__':
    app = OpensecuApp()
    app.run()