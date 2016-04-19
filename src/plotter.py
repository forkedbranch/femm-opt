import matplotlib.pyplot as plt
import matplotlib
from os import path

def plot_searchpath(output_folder, prefix, evaluations):
    width = 270
    height = 270
    
    font = {'family' : 'Bitstream Vera Sans',
            'weight' : 'normal',
            'size'   : 8}
    matplotlib.rc('font', **font)

    yc = list(map(lambda x: x['center'], evaluations))
    r = list(map(lambda x: x['radius'], evaluations))

    fig = plt.figure(num=None, figsize=(6, 6), dpi=96, facecolor='w', edgecolor='k')
    fig.set_size_inches(width/96, height/96)
    
    for i in range(0, len(evaluations)):
        plt.xlim([-0.52, 0.52])
        plt.ylim([0.08, 1.42])
        plt.plot(yc[:i+1], r[:i+1], 'ro')
        
        fig.savefig('{}_{:03d}.png'.format(path.join(output_folder, prefix), i+1), dpi=96)
        fig.clf()

    # full sized final figure with labels
    font = {'family' : 'Bitstream Vera Sans',
            'weight' : 'normal',
            'size'   : 12}
    matplotlib.rc('font', **font)

    fig = plt.figure(num=None, figsize=(6, 6), dpi=96)
    plt.xlim([-0.52, 0.52])
    plt.xlabel("yc")
    plt.ylim([0.08, 1.42])
    plt.ylabel("r")
    plt.plot(yc, r, 'ro')
    fig.savefig('{}.png'.format(path.join(output_folder, prefix)))

def plot_objectives(output_folder, prefix, nl_evals, dl_evals):
    width = 560
    height = 280
    
    font = {'family' : 'Bitstream Vera Sans',
            'weight' : 'normal',
            'size'   : 10}
    matplotlib.rc('font', **font)

    nl_obj = list(map(lambda x: x['objective'] if x['objective'] < 400 else 400, nl_evals))
    dl_obj = list(map(lambda x: x['objective'] if x['objective'] < 400 else 400, dl_evals))

    fig = plt.figure(num=None, figsize=(6, 3), dpi=96, facecolor='w', edgecolor='k')
    fig.set_size_inches(width/96, height/96)
    
    for i in range(0, len(dl_obj)):
        plt.xlim([-1, len(dl_obj)])
        plt.ylim([180, 380])

        dl, = plt.plot(dl_obj[:i+1], 'rs-', label='global', markersize=4)
        nl, = plt.plot(nl_obj[:i+1], 'bo-', label='local', markersize=4)
        
        plt.ylabel("E [V/m]")
        
        plt.legend(handles=[nl, dl])
        
        fig.savefig('{}_{:03d}.png'.format(path.join(output_folder, prefix), i+1), dpi=96)
        fig.clf()
