from zoo_framework.core.aop import event_map
import gevent


class BaseHandler:
    
    def __init__(self):
        pass
    
    def _on_error(self, topic, content, exception: Exception):
        pass
    
    def _on_success(self, topic, content):
        pass
    
    def _on_done(self, topic, content):
        pass
    
    def _serialize_content(self, content):
        return content
    
    def handle(self, topic, content, handler_name="default"):
        events = event_map.get(handler_name)
        if events is None:
            return
        
        event_handler = events.get(topic)
        if event_handler is None:
            return
        
        try:
            _content = self._serialize_content(content)
            g = gevent.spawn(event_handler,_content)
            g.start()
            self._on_success(topic, content)
        except Exception as e:
            self._on_error(topic, content, e)
        finally:
            self._on_done(topic, content)
