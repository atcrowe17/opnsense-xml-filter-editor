1. import csv of filter rules as a dataframe
2. search for existing rule
3. if rule matches, stop
4. if rule doesn't match, gen new uuid
5. create xml version of filter rule, with new uuid
5. update config.XML file
6. push config.xml to opnsense fw
7. restart opense fw services to apply new filter
