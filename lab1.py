import PySimpleGUI as sg
import colorsys

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
tab1_layout =  [[sg.Text('CMYK'), sg.Text('C'), sg.InputText(key='T_CMYK_C', enable_events=True, default_text='0'), sg.Text('M'), sg.InputText(key='T_CMYK_M', enable_events=True, default_text='0'), sg.Text('Y'), sg.InputText(key='T_CMYK_Y', enable_events=True, default_text='0'), sg.Text('K'), sg.InputText(key='T_CMYK_K', enable_events=True, default_text='0')],
            [sg.Text('RGB'), sg.Text('R'), sg.InputText(key='T_RGB_R', enable_events=True, default_text='0'), sg.Text('G'), sg.InputText(key='T_RGB_G', enable_events=True, default_text='0'), sg.Text('B'), sg.InputText(key='T_RGB_B', enable_events=True, default_text='0')],
            [sg.Text('HSV'), sg.Text('H'), sg.InputText(key='T_HSV_H', enable_events=True, default_text='0'), sg.Text('S'), sg.InputText(key='T_HSV_S', enable_events=True, default_text='0'), sg.Text('V'), sg.InputText(key='T_HSV_V', enable_events=True, default_text='0')],
            [sg.Button('Submit Text input')]]

tab2_layout = [[sg.Text('CMYK'), sg.Text('C'), sg.Slider(range=(0.0, 100.0), tick_interval=0.1, orientation="horizontal", key='SL_CMYK_C', enable_events=True), sg.Text('M'), sg.Slider(range=(0.0, 100.0), orientation="horizontal", key='SL_CMYK_M', enable_events=True), sg.Text('Y'), sg.Slider(range=(0.0, 100.0), orientation="horizontal", key='SL_CMYK_Y', enable_events=True), sg.Text('K'), sg.Slider(range=(0.0, 100.0), orientation="horizontal", key='SL_CMYK_K', enable_events=True)],
            [sg.Text('RGB'), sg.Text('R'), sg.Slider(range=(0, 255), orientation="horizontal", key='SL_RGB_R', enable_events=True), sg.Text('G'), sg.Slider(range=(0, 255), orientation="horizontal", key='SL_RGB_G', enable_events=True), sg.Text('B'), sg.Slider(range=(0, 255), orientation="horizontal", key='SL_RGB_B', enable_events=True)],
            [sg.Text('HSV'), sg.Text('H'), sg.Slider(range=(0.0, 360.0), orientation="horizontal", key='SL_HSV_H', enable_events=True), sg.Text('S'), sg.Slider(range=(0, 100), orientation="horizontal", key='SL_HSV_S', enable_events=True), sg.Text('V'), sg.Slider(range=(0, 100), orientation="horizontal", key='SL_HSV_V', enable_events=True)],
            [sg.Button('Submit Slider input')]]

layout = [   
            [sg.Input(text_color='black', enable_events=True, disabled = True, key='-IN-', font=('Arial Bold', 12)), sg.ColorChooserButton("Choose Color")],
            [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400), key="graph")],
            [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])] ]

