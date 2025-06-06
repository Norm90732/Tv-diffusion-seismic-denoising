import numpy as np
import segyio

from pathlib import Path

with segyio.open(Path("data/raw/ST0202R08_PZ_PSDM_FULL_OFFSET_PP_TIME.MIG_FIN.POST_STACK.3D.JS-017534.segy")) as segyfile:
    data_to_np = segyio.tools.cube(segyfile)
    data_to_np.astype(np.float32)
    print(f"Data shape: {data_to_np.shape}")
    print(f"Data type: {data_to_np.dtype}")
    print(f"Min value: {data_to_np.min()}")
    print(f"Max value: {data_to_np.max()}")
    print(f"Mean value: {data_to_np.mean()}")
    print(f"Number of non-zero values: {np.count_nonzero(data_to_np)}")
    print(f"Total number of values: {data_to_np.size}")


    np.save("data/processed/ST0202_full_cube_notnormal.npy",data_to_np)
    
    data_to_np_normalized = data_to_np.copy()
    data_to_np_normalized_min = data_to_np_normalized.min()
    data_to_np_normalized_max = data_to_np_normalized.max()
    data_to_np_normalized_scaled = 2* (data_to_np_normalized - data_to_np_normalized_min) / (data_to_np_normalized_max - data_to_np_normalized_min) -1

    np.save("data/processed/ST0202_full_cube_normalized.npy",data_to_np_normalized_scaled)

#Depth, inline, crossline dimension for cube 


