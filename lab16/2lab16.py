from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        # Main vertical layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Text field for user input
        self.input_box = TextInput(
            hint_text="Type something...",
            multiline=False,
            size_hint=(1, 0.3)
        )
        layout.add_widget(self.input_box)
        
        # Button to display the text
        button = Button(
            text="Show Text",
            size_hint=(1, 0.2),
            font_size='20sp'
        )
        button.bind(on_press=self.display_text)
        layout.add_widget(button)
        
        # Label to show the result
        self.output_label = Label(
            text="",
            font_size='22sp'
        )
        layout.add_widget(self.output_label)
        
        return layout

    def display_text(self, instance):
        # Fetch text from input
        typed_text = self.input_box.text
        # Update label
        self.output_label.text = f"You typed: {typed_text}"

if __name__ == '__main__':
    TextInputApp().run()
