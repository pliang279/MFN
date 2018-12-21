import os
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', default='mosi', type=str)
args = parser.parse_args()

if args.type == 'mosi_mfn':
	alldir = '/media/bighdd7/paul/cluster/temp/'
if args.type == 'mosi':
	alldir = '/media/bighdd7/paul/cluster/res_mfm2/'
if args.type == 'mmmo':
	alldir = '/media/bighdd7/paul/cluster/res_mfm_mmmo/'
if args.type == 'moud':
	alldir = '/media/bighdd7/paul/cluster/res_mfm_moud/'
if args.type == 'you':
	alldir = '/media/bighdd7/paul/cluster/res_mfm_you/'
if args.type == 'missing':
	alldir = '/media/bighdd7/paul/cluster/res_mfm_missing4/'

ttt = 'v'
if 'missing' in alldir:
	arr = os.listdir(alldir)
	arr.sort()
	all_present = []
	l_missing = []
	a_missing = []
	v_missing = []
	for file2 in arr:
		if file2.endswith(".txt"):
			name = alldir + file2
			with open(name) as file:
				a = []
				b = []
				c = []
				d = []
				e = []
				configs = []
				tot = 0
				add = False
				n_err = 0
				for line in file.readlines():
					if 'all present' in line:
						error = [float(err) for err in line.split()[2:]]
						all_present.append(error)
					if 'l missing' in line:
						error = [float(err) for err in line.split()[2:]]
						l_missing.append(error)
					if 'a missing' in line:
						error = [float(err) for err in line.split()[2:]]
						a_missing.append(error)
					if 'v missing' in line:
						error = [float(err) for err in line.split()[2:]]
						v_missing.append(error)

					if ttt =='l':
						if 'scoring y_hat_nol' in line:
							add = True
						if 'scoring y_hat_noa' in line or 'scoring y_hat_nov' in line:
							add = False
					if ttt =='a':
						if 'scoring y_hat_noa' in line:
							add = True
						if 'scoring y_hat_nol' in line or 'scoring y_hat_nov' in line:
							add = False
					if ttt =='v':
						if 'scoring y_hat_nov' in line:
							add = True
						if 'scoring y_hat_nol' in line or 'scoring y_hat_noa' in line:
							add = False
					if add:
						if "Accuracy" in line:
							a.append(float(line.split()[1]))
						if "avg" in line and "total" in line:
							b.append(float(line.split()[5]))
						if 'weighted avg' in line:
							b.append(float(line.split()[4]))
						if "mae" in line and len(line.split()) == 2:
							c.append(float(line.split()[1]))
						if "corr:" in line:
							d.append(float(line.split()[1]))
						if "mult_acc" in line:
							e.append(float(line.split()[1]))
				print file2, tot

				a0 = np.nanmax(np.array(a))
				b0 = np.nanmax(np.array(b))
				print 'acc:', a0
				print 'fscore:', b0
				c0 = np.nanmin(np.array(c))
				d0 = np.nanmax(np.array(d))
				e0 = np.nanmax(np.array(e))
				print 'mae:', c0
				print 'corr:', d0
				print 'mult_acc:', e0
				print

	print np.array(all_present).shape
	print np.array(l_missing).shape
	print np.array(a_missing).shape
	print np.array(v_missing).shape
	all_present = np.min(np.array(all_present),axis=0)
	l_missing = np.min(np.array(l_missing),axis=0)
	a_missing = np.min(np.array(a_missing),axis=0)
	v_missing = np.min(np.array(v_missing),axis=0)
	print 'all_present', all_present
	print 'l_missing', l_missing
	print 'a_missing', a_missing
	print 'v_missing', v_missing
	assert False

a0 = []
b0 = []
c0 = []
d0 = []

