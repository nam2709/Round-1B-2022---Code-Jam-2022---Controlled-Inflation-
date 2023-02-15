# a1 = [30, 10, 40]
# a2 = [20, 50, 60]
# tinh mean max min
import itertools
# combine lists in list
N = int(input())
for z in range(1,N+1):
	E, D  = input().split()
	E = int(E)
	D = int(D)
	u = []
	for l in range(1,E+1):
		l = list(map(int, input().split()))
		u.append(l)
		# create lists in list
	b = list(itertools.chain.from_iterable(u))
	b_l = len(b)
	
	c=[]
	g=[]
	# tim gia tri nho nhat  va lon nhat de so sanh
	for j in range(0, b_l, D):
		# print(b[j:j+D])
		# min in mot khoang
		x= min(b[j:j+D])
		c.append(x)
		y= max(b[j:j+D])
		c.append(y)


	c_l=len(c)
	print(c)
	q=[]
	if c_l > 4:
		for i in range(0,c_l-4,4):
		# 	k = abs(c[i] - c_m)
		# 	q.append(k)
		# q_s=sum(q)
		# print(q)
		# print(q_s)


				p1 = abs(c[i+2]-c[i+1])
				p2 = abs(c[i+3]-c[i+1])
				p3 = abs(c[i+4]-c[i+3])
				p4 = abs(c[i+5]-c[i+3])
				if p1 > p2 and p3 <= p4:
					t = c[i+4]
					c[i+4] = c[i+5]
					c[i+5] = t
				elif p1 > p2 and p3 > p4:
					t1 = c[i+2]
					c[i+2] = c[i+3]
					c[i+3] = t1
					t = c[i+4]
					c[i+4] = c[i+5]
					c[i+5] = t
				elif p1 <= p2 and p3 <= p4:
					c[i+2] = c[i+2]
					c[i+3] = c[i+3]
					c[i+3] = c[i+3]
					c[i+3] = c[i+3]
				elif p1 <= p2 and p3 > p4:
					t3 = c[i+4]
					c[i+4] = c[i+5]
					c[i+5] = t3
				
	elif c_l <= 4:
		for i in range(0,1):
			p1 = abs(c[i+2]-c[i+1])
			p2 = abs(c[i+3]-c[i+1])
			if p1 > p2 :
				t1 = c[i+2]
				c[i+2] = c[i+3]
				c[i+3] = t1
			elif p1 <= p2 :
				c[i+2] = c[i+2]
				c[i+3] = c[i+3]
		# for i in range(0,c_l-3,3):
		# 	print(i)
		# 	if c[i+1] < c[i+3]:
		# 		# if i == 0:
		# 		# 	d = abs(c[i+1] - 0) + abs(c[i+2] - c[i+1]) + abs(c[i+3]-c[i+2])
		# 		# else:
		# 		d = abs(c[i+1]-c[i+2]) + abs(c[i+2]-c[i+3])
		# 		g.append(d)
		# 	elif c[i+1] >= c[i+3]:
		# 		# if i == 0:
		# 		# 	e = abs(c[i+1] - 0) + abs(c[i+3]-c[i+1])  + abs(c[i+3] - c[i+2]) 
		# 		# else:
		# 		e = abs(c[i+3]-c[i+1]) + abs(c[i+2]-c[i+3])
		# 		g.append(e)

	print(c)
	for j in range(0,c_l-1):
		w = abs(c[j+1] - c[j])
		g.append(w)

	print(g)

	h=sum(g)+c[0]

	print('Case #' + str(z)+': ' +str(h))