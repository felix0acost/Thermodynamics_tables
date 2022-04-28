from Thermodynamics_tables import Saturate_water_temperature_table
from Thermodynamics_tables import menus




def run():
    print(menus['menu1'])
    k = float(input("temperatura "))

    xv = [x['temp'] for x in Saturate_water_temperature_table if x['temp']<k and x['temp']>k-5 or x['temp']>k and x['temp']<k+5]

    print(xv)

    yv = [x['press'] for x in Saturate_water_temperature_table if x['temp']<k and x['temp']>k-5 or x['temp']>k and x['temp']<k+5]

    print(yv)

    q = float(yv[0]+(((k-xv[0])/(xv[1]-xv[0]))*(yv[1]-yv[0])))

    print(q)

if __name__ == '__main__':
    run()