def a(s,part1,part2):
	s={v:idx for idx, v in enumerate(s)}
	pt1=[s.get(v,-1) for v in part1]
	pt2=[s.get(v,-1) for v in part2]
	if pt1==sorted(pt1) and pt2==sorted(pt2) and sum(s.values())==sum(pt1+pt2):
		return True
	return False