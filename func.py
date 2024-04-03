# Pakages
import numpy as np

# Helper Functions
dig = 3
yieldStrength = {
    'st 33': [185, 175, np.NAN, np.NAN, np.NAN],
    'st 37-2': [235, 225, 215, 205, 195],
    'ust 37-2': [235, 225, 215, 205, 195],
    'rst 37-2': [235, 225, 215, 215, 215],
    'st 37-3': [235, 225, 215, 215, 215],
    'st 44-2': [275, 265, 255, 245, 235],
    'st 44-3': [275, 265, 255, 245, 235],
    'st 52-3': [355, 345, 335, 325, 315],
    'st 50-2': [295, 285, 275, 265, 255],
    'st 60-2': [335, 325, 315, 305, 295],
    'st 70-2': [365, 355, 345, 335, 325],
    'A25p(L175)': [172],
    'A(L210)': [207],
    'B(L245)': [241],
    'X42(L290)RNQM': [290],
    'X46(L320)NQM': [317],
    'X52(L360)NQM': [359],
    'X56(L390)NQM': [386],
    'X60(L415)NQM': [414],
    'X65(L450)QM': [448],
    'X70(L485)QM': [483],
    'X80(L555)QM': [552],
    'X90(L625)MQ': [625],
    'X100(L690)MQ': [690],
    'X120(L830)M': [830],
}


def smys(t, mat):
    if mat in ['st 33', 'st 37-2', 'ust 37-2', 'rst 37-2', 'st 37-3', 'st 44-2', 'st 44-3', 'st 52-3', 'st 50-2',
               'st 60-2', 'st 70-2']:
        if t > 0 and t <= 16:
            idx = 0
        elif t > 16 and t <= 40:
            idx = 1
        elif t > 40 and t <= 63:
            idx = 2
        elif t > 63 and t <= 80:
            idx = 3
        elif t > 80 and t <= 100:
            idx = 4
        else:
            idx = 4  # Error: thickness not in range--> (0<t<=100)
    else:
        idx = 0
    return yieldStrength[mat][idx]


# Main Functions
def tesPressure(t, d, s=0.75, mat='st 33', unitType='bar'):
    u = smys(t, mat)
    out = 20 * s * u * t / d
    if unitType == 'psi':
        out = out * 14.5038
    return str(round(out, dig)), f"U={u}"


def pipeWeight(t, d, l=1, unitType='kg'):
    out = 0.0246615 * (d - t) * t * l
    if unitType == 'lb':
        out = out * 2.20462
    return str(round(out, dig))


def spiralLength(t, d, l, w, unitType='m'):
    out = (d - t) * np.pi * l / w
    if unitType == 'feet':
        out = out * 3.28084
    return str(round(out, dig))


def spiralDeg(w, d, unitType='deg'):
    out1 = np.arcsin(w / d / np.pi)
    out2 = np.arccos(w / d / np.pi)
    if unitType == 'deg':
        out1 *= 180 / np.pi
        out2 *= 180 / np.pi
    return str(round(out1, dig)), str(round(out2, dig))


def converter(value, toUnit, justNum):
    if value != '':
        if justNum is True:
            if toUnit == 'mm':
                value = round(float(value) * 25.4, dig)
            elif toUnit == 'inch':
                value = round(float(value) / 25.4, dig)
            elif toUnit == 'bar':
                value = round(float(value) / 14.5038, dig)
            elif toUnit == 'psi':
                value = round(float(value) * 14.5038, dig)
            elif toUnit == 'kg':
                value = round(float(value) / 2.20462, dig)
            elif toUnit == 'lb':
                value = round(float(value) * 2.20462, dig)
            elif toUnit == 'm':
                value = round(float(value) / 3.28084, dig)
            elif toUnit == 'feet':
                value = round(float(value) * 3.28084, dig)
            elif toUnit == 'DEG':
                value = round(float(value) * 57.2958, dig)
            elif toUnit == 'RAD':
                value = round(float(value) / 57.2958, dig)
            else:
                value = 'Conversion ERR'
        else:
            if toUnit == 'DEG':
                ss = value.split('\n')
                asin = float(ss[0].split(':')[-1])
                acos = float(ss[1].split(':')[-1])
                value = f'asin:{round(asin * 57.2958, dig)}\nacos:{round(acos * 57.2958, dig)}'
            elif toUnit == 'RAD':
                ss = value.split('\n')
                asin = float(ss[0].split(':')[-1])
                acos = float(ss[1].split(':')[-1])
                value = f'asin:{round(asin / 57.2958, dig)}\nacos:{round(acos / 57.2958, dig)}'
            else:
                value = 'Conversion ERR'

    else:
        pass
    return str(value)
