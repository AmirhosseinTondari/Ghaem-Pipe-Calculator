from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from func import *


# from kivy.core.window import Window
# Window.size = (350, 600)

class trunk(Widget):

    def btn(self):
        if any([self.t.text == "", self.w.text == "", self.d.text == "", self.l.text == "",
                self.coef.text == ""]) or self.mat.text == 'Choose':
            content = Button(text='OK', size_hint=(0.8, 0.9), pos_hint={"center_x": 0.5, "center_y": 0.5})
            popup = Popup(title='Some inputs are missing!!', content=content, auto_dismiss=False, size_hint=(.7, .2))

            content.bind(on_press=popup.dismiss)

            popup.open()
        else:
            mat = self.mat.text

            s = float(self.coef.text)

            t = float(self.t.text)
            if self.ut_t_inch.state == 'down':
                t = t / 0.0393701
            else:
                self.ut_t_mm.state = 'down'

            w = float(self.w.text)
            if self.ut_w_inch.state == 'down':
                w = w / 0.0393701
            else:
                self.ut_w_mm.state = 'down'

            d = float(self.d.text)
            if self.ut_d_inch.state == 'down':
                d = d / 0.0393701
            else:
                self.ut_d_mm.state = 'down'

            l = float(self.l.text)
            if self.ut_l_feet.state == 'down':
                l = l / 3.28084
            else:
                self.ut_l_m.state = 'down'

            if self.unit_type_test_pressure_psi.state == 'down':
                tp_u = 'psi'
            else:
                tp_u = 'bar'
                self.unit_type_test_pressure_bar.state = 'down'
            if self.unit_type_pipe_weight_lb.state == 'down':
                pw_u = 'lb'
            else:
                pw_u = 'kg'
                self.unit_type_pipe_weight_kg.state = 'down'
            if self.unit_type_spiral_length_feet.state == 'down':
                sl_u = 'feet'
            else:
                sl_u = 'm'
                self.unit_type_spiral_length_m.state = 'down'
            if self.unit_type_spiral_ang_RAD.state == 'down':
                sa_u = 'rad'
            else:
                sa_u = 'deg'
                self.unit_type_spiral_ang_DEG.state = 'down'

            #######debug
            # self.test_pressure.text, self.debug_u.text = tesPressure(t=t, s=s,d=d, mat=mat, unitType=tp_u)
            #######
            self.test_pressure.text, self.debug_u.text = tesPressure(t=t, s=s, d=d, mat=mat, unitType=tp_u)
            self.pipe_weight.text = pipeWeight(t=t, d=d, l=l, unitType=pw_u)
            self.spiral_length.text = spiralLength(t=t, d=d, l=l, w=w, unitType=sl_u)
            arcsin, arccos = spiralDeg(w=w, d=d, unitType=sa_u)
            self.spiral_ang.text = f'asin:{arcsin}\nacos:{arccos}'

            #######debug
            # self.debug_fs.text = str(self.height) + "/-/" + str(self.width)
            # print(self.spiral_ang.text)
            #######

    def copy2Clipboard(self):
        temp = f'INPUTS:\nMaterial={self.mat.text}\nPlate Thickness={self.t.text}\nPlate Width={self.w.text}\nPipe Diameter={self.d.text}\nPipe Length={self.l.text}' \
               f'\n\nOUTPUTS:\nTest Pressure={self.test_pressure.text}\nPipe Weight={self.pipe_weight.text}\nSpiral Length={self.spiral_length.text}\nSpiral Angle={self.spiral_ang.text}'

        Clipboard.copy(temp)

    def tBtn(self, btn, btn2, textIn, justNum=True):
        if btn.state == 'down':
            textIn.text = converter(textIn.text, btn.text, justNum)
        else:
            btn2.state = 'down'
            self.tBtn(btn2, btn, textIn, justNum)

    @staticmethod
    def feasCheck(value, LB, UB, radVS, radBS):
        value = float(value.text.split("\n")[0].split(":")[-1])
        if radVS == "down":
            value *= 57.2958
        if radBS == "down":
            LB *= 57.2958
            UB *= 57.2958

        if LB <= value <= UB:
            return (1, 1, 1, 1)
        else:
            return (1, 0.5, 0.5, 1)


class pipeCal(App):
    def build(self):
        return trunk()


if __name__ == "__main__":
    pipeCal().run()
