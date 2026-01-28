// Dame todos
db.facturas.find()

// Dame la primera
db.facturas.findOne()

// Select con where - se mete en las facturas y busca algo con la condicion especifica que le digas.
db.facturas.findOne({nombre:'Jose Vicente'})
