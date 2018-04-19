import pandas as pd

data = pd.read_csv('data/CRDC2013_14.csv')

data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']

hispanic_enr = (data['SCH_ENR_HI_M'] + data['SCH_ENR_HI_F']).sum()

am_ind_enr = (data['SCH_ENR_AM_M'] + data['SCH_ENR_AM_F']).sum()

asian_enr = (data['SCH_ENR_AS_M'] + data['SCH_ENR_AS_F']).sum()

haw_pac_enr = (data['SCH_ENR_HP_M'] + data['SCH_ENR_HP_F']).sum()

black_enr = (data['SCH_ENR_BL_M'] + data['SCH_ENR_BL_F']).sum()

white_enr = (data['SCH_ENR_WH_M'] + data['SCH_ENR_WH_F']).sum()

two_plus_enr = (data['SCH_ENR_TR_M'] + data['SCH_ENR_TR_F']).sum()

male_enr = (data['TOT_ENR_M']).sum()

female_enr = (data['TOT_ENR_F']).sum()

all_enrollment = (data['total_enrollment']).sum()

for subset in [hispanic_enr, am_ind_enr, asian_enr, haw_pac_enr, black_enr, white_enr, two_plus_enr, male_enr, female_enr]:
    print(subset / all_enrollment)
    