from simple_blogger import SimpleBlogger

class SimplestBlogger(SimpleBlogger):
    def _example_task_creator(self, _):
        return [ { "topic_prompt": "Topic prompt" } ]
    
    def _get_category_folder(self, _):
        return '.'
    
    def _task_post_processor(self, *_):
        pass

    def _task_converter(self, item):
        return item
    
    def _task_extractor(self, tasks, _):
        return tasks[0]
    
    def review(self, type='topic'):
        return super().review(type, force_image_regen=True, force_text_regen=True)

    def send(self, type='topic', chat_id=None, **_):
        return super().send(type, True, True, chat_id, None, True, True)
    
    def revert(self):
        pass