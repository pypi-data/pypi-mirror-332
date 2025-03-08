from rasterops import rasterops, compute
from osgeo import gdal
import os
import uuid
import shutil
import warnings
import rioxarray as rxr


class Export:
    
    def __init__(
        self,
        dc: rasterops.DataCube,
    ):
        self.dc = dc
    
    def export_as_tif(
        self,
        var: str,
        output: str,
        tmp_dir: str | None = None,
        group: str = None,
        idxs: list[tuple[int, int]] = [],
        COG=False,
    ) -> None:
        if tmp_dir is None:
            id = str(uuid.uuid4())
            tmp_dir = f"/tmp/{id}"
            if not os.path.exists(tmp_dir):
                os.makedirs(tmp_dir)

        tmp_vrt = self.export_as_tif_tiles(var, tmp_dir, group=group, idxs=idxs)
        if COG:
            gdal.Translate(
                output,
                tmp_vrt,
                format="COG",
                creationOptions=["COMPRESS=DEFLATE", "BIGTIFF=YES"],
            )
        else:
            gdal.Translate(
                output,
                tmp_vrt,
                format="GTiff",
                creationOptions=["COMPRESS=LZW", "BIGTIFF=YES"],
            )
        return output
    
    @classmethod
    def process_tile(
        cls, 
        dc: rasterops.DataCube, 
        var: str, 
        idx: tuple[int, int], 
        dir: str, 
        group: str = None,
    ):
        da = dc.get_single_xarray_tile(var, idx, group=group)
        if da is None:
            return None

        da.rio.write_crs(dc.epsg, inplace=True)
        da.rio.write_nodata(dc.nodata, inplace=True)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            da.rio.to_raster(f"{dir}/{var}_{idx[0]}_{idx[1]}.tif", compress="LZW")
        return idx
                
    def export_as_tif_tiles(
        self, 
        var: str, 
        dir: str, 
        group: str = None, 
        idxs: list[tuple[int, int]] = [],
    ) -> None:
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)

        if len(idxs) == 0:
            if self.dc.store_active_idxs:
                idxs = self.dc.storage.root_group.attrs["stored_idxs"][f"{group}/{var}"]
            else:
                idxs = [i for i in self.dc.tiles._all_tiles()]
                
        compute_items = [
            compute.Args(args=[self.dc, var, idx, dir, group]) for idx in idxs
        ]

        # Use the parallel execution framework
        self.dc.compute.execute(Export.process_tile, compute_items)
        tmp_vrt = gdal.BuildVRT(
            f"{dir}/vrt.vrt",
            [os.path.join(dir, f) for f in os.listdir(dir) if f.endswith(".tif")],
        )
        return tmp_vrt
    
    def as_da(
        self, 
        **kwargs
    ):
        if "tmp_dir" not in kwargs:
            id = str(uuid.uuid4())
            kwargs["tmp_dir"] = f"/tmp/{id}"
            
        if "output" not in kwargs:
            tmp_file = f"/tmp/{id}.tif"
            kwargs["output"] = tmp_file
            
        self.export_as_tif(**kwargs)
        return rxr.open_rasterio(kwargs["output"])
                