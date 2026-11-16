#!/usr/bin/env python3
"""Verifikation Semesteraufgabe B3 Holzbau"""
import math

# ---------------- Material ----------------
# C24 (VH):  fm=24, fc0=21, fc90=2.5, fv=4.0, E0mean=11000, kcr=0.5
# GL24h:     fm=24, fc0=24, fc90=2.5, fv=3.5, E0mean=11500, kcr=0.714
gM = 1.3

print("="*60)
print("POS 1: STUETZE 1  (C24 12/12, h=4.0m)")
print("="*60)
G1, S1, W1 = 10.25, 13.0, 2.0   # G inkl. EG Stuetze 0.25
lf = {
 "LF1 1,35G": (1.35*G1, 0.6),
 "LF2 1,35G+1,5S": (1.35*G1+1.5*S1, 0.9),
 "LF3 1,35G+1,5W": (1.35*G1+1.5*W1, 1.0),
 "LF4 1,35G+1,5S+1,5*0,6W": (1.35*G1+1.5*S1+1.5*0.6*W1, 1.0),
 "LF5 1,35G+1,5W+1,5*0,5S": (1.35*G1+1.5*W1+1.5*0.5*S1, 1.0),
}
for k,(e,km) in lf.items(): print(f"  {k:28s} Ed={e:6.2f} kN  kmod={km}  Ed/kmod={e/km:6.2f}")
NEd = 1.35*G1+1.5*S1; kmod=0.9
print(f"massgebend: NEd={NEd:.2f} kN, kmod=0.9")
b=h=120.
A=b*h
i=0.289*h  # mm
lam=4000/i
print(f"A={A:.0f} mm2, i={i:.2f} mm, lambda={lam:.1f}")
# kc Tabelle C24: 115->0.234, 120->0.216
kc = 0.234 + (lam-115)/5*(0.216-0.234)
print(f"kc(interpoliert)={kc:.3f}")
fc0d = kmod*21/gM
sig = NEd*1e3/A
print(f"fc0d={fc0d:.2f}, sigma={sig:.2f}, eta={sig/(kc*fc0d):.3f}")

