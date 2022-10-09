x = input("Starting Basic: ")
y = input("Increment Percentage Rate: ")
z = input("PF Percentage Rate: ")
a = input("Gratuity Per Year(1 or 2): ")
b = input("Probation Period (In Months): ")

BS = float(x)  # Basic Salary
IR = (float(y)) / 100  # Increment Rate
PR = (float(z)) / 100  # Provident Fund Rate
GR = float(a)  # Gratuity
PP = float(b)  # Probation Period

MMCPF = 0  # My monthly contribution pf
TMCPF = 0  # Total my contribution pf
CMCPF = 0  # Company monthly contribution pf
TCCPF = 0  # Total company contribution pf
TPF = TMCPF + TCCPF

gratuity = 0  # Total Gratuity Amount
TC = gratuity + TPF  # Total compensation

RF = 0  # R factor during probation period

for month in range(1, 505):
    if month <= PP:
        RF = 0
    else:
        RF = 1
    MMCPF = BS * PR * RF
    CMCPF = MMCPF
    TMCPF = TMCPF + MMCPF
    TCCPF = TCCPF + CMCPF
    TPF = round(TMCPF + TCCPF)
    if month % 12 == 0:
        BS = round(BS * (1 + IR))
        gratuity = round(BS * (month / 12) * GR)
    TC = gratuity + TPF
    if month % 12 == 0:
        year = round(month / 12)
        print()
        print(f"After {year} year,")
        print(f"    Your Basic Salary:     {BS}")
        print(f"    Total PF Amount:       {TPF}")
        print(f"    Total Gratuity Amount: {gratuity}")
        print(f"    Total Compensation:    {TC}")
        print()

