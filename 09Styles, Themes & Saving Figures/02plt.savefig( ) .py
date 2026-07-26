'''
Saving Figures: Once you’ve created a plot in Matplotlib, you can save it 
                as an image file (PNG, JPG, SVG, PDF, etc.) using plt.savefig().

        Basic Syntax: plt.savefig("sales.png")
        Always save before calling: plt.show()

        
        plt.savefig(file_name, dpi=300, bbox_inches='tight, transparent=True,facecolor="lightgreen", edgecolor="black" )

        🔹Common Parameters:
            file_name - 	Name of file to be saved with extension.
                	"plot.png" - Best for: Websites, PowerPoint, Portfolio projects
                    "plot.jpg" - Smaller file size, but lossy (slight quality reduction).
                    "plot.pdf" - Best for: Research papers, Reports, Printing.
                                 PDF is vector-based, so it stays sharp when zoomed.
                    "plot.svg" - Excellent for: Web graphics, Logos, High-quality scalable diagrams

            dpi(Dots Per Inch) - Higher DPI means higher resolution. 100 for Screen viewing,
                                 200 for Presentations, 300	for Reports and projects, 600 Publications and print

            bbox_inches - Remove Extra White Space. Sometimes saved images have large empty borders.
                          This crops unnecessary margins automatically.
            
            transparent - Transparent background. Useful for logos or slides.
         
            facecolor -	Background color of a plot to be saved.
                        
   

'''

import matplotlib.pyplot as plt

plt.style.use("ggplot")

fig, ax = plt.subplots(figsize=(10,6))

months = ["Jan","Feb","Mar","Apr","May"]

sales = [15,18,22,30,35]

ax.plot(
    months,
    sales,
    marker="o",
    linewidth=2
)

ax.set_title(
    "Monthly Sales",
    fontsize=18,
    fontweight="bold",
    fontfamily='sans-serif',
    pad=10
)

ax.set_xlabel("Month",
              fontsize=14,
              fontweight="bold",
              color="#333333",
              fontfamily="sans-serif")

ax.set_ylabel("Revenue",
              fontsize=14,
              fontweight="bold",
              color="#333333",
              fontfamily="sans-serif")

ax.grid(alpha=0.3)

plt.savefig(
    "monthly_sales.pdf",
    dpi=300,
    bbox_inches="tight",
    facecolor="lightyellow"
  
)

plt.show()