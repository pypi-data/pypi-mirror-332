# botionplotlib/core.py
# A beautiful and functional redesign of matplotlib defaults

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import os
from matplotlib.animation import PillowWriter
import re
from mpl_toolkits.mplot3d import Axes3D  # Import the 3D toolkit

def apply_style():
    """Apply the Botionplotlib style globally to all matplotlib plots"""
    
    # Set the dark mode aesthetic
    plt.style.use('dark_background')
    
    # Define Apple-inspired colors
    apple_blue = '#0071e3'
    apple_green = '#34c759'
    apple_orange = '#ff9500'
    apple_red = '#ff3b30'
    apple_purple = '#af52de'
    apple_yellow = '#ffcc00'
    
    # Create a custom colormap
    colors = [apple_blue, apple_purple, apple_red, apple_orange, apple_yellow, apple_green]
    apple_cmap = LinearSegmentedColormap.from_list('apple_cmap', colors)
    
    # Register the colormap correctly
    mpl.colormaps.register(apple_cmap, name='apple_cmap')
    
    # Set default colors for plots
    mpl.rcParams['axes.prop_cycle'] = plt.cycler('color', colors)
    
    # Improve figure aesthetics
    mpl.rcParams['figure.facecolor'] = '#1c1c1e'  # Dark background
    mpl.rcParams['axes.facecolor'] = '#1c1c1e'
    mpl.rcParams['savefig.facecolor'] = '#1c1c1e'
    
    # Set default figure size to ensure 1000x1000px output
    mpl.rcParams['figure.figsize'] = [10.0, 10.0]
    mpl.rcParams['figure.dpi'] = 100  # This will make figures 1000x1000 pixels
    
    # Grid styling
    mpl.rcParams['grid.color'] = '#333333'
    mpl.rcParams['grid.linestyle'] = '--'
    mpl.rcParams['grid.linewidth'] = 0.5
    
    # Text styling
    mpl.rcParams['text.color'] = 'white'
    mpl.rcParams['axes.labelcolor'] = 'white'
    mpl.rcParams['xtick.color'] = 'white'
    mpl.rcParams['ytick.color'] = 'white'
    
    # Font styling
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = ['SF Pro Display', 'Arial', 'Helvetica', 'DejaVu Sans']
    mpl.rcParams['font.size'] = 10
    mpl.rcParams['axes.titlesize'] = 14
    mpl.rcParams['axes.labelsize'] = 12
    
    # Line styling
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.markersize'] = 8
    
    # Position legend at the bottom center by default
    mpl.rcParams['legend.loc'] = 'lower center'
    mpl.rcParams['legend.frameon'] = False
    
    # Adjust figure margins to accommodate bottom legend
    mpl.rcParams['figure.subplot.bottom'] = 0.15
    
    # Set default colormap for imshow and other color-based plots
    mpl.rcParams['image.cmap'] = 'apple_cmap'
    
    # Create output directory if it doesn't exist
    os.makedirs('botionplotlib_output', exist_ok=True)
    
    # Override the legend function to position it at the bottom center
    original_legend = plt.legend
    
    def new_legend(*args, **kwargs):
        # Set default position to bottom center below the plot
        if 'bbox_to_anchor' not in kwargs and 'loc' not in kwargs:
            kwargs['bbox_to_anchor'] = (0.5, -0.15)
            kwargs['loc'] = 'lower center'
        
        return original_legend(*args, **kwargs)
    
    # Replace the legend function
    plt.legend = new_legend
    
    # Override the imshow function to use our colormap by default
    original_imshow = plt.imshow
    
    def new_imshow(X, **kwargs):
        if 'cmap' not in kwargs:
            kwargs['cmap'] = 'apple_cmap'
        return original_imshow(X, **kwargs)
    
    plt.imshow = new_imshow
    
    # Override the plot_surface method for 3D plots - correctly targeting the Axes3D class
    original_plot_surface = Axes3D.plot_surface
    
    def new_plot_surface(self, X, Y, Z, **kwargs):
        if 'cmap' not in kwargs:
            kwargs['cmap'] = 'apple_cmap'
        if 'vmin' not in kwargs or 'vmax' not in kwargs:
            # Set a reasonable range for the colormap
            vmin = np.min(Z)
            vmax = np.max(Z)
            kwargs['vmin'] = vmin
            kwargs['vmax'] = vmax
        return original_plot_surface(self, X, Y, Z, **kwargs)
    
    Axes3D.plot_surface = new_plot_surface
    
    # Helper function to sanitize title for filename
    def sanitize_title(title):
        if not title:
            return "untitled"
        # Replace spaces and special characters with underscores
        sanitized = re.sub(r'[^\w\s-]', '', title).strip().lower()
        sanitized = re.sub(r'[-\s]+', '_', sanitized)
        return sanitized
    
    # Override the show function to save figures automatically but not display them
    original_show = plt.show
    
    def new_show(*args, **kwargs):
        # Get all current figures
        figs = [plt.figure(num) for num in plt.get_fignums()]
        
        for i, fig in enumerate(figs):
            # Save static figures as PNG with title-based filename
            if not hasattr(fig, '_botionplotlib_animation'):
                # Try to get the title from the figure
                title = None
                for ax in fig.get_axes():
                    if ax.get_title():
                        title = ax.get_title()
                        break
                
                if title:
                    filename = f'botionplotlib_output/{sanitize_title(title)}.png'
                else:
                    filename = f'botionplotlib_output/figure_{i+1}.png'
                
                fig.savefig(filename, dpi=100, bbox_inches='tight')
                print(f"Saved figure to {filename}")
        
        # Don't actually show the plots - just save them
        plt.close('all')
    
    # Replace the show function
    plt.show = new_show
    
    # Override FuncAnimation to save as GIF automatically
    original_funcanimation = plt.matplotlib.animation.FuncAnimation
    
    def new_funcanimation(*args, **kwargs):
        anim = original_funcanimation(*args, **kwargs)
        
        # Mark the figure as containing an animation
        if len(args) > 0 and hasattr(args[0], 'number'):
            fig = plt.figure(args[0].number)
            fig._botionplotlib_animation = True
            
            # Try to get the title for the filename
            title = None
            for ax in fig.get_axes():
                if ax.get_title():
                    title = ax.get_title()
                    break
            
            if title:
                filename = f'botionplotlib_output/{sanitize_title(title)}.gif'
            else:
                filename = f'botionplotlib_output/animation_{fig.number}.gif'
            
            anim.save(filename, writer=PillowWriter(fps=20))
            print(f"Saved animation to {filename}")
        
        return anim
    
    plt.matplotlib.animation.FuncAnimation = new_funcanimation
    
    print("Botionplotlib style applied globally (legend below, custom colormaps)")
    print("All figures will be saved as 1000x1000px PNGs and animations as GIFs")
    print("Output directory: botionplotlib_output/")
    
    return apple_cmap 

