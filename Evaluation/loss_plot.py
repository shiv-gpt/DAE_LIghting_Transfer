import argparse
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pdb

parser = argparse.ArgumentParser()
parser.add_argument('--file_path', type=str)
parser.add_argument('--output_name', type=str)
opt = parser.parse_args()

def show_plot(iteration,loss, fname, ltype):
    # print(loss)
    plt.plot(iteration,loss)
    plt.xlabel("epochs")
    plt.ylabel("loss")

    # plt.show()
    plt.savefig(fname + '_loss_plot_' + ltype + '.png')
    plt.clf()


def parse_file(opt):
    with open(opt.file_path, "r+") as f:
        content = f.readlines()

    total_loss = []
    recon_loss = []
    intr_s_loss = []
    br_loss = []
    tvw_loss = []
    iterations = []
    i = 0

    for l in content:
        l = l.split("..")
        if "Iteration" in l[0]:


            i += 1
            # try:
            l[0] = l[0].split("--")[1].split(":")[1].lstrip(" ").rstrip(" ")
            l[1] = l[1].split(":")[1].lstrip(" ").rstrip(" ")
            l[2] = l[2].split(":")[1].lstrip(" ").rstrip(" ")
            l[3] = l[3].split(":")[1].lstrip(" ").rstrip(" ")
            l[4] = l[4].split(":")[1].lstrip(" ").rstrip(" ")
            # except:
            #     pdb.set_trace()
            # print(l[0])
            # print(l[2])
            # print(l[1])
            # print(l[1])
            # print(l[1])
            # if i%100 == 0:
            iterations.append(i)
            total_loss.append(float(l[0]))
            recon_loss.append(float(l[1]))
            tvw_loss.append(float(l[2]))
            br_loss.append(float(l[3]))
            intr_s_loss.append(float(l[4]))

    show_plot(iterations, total_loss, opt.output_name, "total_loss_")
    show_plot(iterations, recon_loss, opt.output_name, "recon_loss_")
    show_plot(iterations, br_loss, opt.output_name, "br_loss_")
    show_plot(iterations, tvw_loss, opt.output_name, "tvw_loss_")
    show_plot(iterations, intr_s_loss, opt.output_name, "intr_s_loss_")


parse_file(opt)