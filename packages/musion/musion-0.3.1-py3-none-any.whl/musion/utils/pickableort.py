import onnxruntime as ort

class PickableInferenceSession(ort.InferenceSession): # This is a wrapper to make the current InferenceSession class pickable.
    def __init__(self, model_path, sess_options, providers):
        super().__init__(model_path, sess_options=sess_options, providers=providers)
        self.model_path = model_path
        # self.sess_options = sess_options
        self.providers = providers

    def __getstate__(self):
        return {'model_path': self.model_path, 'providers': self.providers}

    def __setstate__(self, values):
        self.model_path = values['model_path']
        self.providers = values['providers']
        ort_options = ort.SessionOptions()
        ort_options.enable_cpu_mem_arena = False
        ort_options.enable_mem_pattern = False

        super().__init__(self.model_path, sess_options=ort_options, providers=self.providers)
