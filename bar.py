def bar(d,w,lineBreaks=False):
  """Return a bar plot given a dict d of {"Label":value} pairs and maximum line width, w."""
  maxBarWidth=w-max(list(map(len,d.keys())))
  

testd={"Abc":20,"Def geh":30,"Ijk":40,"Lmnop":10}
testw=40

bar(testd,testw)

