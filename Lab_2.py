#Import Libraries
import pyvisa
import time
#Make sure openpyxl is installed
import pandas as pd

# Variables
rm = pyvisa.ResourceManager()
addresses = rm.list_resources()

# Establish addresses for the tabletop equipment
for j in range(len(addresses)):
    if len(addresses[j]) >= 25:
        match addresses[j][22:25]:
            case 'SPD':
                supply = rm.open_resource(addresses[j])
            case 'SDM':
                dmm = rm.open_resource(addresses[j])
            case 'SDG':
                fungen = rm.open_resource(addresses[j])
            case 'SDS':
                oscope = rm.open_resource(addresses[j])
            case _:
                print("No matching instrument")
            # #Setup Devices
print(rm.list_resources())

#Configuring sessions

dmm.read_termination = '\n'
dmm.write_termination = '\n'
dmm.timeout = 10000  # 10 seconds

print("DMM ID:", dmm.query("*IDN?"))

dmm.write("*RST")                   # reset to default
dmm.write("*CLS")                   # clear status
dmm.write("CONF:VOLT:DC")           # DC voltage mode



def part_3():
    data = []
    cv = [.01,.1,1]

    supply.write("OUTP CH1,OFF")
    supply.write("CH1:VOLT 1")
    time.sleep(1)
    supply.write("OUTP CH1,ON")


    for x in cv:
        supply.write(f"CH1:CURR {x}")                   # Set current to 10mA
        time.sleep(1)
        cur = float(supply.query("MEAS:CURR? CH1"))     # Measures what current is set to
        time.sleep(0.5)
        print(cur)
        time.sleep(10)                                  # Allow wires to settle for 2 minutes
        volt = float(dmm.query("MEAS:VOLT:DC?"))        # Measure voltage
        print(volt)
        res = volt/x                                    # Calculates the resistance
        print(res)


        data.append({  # Creates a list of dictioneries for each measurment
            "Voltage": volt,
            "Current": cur,
            "Resistance": res
        })

        df = pd.DataFrame(data, columns=["Voltage", "Current", "Resistance"]) # Exports everything to an excel file in 3 columns
        df.to_excel("part_3.xlsx", index=False)

part_3()
supply.write("OUTP CH1,OFF")

