TEMPLATE = aux

providers.files = providers
providers.path =  $$PREFIX/share/accounts

services.files = services
services.path =  $$PREFIX/share/accounts

ui.files = ui
ui.path =  $$PREFIX/share/accounts

INSTALLS += providers services ui
