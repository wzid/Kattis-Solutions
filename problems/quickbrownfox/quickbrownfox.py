for l in[*open(0)][1:]:
 print((s:=set(map(chr,range(97,123)))-set(l.lower()))and'missing '+''.join(sorted(s))or'pangram')