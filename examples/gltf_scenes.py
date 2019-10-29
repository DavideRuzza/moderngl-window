from pathlib import Path
from pyrr import Matrix44, matrix44, Vector3

import moderngl
import moderngl_window as mglw
from moderngl_window.scene.camera import KeyboardCamera
from base import CameraWindow

class CubeModel(CameraWindow):
    """
    In oder for this example to work you need to clone the gltf
    model samples repository and ensure resource_dir is set correctly:
    https://github.com/KhronosGroup/glTF-Sample-Models/tree/master/2.0
    """
    window_size = 1920, 1080
    aspect_ratio = None
    resource_dir = Path(__file__, '../../../glTF-Sample-Models/2.0').resolve()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wnd.mouse_exclusivity = True

        # --- glTF-Sample-Models ---
        # self.scene = self.load_scene('2CylinderEngine/glTF-Binary/2CylinderEngine.glb')
        # self.scene = self.load_scene('CesiumMilkTruck/glTF-Embedded/CesiumMilkTruck.gltf')
        # self.scene = self.load_scene('CesiumMilkTruck/glTF-Binary/CesiumMilkTruck.glb')
        # self.scene = self.load_scene('CesiumMilkTruck/glTF/CesiumMilkTruck.gltf')
        self.scene = self.load_scene('Sponza/glTF/Sponza.gltf')
        # self.scene = self.load_scene('Lantern/glTF-Binary/Lantern.glb')
        # self.scene = self.load_scene('Buggy/glTF-Binary/Buggy.glb')
        # self.scene = self.load_scene('VC/glTF-Binary/VC.glb')
        # self.scene = self.load_scene('DamagedHelmet/glTF-Binary/DamagedHelmet.glb')
        # self.scene = self.load_scene('BoxInterleaved/glTF/BoxInterleaved.gltf')

        self.camera = KeyboardCamera(self.wnd.keys, fov=75.0, aspect_ratio=self.wnd.aspect_ratio, near=0.1, far=1000.0)
        self.camera.velocity = 7.0
        self.camera.mouse_sensitivity = 0.3

        # Use this for gltf scenes for better camera controls
        if self.scene.diagonal_size > 0:
            self.camera.velocity = self.scene.diagonal_size / 5.0

    def render(self, time: float, frametime: float):
        """Render the scene"""
        self.ctx.enable_only(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        # Create camera matrix with rotation and translation
        translation = matrix44.create_from_translation((0, 0, -1.5))
        camera_matrix = matrix44.multiply(translation, self.camera.matrix)

        self.scene.draw(
            projection_matrix=self.camera.projection.matrix,
            camera_matrix=camera_matrix,
            time=time,
        )

        # # Draw bounding boxes
        # self.scene.draw_bbox(
        #     projection_matrix=self.camera.projection.matrix,
        #     camera_matrix=camera_matrix,
        #     children=True,
        # )


if __name__ == '__main__':
    mglw.run_window_config(CubeModel)
