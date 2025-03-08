from padocc.operations import GroupOperation

lakes = GroupOperation('lakes1',workdir='/home/users/dwest77/cedadev/padocc/padocc/tests/auto_testdata_dir',verbose=1)

#lakes.init_from_file('/home/users/dwest77/cedadev/padocc/padocc/tests/lakes/L3S_v2.1.csv')

lakes.run('scan',mode='kerchunk', forceful=True, thorough=True)