def plot(self, x, y, title=None, xlabel=None, ylabel=None, **kwargs):
    # ... existing code ...
    if title:
        # Increase title font size and make it bold
        plt.title(title, fontsize=16, fontweight='bold')
    if xlabel:
        # Increase x-axis label font size
        plt.xlabel(xlabel, fontsize=14)
    if ylabel:
        # Increase y-axis label font size
        plt.ylabel(ylabel, fontsize=14)
    # ... existing code ...

def scatter(self, x, y, title=None, xlabel=None, ylabel=None, **kwargs):
    # ... existing code ...
    if title:
        plt.title(title, fontsize=16, fontweight='bold')
    if xlabel:
        plt.xlabel(xlabel, fontsize=14)
    if ylabel:
        plt.ylabel(ylabel, fontsize=14)
    # ... existing code ... 

def plot3d(self, x, y, z, title=None, xlabel=None, ylabel=None, zlabel=None, **kwargs):
    # ... existing code ...
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Add this line to increase the padding/margins
    plt.tight_layout(pad=3.0)  # Increase padding around the plot
    
    # Or alternatively, use figure.subplots_adjust
    # fig.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
    
    if title:
        ax.set_title(title, fontsize=16, fontweight='bold')
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=14, labelpad=10)  # Add labelpad to push axis label out
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=14, labelpad=10)
    if zlabel:
        ax.set_zlabel(zlabel, fontsize=14, labelpad=10)
    # ... existing code ... 

def histogram(self, data, bins=10, title=None, xlabel=None, ylabel=None, **kwargs):
    # ... existing code ...
    
    # Enhanced aesthetics for histograms
    hist_color = kwargs.get('color', '#5199FF')  # Default to a nice blue
    edge_color = kwargs.get('edgecolor', '#0066CC')  # Darker blue for edges
    alpha = kwargs.get('alpha', 0.8)  # Semi-transparent bars
    
    plt.hist(data, bins=bins, color=hist_color, edgecolor=edge_color, 
             alpha=alpha, linewidth=1.5)
    
    # Add a subtle grid for better readability
    plt.grid(alpha=0.3, linestyle='--')
    
    if title:
        plt.title(title, fontsize=16, fontweight='bold')
    if xlabel:
        plt.xlabel(xlabel, fontsize=14)
    if ylabel:
        plt.ylabel(ylabel, fontsize=14)
        
    # Add some padding to the layout
    plt.tight_layout()
    # ... existing code ... 