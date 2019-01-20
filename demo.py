import vistool

vt = vistool.VisTool(env='mvis')
vt.register_data(name = 'my_logger', type = 'logger')
vt.register_window(name = 'logging_window', type = 'logger', source='my_logger')
for i in range(10):
    vt.update('my_logger','haha')
vt.sync()
