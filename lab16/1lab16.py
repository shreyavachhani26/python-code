from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        # Initialize counter
        self.count = 0
        
        # Layout for vertical arrangement
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Label to display the counter value
        self.label = Label(text=f"Count: {self.count}", font_size='30sp')
        layout.add_widget(self.label)
        
        # Button to increment counter
        btn = Button(text="Increment", size_hint=(1, 0.3), font_size='24sp')
        btn.bind(on_press=self.increment_counter)
        layout.add_widget(btn)
        
        return layout

    def increment_counter(self, instance):
        # Increase counter value
        self.count += 1
        # Update the label text
        self.label.text = f"Count: {self.count}"

if __name__ == '__main__':
    CounterApp().run()