# Create the Window
window = sg.Window('Color library', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    text_color = '#000000'
    window['graph'].DrawRectangle((200, 200), (250, 300), fill_color=text_color)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == '-IN-':
      window['graph'].DrawRectangle((200, 200), (250, 300), fill_color=values['-IN-'])
    #   window['graph'].update(color=values['-IN-'])
    if event == 'Submit Text input':
        print('You entered ', values[10], " ", values[1], " ", values[4])
    if event == 'Submit Slider input':
        print('You entered ', values[10], " ", values[1], " ", values[4])

    # Обработка RGB слайдера

    if (event == 'SL_RGB_R' or event == 'SL_RGB_G' or event == 'SL_RGB_B'):
            
        r = float(values['SL_RGB_R']) / 2.55
        g = float(values['SL_RGB_G']) / 2.55
        b = float(values['SL_RGB_B']) / 2.55
        c_max = max(r, g, b)
        c_min = min(r, g, b)
        d = c_max - c_min

        window['T_RGB_R'].update(r * 2.55)
        window['T_RGB_G'].update(g * 2.55)
        window['T_RGB_B'].update(b * 2.55)

        if (max(r, g, b) != 0):
            window['SL_CMYK_K'].update(float(100 - max(r, g, b)))
            window['SL_CMYK_C'].update(float((c_max - r) / c_max) * 100)
            window['SL_CMYK_M'].update(float((c_max - g) / c_max) * 100)
            window['SL_CMYK_Y'].update(float((c_max - b) / c_max) * 100)
            window['T_CMYK_K'].update(float(100 - c_max))
            window['T_CMYK_C'].update(float((c_max - r) / c_max) * 100)
            window['T_CMYK_M'].update(float((c_max - g) / c_max) * 100)
            window['T_CMYK_Y'].update(float((c_max - b) / c_max) * 100)
            text_color = '#'
            if len(format(int(values['SL_RGB_R']), 'X')) < 2:
                text_color = text_color + '0' + format(int(values['SL_RGB_R']), 'X')
            else:
                text_color += format(int(values['SL_RGB_R']), 'X')
            if len(format(int(values['SL_RGB_G']), 'X')) < 2:
                text_color = text_color + '0' + format(int(values['SL_RGB_G']), 'X')
            else:
                text_color += format(int(values['SL_RGB_G']), 'X')
            if len(format(int(values['SL_RGB_B']), 'X')) < 2:
                text_color = text_color + '0' + format(int(values['SL_RGB_B']), 'X')
            else:
                text_color += format(int(values['SL_RGB_B']), 'X')
        else:
            text_color = '#000000'
            window['T_CMYK_K'].update('100')
            window['SL_CMYK_K'].update('100')

        if c_max == r and d != 0 and g < b:
            h = 60 * (g - b / d) % 360
        elif c_max == r and d != 0 and g >= b:
            h = 60 * (((g - b) / d) + 6) % 360
        elif c_max == g and d != 0:
            h = 60 * (((b - r) / d) + 2) % 360
        elif c_max == b and d != 0:
            h = 60 * (((r - g) / d) + 4) % 360
        else:
            h = 0
        if c_max == 0:
            s = 0
        else:
            s = 100 * d / c_max
        v = c_max

        window['T_HSV_H'].update(h)
        window['T_HSV_S'].update(s)
        window['T_HSV_V'].update(v)
        window['SL_HSV_H'].update(h)
        window['SL_HSV_S'].update(s)
        window['SL_HSV_V'].update(v)

        window['-IN-'].update(text_color)

        window['graph'].DrawRectangle((200, 200), (250, 300), fill_color=text_color)
        

    # Обработка RGB текста

    if ((event == 'T_RGB_R' and values['T_RGB_R'].isnumeric() and int(values['T_RGB_R']) >= 0 and int(values['T_RGB_R']) <= 255) or (event == 'T_RGB_G' and values['T_RGB_G'].isnumeric() and int(values['T_RGB_G']) >= 0 and int(values['T_RGB_G']) <= 255) or (event == 'T_RGB_B' and values['T_RGB_B'].isnumeric() and int(values['T_RGB_B']) >= 0 and int(values['T_RGB_B']) <= 255)):
        
        r = float(values['T_RGB_R']) / 2.55
        g = float(values['T_RGB_G']) / 2.55
        b = float(values['T_RGB_B']) / 2.55
        c_max = max(r, g, b)
        c_min = min(r, g, b)
        d = c_max - c_min

        window['SL_RGB_R'].update(r * 2.55)
        window['SL_RGB_G'].update(g * 2.55)
        window['SL_RGB_B'].update(b * 2.55)

        if (max(r, g, b) != 0):
            window['T_CMYK_K'].update(float(100 - max(r, g, b)))
            window['T_CMYK_C'].update(float((c_max - r) / c_max) * 100)
            window['T_CMYK_M'].update(float((c_max - g) / c_max) * 100)
            window['T_CMYK_Y'].update(float((c_max - b) / c_max) * 100)
            window['SL_CMYK_K'].update(float(100 - c_max))
            window['SL_CMYK_C'].update(float((c_max - r) / c_max) * 100)
            window['SL_CMYK_M'].update(float((c_max - g) / c_max) * 100)
            window['SL_CMYK_Y'].update(float((c_max - b) / c_max) * 100)
            text_color = '#'
            if len(format(int(float(values['T_RGB_R'])), 'X')) < 2:
                text_color = text_color + '0' + format(int(float(values['T_RGB_R'])), 'X')
            else:
                text_color += format(int(float(values['T_RGB_R'])), 'X')
            if len(format(int(float(values['T_RGB_G'])), 'X')) < 2:
                text_color = text_color + '0' + format(int(float(values['T_RGB_G'])), 'X')
            else:
                text_color += format(int(float(values['T_RGB_G'])), 'X')
            if len(format(int(float(values['T_RGB_B'])), 'X')) < 2:
                text_color = text_color + '0' + format(int(float(values['T_RGB_B'])), 'X')
            else:
                text_color += format(int(float(values['T_RGB_B'])), 'X')
        else:
            text_color = '#000000'
            window['T_CMYK_K'].update('100')
            window['SL_CMYK_K'].update('100')

        if c_max == r and d != 0 and g < b:
            h = 60 * (g - b / d) % 360
        elif c_max == r and d != 0 and g >= b:
            h = 60 * (((g - b) / d) + 6) % 360
        elif c_max == g and d != 0:
            h = 60 * (((b - r) / d) + 2) % 360
        elif c_max == b and d != 0:
            h = 60 * (((r - g) / d) + 4) % 360
        else:
            h = 0
        if c_max == 0:
            s = 0
        else:
            s = 100 * d / c_max
        v = c_max

        window['T_HSV_H'].update(h)
        window['T_HSV_S'].update(s)
        window['T_HSV_V'].update(v)
        window['SL_HSV_H'].update(h)
        window['SL_HSV_S'].update(s)
        window['SL_HSV_V'].update(v)

        window['-IN-'].update(text_color)

        window['graph'].DrawRectangle((200, 200), (250, 300), fill_color=text_color)

        
    # Обработка CMYK слайдера

    if (event == 'SL_CMYK_C' or event == 'SL_CMYK_M' or event == 'SL_CMYK_Y' or event == 'SL_CMYK_K'):
            
        window['T_CMYK_C'].update(values['SL_CMYK_C'])
        window['T_CMYK_M'].update(values['SL_CMYK_M'])
        window['T_CMYK_Y'].update(values['SL_CMYK_Y'])
        window['T_CMYK_K'].update(values['SL_CMYK_K'])

        r = float(0.0255 * (100 - values['SL_CMYK_C']) * (100 - values['SL_CMYK_K']))
        g = float(0.0255 * (100 - values['SL_CMYK_M']) * (100 - values['SL_CMYK_K']))
        b = float(0.0255 * (100 - values['SL_CMYK_Y']) * (100 - values['SL_CMYK_K']))
        window['SL_RGB_R'].update(r)
        window['SL_RGB_G'].update(g)
        window['SL_RGB_B'].update(b)
        window['T_RGB_R'].update(r)
        window['T_RGB_G'].update(g)
        window['T_RGB_B'].update(b)
        text_color = '#'

        if (max(r, g, b) != 0):
            if len(format(int(r), 'X')) < 2:
                text_color = text_color + '0' + format(int(r), 'X')
            else:
                text_color += format(int(r), 'X')
            if len(format(int(g), 'X')) < 2:
                text_color = text_color + '0' + format(int(g), 'X')
            else:
                text_color += format(int(g), 'X')
            if len(format(int(b), 'X')) < 2:
                text_color = text_color + '0' + format(int(b), 'X')
            else:
                text_color += format(int(b), 'X')
        else:
            text_color = '#000000'
            window['T_CMYK_K'].update('100')
            window['SL_CMYK_K'].update('100')

        if c_max == r and d != 0 and g < b:
            h = 60 * (g - b / d) % 360
        elif c_max == r and d != 0 and g >= b:
            h = 60 * (((g - b) / d) + 6) % 360
        elif c_max == g and d != 0:
            h = 60 * (((b - r) / d) + 2) % 360
        elif c_max == b and d != 0:
            h = 60 * (((r - g) / d) + 4) % 360
        else:
            h = 0
        if c_max == 0:
            s = 0
        else:
            s = 100 * d / c_max
        v = c_max

        window['T_HSV_H'].update(h)
        window['T_HSV_S'].update(s)
        window['T_HSV_V'].update(v)
        window['SL_HSV_H'].update(h)
        window['SL_HSV_S'].update(s)
        window['SL_HSV_V'].update(v)

        window['-IN-'].update(text_color)

        window['graph'].DrawRectangle((200, 200), (250, 300), fill_color=text_color)
        

    # Обработка CMYK текста

    if (event == 'T_CMYK_C' or event == 'T_CMYK_M' or event == 'T_CMYK_Y' or event == 'T_CMYK_K'):
           
        window['SL_CMYK_C'].update(int(float(values['T_CMYK_C'])))
        window['SL_CMYK_M'].update(int(float(values['T_CMYK_M'])))
        window['SL_CMYK_Y'].update(int(float(values['T_CMYK_Y'])))
        window['SL_CMYK_K'].update(int(float(values['T_CMYK_K'])))

        r = float(0.0255 * (100 - int(float(values['T_CMYK_C']))) * (100 - int(float(values['T_CMYK_K']))))
        g = float(0.0255 * (100 - int(float(values['T_CMYK_M']))) * (100 - int(float(values['T_CMYK_K']))))
        b = float(0.0255 * (100 - int(float(values['T_CMYK_Y']))) * (100 - int(float(values['T_CMYK_K']))))
        window['SL_RGB_R'].update(r)
        window['SL_RGB_G'].update(g)
        window['SL_RGB_B'].update(b)
        window['T_RGB_R'].update(r)
        window['T_RGB_G'].update(g)
        window['T_RGB_B'].update(b)
        text_color = '#'

        if (max(r, g, b) != 0):
            if len(format(int(r), 'X')) < 2:
                text_color = text_color + '0' + format(int(r), 'X')
            else:
                text_color += format(int(r), 'X')
            if len(format(int(g), 'X')) < 2:
                text_color = text_color + '0' + format(int(g), 'X')
            else:
                text_color += format(int(g), 'X')
            if len(format(int(b), 'X')) < 2:
                text_color = text_color + '0' + format(int(b), 'X')
            else:
                text_color += format(int(b), 'X')
        else:
            text_color = '#000000'
            window['T_CMYK_K'].update('100')
            window['SL_CMYK_K'].update('100')

        if c_max == r and d != 0 and g < b:
            h = 60 * (g - b / d) % 360
        elif c_max == r and d != 0 and g >= b:
            h = 60 * (((g - b) / d) + 6) % 360
        elif c_max == g and d != 0:
            h = 60 * (((b - r) / d) + 2) % 360
        elif c_max == b and d != 0:
            h = 60 * (((r - g) / d) + 4) % 360
        else:
            h = 0
        if c_max == 0:
            s = 0
        else:
            s = 100 * d / c_max
        v = c_max

        window['T_HSV_H'].update(h)
        window['T_HSV_S'].update(s)
        window['T_HSV_V'].update(v)
        window['SL_HSV_H'].update(h)
        window['SL_HSV_S'].update(s)
        window['SL_HSV_V'].update(v)

        window['-IN-'].update(text_color)

        window['graph'].DrawRectangle((200, 200), (250, 300), fill_color=text_color)
        
        

window.close()