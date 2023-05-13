import xml.etree.ElementTree as ET
import pandas as pd

#open csv file and create a pandas dataframe
df = pd.read_csv('new-filters.csv')
print (df)
col_count = len(df.columns)
#print each cell in the dataframe row with for loop
for item in range(len(df)):
    for col in range(col_count):
        print (df.iloc[item,col])
#print nested value from xml file
tree = ET.parse('config.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
    print({x.tag for x in root.findall(child.tag+"/*")})
#get all elements and element values from XML using UUID
for child in root.findall('OPNsense/Firewall/Alias/aliases/alias/content'):
    print(child.tag, child.text)
