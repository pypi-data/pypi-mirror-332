from kirara_ai.events.application import ApplicationStopping
from kirara_ai.events.im import IMAdapterStarted, IMAdapterStopped
from kirara_ai.events.listen import listen
from kirara_ai.events import ApplicationStarted
from kirara_ai.events.llm import LLMAdapterLoaded, LLMAdapterUnloaded
from kirara_ai.events.plugin import PluginStarted, PluginStopped
from kirara_ai.plugin_manager.plugin import Plugin

class TestEventBusPlugin(Plugin):
    def on_load(self):
        pass

    def on_start(self):
        self.setup_event_bus()
        pass

    def on_stop(self):
        pass
    
    def setup_event_bus(self):
        @listen(self.event_bus)
        def test_event(event: ApplicationStarted):
            print(event)

        @listen(self.event_bus)
        def test_event(event: ApplicationStopping):
            print(event)

        @listen(self.event_bus)
        def test_event(event: PluginStarted):
            print(event)

        @listen(self.event_bus)
        def test_event(event: PluginStopped):
            print(event)

        @listen(self.event_bus)
        def test_event(event: LLMAdapterLoaded):
            print(event)

        @listen(self.event_bus)
        def test_event(event: LLMAdapterUnloaded):
            print(event)

        @listen(self.event_bus)
        def test_event(event: IMAdapterStarted):
            print(event)

        @listen(self.event_bus)
        def test_event(event: IMAdapterStopped):
            print(event)