print()
print("="*60)
print("POS 2: UNTERZUG  (GL24h 200/680, L=6.5m)")
print("="*60)
B_einzug = 1.25*4.0
print(f"Einzugsbreite = 1.25*4.0 = {B_einzug} m")
g_decke = 2.5*B_einzug
g_eg = 0.6
g = g_decke+g_eg
q = 2.0*B_einzug
print(f"g_decke={g_decke}, g_EG_UZ={g_eg}, g={g}, q={q} kN/m")
L=6.5
def M_udl(w): return w*L**2/8
def M_p(P): return P*L/4
MG = M_udl(g)+M_p(G1); MQ=M_udl(q); MS=M_p(S1); MW=M_p(W1)
print(f"MG={MG:.2f} (UDL {M_udl(g):.2f} + P {M_p(G1):.2f}), MQ={MQ:.2f}, MS={MS:.2f}, MW={MW:.2f}")
lfm = {
 "LF1 1,35G":            (1.35*MG, 0.6),
 "LF2 +1,5Q":            (1.35*MG+1.5*MQ, 0.8),
 "LF3 +1,5Q+0,75S":      (1.35*MG+1.5*MQ+1.5*0.5*MS, 0.9),
 "LF4 +1,5Q+0,75S+0,9W": (1.35*MG+1.5*MQ+1.5*0.5*MS+1.5*0.6*MW, 1.0),
 "LF5 +1,5S+1,05Q":      (1.35*MG+1.5*MS+1.5*0.7*MQ, 0.9),
}
for k,(e,km) in lfm.items(): print(f"  {k:26s} Md={e:7.2f} kNm kmod={km}  Md/kmod={e/km:7.2f}")
Md = 1.35*MG+1.5*MQ; kmod_b=0.8
print(f"massgebend LF2: Md={Md:.1f} kNm, kmod=0.8")
VG = g*L/2 + G1/2; VQ=q*L/2; VS=S1/2; VW=W1/2
print(f"VG={VG:.2f}, VQ={VQ:.2f}, VS={VS:.2f}, VW={VW:.2f}")
Vd = 1.35*VG+1.5*VQ
print(f"Vd (LF2) = {Vd:.1f} kN = Auflagerkraft Ad")
bb,hb = 200.,680.
Wy = bb*hb**2/6; Iy=bb*hb**3/12
print(f"W={Wy/1e3:.0f} cm3 = {Wy:.3e} mm3, I={Iy/1e4:.0f} cm4")
fmd = 0.8*24/gM
sigm = Md*1e6/Wy
print(f"Biegung: sigma_m,d={sigm:.2f}, fm,d={fmd:.2f}, eta={sigm/fmd:.3f}  (kh=1, h>600)")
fvd = 0.8*3.5/gM
tau = 1.5*Vd*1e3/(0.714*bb*hb)
print(f"Schub: tau_d={tau:.3f}, fv,d={fvd:.3f}, eta={tau/fvd:.3f}")
# Kippen
lef = 0.9*6500+2*hb
kipp = lef*hb/bb**2
print(f"Kippen (ohne Halterung): lef={lef:.0f}, lef*h/b2={kipp:.1f} -> kcrit=1.0 (GL24h Tab. bis 160: 1.0); mit Deckenbalken e=625: {625*hb/bb**2:.1f} <=100")
print(f"h/b = {hb/bb:.2f} <= 4")
# Querdruck unter Stuetze 1
Aef1 = (120+2*30)*120
fc90d_09 = 0.9*2.5/gM
s1 = NEd*1e3/Aef1
print(f"Querdruck unter St1: Aef={Aef1:.0f}, sigma={s1:.3f}, Grenze=1.75*{fc90d_09:.3f}={1.75*fc90d_09:.3f}, eta={s1/(1.75*fc90d_09):.3f}")
# Auflager auf Stuetze 2
Aef2 = (200+2*30)*200
fc90d_08 = 0.8*2.5/gM
s2 = Vd*1e3/Aef2
print(f"Auflager auf St2: Aef={Aef2:.0f}, sigma={s2:.3f}, Grenze={1.75*fc90d_08:.3f}, eta={s2/(1.75*fc90d_08):.3f}")
# GZG
E=11500.
Lmm=6500.
kw_udl = 5*Lmm**4/(384*E*Iy)       # mm per N/mm = per kN/m
kw_p   = Lmm**3/(48*E*Iy)*1e3      # mm per kN
print(f"kw_udl={kw_udl:.4f} mm/(kN/m), kw_p={kw_p:.4f} mm/kN")
wG = g*kw_udl + G1*kw_p
wQ = q*kw_udl; wS=S1*kw_p; wW=W1*kw_p
print(f"wG={wG:.2f} (UDL {g*kw_udl:.2f} + P {G1*kw_p:.2f}), wQ={wQ:.2f}, wS={wS:.2f}, wW={wW:.2f}")
w_char_Q = wG+wQ+0.5*wS+0.6*wW
w_char_S = wG+wS+0.7*wQ+0.6*wW
print(f"winst char (Q fuehrend)={w_char_Q:.2f}, (S fuehrend)={w_char_S:.2f};  L/300={Lmm/300:.1f}")
wqs = wG+0.3*wQ
wcreep = 0.6*wqs
wfin = w_char_Q + wcreep
wnet = wqs+wcreep
print(f"wqs={wqs:.2f}, wcreep={wcreep:.2f}, wfin={wfin:.2f} <= L/200={Lmm/200:.1f}, wnet,fin={wnet:.2f} <= {Lmm/300:.1f}")
print(f"etas: 1a={w_char_Q/(Lmm/300):.2f}, 1b={wfin/(Lmm/200):.2f}, 2={wnet/(Lmm/300):.2f}")
print(f"EG Unterzug tats.: {bb/1000*hb/1000*4.2:.3f} kN/m (angesetzt 0.6)")

print()
print("="*60)
print("POS 3: STUETZE 2  (C24 20/20, h=2.6m)")
print("="*60)
egs2 = 0.2*0.2*2.6*4.2
G2 = VG + egs2
print(f"EG St2={egs2:.2f} -> G2={G2:.2f}, Q={VQ}, S={VS}, W={VW}")
lf2 = {
 "LF1 1,35G":            (1.35*G2, 0.6),
 "LF2 +1,5Q":            (1.35*G2+1.5*VQ, 0.8),
 "LF3 +1,5Q+0,75S":      (1.35*G2+1.5*VQ+1.5*0.5*VS, 0.9),
 "LF4 +1,5Q+0,75S+0,9W": (1.35*G2+1.5*VQ+1.5*0.5*VS+1.5*0.6*VW, 1.0),
 "LF5 +1,5S+1,05Q":      (1.35*G2+1.5*VS+1.5*0.7*VQ, 0.9),
}
for k,(e,km) in lf2.items(): print(f"  {k:26s} Nd={e:7.2f} kN  kmod={km}  Nd/kmod={e/km:7.2f}")
N2 = 1.35*G2+1.5*VQ
b2=200.
i2=0.289*b2
lam2=2600/i2
print(f"massgebend LF2: Nd={N2:.1f}, lambda={lam2:.1f} -> kc=0.844 (Tab. 45)")
fc0d2=0.8*21/gM
s= N2*1e3/(b2*b2)
print(f"sigma={s:.2f}, fc0d={fc0d2:.2f}, eta={s/(0.844*fc0d2):.3f}")
