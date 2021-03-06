#adds pandas for dealing with the data and matplotlib for plotting to the code
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt


# READ CSV with individual responses microdata from census Bureau
df = pd.read_csv('ss14pca.csv')
print(df)

#rewrite datafram to only inlcude important columns
cols_to_keep = ['FOD1P', 'ESR','WAGP','WKHP','OCCP','NAICSP']
df = df[cols_to_keep]
print(df)

#focuses only on college graduates
df = df.dropna(subset=['FOD1P'])
print(df)

#filters out all entries except employment status is only 1 or 2
df = df[(df['ESR']>.9) & (df['ESR']<2.1)]
print(df)

# coerces data that was misinterpretted by pandas
df.FOD1P = pd.to_numeric(df.FOD1P, errors='coerce')
df.ESR = pd.to_numeric(df.ESR, errors='coerce')
df.WAGP = pd.to_numeric(df.WAGP, errors='coerce')
df.WKHP = pd.to_numeric(df.WKHP, errors='coerce')
df.OCCP = pd.to_numeric(df.OCCP, errors='coerce')


dfdtypes = df.dtypes
print(dfdtypes)

# print for checking
# print(field_of_degree)
# print(employment_status)
# print(wage_past_year)
# print(work_hours_per_week)
# print(occupation_title)
# print(naics_industry)
# newdf = pd.DataFrame(field_of_degree,employment_status,wage_past_year)


# analysis

#df.loc[df['a'] == 1, 'b'].sum()
data_1100_major = df[df['FOD1P']==1100]
print(data_1100_major)
mean_salary_1100 = df.loc[df['FOD1P'] == 1100, 'WAGP'].mean()
print(mean_salary_1100)

# .plot.hist(alpha=0.5)
#data_1100_major = df[df['FOD1P']==1100].plot.hist()
print(df.loc[df['FOD1P'] == 1100, 'WAGP'])
#n, bins, patches =
toBePlotted = df.loc[df['FOD1P'] == 1100, 'WAGP']

plt.figure(); toBePlotted.plot();
plt.show()


# plt.plot(toBePlotted)

