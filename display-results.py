import pandas as pd
#import tkinter
import sys
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # Or 'Qt5Agg', 'WebAgg', etc.
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D


# --- Example dataframe with 180 rows ---
#np.random.seed(0)
#df = pd.DataFrame({
#    "category": np.random.choice(["A", "B", "C", "D"], size=180),
#    "label": [f"ID{i:04d}" for i in range(180)]  # 7-char identifiers
#})

def finalresult(row):
	if len(row) > 5: # file had some bitswaps, check that first
		if row[5]=='bitswap':
			return 'BitSwap'
	if row['bpsresult']=='GoodBps':
		return 'Good'
	elif row['netresult']=='Bad':
		return 'CommFail'
	elif row['bpsresult']=='BadBps' or np.isnan(row['bpsresult']):
		return "NoiseFail"
	else:
		return None

# if we get a parameter, assume that is the filename we will use, otherwise we'll pop up the tk dialog
print(sys.argv)
if len(sys.argv) >= 1 : #We got some arguments passed to our python code, it should be the input file
	inputCSVfile=sys.argv[1]
	print("Using input file ",inputCSVfile)
	listlen=1
else:
	from tkinter import filedialog as fd
	inputCSVfile=selectFile('')
	listlen=len(inputCSVfile)
	print('listlen=',listlen)
	print('inputCSVfiles=',inputCSVfiles)
	if listlen<1:
		exit("Must enter one or more (with ctrl-click) files to use")

# read in the batchsummary csv file
batchresults=pd.read_csv(inputCSVfile)

# find the number of entries and columns
entries,columns=batchresults.shape

if entries%90 or entries > 180 :
	print("batch has ",entries," entries, typically expect 90 or 180")
	exit()

if columns > 5 :
	print("Found ",columns," columns, there must be some with bitswap")

# determine the category for each entry

batchresults['final']=batchresults.apply(finalresult,axis=1)

print(batchresults)

# pass dataframe with finalresults and serial numbers
df=batchresults[['final','ChipSN']]
df=df.rename(columns={'final':'category','ChipSN':'label'})
print(df)

# --- Assign colors to categories ---
category_colors = {
    "NoiseFail": "lightcoral",
    "BitSwap": "skyblue",
    "Good": "lightgreen",
    "CommFail": "khaki"
}

# --- Function to draw one 15x6 grid ---
def draw_grid(ax, data, title=""):
    rows, cols = 15, 6   # 15 tall × 6 wide
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            if idx >= len(data):
                continue
            category = data.iloc[idx]["category"]
            label = data.iloc[idx]["label"]

            # Draw colored square
            rect = patches.Rectangle(
                (j, rows - 1 - i), 1, 1,
                facecolor=category_colors.get(category, "white"),
                edgecolor="black"
            )
            ax.add_patch(rect)

            # Add centered label
            ax.text(
                j + 0.5, rows - 1 - i + 0.5,
                label,
                ha="center", va="center",
                fontsize=9, family="monospace"
            )

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=12)

# --- Split into two halves (90 each) ---
data1 = df.iloc[:90]
data2 = df.iloc[90:]

# --- Plot ---
fig, axes = plt.subplots(1, 2, figsize=(16, 10))

draw_grid(axes[0], data1, "Grid 1 (first 90)")
draw_grid(axes[1], data2, "Grid 2 (last 90)")

# --- Add legends outside the axes ---
for ax in axes:
    legend_elements = [
        Line2D([0], [0], marker='s', color='w',
               markerfacecolor=color, markersize=15, label=cat)
        for cat, color in category_colors.items()
    ]
    ax.legend(handles=legend_elements, loc="center left",
              bbox_to_anchor=(1.02, 0.5), fontsize=9, frameon=False)

plt.tight_layout()

svgfile=inputCSVfile.replace("csv","png")
plt.savefig(svgfile,format='png')

plt.show()