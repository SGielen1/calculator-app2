import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# set the app size
Window.size = (500,700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text='0'

    #create a button pressing function
    def button_press(self, button):
        #create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text
        
        #test for error first
        if "Error" in prior:
            prior = ''

        #determine if 0 is sitting there
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    #create function to remove last function in text box
    def remove(self):
        prior = self.ids.calc_input.text
        #remove last item
        prior = prior[:-1]
        #print result in the text box
        self.ids.calc_input.text = prior
    
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # test to see if there is a substraction sign

        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    #create decimal function
    def dot(self):
        prior = self.ids.calc_input.text

        #split out text box by + 
        num_list = prior.split("+")
    
        if "+" in prior and "." not in num_list[-1]:
            #add a decimal
            prior = f'{prior}.'
            #outpout to textbox
            self.ids.calc_input.text = prior
        elif '.' in prior:
            pass
        else:       
            #add a decimal
            prior = f'{prior}.'
            #outpout to textbox
            self.ids.calc_input.text = prior
    
    #create addition function
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        
        #slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'
    
    #create equals to function
    def equals(self):
        prior = self.ids.calc_input.text
        #error handeling
        try:
            #evaluate the math form the text box
            answer = eval(prior)
            #output the answer
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"

        '''
        #addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            #loop thru our list
            for number in num_list:
                answer = answer + float(number)
            
            #print the answer in the text box
            self.ids.calc_input.text = f'{answer}'
        '''    


class CalculaterApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculaterApp().run()