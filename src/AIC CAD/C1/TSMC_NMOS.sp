.title NMOS I-V Cbaracteristic

.lib '..\lib\mix025_1.l' tt
M1 2 1 0 0 nch L=0.24U W=1u
VGS 1 0 dc 0.8
VDS 2 0 dc 1

.op
.dc VDS 0 20 0.1 VGS 0.8 1 0.2
# .dc VGS POI 2 0.8 1

.end
