import optimizer
import nlopt
import utils
import plotter
import imagecomposer
import config

from shutil import rmtree
from os import path

OUTPUT_FOLDER = config.get_output_folder()

rmtree(OUTPUT_FOLDER, True)
 
print('Running local Nelder-Mead optimization...')
nl_evals = optimizer.optimize(nlopt.LN_NELDERMEAD, "NelderMead", OUTPUT_FOLDER)

print('Running global Direct-L optimization...')
dl_evals = optimizer.optimize(nlopt.GN_DIRECT_L, "DirectL", OUTPUT_FOLDER)
 
print('Writing evaluation log files...')
utils.write_evallog(path.join(OUTPUT_FOLDER, 'NelderMead_eval.dat'), nl_evals)
utils.write_evallog(path.join(OUTPUT_FOLDER, 'DirectL_eval.dat'), dl_evals)

print('Creating plots...')
plotter.plot_searchpath(OUTPUT_FOLDER, "NelderMead_searchpath", nl_evals)
plotter.plot_searchpath(OUTPUT_FOLDER, "DirectL_searchpath", dl_evals)
plotter.plot_objectives(OUTPUT_FOLDER, "Objective", nl_evals, dl_evals)

print('Preparing composite images and the movie...')
imagecomposer.make_movie(OUTPUT_FOLDER, "NelderMead", "DirectL", "Objective", 
                         nl_evals, dl_evals, "OptimizationMovie")

print('All done.')
