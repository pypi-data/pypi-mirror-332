from napari.utils.notifications import show_info
from nellie_napari import NellieLoader
import os
import pandas as pd


class FissionFusion:
    def __init__(self, nellie: NellieLoader):
        self.nellie = nellie
        self.is_ready = False

        self.run()

    def check_ready(self):
        if self.nellie.im_info is None:
            self.is_ready = False
            return 'No image loaded. Load one through Nellie.'

        organelle_feature_path = self.nellie.im_info.pipeline_paths['features_organelles']
        if not os.path.exists(organelle_feature_path):
            self.is_ready = False
            return 'No organelle features found. Run feature extraction through Nellie.'

        reassigned_im_path = self.nellie.im_info.pipeline_paths['im_obj_label_reassigned']
        if not os.path.exists(reassigned_im_path) or not self.nellie.visualizer.open_reassign_button.isEnabled():
            self.is_ready = False
            return 'No reassigned image found. Run voxel reassignment through Nellie.'

        self.is_ready = True
        return 'Ready to detect fission and fusion events.'

    def detect_events(self):
        organelle_feature_path = self.nellie.im_info.pipeline_paths['features_organelles']

        nellie_df = pd.read_csv(organelle_feature_path)
        # if 'reassigned_label_raw is all nan, then the reassigned labels are not present
        if nellie_df['reassigned_label_raw'].isnull().all():
            self.is_ready = False
            return 'Rerun feature extraction after running voxel reassignment.'

        nellie_df_small = nellie_df[['t', 'reassigned_label_raw', 'label']]
        max_frame_num = int(nellie_df_small['t'].max()) + 1
        total_num_reassigned_labels = len(nellie_df_small['reassigned_label_raw'].unique())

        events_per_frame = []
        label_differences = None
        for t in range(max_frame_num):
            num_unique_labels_in_t = len(nellie_df_small.loc[nellie_df_small['t'] == t, 'label'].unique())
            label_difference = num_unique_labels_in_t - total_num_reassigned_labels
            if label_differences is None:
                label_differences = [label_difference]
                events_per_frame.append(0)
                continue
            events_per_frame.append(label_difference - label_differences[-1])
            label_differences.append(label_difference)

        fission_events = sum([event for event in events_per_frame if event > 0])
        fusion_events = -sum([event for event in events_per_frame if event < 0])

        self.create_new_savepath()
        save_path = self.nellie.im_info.pipeline_paths['label_changes']

        # colums: t, label_differences_events_per_frame
        save_df = pd.DataFrame({'t': range(max_frame_num), 'label_differences': label_differences, 'events_per_frame': events_per_frame})
        save_df.to_csv(save_path, index=False)

        message = f'Fission: {fission_events} | Fusion: {fusion_events} | Saved to {save_path}'

        return message

    def create_new_savepath(self):
        self.nellie.im_info.create_output_path('label_changes', ext='.csv', for_nellie=False)

    def run(self):
        message = self.check_ready()
        show_info(message)
        if not self.is_ready:
            return

        message = self.detect_events()
        show_info(message)


def count_label_changes(nellie: NellieLoader):
    fission_fusion = FissionFusion(nellie)
    return fission_fusion


if __name__ == '__main__':
    import napari
    viewer = napari.Viewer()
    napari.run()
