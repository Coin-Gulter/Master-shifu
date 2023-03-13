import json



class js_setting():

    def __init__(self, setting_file_path):

        self.page_setting_face_id_complexity_slider = None
        self.page_setting_face_id_training_slider = None
        self.page_setting_windows_notification_checkbox = None
        self.page_setting_autostart_checkbox = None
        self.page_setting_auto_face_id_always_checkbox = None
        self.face_id_registered = None

        self.setting_file = setting_file_path


    def load_setting(self, page_setting_face_id_complexity_slider:int=50, page_setting_face_id_training_slider:int=50, page_setting_windows_notification_checkbox:bool=True, page_setting_autostart_checkbox:bool=True, page_setting_auto_face_id_always_checkbox:bool=False, face_id_registered:bool=False):
        setting_dict = {"page_setting_face_id_complexity_slider":page_setting_face_id_complexity_slider,
                        "page_setting_face_id_training_slider":page_setting_face_id_training_slider,
                        "page_setting_windows_notification_checkbox":bool(page_setting_windows_notification_checkbox),
                        "page_setting_autostart_checkbox":bool(page_setting_autostart_checkbox),
                        "page_setting_auto_face_id_always_checkbox":bool(page_setting_auto_face_id_always_checkbox),
                        "face_id_registered":bool(face_id_registered)}

        with open(self.setting_file, 'w') as js_wr:
            json.dump(setting_dict, js_wr, indent=4)

        self.get_setting()

    def get_setting(self):
        with open(self.setting_file, 'r') as js_wr:
            dict_obj = json.load(js_wr)

        self.page_setting_face_id_complexity_slider = dict_obj["page_setting_face_id_complexity_slider"]
        self.page_setting_face_id_training_slider = dict_obj["page_setting_face_id_training_slider"]
        self.page_setting_windows_notification_checkbox = dict_obj["page_setting_windows_notification_checkbox"]
        self.page_setting_autostart_checkbox = dict_obj["page_setting_autostart_checkbox"]
        self.page_setting_auto_face_id_always_checkbox = dict_obj["page_setting_auto_face_id_always_checkbox"]
        self.face_id_registered = dict_obj["face_id_registered"]

        return dict_obj

    def set_face_id_status(self, contents:bool):
        self.load_setting(self.page_setting_face_id_complexity_slider, self.page_setting_face_id_training_slider, self.page_setting_windows_notification_checkbox, self.page_setting_autostart_checkbox, self.page_setting_auto_face_id_always_checkbox, contents)


if __name__ == "__main__":
    setting = js_setting()
    setting.load_setting()
    print(setting.get_setting())
    print(setting.page_setting_face_id_complexity_slider, setting.page_setting_face_id_training_slider, setting.page_setting_windows_notification_checkbox, setting.page_setting_autostart_checkbox, setting.page_setting_auto_face_id_always_checkbox)
