# 26EET32101-Lab2

EET-321 Measurement and Test Lab 2 – Measuring Small Resistances

Lab Instructions: Measuring Small Resistances with a Siglent DMM

Objective:

The objective of this lab is to compare methods for accurately measuring small resistances
below 1 Ohm using a Siglent SDM3055 digital multimeter (DMM). You will test various
measurement techniques and analyze the results to determine the most accurate method.

Equipment:

- Siglent SDM3055 digital multimeter

- 5 lengths of 12-inch 22 AWG wire

- Banana plug to alligator clip leads

- Optional: Siglent SPD3303X-E DC power supply for alternate 4-wire method

Procedure:

PART I

1. Calculate theoretical resistance using formula:

        R = ρ L / A

Look up resistivity value for copper and cross-sectional area of 22AWG wire.

Record this value for later analysis.

Use the following five resistance measurement methods to measure the resistance of each wire:

1. Null Method

- Short the leads of the DMM together and press the “REL” button to zero out the lead resistance

- Connect each length of wire between the leads and record the resistance measurement


2. 4-Wire Method

- Connect the wires to use the DMM's built-in 4-wire resistance mode (see wiring diagram)

- Record resistance measurements for each wire


3. Alternate 4-Wire Method

- Use an external DC power supply instead of the DMM's internal source

- Force different test currents (10 mA, 100 mA, 1A) and measure voltage drop to calculate
- resistance per Ohm's Law

- Allow wires to settle for 2 minutes between tests as temperature may increase resistance

- Create a Python script to automatically set the test current from the power supply, make
- the voltage drop measurement with the DMM, and calculate the resistance. Have the script
- write these values to a spreadsheet or database. The program should include the 2 minute
- wait time between each current setting and measurement.


4. No Lead Method

- Connect banana plugs directly to the ends of each wire length

- Record the resistance measurements


5. Negated Lead Method

- Short leads and note this baseline resistance value

- Connect wires and measure resistance

- Subtract baseline lead resistance manually to get wire resistance


PART II

Have each group get three precision 100mOhm resistors from the tool room.

Each group will perform a different measurement method from steps 1-5 in Part I.
Record the results in a spreadsheet. The lead team will analyze all the data to see
which method(s) gave the most accurate and repeatable measurements.


Data Analysis:

- Import the resistance data into either MATLAB or Python

- In MATLAB, use functions like mean() and std() to calculate error metrics

- In Python, use NumPy, Pandas, etc. to calculate statistics like mean, standard deviation

- Compare measured resistance values to the expected resistance per length

- Calculate percent error between measured and theoretical values

- Evaluate measurement repeatability by method via standard deviation

- Create plots in MATLAB or matplotlib/seaborn in Python to visualize the data

- Determine which method provides the most accurate and consistent small resistance measurements


Discussion Questions:


Calculate the error and % error between the theoretical and measured values in the data
collected for tasks 1- 5 and Part II.

Perform the previous step with the data taken from your automated testing. Compare the
results from the various methods for measuring resistance.

Determine which method is the most accurate.

Explain why the 4-wire method should be more accurate than the other methods. Was that
what you observed? What are some possible sources of error in this lab? How could they
be mitigated?

How does temperature affect the resistance of copper? Why?