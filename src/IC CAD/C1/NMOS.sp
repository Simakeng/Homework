.title NMOS_DC
.lib '..\lib\tsmc018r.lib' TT

VVDS net2 0 DC 1v
VVGS net1 0 DC 1v
MNM0 net2 net1 0 nch1 W=10u L=180n
.temp 27
.op
.dc VVDS 0 1.8 0.1 VVGS 0 1.8 1

.option post accurate probe
.probe v(net2) v(net1) I(MNM0)
.end