arr = os.listdir(alldir)
arr.sort()
for file2 in arr:
	if file2.endswith(".txt"):
		name = alldir + file2
		if args.type == 'ie2':
			a0 = []
			b0 = []
			c0 = []
			d0 = []
		if ('pom' in alldir and args.type != 'pom3' and args.type != 'pom4') or args.type == 'ie2':
			with open(name) as file:
				tot = 0
				for line in file.readlines():
					tot += 1
					if "mae:" in line and 'test' not in line:
						curr = [float(x) for x in line[line.index('[')+1:line.index(']')].split(',')]
						a0.append(curr)
					if "corr:" in line:
						curr = [float(x) for x in line[line.index('[')+1:line.index(']')].split(',')]
						b0.append(curr)
					if "mult_acc:" in line:
						curr = [float(x) for x in line[line.index('[')+1:line.index(']')].split(',')]
						c0.append(curr)
				print file2, tot
			try:
				if args.type == 'ie2':
					i = 0
					af = []
					bf = []
					cf = []
					df = []
					for (a,b,c,d) in [(a0,b0,c0,d0)]:
						af += [list(np.nanmin(np.array(a),axis=0))]
						bf += [list(np.nanmax(np.array(b),axis=0))]
						cf += [list(np.nanmax(np.array(c),axis=0))]
						a = zip(np.nanmin(np.array(a),axis=0),np.argmin(np.array(a),axis=0))
						b = zip(np.nanmax(np.array(b),axis=0),np.argmax(np.array(b),axis=0))
						c = zip(np.nanmax(np.array(c),axis=0),np.argmax(np.array(c),axis=0))
						want = [0,1,2]
						print 'mae:', '&'.join([[str(round(x,3)) for (x,lx) in a][ind] for ind in want])
						print 'corr:', '&'.join([[str(round(x,3)) for (x,lx) in b][ind] for ind in want])
						print
						i += 1
			except:
				print 'not yet'
			print
		else:
			with open(name) as file:
				a = []
				b = []
				c = []
				d = []
				e = []
				configs = []
				tot = 0
				for line in file.readlines():
					if 'OrderedDict' in line:
						tot += 1
						configs.append(line)
					if "Accuracy" in line:
						a.append(float(line.split()[1]))
					if "avg" in line and "total" in line:
						b.append(float(line.split()[5]))
					if 'weighted avg' in line:
						b.append(float(line.split()[4]))
					if "mae" in line and len(line.split()) == 2:
						c.append(float(line.split()[1]))
					if "corr:" in line:
						d.append(float(line.split()[1]))
					if "mult_acc" in line:
						e.append(float(line.split()[1]))
				print file2, tot
				#try:
				if 'you' in args.type or 'moud' in args.type or 'ie' in args.type or args.type == 'mmmo2' or args.type == 'pom3' or 'mosi_acc' in args.type:
					a0 = np.nanmax(np.array(a))
					b = np.nanmax(np.array(b))
					print 'acc:', a0
					print 'fscore:', b
					best = list(a).index(a0)
					# print configs[best]
				elif args.type == 'pom4':
					c0 = np.nanmin(np.array(c))
					d = np.nanmax(np.array(d))
					e = np.nanmax(np.array(e))
					print 'mae:', c0
					print 'corr:', d
					print 'mult_acc:', e
					best = list(c).index(c0)
					# print configs[best]
				elif 'mosi' in args.type or args.type == 'mmmo':
					a0 = np.nanmax(np.array(a))
					b0 = np.nanmax(np.array(b))
					print 'acc:', a0
					print 'fscore:', b0
					try:
						c0 = np.nanmin(np.array(c))
						d0 = np.nanmax(np.array(d))
						e0 = np.nanmax(np.array(e))
						print 'mae:', c0
						print 'corr:', d0
						print 'mult_acc:', e0
						best = list(c).index(c0)
					except:
						pass
					print


if ('pom' in alldir and args.type != 'pom3' and args.type != 'pom4'):
	i = 0
	af = []
	bf = []
	cf = []
	df = []
	for (a,b,c,d) in [(a0,b0,c0,d0)]:
		af += [list(np.nanmin(np.array(a),axis=0))]
		bf += [list(np.nanmax(np.array(b),axis=0))]
		cf += [list(np.nanmax(np.array(c),axis=0))]
		a = zip(np.nanmin(np.array(a),axis=0),np.argmin(np.array(a),axis=0))
		b = zip(np.nanmax(np.array(b),axis=0),np.argmax(np.array(b),axis=0))
		c = zip(np.nanmax(np.array(c),axis=0),np.argmax(np.array(c),axis=0))
		#d = np.max(np.array(d),axis=0)
		if 'pom' in alldir:
			want = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16]
		if args.type == 'ie2':
			want = [0,1,2]
		print 'mae:', '&'.join([[str(round(x,3)) for (x,lx) in a][ind] for ind in want])
		print 'corr:', '&'.join([[str(round(x,3)) for (x,lx) in b][ind] for ind in want])
		if 'pom' in alldir:
			print 'acc:', '&'.join([[str(round(x,3)*100.0) for (x,lx) in c][ind] for ind in want])

		print
		i += 1

assert False

