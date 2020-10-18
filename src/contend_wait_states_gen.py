endl = '\n'
s = 'TStates,WaitStates' + endl

pattern = [6,5,4,3,2,1,0,0]

def wstates(tstate):
    tstate += 1
    line = tstate // 224
    if line < 64 or line >= 192: return 0
    halfpix = tstate % 224;
    if halfpix < 128: return 0
    return pattern[tstate%8]

for tstate in range(69888):
    s += str(tstate) + ',' + str(wstates(tstate)) + endl;

fn = "contend_wait_states.csv"
f = open(fn, 'wt')
f.write(s)
f.close()

