# horiz bar
# heatmap
# stacked bar
# boxplot
# column sparkline
# win/loss sparkline
# treemap
# matrix diagram
# pictorial fracrion
# horiz hist
# waffle
# funnel
# linear process diag
# grouped bar
# nested/layered proportional area
# pictorial unit
# dot plot
# pyramid diag
# dumbell plot
# bullet diag
# venn diag
# partition layer chart icicle diag
# stepped line graph
# scaled up number
# lolypop chart
# tally chart
# comparison chart
# kagi chart
# dot matix
# pictogram
# stem and leaf 


barFull=""
bar7_8th=""
bar6_8th=""
bar5_8th=""
bar4_8th=""
bar3_8th=""
bar2_8th=""
bar1_8th=""
barSpace="" #Unicode full char width spacing char



def bar(d,w,lineBreaks=False):
  """Return a bar plot given a dict d of {"Label":value} pairs and maximum line width, w."""
  maxBarWidth=w-max(list(map(len,d.keys())))
  

testd={"Abc":20,"Def geh":30,"Ijk":40,"Lmnop":10}
testw=40

bar(testd,testw)

