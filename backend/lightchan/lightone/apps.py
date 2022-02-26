from django.apps import AppConfig

class LightoneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lightone'
    def ready(self) -> None:
        print("inside the ready function")
        # thread = Thread(target = threaded_function, args = (10, ), daemon=True)
        # thread.start()
        # # thread.join() 
        return super().ready()