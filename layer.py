layer = iface.activeLayer()

fields = layer.pendingFields()
print fields.count()
print dir(fields.field(0))

for field in fields:
    print field.name()


#features = layer.getFeatures()

#or...
#for feature in layer.getFeatures():
#    if feature[1].find('North Carolina') <> -1:
#        print feature[1]


#for feature in features:
#    attr = feature[0]
#    print attr
    
#    or
#    attr = feature.attributes()
#    print attr[3]

#sFeatures  = layer.selectedFeatures()
#for feat in sFeatures:
#    print feat[1]
