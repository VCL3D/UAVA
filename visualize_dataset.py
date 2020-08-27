import argparse
import sys
import dataset
import visualization
import torch


def parse_arguments(args):
    usage_text = (
        "UAVA tools."
        "Usage:  python visualize_dataset.py [options],"
        "   with [options]: (as described below)"
    )
    parser = argparse.ArgumentParser(description=usage_text)
    # durations
    parser.add_argument('-b',"--batch_size", default=8, type = int, help = "Train with a <batch_size> number of samples each train iteration.")
    parser.add_argument("--test_batch_size", default= 8, type = int, help = "Test with a <batch_size> number of samples each test iteration.")    
    parser.add_argument('-w','--workers', type=int, default=4, help='Test model every <test_iters> iterations.')
    # paths
    parser.add_argument("--root_path", type = str, help = "Path to the root folder containing all the files")
    parser.add_argument("--trajectory_path", type = str, help = "Path containing the ground_truth poses")
    #dataset parameters
    parser.add_argument("--view_list",nargs="*", type=str, default = ["egocentric","exocentric"], help = "List of views to be loaded")
    parser.add_argument("--drone_list",nargs="*", type=str, default = ["M2ED"], help = "List of drone models to be loaded")
    parser.add_argument("--frame_list",nargs="*", type=int, default = [0,1], help = "List of frames to be included")
    parser.add_argument("--types_list",nargs="*", type=str, default = ["colour", "depth","silhouette","normal"], help = "List of different modalities to be loaded")


    return parser.parse_known_args(args)



if __name__ == "__main__":
    #parse arguments
    args, unknown = parse_arguments(sys.argv)
    # training data loader
    #NOTE: use the data_split flag(e.g. "train", "test" , "val") to load the correct split
    train_data_params = dataset.dataloader.DataLoaderParams(\
        root_path=args.root_path, trajectories_dir = args.trajectory_path,data_split = "train", drone_list = args.drone_list,view_list=args.view_list,\
        frame_list = args.frame_list, types_list = args.types_list, transform = None) 
    train_data_iterator = dataset.dataloader.DataLoad(train_data_params)
    train_set = torch.utils.data.DataLoader(train_data_iterator,\
        batch_size = args.batch_size, shuffle=True,\
        num_workers = args.workers, pin_memory=False)

    
    #initialise visualiser
    viz = visualization.VisdomImageVisualizer("UAVA", "127.0.0.1")
    #TODO: add a visualisation script to be added in the UAVA dataset
    for batch_id, batch in enumerate(train_set):
        #exocentric -- frame_0
        viz.show_images_grid(batch['exocentric'][0]["colour"], "Exocentric view colour")
        viz.show_depths_grid(batch['exocentric'][0]["depth"], "Exocentric view depth")
        viz.show_normals_grid(batch['exocentric'][0]["normal"], "Exocentric view normals")
        viz.show_images_grid(batch['exocentric'][0]["silhouette"], "Exocentric view silhouette masks")
        #egocentric -- frame_0
        viz.show_images_grid(batch['egocentric'][0]["colour"], "Egocentric view colour")
        viz.show_depths_grid(batch['egocentric'][0]["depth"], "Egocentric view depth")
        viz.show_normals_grid(batch['egocentric'][0]["normal"], "Egocentric view normals")
