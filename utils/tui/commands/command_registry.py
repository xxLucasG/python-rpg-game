import utils.utils


class CommandRegistry(utils.utils.registry.Registry, utils.utils.event.event_emitter.EventEmitter):
    def __init__(self):
        utils.utils.registry.Registry.__init__(self)
        utils.utils.event.event_emitter.EventEmitter.__init__(self)

    def execute(self, command, *args):
        if self.emit('on_command_execute', command, args):
            self.get(command.name).__execute__(*args)

    def register_command(self, command):
        if self.emit('on_command_register', command):
            self.register(command.name, command)

    def unregister_command(self, command):
        if self.emit('on_command_unregister', command):
            self.unregister(command.name)
