import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
key = [150, 160, 170, 172, 176]
fig, ax = plt.subplots(figsize=(7,4))
ax.plot(key)
for i , p in enumerate(key):
    ax.annotate(f"{p}cm",(i,p), textcoords="offset points", xytext=(0,8), ha= 'center')

ax.set_title("나의 키 변화")
fig.savefig("my_first_chart.png")
