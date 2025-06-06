import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split

#Creating smaller sectioned cubes, allocating training, validation, testing

def patch_cube(cube, patch_size, stride):
    patches = []
    for i in range(0, cube.shape[0] - patch_size[0] + 1, stride[0]):
        for j in range(0, cube.shape[1] - patch_size[1] + 1, stride[1]):
            for k in range(0, cube.shape[2] - patch_size[2] + 1, stride[2]):
                patch = cube[i:i+patch_size[0], j:j+patch_size[1], k:k+patch_size[2]]
                patches.append(patch)
    return patches

filePath = Path('../data/processed/ST0202_full_cube_normalized.npy')

array = np.load(filePath)

patches = patch_cube(array, (32,32,32), (16,16,16))
patches = np.array(patches)
print(patches.shape)


train, temp = train_test_split(patches, test_size=0.2, random_state=39)
val,test = train_test_split(temp, test_size=0.5, random_state=39)

np.save('../data/processed/train_patches.npy', train)
np.save('../data/processed/val_patches.npy', val)
np.save('../data/processed/test_patches.npy', test)

print(train.shape, val.shape, test.shape)