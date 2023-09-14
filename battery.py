#!/usr/bin/python
from time import sleep, gmtime
from shlex import split, quote
from subprocess import call
from psutil import sensors_battery

LAST_STATUS = None
DEFAULT_LANG = 'es'
LOW_LEVEL = 25.0
CRITICAL_LEVEL = 10.0
UPDATE_INTERVAL = 0.3 #in seconds
TITLE = {
    'en':{
        'critical':' batery level is critical',
        'low-battery': '󱊡 low batery',
        'charging': ' Plug connected',
        'discharging': ' batery is discharging',
        'full' : ' Charge complete!'
    },
    'es':{
        'critical':' nivel critico de bateria',
        'low-battery': '󱊡 bateria baja',
        'charging': ' cargando',
        'discharging': ' bateria descargandose',
        'full' : ' Carga completa!'
        
    }
}


LANG = {
    'en':{
        'status':{
            'critical':'BATTERY LEVEL IS CRITICAL\nHas {}%\nLeft {} hours',
            'low-battery': 'Battery level is low\nPlease Charge\nHas {}%\nLeft {} hours',
            'charging': 'Plug connected\nThe batery is charging',
            'discharging': 'Battery discharging\nHas {}%\nLeft {} hours',
            'full' : 'Can unplug charger'
            
        }
    },
    'es':{
        'status':{
            'critical':'NIVEL CRITICO\ntiene {}%\nRestan {} horas',
            'low-battery': 'Nivel de bateria bajo\nConecta el cargador\ntiene {}%\nRestan {} horas',
            'charging': 'Cargador conectado\nLa bateria se esta cargando',
            'discharging': 'Bateria descargandose\ntiene {}%\nRestan {} horas',
            'full' : 'Puedes desconectar el cargador'
            
        }
    }
}


def notify(title:str, msg:str, urgency='normal', time=5000):
    command = "notify-send {} {} -u {}".format(
        quote(title), 
        quote(msg),
        urgency
    )
    print(command)
    try:
        sh_command = split(command)
        call(sh_command)
    except:
        pass

def determine_battery_status(percent, plug):
    low = LOW_LEVEL
    critical = CRITICAL_LEVEL
    if plug:
        return 'charging'
    if percent == 100:
        return 'full'
    low, critical = (critical, low) if low <= critical else (low, critical)
    if percent > low:
        return 'discharging'
    elif percent <= low and critical < percent:
        return 'low-battery'
    else:
        return 'critical'
    
def send_notify():
    global LAST_STATUS
    msg = ''
    try:
        status = sensors_battery()
        percent = status.percent
        time_left = gmtime(status.secsleft)
        time_left = '{}:{}'.format(time_left.tm_hour, time_left.tm_min)
        status_title = determine_battery_status(percent, status.power_plugged)
        ntitle = '  '.join(word.capitalize() for word in TITLE[DEFAULT_LANG][status_title].split())
        msg = LANG[DEFAULT_LANG]['status'][status_title]
        msg = msg.format(int(percent), time_left).split('\n')
        msg = '\n'.join(sentence.capitalize() for sentence in msg)
        print(LAST_STATUS, status_title)
        if status_title != LAST_STATUS:
            LAST_STATUS = status_title
            urgency = 'normal'
            time = 5000
            if LAST_STATUS == 'critical':
                urgency = 'critical'
                time *= 2
            notify(ntitle, msg, urgency, time)
    except Exception as error: 
        return str(error)
    return msg



def main():
    while True:
        send_notify()
        sleep(UPDATE_INTERVAL)

if __name__ == '__main__':
    main()