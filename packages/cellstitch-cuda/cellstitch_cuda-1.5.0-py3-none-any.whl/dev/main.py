import tifffile
from cellstitch_cuda.pipeline import cellstitch_cuda, correction

# img = r"Z:\Rheenen\tvl_jr\SP8\2024Nov22_SI_1mg_1year_3D_2D-merge\Villus_crops\2024Nov22_SI_1mg_1year_3D_2D-merge-1-2\2.tif"

# cellstitch_cuda(
#     img,
#     # output_path=r"Z:\Rheenen\tvl_jr\SP8\2025Feb19_Ileum_8d_fresh_3D\2025Feb19_Ileum_8d_fresh_3D-1",
#     output_masks=True,
#     verbose=True,
#     seg_mode="nuclei_cells",
#     # interpolation=True,
#     n_jobs=-1,
#     z_step=3.5/2,
#     pixel_size=1/2.2,
#     bleach_correct=False,
# )

masks = tifffile.imread(r"Z:\Rheenen\tvl_jr\SP8\2025Feb19_Ileum_8d_fresh_3D\2025Feb19_Ileum_8d_fresh_3D-1\cellstitch_masks.tif")

masks = correction(masks, n_jobs=1)

tifffile.imwrite(r"Z:\Rheenen\tvl_jr\SP8\2025Feb19_Ileum_8d_fresh_3D\2025Feb19_Ileum_8d_fresh_3D-1\cellstitch_masks_split.tif", masks)