# toBePlotted.plot(kind='hist')
# toBePlotted.hist()
# num_bins = 50
# #plt.hist(toBePlotted, num_bins, normed=1, facecolor='green', alpha=0.5)
#
# # the histogram of the data
# n, bins, patches = plt.hist(toBePlotted, num_bins, facecolor='green')
# # add a 'best fit' line
# #y = mlab.normpdf(bins, mu, sigma)
# plt.plot(bins)
# plt.xlabel('$')
# plt.ylabel('Count')
# plt.title('Histogram of Salary')
# plt.show()
# https://docs.google.com/presentation/d/1zi5pdEuYItSaiIOGMrStaAsB8p9XvP653pyb5fUDcmw/edit?usp=sharing
"""
IMPORTANT COLUMNS
ESR 1
Employment status recode
b .N/A (less than 16 years old)
1 .Civilian employed, at work
2 .Civilian employed, with a job but not at work
3 .Unemployed
4 .Armed forces, at work
5 .Armed forces, with a job but not at work
6 .Not in labor force

FOD1P 4
Recoded field of degree - first entry
bbbb .N/A (less than bachelor's degree)
1100 .GENERAL AGRICULTURE
1101 .AGRICULTURE PRODUCTION AND MANAGEMENT
1102 .AGRICULTURAL ECONOMICS
1103 .ANIMAL SCIENCES
1104 .FOOD SCIENCE
1105 .PLANT SCIENCE AND AGRONOMY
1106 .SOIL SCIENCE
1199 .MISCELLANEOUS AGRICULTURE
1301 .ENVIRONMENTAL SCIENCE
1302 .FORESTRY
1303 .NATURAL RESOURCES MANAGEMENT
1401 .ARCHITECTURE
1501 .AREA ETHNIC AND CIVILIZATION STUDIES
1901 .COMMUNICATIONS
1902 .JOURNALISM
1903 .MASS MEDIA
1904 .ADVERTISING AND PUBLIC RELATIONS
2001 .COMMUNICATION TECHNOLOGIES
2100 .COMPUTER AND INFORMATION SYSTEMS
2101 .COMPUTER PROGRAMMING AND DATA PROCESSING
2102 .COMPUTER SCIENCE
2105 .INFORMATION SCIENCES
2106 .COMPUTER ADMINISTRATION MANAGEMENT AND SECURITY
2107 .COMPUTER NETWORKING AND TELECOMMUNICATIONS
2201 .COSMETOLOGY SERVICES AND CULINARY ARTS
2300 .GENERAL EDUCATION
2301 .EDUCATIONAL ADMINISTRATION AND SUPERVISION
2303 .SCHOOL STUDENT COUNSELING
2304 .ELEMENTARY EDUCATION
2305 .MATHEMATICS TEACHER EDUCATION
2306 .PHYSICAL AND HEALTH EDUCATION TEACHING
2307 .EARLY CHILDHOOD EDUCATION
2308 .SCIENCE AND COMPUTER TEACHER EDUCATION
2309 .SECONDARY TEACHER EDUCATION
2310 .SPECIAL NEEDS EDUCATION
2311 .SOCIAL SCIENCE OR HISTORY TEACHER EDUCATION
2312 .TEACHER EDUCATION: MULTIPLE LEVELS
2313 .LANGUAGE AND DRAMA EDUCATION
2314 .ART AND MUSIC EDUCATION
2399 .MISCELLANEOUS EDUCATION
2400 .GENERAL ENGINEERING
2401 .AEROSPACE ENGINEERING
2402 .BIOLOGICAL ENGINEERING
2403 .ARCHITECTURAL ENGINEERING
2404 .BIOMEDICAL ENGINEERING
2405 .CHEMICAL ENGINEERING
2406 .CIVIL ENGINEERING
2407 .COMPUTER ENGINEERING
2408 .ELECTRICAL ENGINEERING
2409 .ENGINEERING MECHANICS PHYSICS AND SCIENCE
2410 .ENVIRONMENTAL ENGINEERING
2411 .GEOLOGICAL AND GEOPHYSICAL ENGINEERING
2412 .INDUSTRIAL AND MANUFACTURING ENGINEERING
2413 .MATERIALS ENGINEERING AND MATERIALS SCIENCE
2414 .MECHANICAL ENGINEERING
2415 .METALLURGICAL ENGINEERING
2416 .MINING AND MINERAL ENGINEERING
2417 .NAVAL ARCHITECTURE AND MARINE ENGINEERING
2418 .NUCLEAR ENGINEERING
2419 .PETROLEUM ENGINEERING
2499 .MISCELLANEOUS ENGINEERING
2500 .ENGINEERING TECHNOLOGIES
2501 .ENGINEERING AND INDUSTRIAL MANAGEMENT
2502 .ELECTRICAL ENGINEERING TECHNOLOGY
2503 .INDUSTRIAL PRODUCTION TECHNOLOGIES
2504 .MECHANICAL ENGINEERING RELATED TECHNOLOGIES
2599 .MISCELLANEOUS ENGINEERING TECHNOLOGIES
2601 .LINGUISTICS AND COMPARATIVE LANGUAGE AND LITERATURE
2602 .FRENCH GERMAN LATIN AND OTHER COMMON FOREIGN LANGUAGE STUDIES
2603 .OTHER FOREIGN LANGUAGES
2901 .FAMILY AND CONSUMER SCIENCES
3201 .COURT REPORTING
3202 .PRE-LAW AND LEGAL STUDIES
3301 .ENGLISH LANGUAGE AND LITERATURE
3302 .COMPOSITION AND RHETORIC
3401 .LIBERAL ARTS
3402 .HUMANITIES
3501 .LIBRARY SCIENCE
3600 .BIOLOGY
3601 .BIOCHEMICAL SCIENCES
3602 .BOTANY
3603 .MOLECULAR BIOLOGY
3604 .ECOLOGY
3605 .GENETICS
3606 .MICROBIOLOGY
3607 .PHARMACOLOGY
3608 .PHYSIOLOGY
3609 .ZOOLOGY
3611 .NEUROSCIENCE
3699 .MISCELLANEOUS BIOLOGY
3700 .MATHEMATICS
3701 .APPLIED MATHEMATICS
3702 .STATISTICS AND DECISION SCIENCE
3801 .MILITARY TECHNOLOGIES
4000 .MULTI/INTERDISCIPLINARY STUDIES
4001 .INTERCULTURAL AND INTERNATIONAL STUDIES
4002 .NUTRITION SCIENCES
4005 .MATHEMATICS AND COMPUTER SCIENCE
4006 .COGNITIVE SCIENCE AND BIOPSYCHOLOGY
4007 .INTERDISCIPLINARY SOCIAL SCIENCES
4101 .PHYSICAL FITNESS PARKS RECREATION AND LEISURE
4801 .PHILOSOPHY AND RELIGIOUS STUDIES
4901 .THEOLOGY AND RELIGIOUS VOCATIONS
5000 .PHYSICAL SCIENCES
5001 .ASTRONOMY AND ASTROPHYSICS
5002 .ATMOSPHERIC SCIENCES AND METEOROLOGY
5003 .CHEMISTRY
5004 .GEOLOGY AND EARTH SCIENCE
5005 .GEOSCIENCES
5006 .OCEANOGRAPHY
5007 .PHYSICS
5008 .MATERIALS SCIENCE
5098 .MULTI-DISCIPLINARY OR GENERAL SCIENCE
5102 .NUCLEAR, INDUSTRIAL RADIOLOGY, AND BIOLOGICAL TECHNOLOGIES
5200 .PSYCHOLOGY
5201 .EDUCATIONAL PSYCHOLOGY
5202 .CLINICAL PSYCHOLOGY
5203 .COUNSELING PSYCHOLOGY
5205 .INDUSTRIAL AND ORGANIZATIONAL PSYCHOLOGY
5206 .SOCIAL PSYCHOLOGY
5299 .MISCELLANEOUS PSYCHOLOGY
5301 .CRIMINAL JUSTICE AND FIRE PROTECTION
5401 .PUBLIC ADMINISTRATION
5402 .PUBLIC POLICY
5403 .HUMAN SERVICES AND COMMUNITY ORGANIZATION
5404 .SOCIAL WORK
5500 .GENERAL SOCIAL SCIENCES
5501 .ECONOMICS
5502 .ANTHROPOLOGY AND ARCHEOLOGY
5503 .CRIMINOLOGY
5504 .GEOGRAPHY
5505 .INTERNATIONAL RELATIONS
5506 .POLITICAL SCIENCE AND GOVERNMENT
5507 .SOCIOLOGY
5599 .MISCELLANEOUS SOCIAL SCIENCES
5601 .CONSTRUCTION SERVICES
5701 .ELECTRICAL, MECHANICAL, AND PRECISION TECHNOLOGIES AND PRODUCTION
5901 .TRANSPORTATION SCIENCES AND TECHNOLOGIES
6000 .FINE ARTS
6001 .DRAMA AND THEATER ARTS
6002 .MUSIC
6003 .VISUAL AND PERFORMING ARTS
6004 .COMMERCIAL ART AND GRAPHIC DESIGN
6005 .FILM VIDEO AND PHOTOGRAPHIC ARTS
6006 .ART HISTORY AND CRITICISM
6007 .STUDIO ARTS
6099 .MISCELLANEOUS FINE ARTS
6100 .GENERAL MEDICAL AND HEALTH SERVICES
6102 .COMMUNICATION DISORDERS SCIENCES AND SERVICES
6103 .HEALTH AND MEDICAL ADMINISTRATIVE SERVICES
6104 .MEDICAL ASSISTING SERVICES
6105 .MEDICAL TECHNOLOGIES TECHNICIANS
6106 .HEALTH AND MEDICAL PREPARATORY PROGRAMS
6107 .NURSING
6108 .PHARMACY PHARMACEUTICAL SCIENCES AND ADMINISTRATION
6109 .TREATMENT THERAPY PROFESSIONS
6110 .COMMUNITY AND PUBLIC HEALTH
6199 .MISCELLANEOUS HEALTH MEDICAL PROFESSIONS
6200 .GENERAL BUSINESS
6201 .ACCOUNTING
6202 .ACTUARIAL SCIENCE
6203 .BUSINESS MANAGEMENT AND ADMINISTRATION
6204 .OPERATIONS LOGISTICS AND E-COMMERCE
6205 .BUSINESS ECONOMICS
6206 .MARKETING AND MARKETING RESEARCH
6207 .FINANCE
6209 .HUMAN RESOURCES AND PERSONNEL MANAGEMENT
6210 .INTERNATIONAL BUSINESS
6211 .HOSPITALITY MANAGEMENT
6212 .MANAGEMENT INFORMATION SYSTEMS AND STATISTICS
6299 .MISCELLANEOUS BUSINESS & MEDICAL ADMINISTRATION
6402 .HISTORY
6403 .UNITED STATES HISTORY
"""
