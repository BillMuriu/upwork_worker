from seleniumbase import BaseCase


class RecorderTest(BaseCase):
    def test_recording(self):
        if self.undetectable:
            self.uc_open_with_disconnect(
                "https://notion.so"
            )
        if self.recorder_ext:
            # When done recording actions,
            # type "c", and press [Enter].
            import pdb; pdb.set_trace()
